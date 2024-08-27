from dotenv import load_dotenv
import streamlit as st
from streamlit_extras import add_vertical_space as avs
import google.generativeai as genai
import os
import PyPDF2
from PIL import Image

# Load environment variables from a .env file
load_dotenv()

# Set page configuration as the first Streamlit command
st.set_page_config(page_title="CareerCraft: ATS-Optimized Resume Analyzer using Gemini Model", layout="wide")

# Configure the Google generative AI model using an API key stored in environment variables
google_api_key = st.text_input("Enter your Google API Key", type="password")  # Input field for API key

# Check if API key is provided and configure the model
if google_api_key:
    genai.configure(api_key=google_api_key)

# Create an instance of the generative AI model
model = genai.GenerativeModel('gemini-pro')

def get_gemini_response(input):
    response = model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ''
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text += str(page.extract_text())
    return text

input_prompt = """
As an experienced ATS (Applicant Tracking System), proficient in the technical domain encompassing Software Engineering,
Data Science, Data Analysis, Big Data Engineering, Web Developer, Mobile App Developer, DevOps Engineer, Machine Learning Engineer,
Cybersecurity Analyst, Cloud Solutions Architect, Database Administrator, Network Engineer, AI Engineer, Systems Analyst, Full Stack Developer,
UI/UX Designer, IT Project Manager, and additional specialized areas, your objective is to meticulously assess resumes against provided job descriptions. 
In a fiercely competitive job market, your expertise is crucial in offering top-notch guidance for resume enhancement.
Assign precise matching percentages based on the JD (Job Description) and meticulously identify any missing keywords with utmost accuracy.
resume:{text}
description:{jd}

I want the response in the following structure:
The first line indicates the percentage match with the job description (JD).
The second line presents a list of missing keywords.
The third section provides a profile summary.

Mention the title for all the three sections.
While generating the response put some space to separate all the three sections.
"""

# Add vertical space
avs.add_vertical_space(4)

# Define columns layout
col1, col2 = st.columns([3, 2])

# Content for the first set of columns
with col1:
    st.title("CareerCraft")
    st.header("Enhance Your Tech Career Path!")
    st.markdown("""
    <p style='text-align: justify;'>
    Introducing CareerCraft, your ultimate solution for enhancing job applications and accelerating career growth in the tech industry.
    Our innovative platform leverages advanced ATS technology to provide job seekers with valuable insights into their resumes' compatibility with job descriptions.
    From resume optimization and skill enhancement to career progression guidance, CareerOptimizer empowers users to stand out in today’s competitive job market. 
    Streamline your job application process, enhance your skills, and confidently navigate your career path. 
    Use CareerOptimizer today and unlock new opportunities for professional success!
    </p>
    """, unsafe_allow_html=True)

with col2:
    st.image('https://cdn.dribbble.com/userupload/12500996/file/original-b458fe398a6d7f4e9999ce66ec856ff9.gif', use_column_width=True)

# Add vertical space
avs.add_vertical_space(10)

# Define columns layout for the second part
col1, col2 = st.columns([3, 2])

with col2:
    st.header("Comprehensive Services")
    st.write('- Advanced Resume Analysis')
    st.write('- Tailored Resume Optimization')
    st.write('- Skill Enhancement Strategies')
    st.write('- Guidance for Career Advancement')
    st.write('- Customized Profile Summaries')
    st.write('- Optimized Job Application Process')
    st.write('- Personalized Career Recommendations')
    st.write('- Efficient Career Navigation Tools')

with col1:
    img1 = Image.open("images/icon1.png")
    st.image(img1, use_column_width=True)

# Add vertical space
avs.add_vertical_space(10)

# Define columns layout for the third part
col1, col2 = st.columns([3, 2])

with col1:
    st.markdown("<h1 style='text-align: center;'>Embark on Your Career Adventure</h1>", unsafe_allow_html=True)
    jd = st.text_area("Paste the Job Description")
    uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the pdf")

    submit = st.button("Submit")

    if submit:
        if uploaded_file is not None:
            text = input_pdf_text(uploaded_file)
            response = get_gemini_response(input_prompt.format(text=text, jd=jd))  # Format input prompt with user input
            st.subheader(response)

with col2:
    img2 = Image.open("images/icon2.png")
    st.image(img2, use_column_width=True)

# Add vertical space
avs.add_vertical_space(10)

col1, col2 = st.columns([2, 3])
with col2:
    st.markdown("<h1 style='text-align: center;'>FAQ</h1>", unsafe_allow_html=True) 
    st.write("Question: How does CareerCraft analyze resumes and job descriptions?") 
    st.write("""Answer: CareerCraft uses advanced algorithms to analyze resumes and job descriptions,
           identifying key keywords and assessing compatibility between the two.""") 
    avs.add_vertical_space(3)
    st.write("Question: Can CareerCraft suggest improvements for my resume?")
    st.write("""Answer: Yes, CareerCraft provides personalized recommendations to optimize your resume
           for specific job openings, including suggestions for missing keywords and alignment with 
           desired job roles.""")
    avs.add_vertical_space(3)
    st.write("Question: Is CareerCraft suitable for both entry-level and experienced professionals?") 
    st.write("""Answer: Absolutely! CareerCraft caters to job seekers at all career stages, offering 
           tailored insights and guidance to enhance their resumes and advance their careers.""")

with col1:
    img3 = Image.open("images/icon3.png")
    st.image(img3, use_column_width=True)
