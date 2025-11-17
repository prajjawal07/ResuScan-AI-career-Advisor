import streamlit as st
import pdfplumber   # UPDATED: replacing fitz
import re
import base64
from pathlib import Path


# --- Streamlit Configuration ---
st.set_page_config(page_title="ResuScan Career Advisor", layout="wide", page_icon="")


# --- Background Image Setup ---
def set_background():
    """Set background image with professional styling"""
    bg_path = "f8d24a3aabc0d8095c712d70afa549fe.jpg"
    
    try:
        image_data = Path(bg_path).read_bytes()
        b64_string = base64.b64encode(image_data).decode()
        
        css = f"""
        <style>
        .stApp {{
            background-image: url('data:image/jpeg;base64,{b64_string}');
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
        }}
        .stApp::before {{
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
        }}
        [data-testid="stHeader"], [data-testid="stToolbar"] {{
            background: transparent;
        }}
        .block-container {{
            max-width: 1000px;
            background: rgba(20, 30, 55, 0.3);
            backdrop-filter: blur(8px);
            border-radius: 15px;
            padding: 2rem 2.5rem;
            border: 1px solid rgba(100, 150, 255, 0.15);
            margin-top: 3rem;
            margin-right:2rem;
            margin-bottom:3rem;
        }}
        [data-testid="stSidebar"] {{
            background: rgba(15, 20, 40, 0.6);
            backdrop-filter: blur(10px);
            border-right: 1px solid rgba(100, 150, 255, 0.15);
            margin-right:1.5rem;
        }}
        </style>
        """
        st.markdown(css, unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning("Background image not found. Make sure the image is in the app directory.")


set_background()


st.title("📃 ResuScan Career Advisor")
st.markdown("""
Upload your resume, choose your career goal, and get:
- Your **skill match percentage**
- **Udemy courses** to learn missing skills
- **Common interview questions**
- **Top companies** hiring for that role
""")


# --- PDF Extractor (UPDATED FUNCTION) ---
def extract_text_from_pdf(uploaded_file):
    """Extract text using pdfplumber (Streamlit Cloud friendly)"""
    full_text = ""
    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                full_text += text + "\n"
    return full_text


# --- Cleaner ---
def clean_text(text):
    text = re.sub(r"[^a-zA-Z ]", " ", text)
    return text.lower()


# ------------------------ DATA -------------------------

job_skills = {
    "Python Developer": ["python", "flask", "django", "api", "sql", "git"],
    "Data Analyst": ["excel", "sql", "pandas", "data", "visualization", "power bi", "tableau"],
    "Machine Learning Engineer": ["machine learning", "tensorflow", "pytorch", "scikit-learn", "deep learning", "ai"],
    "Web Developer": ["html", "css", "javascript", "react", "node", "django", "frontend", "backend"],
    "Android Developer": ["android", "kotlin", "java", "firebase", "mobile", "xml"],
    "DevOps Engineer": ["aws", "docker", "jenkins", "kubernetes", "ci/cd", "cloud"],
    "Database Administrator": ["mysql", "postgresql", "mongodb", "queries", "database", "backup"],
    "Software Tester / QA Engineer": ["testing", "selenium", "jira", "manual", "automation", "agile"],
    "Cybersecurity Analyst": ["security", "firewall", "network", "siem", "threat", "penetration"],
    "AI Engineer": ["nlp", "deep learning", "neural", "tensorflow", "pytorch", "transformer"]
}

udemy_courses = {
    "python": "https://www.udemy.com/course/complete-python-bootcamp/",
    "flask": "https://www.udemy.com/course/python-and-flask-framework-complete-course/",
    "django": "https://www.udemy.com/course/python-django-dev-to-deployment/",
    "sql": "https://www.udemy.com/course/the-complete-sql-bootcamp/",
    "git": "https://www.udemy.com/course/git-complete/",
    "excel": "https://www.udemy.com/course/microsoft-excel-2013-from-beginner-to-advanced-and-beyond/",
    "pandas": "https://www.udemy.com/course/data-analysis-with-pandas/",
    "power bi": "https://www.udemy.com/course/microsoft-power-bi-up-running-with-power-bi-desktop/",
    "tableau": "https://www.udemy.com/course/tableau-data-visualization/",
    "machine learning": "https://www.udemy.com/course/machinelearning/",
    "tensorflow": "https://www.udemy.com/course/deeplearning/",
    "pytorch": "https://www.udemy.com/course/pytorch-for-deep-learning/",
    "scikit-learn": "https://www.udemy.com/course/machine-learning-with-scikit-learn/",
    "html": "https://www.udemy.com/course/html-and-css-for-beginners-crash-course-learn-fast-easy/",
    "css": "https://www.udemy.com/course/css-the-complete-guide/",
    "javascript": "https://www.udemy.com/course/the-complete-javascript-course/",
    "react": "https://www.udemy.com/course/react-the-complete-guide-incl-redux/",
    "node": "https://www.udemy.com/course/the-complete-nodejs-developer-course-2/",
    "aws": "https://www.udemy.com/course/aws-certified-solutions-architect-associate/",
    "docker": "https://www.udemy.com/course/docker-mastery/",
    "jenkins": "https://www.udemy.com/course/jenkins-from-zero-to-hero/",
    "kubernetes": "https://www.udemy.com/course/kubernetes-for-the-absolute-beginners-hands-on/",
    "android": "https://www.udemy.com/course/android-kotlin-developer/",
    "security": "https://www.udemy.com/course/the-complete-cyber-security-course-hackers-exposed/",
    "nlp": "https://www.udemy.com/course/nlp-natural-language-processing-with-python/",
}

interview_questions = {
    "Python Developer": [
        "What are Python decorators and how are they used?",
        "Explain list comprehensions with an example.",
        "What's the difference between deep and shallow copy?",
        "How does garbage collection work in Python?",
        "What are Python generators?",
        "What is the GIL (Global Interpreter Lock)?",
        "Explain Flask vs Django.",
        "How do you write unit tests in Python?",
    ],
    "Data Analyst": [
        "How do you handle missing data?",
        "Explain joins in SQL.",
        "What is normalization?",
        "How to detect outliers?",
        "Difference between merge() and concat() in Pandas?",
    ],
    "Machine Learning Engineer": [
        "Explain bias-variance tradeoff.",
        "What is gradient descent?",
        "Difference between bagging and boosting?",
        "What is overfitting?",
        "Explain cross-validation."
    ]
}

companies = {
    "Python Developer": ["Google", "IBM", "TCS", "Infosys", "Accenture", "Capgemini", "Deloitte"],
    "Data Analyst": ["Microsoft", "Mu Sigma", "EY", "KPMG", "Amazon"],
    "Machine Learning Engineer": ["NVIDIA", "Google", "Amazon", "Flipkart", "Bosch"],
    "Web Developer": ["Meta", "Zoho", "Infosys", "Wipro"],
    "Android Developer": ["Samsung", "Paytm", "Zomato", "Ola"],
    "DevOps Engineer": ["AWS", "Azure", "Netflix", "Adobe"],
    "Database Administrator": ["Oracle", "SAP", "IBM", "Capgemini"],
    "Software Tester / QA Engineer": ["Cognizant", "Wipro", "Infosys"],
    "Cybersecurity Analyst": ["Cisco", "Palo Alto Networks", "Deloitte"],
    "AI Engineer": ["OpenAI", "Google DeepMind", "Microsoft"]
}

# --------------------------------------------------------

# Sidebar
st.sidebar.header("Upload & Goal Selection")
resume_file = st.sidebar.file_uploader("📄 Upload Resume (PDF)", type=["pdf"])
goal = st.sidebar.selectbox("🎯 Career Goal", list(job_skills.keys()))

# ------------------------ MAIN LOGIC ------------------------

if resume_file:
    resume_text = extract_text_from_pdf(resume_file)
    cleaned_resume = clean_text(resume_text)

    st.success("✅ Resume scanned successfully!")

    required_skills = job_skills[goal]
    matched = [s for s in required_skills if s in cleaned_resume]
    missing = [s for s in required_skills if s not in matched]
    match_percent = round((len(matched) / len(required_skills)) * 100, 2)

    st.subheader(f"🎯 Career Goal: {goal}")
    st.metric("Skill Match Percentage", f"{match_percent}%")

    col1, col2 = st.columns(2)
    col1.write("**Matched Skills:**")
    col1.write(", ".join(matched) if matched else "None")

    col2.write("**Missing Skills:**")
    col2.write(", ".join(missing) if missing else "None 🎉")

    st.progress(int(match_percent))

    # Udemy Courses
    if missing:
        st.subheader("📚 Recommended Udemy Courses")
        for skill in missing:
            if skill in udemy_courses:
                st.markdown(f"- [{skill.title()} Course]({udemy_courses[skill]})")
            else:
                st.markdown(f"- {skill.title()} (Search manually on Udemy)")

    # Interview Questions
    st.subheader("💬 Common Interview Questions")
    if goal in interview_questions:
        with st.expander(f"View Interview Questions for {goal}"):
            for q in interview_questions[goal]:
                st.markdown(f"- {q}")

    # Companies
    st.subheader("🏢 Top Companies Hiring for This Role")
    st.markdown(", ".join(companies[goal]))

else:
    st.info("👆 Upload your resume and select your career goal to begin analysis.")
