from textwrap import dedent

PROMPT_HTML_TRANSFORMATION = dedent("""
    Transform the following resume text into a professionally styled HTML resume. Ensure the following:
    - Header Design: The person's name should be prominently displayed in the header with the largest font size and below that basic detail about the individual. And make the header space quite dark to differentiate it from the other content part.
    - Text Hierarchy: All other text should have smaller font sizes compared to the name header.
    - Content Cleanliness: Remove any extraneous lines or formatting artifacts that are not part of the original PDF content.
    - Premium Experience: Design the HTML to provide a polished and high-quality user experience. Use semantic HTML tags for better structure.
    - Use a mixture of dark and light contrasting colors to present it with a more premium feel.
    - Include inline CSS styles to ensure the resume looks good across different devices.
    - Add all the fields like Contact, Top Skills, Certificates, Summary, Experience, Education, links, and other details in the uploaded resume.
    - Make sure to add all the details or text present in the resume.

    Resume Text: {resume_text}
""")
