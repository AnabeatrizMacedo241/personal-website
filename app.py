from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "AnaBeatrizMacedo_Resumé_EN.pdf"
profile_pic = current_dir / "assets" / "new-profile-modified.png"
twitter_pic = current_dir / "assets"/ "twitter.png"
tcc = current_dir / "assets"/ "Capstone Project PT-BR.pdf"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Portfolio|Ana Beatriz Macedo"
PAGE_ICON = ":wave:"
NAME = "Ana Beatriz Macedo"
DESCRIPTION = """Data Scientist | Sports Analyst"""
skills = " Machine & Deep Learning | Generative AI"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/anabeatrizmacedo241/",
    "GitHub": "https://github.com/AnabeatrizMacedo241",
    "Twitter": "https://twitter.com/AnaBeaM241",
}
publications = {"Machine Learning Uncovers Nine Distinct Player Types in the NBA":"https://www.samford.edu/sports-analytics/fans/2023/Machine-Learning-Uncovers-Nine-Distinct-Player-Types-in-the-NBA?image",
    "Can Harry Kane become the second All-time scorer of the EPL and surpass Wayne Rooney?": "https://www.samford.edu/sports-analytics/fans/2022/Can-Harry-Kane-become-the-second-All-time-scorer-of-the-EPL-and-surpass-Wayne-Rooney?image",
    "How Did Ronaldo’s Return to the Premier League Affect Manchester United’s Performance?": "https://www.samford.edu/sports-analytics/fans/2022/How-Did-Ronaldos-Return-to-the-Premier-League-Affect-Manchester-Uniteds-Performance?image",
    "Sports Brand Affinity Among Universities": "https://www.samford.edu/sports-analytics/fans/2022/Sports-Brand-Affinity-Among-Universities?image"
}

APPS = {"NBA Shot Chart App":"https://anabeatrizmacedo241-nba-shotschart-app-hello-zk4019.streamlit.app/",
       "Statsbomb Free Data Extraction":"https://statsbombchartapp-anabeatrizmacedo.streamlit.app/"}
PROJECTS = {"NBA All-time Points Analysis API": "https://github.com/AnabeatrizMacedo241/NBA_AllTimePTS_API",
    "Predicting Covid-19 and recommending ideal doctors": "https://github.com/AnabeatrizMacedo241/CovidPrediction_DoctorRecommendation"
}

#st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout="centered",
    initial_sidebar_state="auto",
)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.write(skills)

# --- SOCIAL LINKS ---
st.markdown(
    """
    <style>
    .social-icons a {
        margin-right: 10px;
        text-decoration: none;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Create columns for social media icons and the resumé button
col1, col2 = st.columns([3, 1])  # Adjust column widths as needed

with col1:
    st.markdown(
        """
        <div class="social-icons">
            <a href="https://www.linkedin.com/in/anabeatrizmacedo241/" target="_blank">
                <img src="https://img.shields.io/badge/LinkedIn-blue?logo=linkedin&style=for-the-badge" alt="LinkedIn">
            </a>
            <a href="https://github.com/AnabeatrizMacedo241" target="_blank">
                <img src="https://img.shields.io/badge/GitHub-black?logo=github&style=for-the-badge" alt="GitHub">
            </a>
            <a href="https://twitter.com/AnaBeaM241" target="_blank">
                <img src="https://img.shields.io/badge/Twitter-blue?logo=twitter&style=for-the-badge" alt="Twitter">
            </a>
            <a href="anabeatrizmacedo241@gmail.com" target="_blank">
                <img src="https://img.shields.io/badge/Email-red?logo=gmail&style=for-the-badge" alt="Email">
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    with open(resume_file, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    st.download_button(
        label="Resumé",
        data=PDFbyte,
        file_name="Ana_Beatriz_Macedo_Resume.pdf",
        mime="application/pdf",
    )

# --- Projects ---
st.write('\n')
st.subheader("Projects")
st.write("---")
col3, col4, col5 = st.columns(3)
with col3:
    video1_description = st.write("[NBA Shot Chart App](https://anabeatrizmacedo241-nba-shotschart-app-hello-zk4019.streamlit.app/)")
    video1_url = "https://youtu.be/7rkKmtRIPlc"
    st.video(video1_url)

with col4:
    video2_description = st.write("[Statsbomb Analysis App](https://statsbombchartapp-anabeatrizmacedo.streamlit.app/)")
    video2_url = "https://youtu.be/4Ik-saIB_ok"
    st.video(video2_url)
with col5:
    video3_description = st.write("['Where's Wally?' Detector](https://github.com/AnabeatrizMacedo241/WheresWally_Detector)")
    video3_url = "https://youtu.be/Kit9FLJ7C08"
    st.video(video3_url)

with st.expander("Applying Artificial Intelligence to Enrich Visual Stimuli in Children’s Cognitive Development: Animal Detection in Videos."):
    st.write("Capstone Project that explores the role of visual diversity in early childhood cognitive development and how AI can help address the lack of adequate visual stimuli. It proposes a methodology to identify key elements in digital videos using AI, focusing on an extended YOLO neural network to detect dogs. By doing so, the research aims to enhance cognitive stimulation for children up to age 2.")

    with open(tcc, "rb") as tcc_file:
            tcc_data = tcc_file.read()
    st.download_button(
            label="Article",
            data=tcc_data,
            file_name="Capstone_Project_PT-BR.pdf",
            mime="application/pdf",
        )
with st.expander("NBA role evolution based on ML clustering publication"):
    st.write("In the modern NBA, the players who do a little bit of everything stand out usually have the best performances, and are able to capture the public eye. It is hard seeing a player with a single role like a shooter, rebounder, or playmaker skills nowadays. In my newest article for the Center for Sports Analytics at Samford University I try to understand patterns to uncover new types of roles for the players through Machine Learning models in today's NBA era. If you are also wondering how old-school players would fit in today's NBA and check their career evolution, you can check out the dashboard on your desktop.")

    st.write("[Article](https://www.samford.edu/sports-analytics/fans/2023/Machine-Learning-Uncovers-Nine-Distinct-Player-Types-in-the-NBA)")
    st.write("[Dashboard](https://public.tableau.com/app/profile/ana.beatriz.oliveira.de.macedo/viz/NBA_Cluster_Roles_AnaMacedo/Dashboard1)")
    image1 = Image.open('evolution.png')
    st.image(image1)

with st.expander("Predicting NBA MVP Contenders"):
    st.write("This study highlights the potential of machine learning in predicting NBA MVP contenders, supporting data-driven decisions in sports analytics.")

    st.write("[Article](https://www.samford.edu/sports-analytics/fans/2023/Predicting-NBA-MVP-Contenders?image)")

with st.expander("Soccermatics Scouting Project | Scouting Dashboard - Qatar World Cup"):
    st.write("Developed for the course taught by David Sumpter of Twelve and Friends of Tracking. It contains data from the 2022/23 Season for the Top 5 Leagues of European Football.")
    video_url = "https://youtu.be/UHeFnqRyMvc"
    st.video(video_url)
    st.write("Scouting dashboard to analyze players' performance during the 2022 Qatar World Cup that I developed for the Center for Sports Analytics at Samford University. The aim of this was to understand which players would catch the eye of many big clubs after the competition. Players like Cody Gakpo, João Félix, and Enzo Fernandéz were just some of the players involved in new club discussion signings.")
    st.write("[Dashboard](https://public.tableau.com/app/profile/ana.beatriz.oliveira.de.macedo/viz/Qatar2022-PlayerScouting/Dashboard5?publish=yes)")
    image2 = Image.open('scouting.png')
    st.image(image2)

with st.expander("Euro 2020 -  Machine Learning Analysis for Women In Sports Data Hackaton"):
    st.write("This project is a tool to help General Managers, Coaches and passionate fans get insights on the performance of the teams and players during the Euro 2020. To begin the construction, we needed to understand how Statsbomb worked and see what we were able to come up with their available dataset. We would like to provide insights on Player Skills, such as: scoring, passing, and defending based on their respective position.")
    st.write("[Github](https://github.com/AnabeatrizMacedo241/Euro2020_API)")
    image3 = Image.open('wisd.png')
    st.image(image3)

for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

# --- Publications ---
st.write('\n')
st.subheader("Publications")
st.write("---")
for project, link in publications.items():
    st.write(f"[{project}]({link})")

st.write('\n')
st.subheader("Twitter Data Visualization")
st.write("---")
image = Image.open('twitter.png')
st.image(image, caption='Twitter Posts')

st.write('\n')
st.subheader("Conferences")
st.write("---")
st.write()
st.write("[Speaker at FAME: Football Analytics Modeling Experience (2023)](https://salabufmg.github.io/FAME23/palestrantes/)")
st.write("[Speaker at COB Expo: Brazilian Olympic Committee event (2024)](https://cobexpo.com.br/palestrantes/)")

st.markdown(
    """
    <style>
    footer {
        text-align: center;
        padding: 10px;
        margin-top: 50px;
        font-size: 12px;
        color: #aaa;
    }
    </style>
    <footer>
        © 2025 Ana Beatriz Macedo. All rights reserved.
    </footer>
    """,
    unsafe_allow_html=True,
)