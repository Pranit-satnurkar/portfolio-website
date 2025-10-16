from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import os # <-- 1. Import os module

# 2. Define absolute paths for templates and static folders
template_dir = os.path.abspath('./templates')
static_dir = os.path.abspath('./static')

# 3. Pass the paths to the Flask app
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
CORS(app)

# --- Your Personal Data ---
your_data = {
    "experience": [
        {
            "date": "2025",
            "title": "Data Analyst Intern",
            "company": "Lazarus Network",
            "company_url": "#",
            "description_points": [
                "Cleaned and preprocessed multiple large-scale datasets using Python (Pandas) and SQL, improving data accuracy by over 95% and enabling reliable downstream analysis.",
                "Developed and automated data validation scripts, which reduced data-related errors in reporting by 30%."
            ],
            "tags": ["Python", "Pandas", "SQL"]
        },
        {
            "date": "2023 — 2024",
            "title": "Assistant Engineer",
            "company": "NJS Engineers India Pvt. Ltd.",
            "company_url": "#",
            "description_points": [
                "Prepared accurate cost estimates for JMM & MJP schemes, leading to effective risk mitigation.",
                "Supervised site activities to maintain project timelines and budgets, resulting in strong client relationships."
            ],
            "tags": ["Cost Estimation", "Site Supervision", "Civil Engineering"]
        },
        {
            "date": "2022",
            "title": "University Internship",
            "company": "Mehendale & Associates",
            "company_url": "#",
            "description_points": [
                "Assisted with technical analysis and estimation of structural elements, developing foundational skills in quantitative data."
            ],
            "tags": ["Structural Analysis", "Quantitative Data"]
        },
        {
            "date": "Ongoing",
            "title": "Guitar Teacher & Performer",
            "company": "RSL Certified Instructor · Freelance",
            "company_url": "#",
            "description_points": [
                "Teaching Electric Guitar, Acoustic Guitar, and Piano, judging competitions, and performing at university events."
            ],
            "tags": ["Music Education", "Live Performance", "Piano", "Guitar"]
        }
    ],
    "projects": [
        {
            "title": "Men's T-Shirt Sales Performance Dashboard",
            "description": "Built a Power BI dashboard that analyzed sales data from Azure SQL, identifying key profitability trends that informed a new pricing strategy projected to increase margins by 15%.",
            "tags": ["Power BI", "Azure SQL", "Data Analysis"],
            "url": "#"
        },
        {
            "title": "Production Environment Inventory Analysis",
            "description": "Created a Power BI dashboard to monitor inventory, which identified supply shortages 25% faster and provided insights that helped reduce carrying costs by 10%.",
            "tags": ["Power BI", "MySQL", "Inventory Management"],
            "url": "#"
        },
        {
            "title": "Interactive Music Trends Dashboard",
            "description": "Engineered a dynamic dashboard using JavaScript and the Spotify API to visualize music trends, increasing user engagement with historical data by 40%.",
            "tags": ["JavaScript", "Spotify API", "Chart.js", "Data Viz"],
            "url": "#"
        },
        {
            "title": "Automated Sales Report Generator",
            "description": "Created a Python script to automate the generation of weekly sales reports from raw transactional data, saving an estimated 5 hours of manual work per week.",
            "tags": ["Python", "Pandas", "Matplotlib", "Automation"],
            "url": "#"
        },
        {
            "title": "Python Web Scraper",
            "description": "Developed a robust web scraper to extract structured product information and pricing data from e-commerce sites, parsing the collected data into a clean CSV format for market analysis.",
            "tags": ["Python", "Beautiful Soup", "Requests", "Pandas"],
            "url": "#"
        },
        {
            "title": "Housing Market Analysis Dashboard",
            "description": "Developed a comprehensive dashboard using Google BigQuery data to visualize housing market trends, providing key insights that helped identify undervalued investment opportunities.",
            "tags": ["Power BI", "Google BigQuery"],
            "url": "#"
        }
    ],
    "blog_posts": [
        {
            "id": 1, "title": "The Price of Ascent: When the Summit Feels Empty", "date": "2025-05-18",
            "excerpt": "A reflection on the surprising feelings of emptiness that can accompany the achievement of a long-sought goal.",
            "category": "Personal Growth", "url": "https://deepcurrentswrites.blogspot.com/2025/05/the-price-of-ascent-when-summit-feels.html"
        },
        {
            "id": 2, "title": "The Illusion of Perfection: A Hard-Learned Truth", "date": "2025-02-22",
            "excerpt": "Exploring the journey of letting go of perfectionism and embracing the value of progress over flawlessness.",
            "category": "Mindset", "url": "https://deepcurrentswrites.blogspot.com/2025/02/the-llusion-of-perfection-hard-learned.html"
        }
    ],
    "social_links": {
        "github": "https://github.com/Pranit-satnurkar/",
        "linkedin": "https://www.linkedin.com/in/pranit-satnurkar-143806240/",
        "youtube": "https://www.youtube.com/@Pranit.Guitarist",
        "adobe_stock": "https://stock.adobe.com/in/contributor/208823292/Pranit?asset_id=533002621",
        "goodreads": "https://www.goodreads.com/user/show/189489858-pranit",
        "discord": "https://discordapp.com/users/729015366340050954",
        "email": "mailto:pranit.satnurkar@gmail.com"
    }
}


@app.route('/api/data')
def get_data():
    return jsonify(your_data)


@app.route('/contact', methods=['POST'])
def handle_contact():
    data = request.json
    print(f"Contact form submitted: {data}")
    return jsonify({"status": "success", "message": "Message received!"})


@app.route('/')
def home():
    return render_template('index.html', data=your_data)


if __name__ == '__main__':
    app.run(debug=True)
