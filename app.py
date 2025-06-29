from dotenv import load_dotenv

load_dotenv()
import base64
import streamlit as st
import os
import io
from PIL import Image 
import pdf2image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input,pdf_cotent,prompt):
    model=genai.GenerativeModel('gemini-1.5-flash')
    response=model.generate_content([input,pdf_content[0],prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        ## Convert the PDF to image
        images=pdf2image.convert_from_bytes(uploaded_file.read())

        first_page=images[0]

        # Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

## Streamlit App

st.set_page_config(page_title="ATS Resume EXpert")
st.header("ATS Tracking System")
input_text=st.text_area("Job Description: ",key="input")
uploaded_file=st.file_uploader("Upload your resume(PDF)...",type=["pdf"])


if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")


submit1 = st.button("Tell Me About the Resume")

submit2 = st.button("How Can I Improvise my Skills")

submit3 = st.button("Percentage match")

input_prompt1 = """
You are an experienced Technical Human Resource Manager with expertise in evaluating resumes for technical roles. Your task is to review the provided resume against the job description and provide a professional evaluation of the candidate's alignment with the role. Structure your response as follows:
1. **Summary**: A brief assessment of how well the candidate's profile matches the job requirements.
2. **Strengths**: Highlight specific technical skills, experiences, certifications, or qualifications that align with the job description, using bullet points.
3. **Weaknesses**: Identify gaps or areas where the candidate's profile does not meet the job requirements, using bullet points.
4. **Recommendations**: Suggest actionable steps to address weaknesses (e.g., gaining specific skills or certifications).
Ensure your evaluation is concise, specific to the job's industry and level (e.g., entry-level, mid-level, senior), and avoids generic statements. Use examples from the resume and job description to support your analysis.
"""
input_prompt2 = """
You are a career coach with expertise in technical roles and professional development. Your task is to analyze the provided resume against the job description and suggest specific ways the candidate can improve their skills to better align with the role. Structure your response as follows:
1. **Skill Gaps**: Identify key skills, tools, or qualifications from the job description that are missing or underdeveloped in the resume, using bullet points.
2. **Improvement Plan**: Provide actionable recommendations to address each gap, such as:
   - Online courses or certifications (specify platforms like Coursera, Udemy, or vendor-specific programs).
   - Practical projects or tools to learn (e.g., building a portfolio project, contributing to open-source).
   - Networking or professional development activities (e.g., joining industry groups, attending webinars).
3. **Prioritization**: Highlight which improvements are most critical for the role and why.
Ensure recommendations are specific to the job's industry, level (e.g., entry-level, senior), and requirements. Avoid generic suggestions and provide concrete examples (e.g., course names, tools).
"""

input_prompt3 = """
You are a skilled ATS (Applicant Tracking System) scanner with expertise in data science and resume optimization. Your task is to evaluate the provided resume against the job description and calculate a percentage match based on the overlap of key skills, qualifications, tools, and experience. Structure your response as follows:
1. **Percentage Match**: A number (0-100%) reflecting the resume's alignment with the job description, calculated by comparing keywords, skills, and qualifications.
2. **Missing Keywords**: List specific keywords, skills, tools, or qualifications from the job description that are absent or underrepresented in the resume, using bullet points.
3. **Final Thoughts**: Provide a concise summary of the resume's overall fit for the role and suggestions for improving the match score.
Ensure the evaluation is precise, prioritizes critical job requirements (e.g., technical skills, certifications), and avoids vague terms. Use examples from the job description to justify missing keywords.
"""



if submit1:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt1,pdf_content,input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume")

elif submit2:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response("How can I improvise my skills?",pdf_content,input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume")
        
elif submit3:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt3,pdf_content,input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume")



   





