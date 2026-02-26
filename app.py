from pathlib import Path
import streamlit as st

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = current_dir / "assets" / "AnaBeatrizMacedo_Resume_.pdf"

# --- SETTINGS ---
PAGE_TITLE = "Ana Beatriz Macedo | Portfolio"
NAME = "Ana Beatriz Macedo"
TITLE = "Data Scientist | Machine Learning | AI"

SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/anabeatrizmacedo241/",
    "GitHub": "https://github.com/AnabeatrizMacedo241",
    "Email": "mailto:anabeatrizmacedo241@gmail.com",
    'Twitter': "https://x.com/AnaBeaM241",
}

# Professional Projects
PROFESSIONAL_PROJECTS = [
    {
        "title": "Delinquency Analysis & Credit Risk Modeling",
        "company": "Serasa Experian",
        "objective": "Develop statistical models and scoring systems to predict delinquency and credit risk across retail and corporate portfolios in the agribusiness sector.",
        "role": "Lead statistical modeling and validation of credit risk scores. Conduct pattern analysis across customer segments to identify early warning indicators of delinquency.",
        "impact": "Enhanced predictive accuracy (Gini/KS), leading to reduced portfolio losses and optimized monitoring for financial institutions.",
        "approach": "Applied advanced statistical modeling and machine learning tailored to agribusiness credit patterns. Validated models through rigorous backtesting and cross-validation.",
        "technologies": "Python • Statistical Modeling • Credit Risk Analysis • Machine Learning",
        "category": "Finance"
    },
    {
        "title": "Branch Occupancy Detection & Anomaly Analysis",
        "company": "Itaú Unibanco",
        "objective": "Identify and analyze overcrowding patterns in bank branches to improve operational efficiency and customer experience.",
        "role": "Developed PyTorch-based computer vision model to detect occupancy levels in real-time from branch camera feeds. Analyzed patterns across the branch network to identify systemic issues.",
        "impact": "Identified occupancy anomalies in 40% of branches. Discovered that 47% of problematic branches were affected by customer migration from closed locations, enabling strategic resource reallocation.",
        "approach": "Chose PyTorch for its flexibility in custom model architectures and real-time inference. Used transfer learning from pre-trained models. Major challenge was handling varying branch layouts and lighting conditions.",
        "technologies": "Python • PyTorch • Computer Vision • OpenCV • Deep Learning",
        "category": "Finance"
    },
    {
        "title": "AI-Powered Document Analysis",
        "company": "Itaú Unibanco",
        "objective": "Automate the extraction and analysis of information from thousands of audit documents to expand sample coverage and accelerate compliance reviews.",
        "role": "Designed end-to-end document processing pipeline using OCR, NLP, and generative AI. Implemented regex patterns for structured data extraction. Integrated OpenAI API for intelligent document summarization.",
        "impact": "Processes 2,000+ documents in seconds. Saved over 300 hours of manual labor per audit cycle. Significantly expanded audit sample size, enabling more comprehensive risk assessment.",
        "approach": "Selected PyTesseract for OCR due to accuracy with scanned documents. Used OpenAI API for complex extraction tasks. Primary challenge was handling document quality variations.",
        "technologies": "Python • PyTesseract • OpenAI API • NLP • Regex • OCR • Generative AI",
        "category": "Finance"
    },
    {
        "title": "Fraud Detection & Prevention System",
        "company": "Itaú Unibanco",
        "objective": "Build machine learning models to proactively identify fraudulent transactions and suspicious behavioral patterns before financial losses occur.",
        "role": "Developed and validated supervised learning models for fraud detection. Performed feature engineering on transactional and behavioral data. Collaborated with fraud investigation teams to refine model outputs.",
        "impact": "Prevented up to $125K in potential financial losses through early fraud detection. Enhanced the bank's ability to respond to emerging fraud patterns. Reduced false positive rate while maintaining high detection accuracy.",
        "approach": "Used ensemble methods combining decision trees and logistic regression for interpretability and performance. Addressed class imbalance through SMOTE and careful threshold selection.",
        "technologies": "Python • Scikit-learn • Machine Learning • Feature Engineering • SQL",
        "category": "Finance"
    },
    {
        "title": "Football Analyst with LLMs",
        "company": "Twelve Football",
        "objective": "Helped build AI-powered analytical tools that transform football match data into actionable tactical insights for coaches and clubs using large language models.",
        "role": "Applied prompt engineering to develop specialized AI agents for match and season analysis. Designed prompts that guide LLMs to generate accurate, contextual football analysis.",
        "impact": "Enabled automated generation of detailed match reports and tactical insights that previously required hours of analyst time. Provided scalable solution for analyzing multiple matches simultaneously.",
        "approach": "Leveraged OpenAI API for its strong reasoning capabilities. Structured prompts with clear context about football tactics and performance metrics. Challenge was ensuring consistency in analysis quality.",
        "technologies": "Python • OpenAI API • Prompt Engineering • NLP • Generative AI • Football Analytics",
        "category": "Sports Analytics"
    },
    {
        "title": "Player Performance & Threat Detection Model",
        "company": "Orlando City SC",
        "objective": "Built machine learning models to quantify match threats and evaluate player performance for scouting.",
        "role": "Built ML models analyzing match event data to identify dangerous situations and assess player contributions. Created Tableau dashboards visualizing performance metrics for technical staff.",
        "impact": "Provided data-driven insights supporting player recruitment decisions. Helped technical staff identify performance patterns not visible through traditional analysis.",
        "approach": "Selected gradient boosting models for their ability to capture non-linear relationships in football data. Challenge was defining 'threat' quantitatively.",
        "technologies": "Python • Scikit-learn • Tableau • Machine Learning • Sports Analytics",
        "category": "Sports Analytics"
    }
]

# Personal Projects
PERSONAL_PROJECTS = [
    {
        "title": "StatsBomb Football Analytics Platform",
        "description": "Comprehensive football analytics dashboard utilizing StatsBomb's free data API. Features tactical analysis tools, player comparison metrics, and match event visualization.",
        "video": "https://youtu.be/7gzVQaovHBw",
        "link": "https://anabeatrizmacedostatsbombapp.streamlit.app/",
        "technologies": "Python • StatsBomb • Tactical Analysis • Football Analytics • Streamlit",
        'category': 'Sports Analytics'
    },
     {
        "title": "Applying Artificial Intelligence to Enrich Visual Stimuli in Children's Cognitive Development: Animal Detection in Videos.",
        "description": "Capstone Project that explores the role of visual diversity in early childhood cognitive development and how AI can help address the lack of adequate visual stimuli. It proposes a methodology to identify key elements in digital videos using AI, focusing on an extended YOLO neural network to detect dogs. By doing so, the research aims to enhance cognitive stimulation for children up to age 2.",
        "link": "https://anabeatrizmacedo241-nba-shotschart-app-hello-zk4019.streamlit.app/",
        "technologies": "Python • Deep Learning • Computer Vision • Data Visualization • CNN • YOLO",
        'category': 'Computer Vision'
    },
    {
        "title": "Where's Wally Computer Vision Detector",
        "description": "Deep learning-based object detection system using extended YOLO architecture to locate Wally in complex images.",
        "video": "https://youtu.be/Kit9FLJ7C08",
        "link": "https://github.com/AnabeatrizMacedo241/WheresWally_Detector",
        "technologies": "Python • YOLO • Computer Vision • Deep Learning • PyTorch",
        'category': 'Computer Vision'
    },
    {
        "title": "NBA Player Role Classification Using ML Clustering",
        "description": "Applied unsupervised machine learning to identify nine distinct player archetypes in modern NBA. Created interactive Tableau dashboard tracking role evolution.",
        "link": "https://www.samford.edu/sports-analytics/fans/2023/Machine-Learning-Uncovers-Nine-Distinct-Player-Types-in-the-NBA",
        "dashboard": "https://public.tableau.com/app/profile/ana.beatriz.oliveira.de.macedo/viz/NBA_Cluster_Roles_AnaMacedo/Dashboard1",
        "technologies": "Python • Scikit-learn • K-means • Tableau • Machine Learning • Basketball Analytics",
        'category': 'Sports Analytics'
    },
    {
        "title": "NBA Shot Chart Application",
        "description": "Interactive web application for visualizing NBA player shot charts with advanced filtering capabilities. Built with Streamlit and NBA API, enabling real-time analysis of shooting patterns.",
        "video": "https://youtu.be/7rkKmtRIPlc",
        "link": "https://anabeatrizmacedo241-nba-shotschart-app-hello-zk4019.streamlit.app/",
        "technologies": "Python • Streamlit • NBA API • Data Visualization • Basketball Analytics",
        'category': 'Sports Analytics'
    },
    {
        "title": "Soccermatics Course Scouting Project",
        "description": "Built comprehensive player scouting dashboard for World Cup participants. Successfully identified high-value transfer targets including Cody Gakpo and Enzo Fernández.",
        "link": "https://public.tableau.com/app/profile/ana.beatriz.oliveira.de.macedo/viz/Qatar2022-PlayerScouting/Dashboard5",
        "video": "https://youtu.be/UHeFnqRyMvc",
        "technologies": "Python • Tableau • Football Analytics • Player Scouting • Data Visualization",
        'category': 'Sports Analytics'
    },
    {
        "title": "Twitter Account for Viz & ML",
        "description": "A dedicated space where I share data visualizations, sports analytics insights. I focus on transforming sports data statistics into intuitive plots to engage with the sports analytics community.",
        "link": "https://x.com/AnaBeaM241",
        "technologies": "Data Visualization • Matplotlib/Seaborn • Machine Learning • Sports Analytics",
        "category": "Sports Analytics"
    },
    {
        "title": "Euro 2020 Analysis API",
        "description": "Project developed for Women In Sports Data Hackathon (2022), providing endpoints for skills assessment and team and player metrics.",
        "link": "https://github.com/AnabeatrizMacedo241/Euro2020_API",
        "technologies": "Python • FastAPI • StatsBomb • Football Analytics • Hackaton",
        'category': 'Sports Analytics'
    }
]

import base64

def get_pdf_display_link(file_path, link_text):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    return f'<a href="data:application/pdf;base64,{base64_pdf}" target="_blank" class="publication-link">{link_text}</a>'

PUBLICATIONS = [
    {"title": "Applying Artificial Intelligence to Enrich Visual Stimuli in Early Childhood Cognitive Development: Animal Detection in Videos", 
    "file": "Capstone Project PT-BR.pdf",
    "year": "2024",
    "is_local": True
    },
    {"title": "Machine Learning Uncovers Nine Distinct Player Types in the NBA", "url": "https://www.samford.edu/sports-analytics/fans/2023/Machine-Learning-Uncovers-Nine-Distinct-Player-Types-in-the-NBA", "year": "2023"},
    {"title": "Predicting NBA MVP Contenders", "url": "https://www.samford.edu/sports-analytics/fans/2023/Predicting-NBA-MVP-Contenders", "year": "2023"},
    {"title": "Can Harry Kane Become the Second All-Time Scorer of the EPL?", "url": "https://www.samford.edu/sports-analytics/fans/2022/Can-Harry-Kane-become-the-second-All-time-scorer-of-the-EPL-and-surpass-Wayne-Rooney", "year": "2022"},
    {"title": "How Did Ronaldo's Return Affect Manchester United?", "url": "https://www.samford.edu/sports-analytics/fans/2022/How-Did-Ronaldos-Return-to-the-Premier-League-Affect-Manchester-Uniteds-Performance", "year": "2022"}
]

CONFERENCES = [
    {"name": "FAME: Football Analytics Modeling Experience", "year": "2023", "location": "Brazil", "role": "Speaker", "url": "https://salabufmg.github.io/FAME23/palestrantes/"},
    {"name": "COB Expo: Brazilian Olympic Committee Event", "year": "2024", "location": "Brazil", "role": "Speaker", "url": "https://cobexpo.com.br/palestrantes/"}
]

st.set_page_config(page_title=PAGE_TITLE, layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
* { font-family: 'Inter', sans-serif; margin: 0; padding: 0; box-sizing: border-box; }
body { background: #ffffff; }
.main { padding: 0; max-width: 100%; }

/* Sticky Navigation Bar */
.nav-bar {
    position: sticky;
    top: 0;
    z-index: 1000;
    background: #ffffff;
    border-bottom: 1px solid #e5e7eb;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    padding: 1rem 3rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.nav-brand { font-size: 1.25rem; font-weight: 700; color: #111827; }
.nav-links {
    display: flex;
    gap: 2rem;
    align-items: center;
}
.nav-links a {
    color: #4b5563;
    text-decoration: none;
    font-size: 0.95rem;
    font-weight: 500;
    padding: 0.5rem 1rem;
    border-radius: 6px;
    transition: all 0.2s;
}
.nav-links a:hover {
    background: #f3f4f6;
    color: #111827;
}

/* Content Container */
.content { padding: 3rem; max-width: 1400px; margin: 0 auto; }

/* Header */
.header {
    padding: 3rem 0;
    border-bottom: 1px solid #e5e7eb;
    margin-bottom: 4rem;
}
.header h1 {
    font-size: 3rem;
    font-weight: 700;
    color: #111827;
    margin-bottom: 0.75rem;
    letter-spacing: -0.02em;
}
.header .subtitle {
    font-size: 1.25rem;
    color: #6b7280;
    margin-bottom: 0.5rem;
}
.header .location {
    font-size: 1rem;
    color: #9ca3af;
}

/* Section Titles */
.section-title {
    font-size: 2rem;
    font-weight: 700;
    color: #111827;
    margin: 4rem 0 2.5rem 0;
    letter-spacing: -0.01em;
}

/* Professional Project Card */
.prof-project-card {
    background: #ffffff;
    border: 1px solid #e5e7eb;
    border-radius: 12px;
    padding: 3rem;
    margin-bottom: 2rem;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
}
.prof-project-header {
    margin-bottom: 2rem;
    padding-bottom: 1.5rem;
    border-bottom: 1px solid #f3f4f6;
}
.prof-project-title {
    font-size: 1.75rem;
    font-weight: 700;
    color: #111827;
    margin-bottom: 0.75rem;
}
.prof-project-meta {
    color: #6b7280;
    font-size: 1rem;
    font-weight: 500;
}
.prof-section {
    margin-bottom: 1.75rem;
}
.prof-section-title {
    font-size: 0.875rem;
    font-weight: 700;
    color: #6b7280;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: 0.75rem;
}
.prof-section-content {
    color: #374151;
    line-height: 1.8;
    font-size: 1rem;
}
.prof-tech {
    color: #6b7280;
    font-size: 0.95rem;
    margin-top: 2rem;
    padding-top: 1.5rem;
    border-top: 1px solid #f3f4f6;
    font-weight: 500;
}

/* Personal Project Card */
.personal-project {
    background: #ffffff;
    border: 1px solid #e5e7eb;
    border-radius: 12px;
    padding: 0;
    overflow: hidden;
    transition: all 0.3s ease;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
}
.personal-project:hover {
    box-shadow: 0 8px 16px rgba(0,0,0,0.1);
    transform: translateY(-4px);
}
.personal-project-content {
    padding: 2rem;
}
.personal-project-title {
    font-size: 1.25rem;
    font-weight: 700;
    color: #111827;
    margin-bottom: 1rem;
}
.personal-project-desc {
    color: #4b5563;
    line-height: 1.7;
    font-size: 0.95rem;
    margin-bottom: 1.5rem;
}
.personal-project-tech {
    color: #6b7280;
    font-size: 0.875rem;
    font-weight: 500;
    margin-bottom: 1.5rem;
}
.personal-project-links {
    display: flex;
    gap: 1rem;
    flex-wrap: wrap;
}
.personal-project-link {
    color: #111827;
    text-decoration: none;
    font-size: 0.9rem;
    font-weight: 500;
    padding: 0.5rem 1rem;
    border: 1px solid #e5e7eb;
    border-radius: 6px;
    transition: all 0.2s;
}
.personal-project-link:hover {
    background: #f9fafb;
    border-color: #d1d5db;
}

/* Carousel Controls */
.carousel-controls {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 2rem;
}
.carousel-counter {
    text-align: center;
    color: #6b7280;
    font-size: 0.95rem;
    font-weight: 500;
}

/* Publication */
.publication {
    background: #ffffff;
    border: 1px solid #e5e7eb;
    border-left: 4px solid #111827;
    padding: 1.75rem 2rem;
    margin-bottom: 1.25rem;
    border-radius: 8px;
    transition: all 0.2s;
}
.publication:hover {
    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
}
.publication-title {
    font-size: 1.1rem;
    font-weight: 600;
    margin-bottom: 0.5rem;
}
.publication-title a {
    color: #111827;
    text-decoration: none;
}
.publication-title a:hover {
    color: #4b5563;
}
.publication-meta {
    color: #6b7280;
    font-size: 0.9rem;
}

/* Conference */
.conference {
    background: #f9fafb;
    border: 1px solid #e5e7eb;
    border-radius: 12px;
    padding: 2rem;
    margin-bottom: 1.5rem;
}
.conference-name {
    font-size: 1.3rem;
    font-weight: 700;
    color: #111827;
    margin-bottom: 0.75rem;
}
.conference-meta {
    color: #6b7280;
    font-size: 1rem;
    margin-bottom: 1.25rem;
}
.conference-link {
    color: #111827;
    text-decoration: none;
    font-size: 0.95rem;
    font-weight: 500;
    padding: 0.5rem 1.25rem;
    border: 1px solid #e5e7eb;
    border-radius: 6px;
    display: inline-block;
    transition: all 0.2s;
}
.conference-link:hover {
    background: #ffffff;
    border-color: #d1d5db;
}

/* Buttons */
.stButton button {
    background: #111827;
    color: white;
    border: none;
    padding: 0.75rem 2rem;
    font-size: 1rem;
    border-radius: 8px;
    font-weight: 600;
    transition: all 0.2s;
}
.stButton button:hover {
    background: #1f2937;
    transform: translateY(-1px);
}
.stButton button:disabled {
    background: #d1d5db;
    cursor: not-allowed;
    transform: none;
}

.stDownloadButton button {
    background: #111827;
    color: white;
    border: none;
    padding: 0.75rem 2rem;
    font-size: 1rem;
    border-radius: 8px;
    font-weight: 600;
}

/* Video */
[data-testid="stVideo"] {
    border-radius: 8px;
    overflow: hidden;
    border: 1px solid #e5e7eb;
    margin-top: 1.5rem;
}

/* Hide Streamlit Branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Smooth Scroll */
html { scroll-behavior: smooth; }

/* ========== MOBILE RESPONSIVE ========== */
@media (max-width: 768px) {
    /* Force columns to stack */
    [data-testid="column"] {
        width: 100% !important;
        flex: 100% !important;
        min-width: 100% !important;
    }
    
    /* Navigation */
    .nav-bar { 
        padding: 1rem;
        flex-direction: column;
        gap: 0.75rem;
        align-items: stretch;
    }
    .nav-brand {
        text-align: center;
        font-size: 1.1rem;
    }
    .nav-links {
        flex-direction: column;
        gap: 0.5rem;
        width: 100%;
    }
    .nav-links a {
        text-align: center;
        padding: 0.75rem;
        width: 100%;
    }
    
    /* Content */
    .content { 
        padding: 1rem;
    }
    
    /* Header */
    .header { 
        padding: 2rem 0;
        margin-bottom: 2rem;
    }
    .header h1 { 
        font-size: 2rem;
        text-align: center;
    }
    .header .subtitle {
        font-size: 1.1rem;
        text-align: center;
    }
    .header .location {
        text-align: center;
    }
    
    /* Section Titles */
    .section-title { 
        font-size: 1.5rem;
        margin: 2.5rem 0 1.5rem 0;
    }
    
    /* Professional Projects */
    .prof-project-card {
        padding: 1.5rem;
        margin-bottom: 1.5rem;
    }
    .prof-project-title {
        font-size: 1.3rem;
    }
    .prof-project-meta {
        font-size: 0.9rem;
    }
    .prof-section-content {
        font-size: 0.95rem;
        line-height: 1.6;
    }
    .prof-tech {
        font-size: 0.85rem;
    }
    
    /* Personal Projects */
    .personal-project-content {
        padding: 1.5rem;
    }
    .personal-project-title {
        font-size: 1.1rem;
    }
    .personal-project-desc {
        font-size: 0.9rem;
    }
    
    /* Publications */
    .publication {
        padding: 1.25rem 1.5rem;
    }
    .publication-title {
        font-size: 1rem;
    }
    
    /* Conferences */
    .conference {
        padding: 1.5rem;
    }
    .conference-name {
        font-size: 1.1rem;
    }
    .conference-meta {
        font-size: 0.9rem;
    }
    
    /* Buttons */
    .stButton button {
        width: 100%;
        padding: 0.75rem 1rem;
        font-size: 0.95rem;
    }
    
    .stDownloadButton button {
        width: 100%;
    }
    
    /* Carousel controls */
    .carousel-counter {
        font-size: 0.85rem;
    }
    
    /* Streamlit selectbox */
    [data-testid="stSelectbox"] {
        width: 100%;
    }
}

/* Extra small devices */
@media (max-width: 575px) {
    .nav-bar {
        padding: 0.75rem;
    }
    
    .content {
        padding: 0.75rem;
    }
    
    .header h1 {
        font-size: 1.75rem;
    }
    
    .section-title {
        font-size: 1.3rem;
    }
    
    .prof-project-card {
        padding: 1.25rem;
    }
    
    .prof-project-title {
        font-size: 1.2rem;
    }
    
    .personal-project-content {
        padding: 1.25rem;
    }
}
</style>
""", unsafe_allow_html=True)

# Navigation Bar
st.markdown(f"""
<div class="nav-bar">
    <div class="nav-brand">{NAME}</div>
    <div class="nav-links">
        <a href="#professional-projects">Professional</a>
        <a href="#personal-projects">Personal</a>
        <a href="#publications">Publications</a>
        <a href="#conferences">Conferences</a>
        <a href="{SOCIAL_MEDIA['LinkedIn']}" target="_blank">LinkedIn</a>
        <a href="{SOCIAL_MEDIA['GitHub']}" target="_blank">GitHub</a>
        <a href="{SOCIAL_MEDIA['Twitter']}" target="_blank">Twitter</a>
    </div>
</div>
""", unsafe_allow_html=True)

try:
    with open(resume_file, "rb") as pdf_file:
        st.download_button("Download Resumé", pdf_file.read(), file_name="Ana_Beatriz_Macedo_Resume.pdf", mime="application/pdf")
except: pass

# Professional Projects
st.markdown('<div id="professional-projects" class="section-title">Professional Projects</div>', unsafe_allow_html=True)

categories = ["All"] + list(set(p['category'] for p in PROFESSIONAL_PROJECTS))
selected_category = st.selectbox("Filter by topic:", categories)

filtered_projects = [
    p for p in PROFESSIONAL_PROJECTS 
    if selected_category == "All" or p['category'] == selected_category
]

if 'last_category' not in st.session_state or st.session_state.last_category != selected_category:
    st.session_state.current_project = 0
    st.session_state.last_category = selected_category

start_idx = st.session_state.current_project
display_projects = filtered_projects[start_idx : start_idx + 2]

cols = st.columns(2)
for i, p in enumerate(display_projects):
    with cols[i]:
        st.markdown(f"""
        <div class="prof-project-card">
            <div class="prof-project-header">
                <h3 class="prof-project-title">{p['title']}</h3>
                <div class="prof-project-meta">{p['company']}</div>
            </div>
            <div class="prof-section">
                <div class="prof-section-title">Objective</div>
                <div class="prof-section-content">{p['objective']}</div>
            </div>
            <div class="prof-section">
                <div class="prof-section-title">Impact</div>
                <div class="prof-section-content">{p['impact']}</div>
            </div>
            <div class="prof-tech"><strong>Technologies:</strong> {p['technologies']}</div>
        </div>
        """, unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    if st.button("← Previous", disabled=start_idx == 0):
        st.session_state.current_project = max(0, start_idx - 2)
        st.rerun()

with col2:
    total = len(filtered_projects)
    end_num = min(start_idx + 2, total)
    st.markdown(f'<div class="carousel-counter">Showing {start_idx + 1}-{end_num} of {total}</div>', unsafe_allow_html=True)

with col3:
    if st.button("Next →", disabled=start_idx + 2 >= total):
        st.session_state.current_project += 2
        st.rerun()

# Personal Projects
st.markdown('<div id="personal-projects" class="section-title">Personal & Academic Projects</div>', unsafe_allow_html=True)

personal_categories = ["All"] + list(set(p.get('category', 'General') for p in PERSONAL_PROJECTS))
selected_personal_cat = st.selectbox("Filter by topic:", personal_categories, key="personal_filter")

filtered_personal = [
    p for p in PERSONAL_PROJECTS 
    if selected_personal_cat == "All" or p.get('category', 'General') == selected_personal_cat
]

if not filtered_personal:
    st.info("No projects found for this category.")
else:
    for i in range(0, len(filtered_personal), 2):
        cols = st.columns(2, gap="large")
        for idx, proj in enumerate(filtered_personal[i:i+2]):
            with cols[idx]:
                with st.container():
                    st.markdown(f"""
                    <div class="personal-project">
                        <div class="personal-project-content">
                            <h3 class="personal-project-title" style="margin-bottom:0px;">{proj['title']}</h3>
                            <span style="font-size: 0.8em; color: #888;">{proj.get('category', '')}</span>
                            <p class="personal-project-desc" style="margin-top:10px;">{proj['description']}</p>
                            <div class="personal-project-tech"><strong>{proj['technologies']}</strong></div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    l_col1, l_col2 = st.columns(2)
                    if proj.get("link"):
                        l_col1.link_button("View Project", proj["link"], use_container_width=True)
                    if proj.get("dashboard"):
                        l_col2.link_button("Dashboard", proj["dashboard"], use_container_width=True)
                    
                    if proj.get('video'):
                        with st.expander("📺 Watch Demo"):
                            st.video(proj['video'])
                st.markdown("---")

# Publications
import base64

def get_pdf_base64(file_path):
    try:
        with open(file_path, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        return f"data:application/pdf;base64,{base64_pdf}"
    except FileNotFoundError:
        return "#"

st.markdown('<div id="publications" class="section-title">Publications</div>', unsafe_allow_html=True)

for pub in PUBLICATIONS:
    if pub.get('is_local'):
        target_link = get_pdf_base64(pub['file'])
        source_label = "Capstone Project (PT-BR)"
    else:
        target_link = pub['url']
        source_label = "Samford University Center for Sports Analytics"

    st.markdown(f"""
    <div class="publication">
        <div class="publication-title">
            <a href="{target_link}" target="_blank">{pub['title']}</a>
        </div>
        <div class="publication-meta">{pub['year']} • {source_label}</div>
    </div>
    """, unsafe_allow_html=True)

# Conferences
st.markdown('<div id="conferences" class="section-title">Conference Presentations</div>', unsafe_allow_html=True)

cols = st.columns(2, gap="large")
for idx, conf in enumerate(CONFERENCES):
    with cols[idx]:
        st.markdown(f"""
        <div class="conference">
            <div class="conference-name">{conf['name']}</div>
            <div class="conference-meta">{conf['year']} • {conf['location']} • {conf['role']}</div>
            <a href="{conf['url']}" target="_blank" class="conference-link">Event Details</a>
        </div>
        """, unsafe_allow_html=True)

st.markdown('<div style="text-align: center; padding: 4rem 0 2rem 0; border-top: 1px solid #e5e7eb; color: #9ca3af;">Ana Beatriz Macedo | Data Scientist</div>', unsafe_allow_html=True)