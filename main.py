from flask import Flask, render_template, request, send_file
import PyPDF2
import openai
import os
from dotenv import load_dotenv
from prompts import PROMPT_HTML_TRANSFORMATION

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

class PDFExtractor:
    def __init__(self, file):
        self.file = file
    
    def extract_text(self):
        pdf_reader = PyPDF2.PdfReader(self.file)
        extracted_text = ""
        for page in pdf_reader.pages:
            extracted_text += page.extract_text() or ""
        return extracted_text

class HTMLFormatter:
    def __init__(self, text):
        self.text = text
    
    def format_html(self):
        
        # Combine the stored prompt with the extracted resume text
        prompt = PROMPT_HTML_TRANSFORMATION.format(resume_text=self.text)
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Specify the chat-based model
            messages=[
                {"role": "user", "content": prompt}
            ],
        )
        html_content = response['choices'][0]['message']['content']
        return html_content.replace("```html", '').replace('```', '').strip()

class FileHandler:
    @staticmethod
    def save_file(filename, content):
        with open(filename, "w") as file:
            file.write(content)
    
    @staticmethod
    def send_file(filename):
        return send_file(filename, as_attachment=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Get the uploaded PDF file from the form
    pdf_file = request.files['resume']
    
    # Extract text from PDF
    extractor = PDFExtractor(pdf_file)
    extracted_text = extractor.extract_text()
    
    # Format HTML content using OpenAI
    formatter = HTMLFormatter(extracted_text)
    html_content = formatter.format_html()
    
    # Save and send the HTML file
    html_filename = "resume.html"
    FileHandler.save_file(html_filename, html_content)
    
    return FileHandler.send_file(html_filename)

if __name__ == '__main__':
    app.run(debug=True)
