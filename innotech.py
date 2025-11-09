import streamlit as st
import fitz
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
        /* Background setup */
        .stApp {{
            background-image: url('data:image/jpeg;base64,{b64_string}');
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
        }}
        
        /* Dark overlay for readability */
        .stApp::before {{
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            # background: linear-gradient(135deg, rgba(10, 15, 30, 0.75) 0%, rgba(20, 25, 45, 0.7) 100%);
            z-index: -1;
        }}
        
        /* Hide header and toolbar */
        [data-testid="stHeader"], [data-testid="stToolbar"] {{
            background: transparent;
        }}
        
        /* Main container styling */
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
        
        /* Sidebar styling */
        [data-testid="stSidebar"] {{
            background: rgba(15, 20, 40, 0.6);
            backdrop-filter: blur(10px);
            border-right: 1px solid rgba(100, 150, 255, 0.15);
            margin-right:1.5rem;
        }}
        
        [data-testid="stSidebar"] [data-testid="stVerticalBlock"] {{
            gap: 1.5rem;
        }}

        .stSubheader {{
            color: #a0b8ff !important;
            font-size: 2.5rem;
            font-weight: 600 !important;
            margin-top: 1.5rem;
            margin-bottom: 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid rgba(100, 150, 255, 0.3);
            
        }}
        
        /* Heading styles */
        h1 {{
            color: #ffffff !important;
            font-size: 2.5rem !important;
            font-weight: 700 !important;
            text-align: center;
            margin-bottom: 1rem;
            text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
        }}
        
        h2 {{
            color: #e0e8ff !important;
            font-size: 1.5rem !important;
            font-weight: 600 !important;
            margin-top: 1.5rem;
            margin-bottom: 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid rgba(100, 150, 255, 0.3);
        }}
        
        h3 {{
            color: #c8d5ff !important;
            font-size: 1.1rem !important;
            font-weight: 600 !important;
        }}
        
        /* Paragraph styles */
        p {{
            color: #d0d8e8 !important;
            font-size: 0.95rem;
            line-height: 1.6;
        }}
        
        /* Markdown text */
        .stMarkdown {{
            color: #d0d8e8 !important;
        }}
        
        /* Metrics styling */
        [data-testid="metric-container"] {{
            background: linear-gradient(135deg, rgba(70, 130, 220, 0.25) 0%, rgba(100, 150, 255, 0.15) 100%) !important;
            border: 1.5px solid rgba(100, 150, 255, 0.4) !important;
            border-radius: 12px !important;
            padding: 1.5rem !important;
            box-shadow: 0 8px 20px rgba(100, 150, 255, 0.15) !important;
        }}
        
        /* Success alert styling */
        .stSuccess {{
            background: linear-gradient(135deg, rgba(76, 175, 80, 0.20) 0%, rgba(100, 200, 100, 0.15) 100%) !important;
            border: 1.5px solid rgba(76, 175, 80, 0.5) !important;
            border-radius: 12px !important;
            padding: 1rem !important;
            box-shadow: 0 8px 20px rgba(76, 175, 80, 0.1) !important;
        }}
        
        /* Warning alert styling */
        .stWarning {{
            background: linear-gradient(135deg, rgba(255, 152, 0, 0.25) 0%, rgba(255, 180, 0, 0.15) 100%) !important;
            border: 1.5px solid rgba(255, 152, 0, 0.5) !important;
            border-radius: 12px !important;
            padding: 1rem !important;
            box-shadow: 0 8px 20px rgba(255, 152, 0, 0.1) !important;
        }}
        
        /* Error alert styling */
        .stError {{
            background: linear-gradient(135deg, rgba(244, 67, 54, 0.25) 0%, rgba(255, 100, 80, 0.15) 100%) !important;
            border: 1.5px solid rgba(244, 67, 54, 0.5) !important;
            border-radius: 12px !important;
            padding: 1rem !important;
            box-shadow: 0 8px 20px rgba(244, 67, 54, 0.1) !important;
        }}
        
        /* Info alert styling */
        .stInfo {{
            background: linear-gradient(135deg, rgba(33, 150, 243, 0.25) 0%, rgba(100, 180, 255, 0.15) 100%) !important;
            border: 1.5px solid rgba(33, 150, 243, 0.5) !important;
            border-radius: 12px !important;
            padding: 1rem !important;
            box-shadow: 0 8px 20px rgba(33, 150, 243, 0.1) !important;
        }}
        
        /* Progress bar styling */
        .stProgress > div > div > div {{
            background: linear-gradient(90deg, #6495dc 0%, #7e70d4 50%, #a366ff 100%) !important;
            border-radius: 8px !important;
            box-shadow: 0 0 10px rgba(100, 150, 255, 0.4) !important;
        }}
        
        /* Write text styling */
        .stWrite {{
            color: #d0d8e8 !important;
        }}
        
        /* Column styling */
        .stColumn {{
            background: rgba(30, 45, 70, 0.4);
            padding: 1.2rem;
            border-radius: 10px;
            border: 1px solid rgba(100, 150, 255, 0.2);
        }}
        
        /* Expander styling */
        .streamlit-expanderHeader {{
            background: rgba(50, 80, 140, 0.3);
            border-radius: 8px;
            color: #c8d5ff;
        }}
        
        /* Links */
        a {{
            color: #6fa3ff !important;
            text-decoration: none;
        }}
        
        a:hover {{
            color: #9fbfff !important;
            text-decoration: underline;
        }}
        
        /* Input and select styling */
        .stTextInput > div > div > input,
        .stSelectbox > div > div > select,
        .stFileUploader {{
            background: rgba(30, 50, 80, 0.6) !important;
            border: 1px solid rgba(100, 150, 255, 0.3) !important;
            color: #d0d8e8 !important;
            border-radius: 8px !important;
        }}
        
        /* Divider styling */
        hr {{
            border: 1px solid rgba(100, 150, 255, 0.2);
            margin: 2rem 0;
        }}
        </style>
        """
        st.markdown(css, unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning("Background image not found. Make sure 'f8d24a3aabc0d8095c712d70afa549fe.jpg' is in the app directory.")


set_background()


st.title("📃 ResuScan Career Advisor")
st.markdown("""
Upload your resume, choose your career goal, and get:
- Your **skill match percentage**
- **Udemy courses** to learn missing skills
- **Common interview questions**
- **Top companies** hiring for that role
""")


# --- PDF Extractor ---
def extract_text_from_pdf(uploaded_file):
    text = ""
    pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    for page in pdf:
        text += page.get_text("text")
    return text


# --- Cleaner ---
def clean_text(text):
    text = re.sub(r"[^a-zA-Z ]", " ", text)
    return text.lower()


# --- Job Skill Mapping ---
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


# --- Udemy Course Recommendations ---
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


# --- Interview Question Bank ---
interview_questions = {
    "Python Developer": [
        "What are Python decorators and how are they used?",
        "Explain list comprehensions with an example.",
        "What's the difference between deep and shallow copy?",
        "How does garbage collection work in Python?",
        "What are Python generators?",
        "How do you manage dependencies in Python projects?",
        "What is the Global Interpreter Lock (GIL)?",
        "Explain Flask vs Django.",
        "What's your approach to writing unit tests in Python?",
        "What databases have you integrated using Python?"
    ],
    "Data Analyst": [
        "How do you handle missing data in a dataset?",
        "Explain the difference between inner and outer joins.",
        "How would you detect outliers?",
        "What is data normalization?",
        "How do you optimize SQL queries?",
        "Difference between Pandas merge() and concat().",
        "What's the use of groupby() in Pandas?",
        "How do you measure correlation between variables?",
        "Explain a project where you used visualization tools.",
        "Which KPIs do you track in analytics?"
    ],
    "Machine Learning Engineer": [
        "Explain bias-variance tradeoff.",
        "Difference between bagging and boosting?",
        "What is overfitting and how do you prevent it?",
        "Explain precision vs recall.",
        "How do you handle imbalanced datasets?",
        "What is gradient descent?",
        "What's the difference between classification and regression?",
        "Describe a real-world ML project you built.",
        "What are hyperparameters?",
        "Explain cross-validation."
    ],
    "Web Developer": [
        "What is the DOM and how does it work?",
        "Explain REST APIs.",
        "What's the difference between React and Angular?",
        "How do you optimize web performance?",
        "What is responsive design?",
        "Explain the concept of closures in JavaScript.",
        "How do you manage state in React?",
        "What is CORS and how to handle it?",
        "Explain server-side rendering.",
        "How do you secure a web application?"
    ],
    "Android Developer": [
        "What's the difference between Activity and Fragment?",
        "Explain the Android lifecycle.",
        "What is an Intent?",
        "What is View Binding?",
        "Explain RecyclerView.",
        "How do you handle API calls in Android?",
        "What are LiveData and ViewModel?",
        "Explain MVVM architecture.",
        "How do you optimize app performance?",
        "What is Room Database?"
    ],
    "DevOps Engineer": [
        "Explain CI/CD pipelines.",
        "How does Docker differ from VMs?",
        "What is container orchestration?",
        "How do you monitor application performance?",
        "What are common Jenkins pipelines?",
        "How do you handle rollback in deployments?",
        "What is Infrastructure as Code?",
        "How do you use Ansible or Terraform?",
        "Explain the blue-green deployment strategy.",
        "What is version control and branching strategy?"
    ]
}


# --- Top Companies Hiring ---
companies = {
    "Python Developer": ["Google", "IBM", "TCS", "Infosys", "Accenture", "Capgemini", "Deloitte"],
    "Data Analyst": ["Microsoft", "Mu Sigma", "EY", "KPMG", "ZS Associates", "Amazon"],
    "Machine Learning Engineer": ["NVIDIA", "Google", "Amazon", "Flipkart", "Bosch", "Adobe"],
    "Web Developer": ["Meta", "Zoho", "Infosys", "Wipro", "Accenture", "Swiggy", "Byjus"],
    "Android Developer": ["Samsung", "Paytm", "Zomato", "Ola", "Swiggy", "CRED"],
    "DevOps Engineer": ["AWS", "Azure", "Netflix", "Adobe", "IBM", "Oracle", "TCS"],
    "Database Administrator": ["Oracle", "SAP", "IBM", "Capgemini", "HCL", "Infosys"],
    "Software Tester / QA Engineer": ["Cognizant", "Wipro", "Infosys", "TCS", "Tech Mahindra"],
    "Cybersecurity Analyst": ["Cisco", "Palo Alto Networks", "Deloitte", "EY", "IBM"],
    "AI Engineer": ["OpenAI", "Google DeepMind", "Microsoft", "Amazon", "Adobe", "Bosch"]
}


# --- Sidebar ---
st.sidebar.header("Upload & Goal Selection")
resume_file = st.sidebar.file_uploader("📄 Upload Resume (PDF)", type=["pdf"])
goal = st.sidebar.selectbox("🎯 Career Goal", list(job_skills.keys()))


# --- Resume Analysis ---
if resume_file:
    resume_text = extract_text_from_pdf(resume_file)
    cleaned_resume = clean_text(resume_text)

    st.success("✅ Resume scanned successfully!")

    # --- Skill Match ---
    required_skills = job_skills[goal]
    matched = [s for s in required_skills if s in cleaned_resume]
    missing = [s for s in required_skills if s not in matched]
    match_percent = round((len(matched) / len(required_skills)) * 100, 2)

    st.subheader(f"🎯 Career Goal: {goal}")
    st.metric("Skill Match Percentage", f"{match_percent}%")

    col1, col2 = st.columns(2)
    with col1:
        st.write("**Matched Skills:**")
        st.write(", ".join(matched) if matched else "None")
    with col2:
        st.write("**Missing Skills:**")
        st.write(", ".join(missing) if missing else "None 🎉")

    st.progress(int(match_percent))

    if match_percent >= 80:
        st.success("You're nearly ready for this role! Just refine your portfolio and projects.")
    elif match_percent >= 50:
        st.warning("Good start! Strengthen the missing areas for a better chance.")
    else:
        st.error("You need to learn several new skills to qualify for this role.")

    # --- Udemy Recommendations ---
    if missing:
        st.subheader("📚 Recommended Udemy Courses")
        for skill in missing:
            if skill in udemy_courses:
                st.markdown(f"- [{skill.capitalize()} Course]({udemy_courses[skill]})")
            else:
                st.markdown(f"- {skill.capitalize()} (Search manually on Udemy)")

    # --- Interview Questions ---
    st.subheader("💬 Common Interview Questions")
    if goal in interview_questions:
        with st.expander(f"View Interview Questions for {goal}"):
            for q in interview_questions[goal]:
                st.markdown(f"- {q}")

    # --- Companies Hiring ---
    st.subheader("🏢 Top Companies Hiring for This Role")
    if goal in companies:
        st.markdown(", ".join(companies[goal]))
else:
    st.info("👆 Upload your resume and select your career goal to begin analysis.")
