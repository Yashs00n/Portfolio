# app.py
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
from datetime import datetime

app = Flask(__name__)

# Sample resume data - in a real application, you might load this from a JSON file or database
resume_data = {
    "personal_info": {
        "name": "Yashpal Singh",
        "title": "Junior Software Engineer",
        "email": "yashpalsingh0746@gmail.com",
        "phone": "+91 7818042841",
        "location": "Rupnagar, Punjab, India",
        "linkedin": "https://www.linkedin.com/in/yashpal-singh-971854265/",
        "github": "https://github.com/Yashs00n",
        "summary": "Skilled Software Engineer specializing in Python and JavaScript development. Focused on building full-stack applications that are efficient, scalable, and easy to maintain. Experienced in using cloud technologies to deploy and manage modern, reliable systems. Committed to writing clean, effective code and continuously improving development practices."
    },
    "education": [
        {
            "degree": "Btech. in Computer Science with Artificial Intelligence And Machine Learning",
            "institution": "Lamrin Tech Skills University Punjab",
            "location": "Punjab,India",
            "period": "2023 - 2027",
            "description": "Focus on Software Engineering and Machine Learning. Graduated with a 7.8 GPA."
        },
        {
            "degree": "Diploma in Computer Science",
            "institution": "Mahamaya of Information Technology Aligarh",
            "location": "Uttar Pradesh, India",
            "period": "2021 - 2023",
            "description": "Focus on Software Engineering and Machine Learning.."
        }
    ],
    "skills": {
        "technical": [
            "Python", "JavaScript", "React", "Node.js", "Django", "Flask", 
            "PostgreSQL", "MongoDB",
            "CI/CD", "Git", "RESTful APIs",
        ],
        "soft": [
            "Team Leadership", "Project Management", "Agile Methodologies", 
            "Technical Documentation", "Mentoring", "Problem Solving",
            "Communication", "Time Management"
        ]
    },
    "projects": [
        {
            "title": "E-commerce Platform",
            "description": "Developed a full-stack e-commerce platform with user authentication, product management, and payment processing integration.",
            "technologies": ["React", "Node.js", "MongoDB", "Stripe API"],
        },
        {
            "title": "Task Management System",
            "description": "Created a collaborative task management system with real-time updates and team collaboration features.",
            "technologies": ["Python", "Django", "PostgreSQL", "WebSockets"],
        }
    ],
    "certifications": [
        {
            "name": "Geodata in Machine learning with Python",
            "issuer": "Isro",
            "date": "2025"
        },
        {
            "name": "Young Profesinal ",
            "issuer": "TCSion",
            "date": "2024"
        }
    ],
    "languages": [
        {"name": "English", "proficiency": "Professional Working Proficiency"},
        {"name": "Hindi", "proficiency": "Native"},
        {"name": "Urdu", "proficiency": "Intermediate"}
    ]
}

# Context processor to add the current year to all templates
@app.context_processor
def inject_current_year():
    return {'current_year': datetime.now().year}

@app.route('/')
def home():
    return render_template('resume.html', resume=resume_data)

@app.route('/download')
def download_resume():
    # Ensure the file exists before serving it
    file_path = os.path.join('static', 'files', 'resume.pdf')
    if not os.path.exists(file_path):
        return "Resume file not found.", 404
    return send_from_directory('static/files', 'resume.pdf')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Process form data with fallback for missing fields
        name = request.form.get('name', 'Anonymous')
        email = request.form.get('email', 'No email provided')
        message = request.form.get('message', 'No message provided')
        
        # For demonstration, just redirect back with a success parameter
        return redirect(url_for('contact', success=True))
    
    success = request.args.get('success', False)
    return render_template('contact.html', resume=resume_data, success=success)

if __name__ == '__main__':
    app.run(debug=True)