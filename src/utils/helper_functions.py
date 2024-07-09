import docx
import logging
from src.logger import logger

from transformers import T5Tokenizer, T5ForConditionalGeneration



def initialize_t5_model():
    """
    Initialize the T5 tokenizer and model.
    Returns:
    - tokenizer (T5Tokenizer): Initialized T5 tokenizer.
    - model (T5ForConditionalGeneration): Initialized T5 model.
    """
    tokenizer = T5Tokenizer.from_pretrained('t5-large')
    model = T5ForConditionalGeneration.from_pretrained('t5-large')
    return tokenizer, model


def extract_text_from_docx(docx_file):
    """
    Extracts text content from a DOCX file.

    Parameters:
    - docx_file (str): Path to the DOCX file.

    Returns:
    - str: Extracted text content, or None on error.

    """
    try:
        doc = docx.Document(docx_file)
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
        return "\n".join(full_text)
    except Exception as e:
        logger.error(f"Error extracting text from DOCX: {e}")
        return None

def generate_resume(original_resume_text, job_description_text,openai):
    """
    Generate a resume based on the original resume and job description using OpenAI's ChatGPT.
    
    Args:
    - original_resume_text (str): The original resume text.
    - job_description_text (str): The job description text to match against.
    
    Returns:
    - generated_resume (str): The generated resume text.
    """
    # Define the prompt combining original resume and job description
    prompt = f"Original Resume:\n{original_resume_text}\n\nJob Description:\n{job_description_text}\n\nGenerated Resume:"

    response = openai.completions.create(
        model="gpt-3.5-turbo",  # Using the Codex engine (powerful for text generation)
        prompt=prompt,
        max_tokens=2000,  # Adjust length as needed
        temperature=0.7,  # Adjust creativity vs. coherence
        stop=None  # Allow the model to finish the thought
    )
    # Extract generated resume from response
    generated_resume = response.choices[0].text.strip()
    
    return generated_resume


def update_resume(original_resume_text, job_description_text, tokenizer, model):
    """
    Update the resume based on the job description using T5 model.
    Args:
    - original_resume_text (str): Original resume text.
    - job_description_text (str): Job description text to match.
    - tokenizer (T5Tokenizer): T5 tokenizer object.
    - model (T5ForConditionalGeneration): T5 model object.
    Returns:
    - updated_resume (str): Updated resume text.
    """
    # Prepare input for T5
    input_text = f"update resume: {original_resume_text} to match job description: {job_description_text}"
    input_ids = tokenizer.encode(input_text, return_tensors="pt")

    # Generate updated resume
    outputs = model.generate(input_ids, max_length = 5000)
    updated_resume = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return updated_resume