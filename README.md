# ATS-Resume-Tracking

A Streamlit-based web application designed to help job seekers optimize their resumes for technical roles by evaluating them against job descriptions and providing actionable improvement suggestions. Built with Python, it leverages the Gemini API for intelligent resume analysis and supports PDF uploads for seamless processing.
Access the app here: https://tovohcue2y8qb26mlicoal.streamlit.app/

## Features

- **Resume Evaluation**: Analyzes a resume against a job description, providing a structured assessment of alignment, strengths, weaknesses, and recommendations for improvement.
- **Skill Improvement Suggestions**: Identifies skill gaps and offers tailored advice, including online courses, projects, and networking opportunities to enhance the resume.
- **ATS Percentage Match**: Calculates a percentage match between the resume and job description, highlighting missing keywords and suggesting improvements for better ATS compatibility.
- **User-Friendly Interface**: Built with Streamlit, the app allows users to upload PDF resumes, input job descriptions, and download analysis results as text files.
- **Progress Visualization**: Displays the ATS match score as a progress bar for intuitive feedback.

## Project Structure
ATS-Resume-Expert/
├── app.py              # Main Streamlit application
├── requirements.txt     # Python dependencies
├── packages.txt        # System dependencies for Streamlit Cloud
└── README.md           # Project documentation

## Installation (Local Development)

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/ATS-Resume-Expert.git
   cd ATS-Resume-Expert

Set Up a Virtual Environment:
pip install -r requirements.txt

Install Poppler (for PDF processing):

    Windows: Download and install Poppler from here and add it to your PATH.
    Linux/Mac: Install via package manager:
    sudo apt-get install poppler-utils  # Ubuntu/Debian
brew install poppler               # macOS


Set Up Environment Variables: Create a .env file in the project root:
GOOGLE_API_KEY=your_gemini_api_key


