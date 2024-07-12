import openai 

from src.logger import logger
# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM

from src.utils.helper_functions import extract_text_from_docx as extract
from src.utils.helper_functions import generate_resume_llama

def main():
    file = "data/resume.docx"
    text = extract(docx_file=file)
    file = "data/job_description.docx"
    JD = extract(docx_file=file)

    tokenizer = AutoTokenizer.from_pretrained("meta-llama/Meta-Llama-3-8B",token = "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")
    model = AutoModelForCausalLM.from_pretrained("meta-llama/Meta-Llama-3-8B",token = "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")

    # Generate updated resume based on the job description
    generated_resume = generate_resume_llama(text, JD, model, tokenizer)

    # Log the result
    logger("Resume : content created")

    # Print or use updated resume
    print("Updated Resume:")
    print(generated_resume)


if __name__ == "__main__":
    main()

