import openai 
from artifacts.api_key import api_key
api_key = api_key

openai.api_key = api_key

from src.utils.helper_functions import extract_text_from_docx as extract

from transformers import T5Tokenizer, T5ForConditionalGeneration
from src.utils.helper_functions import initialize_t5_model
from src.utils.helper_functions import update_resume

def main():
    file = "data/resume.docx"
    text = extract(docx_file=file)
    file = "data/job_description.docx"
    JD = extract(docx_file=file)
    tokenizer, model = initialize_t5_model()
    # Update the resume based on job description
    updated_resume = update_resume(text, JD, tokenizer, model)

    # Print or use updated resume
    print("Updated Resume:")
    print(updated_resume)


if __name__ == "__main__":
    main()