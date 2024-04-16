import PyPDF2
import re
import os

def read_pdf(pdf_path):
    
    with open(pdf_path, 'rb') as f:
        
        reader = PyPDF2.PdfReader(f)
        page = reader.getPage(0)
        text = page.extract_text()
        
    return text

def extract_words(text):
    
    words = re.findall(r'\w+', text)
    
    return words

def compare_words(words, dictionary):
    
    common_words = []
    for word in words:
        
        if word.lower() in dictionary:
            common_words.append(word)
            
    return common_words

def generate_new_pdf(common_words, output_path):
    
    with open(output_path, 'w', encoding='utf-8') as f:
        
        for word in common_words:
            
            f.write(word + '\n')

def main():
    
    pdf_path = 'Colocarpdf.pdf'
    dictionary_path = 'Colocardiccionario.txt'
    output_path = 'Dondeiraelpdf.pdf'

    text = read_pdf(pdf_path)
    words = extract_words(text)

    with open(dictionary_path, 'r') as f:
        dictionary = [line.strip() for line in f]

    common_words = compare_words(words, dictionary)

    generate_new_pdf(common_words, output_path)

    print("Archivo PDF generado con éxito:", output_path)

if __name__ == "__main__":
    main()
