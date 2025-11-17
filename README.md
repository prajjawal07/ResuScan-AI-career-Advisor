# 🎯 ResuScan Career Advisor

**AI-Powered Resume Analyzer and Career Recommendation System**

ResuScan Career Advisor Pro is a smart NLP-based application that evaluates resumes, analyzes skill gaps, and recommends career paths, learning resources, and top companies hiring for specific roles.  
It’s built using **Streamlit**, **Python**, and **Natural Language Processing (NLP)** to help students and professionals align their skills with industry demands.

---

## 🚀 Features

✅ **Resume Parsing & Text Extraction**  
Extracts clean text from uploaded PDF resumes using **PyMuPDF (fitz)**.

✅ **Skill Matching & Scoring**  
Compares resume content against predefined job role requirements using **TF-IDF vectorization** and **cosine similarity**.  

✅ **Career Fit Percentage**  
Generates a score that indicates how closely the resume matches the selected career goal.

✅ **Skill Gap Identification**  
Lists missing and matched skills with intuitive visual indicators.

✅ **Smart Recommendations**
- **Learning Path:** Suggests Udemy courses for missing skills  
- **Companies Hiring:** Displays top organizations hiring for the chosen role  
- **Interview Preparation:** (Optional feature) Role-based question bank for practice  

✅ **Interactive UI**  
A clean, grayscale-themed **Streamlit UI** — minimal, fast, and elegant.

---

## 🧠 How It Works

1. **Upload your Resume (PDF)**  
   The system extracts and preprocesses text using `PyMuPDF` and `Regex`.

2. **Select Career Goal**  
   Choose from predefined job profiles (e.g., Data Analyst, Python Developer, ML Engineer, etc.).

3. **TF-IDF + Cosine Similarity Matching**  
   Your resume is vectorized using **TF-IDF**, and compared with the target role’s required skills to compute similarity and fit score.

4. **Skill Analysis & Visualization**  
   Displays matched and missing skills, with a dynamic progress bar for percentage match.

5. **Recommendations**  
   - Missing skills → Udemy course links  
   - Role-based interview questions (future addition)  
   - Companies hiring for that position  

---

## 🛠️ Tech Stack

| Category | Tools / Libraries |
|-----------|-------------------|
| **Frontend** | Streamlit |
| **Backend / NLP** | Python, scikit-learn, NLTK, re |
| **Resume Parsing** | PyMuPDF (fitz) |
| **Similarity Engine** | TF-IDF Vectorizer, Cosine Similarity |
| **Dataset** | Predefined skill-role mapping dictionary |
| **UI Design** | Streamlit layout customization (no external CSS) |

---
## 🚀 Live Demo
[Click here to open the deployed app](https://your-streamlit-link.streamlit.app)

## 📸 Preview

<img width="1905" height="1056" alt="image" src="https://github.com/user-attachments/assets/8201110e-783c-41aa-9ff9-e70cb7edec48" />

