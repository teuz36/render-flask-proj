from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory

app = Flask(__name__)
app.secret_key = "your_secret_key_here"

@app.route('/')
def home():
    profile = {
        "hero_intro": "Hello, I'm Mateuz Andrei Caspillo",
        "hero_highlight": "A Student from Laguna State Polytechnic University - Los Baños Campus."
    }
    return render_template("index.html", profile=profile)


@app.route('/about')
def about():
    about_info = {
        "title": "About Me",
        "content": (
            "Greetings! I am Mateuz Andrei T. Caspillo, I am currently 21 years old and a 3rd-year "
            "student taking Bachelor of Science in Computer Science at LSPU – Los Baños. "
            "The reason why I chose Computer Science is because I want to become a developer "
            "especially in game development and interactive software. "
            "As of now, I’m focused on improving my programming and design skills to reach my goals."
        ),
        "more_title": "Skills",
        "more_about": (
            "For the Programming I am skilled at is Python, C2, and Java. "
            "For the tools that I am skilled at is Figma, Canva, Excel, and HTML."

        ),
        "projects_title": "Projects",
        "projects": [
            "Time Management",
            "Adaptability",
            "Pagiging Kupal",
            "Teamwork",
            "Event Management System"
        ],
        "things_love": [
            "ENLYTE Science and Technology (2022)",
            "New normal na nutrisyon, sama-samang gawan ng solusyon! (2022)",
            "Challenges are facing in our Political life (2022)",
            "Nutrition for Adolescence (2023)",
            "Don't take the Risk, Get Educated (2023)"
        ],
        "things_fav": [
            "Gaming",
            "Sleep",
            "Listen to music",
            "Watch movies",
            "Learn new stuff"
        ],
        "things_award": [
            "Loyalty Award (2017)",
            "With Honors - JHS (2021)",
            "With Honors - SHS (2023)",
            "Dean’s Lister (2024, 2025)"
        ],
        "things_certifications": [
            "Crash Course on Python (Coursera, 2023)"
        ]

    }
    return render_template("about.html", about_info=about_info)


@app.route('/projects')
def projects():
    project_list = [
        {
            "title": "Shoetopia",
            "subtitle": "School Project",
            "description": "A simple online shoe store built using Figma.",
            "image": url_for('static', filename='shoe.jpg'),
            "tags": ["Figma"]
        },
        {
            "title": "FlyEasy Booking System",
            "subtitle": "School Project",
            "description": "A simple flight booking system using Java with a clean interface and backend integration.",
            "image": url_for('static', filename='flyeasy.jpg'),
            "tags": ["Java", "MySQL"]
        },
        {
            "title": "Smart Enroll",
            "subtitle": "School Project",
            "description": "A simple school enrollment system using C# and SQL Server to manage student records.",
            "image": url_for('static', filename='smart.jpg'),
            "tags": ["C#"]
        },
        {
            "title": "Event Management System",
            "subtitle": "School Project",
            "description": "A simple event management system using Python and SQLite for the data of the system.",
            "image": url_for('static', filename='event.jpg'),
            "tags": ["Python", "MySQL"]
        }
    ]
    return render_template("projects.html", project_list=project_list)


@app.route('/cv')
def cv():
    info = {
        "name": "Mateuz Andrei Caspillo",
        "title": "Computer Science Student",
        "objective": (
            "A passionate student eager to learn more about programming, AI, and software development. "
            "I aim to contribute my skills and creativity to real-world projects while continuing to grow as a developer."
        ),
        "education": [
            {"school": "Laguna State Polytechnic University – Los Baños Campus", "year": "2023 - Present", "major": "BS in Computer Science"},
            {"school": "Laguna State Polytechnic University – Los Baños Campus (Senior High School)", "year": "2021 - 2023", "major": "ICT Strand"},
            {"school": "Los Baños National High School", "year": "2017 - 2021", "major": ""}
        ],
        "experiences": [
            {"role": "Special Program for Employment of Students", "place": "Los Baños, Laguna", "year": "2022 - 2025"},
            {"role": "Work Immersion", "place": "Laguna State Polytechnic University – Los Baños Campus Guidance Office", "year": "2023"}
        ],
        "skills": {
            "Programming Languages": ["Python", "C#"],
            "Tools": ["HTML", "Figma", "Canva", "Excel"],
            "Other Skills": ["Hardworking", "Time Management", "Adaptability", "Collaboration"]
        },
        "certifications": ["Crash Course on Python (Coursera, 2023)"],
        "languages": ["English", "Filipino"],
        "contacts": [
            {"icon": "bi-facebook", "label": "Mateuz", "url": "https://www.facebook.com/teuztwt"},
            {"icon": "bi-telephone", "label": "09083569674", "url": "#"},
            {"icon": "bi-envelope-fill", "label": "caspillomateuz36@gmail.com", "url": "mailto:caspillomateuz36@gmail.com"},
            {"icon": "bi-linkedin", "label": "Mateuz Andrei Caspillo", "url": "https://www.linkedin.com/in/teuzcaspillo/"}
        ]
    }
    return render_template("cv.html", info=info)


@app.route('/download_cv')
def download_cv():
    return send_from_directory('static/files', 'Mateuz - CV.pdf', as_attachment=True)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    contact_info = {
        "title": "Contact Me",
        "subtitle": "Want to talk about something? Send me a message using the form or reach out through my socials!",
        "email": "caspillomateuz36@gmail.com",
        "facebook": "https://www.facebook.com/teuztwt",
        "instagram": "https://www.instagram.com/_mateuzz36/",
        "linkedin": "https://www.linkedin.com/in/teuzcaspillo/",
        "phone": "09083569674"
    }

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        print(f"New message from {name} ({email}): {message}")
        flash("Your message has been sent successfully!", "success")
        return redirect(url_for('thankyou'))

    return render_template("contact.html", contact_info=contact_info)


@app.route('/thankyou', methods=['GET'])
def thankyou():
    return render_template("thankyou.html")


if __name__ == "__main__":
    app.run(debug=True)