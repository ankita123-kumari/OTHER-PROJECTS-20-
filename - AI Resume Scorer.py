import tkinter as tk
from tkinter import filedialog, messagebox
import pdfplumber
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Define keywords for scoring
skills_keywords = ["Python", "Flask", "API development", "Machine Learning", "Backend development"]
experience_keywords = ["developer", "engineer", "software", "programming", "experience", "project"]

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())
    return text

# Function to preprocess text
def preprocess_resume(resume_text):
    doc = nlp(resume_text.lower())
    return " ".join([token.lemma_ for token in doc if not token.is_stop and token.is_alpha])

# Function to score resume
def score_resume(resume_text):
    processed_text = preprocess_resume(resume_text)
    vectorizer = TfidfVectorizer(vocabulary=skills_keywords + experience_keywords)
    vectorized_resume = vectorizer.fit_transform([processed_text])
    match_score = vectorized_resume.toarray().sum()
    return match_score

# Function to analyze resume
def analyze_resume():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if not file_path:
        return

    resume_text = extract_text_from_pdf(file_path)
    score = score_resume(resume_text)

    messagebox.showinfo("Resume Analysis", f"Resume Score: {score:.2f}\n\nExtracted Text:\n{resume_text[:500]}...")

# GUI Setup
root = tk.Tk()
root.title("AI-Powered Resume Scorer")

tk.Label(root, text="Upload a Resume (PDF)").pack(pady=10)
tk.Button(root, text="Analyze Resume", command=analyze_resume).pack(pady=10)

root.mainloop()