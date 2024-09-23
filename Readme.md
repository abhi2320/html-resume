# Resume Generator from PDF

## Project Overview

This project is a web application that converts LinkedIn resumes in PDF format into professionally styled HTML resumes. It uses Flask as the web framework, OpenAI's GPT-3.5 for formatting the resume text, and PyPDF2 for extracting text from PDFs. The application provides a user-friendly interface for uploading a resume and receiving a styled HTML resume in return.

## Features

- **PDF Text Extraction**: Extracts text content from uploaded LinkedIn PDF resumes.
- **HTML Formatting**: Uses OpenAI's GPT-3.5 to transform the resume text into a well-organized, professionally styled HTML format.
- **User Interface**: Simple and clean interface for uploading resumes and downloading the formatted HTML file.
- **Dark Mode Styling**: The user interface is designed with a modern dark theme for a premium feel.

## Live Demo

You can try the live version of the application here: [Resume Generator](https://python-verbaflow.onrender.com)

## Installation

### Prerequisites

- Python 3.7 or higher
- `pip` (Python package installer)

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name


2. **Create and Activate a Virtual Environment**

    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`


3. **Install Dependencies**

    pip install -r requirements.txt

4. **Create a .env File**

    OPENAI_API_KEY=your_openai_api_key

5. **Run the Application**

    python main.py

The application will be available at http://127.0.0.1:5000/


**Dependencies**
Ensure you have the following packages installed:

Flask
PyPDF2
OpenAI
python-dotenv


**Use Cases for this project are**

1. Quickly Convert LinkedIn Profiles: Professionals can easily transform their LinkedIn PDF exports into visually appealing, structured HTML resumes without manually formatting.

2. Tailored Resume Customization: Users can generate professional resumes customized to specific job applications, allowing quick adjustments to design and layout as needed.

3. Recruitment Tools: Recruitment agencies or HR departments can integrate the tool to help candidates submit well-formatted resumes, ensuring consistency in presentation.

4. Portfolio Building: Freelancers or job seekers can use it to create an online portfolio of HTML resumes that can be shared via personal websites or email for better visibility.

5. Resume Review Platforms: It can be integrated into resume review services to format and improve the design of submitted resumes, ensuring professionalism and readability.
