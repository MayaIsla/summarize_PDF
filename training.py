import pandas as pd
import openai
import fitz  # PyMuPDF
import os


dict = "C:/training.csv"

df = pd.read_csv(dict, sep=',')

# Path to file containing API key
api_key_file_path = "C:/openai_key.txt"

log_path = "C:/log.txt"
dup_path = "C:/remove_dup.txt"

with open(api_key_file_path, 'r') as f:
    openai.api_key = f.read().strip()

def read_pdf(file_path):
    text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def summarize_text_with_openai(text, chunk_len=2000, temperature=0.2):
    prompt_chunks = [text[i:i + chunk_len] for i in range(0, len(text), chunk_len)]
    summarized_text = ""
    for j in df['Prompt']:
        for chunk in prompt_chunks:
                try:
                    strJ = str(j)
                    response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[
                        {"role": "user", "content": f' + {strJ} + "\n" + {chunk}'}
                    ],
                    max_tokens=min(4096, chunk_len),
                    temperature=temperature
                )
                    summarized_text += response['choices'][0]['message']['content'].strip() + "\n"
                    
                except openai.error.OpenAIError as e:
                    print(f"An error occurred: {str(e)}")
    return summarized_text

def remove_duplicates():
    lines_seen = set() # holds lines already seen
    outfile = open(dup_path, "w+")
    for line in open(log_path, "r+"):
        if line not in lines_seen: # not a duplicate
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()
        


    
pdf_path = "C:/PDF.pdf"
text = read_pdf(pdf_path)
if text:
    summarized_text = summarize_text_with_openai(text)
    string_text = str(summarized_text)
    f = open(log_path, "a")
    f.write(string_text)
    f.close
    remove_duplicates()
    print("Done.")
    
   
else:
    print("Failed to extract text from the PDF.")
