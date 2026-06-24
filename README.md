
# AI Job Agent🤖💼

An AI-powered job search agent that leverages large language models to analyze job descriptions, match candidate skills, optimize resumes, and automate application submissions.
An autonomous, AI-powered assistant designed to automate and optimize the job search process. The system parses resumes, calculates ATS scores, analyzes skill gaps using Generative AI, and fetches real-time job recommendations.

---

## 🚀 Features

* **📄 Resume Upload & Parsing**
  * Upload resumes in PDF format.
  * Extracts text automatically from the uploaded resume.
* **🧠 AI Resume Analysis**
  * Uses Generative AI to analyze the resume.
  * Generates detailed insights about the candidate's profile.
* **🛠 Skill Extraction**
  * Detects technical and professional skills from the resume.
  * Displays extracted skills in an interactive dashboard.
* **📊 ATS Score Calculation**
  * Calculates an Applicant Tracking System (ATS) score.
  * Helps users understand how ATS-friendly their resume is.
* **🎯 Skill Gap Analysis**
  * Identifies missing skills required for recommended jobs.
  * Helps users improve their employability.
* **💼 Job Recommendation System**
  * Matches resume skills against job requirements.
  * Provides ranked job recommendations with match percentages.
* **🌐 Live Job Search Integration**
  * Fetches real-time job opportunities using Job Search APIs.
  * Displays company name, location, and application links.
* **🎨 Interactive Dashboard**
  * Modern and responsive user interface.
  * **Displays:** Resume details, ATS score, Skill analysis, Missing skills, AI insights, and Recommended jobs.

---

## 🔄 System Workflow

```text
Resume Upload 
     ↓ 
Resume Parsing 
     ↓ 
Skill Extraction 
     ↓ 
ATS Score Analysis 
     ↓ 
Skill Gap Detection 
     ↓ 
AI Resume Analysis 
     ↓ 
Job Recommendation Engine 
     ↓ 
Live Job Search API 
     ↓ 
Interactive Dashboard
```

---

## 🛠️ Technology Stack

### Frontend
* HTML5
* CSS3
* Jinja2 Templates

### Backend
* Python
* Flask

### Libraries
* `pdfplumber` (PDF text extraction)
* `pandas` (Data manipulation)
* `requests` (API HTTP requests)
* `google-generativeai` (Gemini API integration)
* `reportlab` (PDF generation)

### APIs Used
RAPIDAPI_KEY=c9d7d5dee6msh20246da560c866p1d30c8jsn9f1aff6c6933
NGROK_AUTHTOKEN=3FRMxgVGB0CguFPPVbCXKMIQeTx_3WcndHgbZ13vchUjnGjGx

---

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd ai-job-agent
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your Environment Variables:**
   Create a `.env` file in the root directory and add your API keys:
   ```env
   GEMINI_API_KEY=your_gemini_key_here
   RAPIDAPI_KEY=your_rapidapi_key_here
   FLASK_SECRET_KEY=your_secret_key
   ```

5. **Run the application:**
   ```bash
   python app.py
   ```
   Open `http://127.0.0.1:5000` in your web browser.
