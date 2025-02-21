import google.generativeai as genai
import os
import json
import PyPDF2

# Configuration for Google API key
GOOGLE_API_KEY = ""
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
genai.configure(api_key=GOOGLE_API_KEY)

# Define the model
model = genai.GenerativeModel("gemini-1.5-flash")


# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text



# Example usage
pdf_path = "Samyak Nahar resume.pdf"  # Replace with the path to your PDF file
resume_text = extract_text_from_pdf(pdf_path)
# print(text)

prompt = f"""
You are a powerful language model trained to understand and parse structured data.
I am going to provide you with my resume text, and I need you to convert it into a structured JSON format.
The JSON should contain sections for Contact Information, Profile, Skills, Education, Extracurricular Activities, Hobbies, Certifications/Courses, Experience, and Projects. 
Please ensure that each section is accurately represented in the JSON format.
Here is my resume text:

{resume_text}

Please convert this resume text into the following JSON format:
{{
  "Contact Information": {{
    "Name": "John Doe",
    "Email": "john.doe@example.com",
    "Phone": "+1234567890",
    "GitHub": "https://github.com/johndoe",
    "LinkedIn": "https://www.linkedin.com/in/johndoe/"
  }},
  "Profile": "Professional summary...",
  "Skills": {{
    "Core Languages": ["C++", "Python", "C"],
    "Machine Learning": ["TensorFlow", "CNN", "Image Processing", "OpenCV", "NLP", "LLM"],
    "Web Dev": ["HTML & CSS", "JavaScript", "Django", "React", "MySQL"]
  }},
  "Education": [
    {{
      "Institution": "XYZ University",
      "Degree": "B.Tech in Artificial Intelligence & Data Science",
      "CGPA": "8.23",
      "Year": "2021 - 2025"
    }},
    {{
      "Institution": "ABC School",
      "Degree": "12TH",
      "Percentage": "81.67%",
      "Year": "2019 - 2021"
    }},
    {{
      "Institution": "DEF School",
      "Degree": "10TH",
      "Percentage": "78.20%",
      "Year": "2009 - 2019"
    }}
  ],
  "Extracurricular Activities": [
    "Participated in XYZ Hackathon",
    "Member of ABC Club"
  ],
  "Hobbies": [
    "Exploring cool Python libraries",
    "Playing Chess, Football",
    "Gym"
  ],
  "Certifications/Courses": [
    "TensorFlow - Udemy",
    "PyTorch - Udemy",
    "Computer Vision - Udemy",
    "OpenCV - Udemy",
    "Web-Dev - Udemy",
    "Django - Django docs"
  ],
  "Experience": [
    {{
      "Role": "Intern",
      "Company": "ABC Corp",
      "Duration": "June 2021 - August 2021",
      "Responsibilities": [
        "Led backend development project and collaborated with senior engineers.",
        "Optimized algorithms to significantly improve search efficiency and data retrieval."
      ],
      "Tech Used": "Python, Django, React, MySQL"
    }}
  ],
  "Projects": [
    {{
      "Name": "Chatbot Project",
      "Description": "Developed a chatbot using Python and NLTK.",
      "Tech Stack": "Python, NLTK"
    }},
    {{
      "Name": "Web Development Project",
      "Description": "Created a full-stack web application using Django and React.",
      "Tech Stack": "Django, React, PostgreSQL"
    }}
  ]
}}
"""

response = model.generate_content(prompt)
generated_json = response.text
if generated_json.startswith("```json"):
    generated_json = generated_json[len("```json") :].strip()
if generated_json.endswith("```"):
    generated_json = generated_json[: -len("```")].strip()
# Save the generated JSON to a file
output_path = "resume.json"
with open(output_path, "w") as json_file:
    json_file.write(generated_json)

print(f"JSON data saved to {output_path}")
