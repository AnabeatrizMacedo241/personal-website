from pathlib import Path
import streamlit as st
from PIL import Image
# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"
twitter_pic = current_dir / "assets"/ "twitter.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Portfolio|Ana Beatriz Macedo"
PAGE_ICON = ":wave:"
NAME = "Ana Beatriz Macedo"
DESCRIPTION = """Data Scientist | Sports Analyst"""
skills = "Python | Tableau | SQL | R"
EMAIL = "anabeatrizmacedo241@gmail.com"
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


PROJECTS = {"NBA role evolution based on ML clustering publication":"https://public.tableau.com/app/profile/ana.beatriz.oliveira.de.macedo/viz/NBA_Cluster_Roles_AnaMacedo/Dashboard1",
            "Statsbomb Free Data Extraction App":"https://statsbombchartapp-anabeatrizmacedo.streamlit.app/",
    "Scouting Dashboard - Qatar World Cup": "https://public.tableau.com/app/profile/ana.beatriz.oliveira.de.macedo/viz/Qatar2022-PlayerScouting/Dashboard5",
    "Euro 2020 -  Machine Learning Analysis for Women In Sports Data Hackaton": "https://github.com/AnabeatrizMacedo241/Euro2020_API",
    "NBA All-time Points Analysis API": "https://github.com/AnabeatrizMacedo241/NBA_AllTimePTS_API",
    "Predicting Covid-19 and recommending ideal doctors": "https://github.com/AnabeatrizMacedo241/CovidPrediction_DoctorRecommendation"
}
videos = {"Marco Silva tactics and his philosophy | Fulham | Premier League 2022/23": "https://www.youtube.com/watch?v=WlkEKj13AwM",
    "Roger Schmidt: His Philosophy & Tactics Explained | Benfica 2022/23": "https://www.youtube.com/watch?v=kexvNBxjQiY&list=PLkfpUmGJU_jZ-bd0GKgc0lGYBYNrSOPpi&index=29",
    "Xavi: His Barcelona tactics and philosophy | How Xavi uses Pedri and Gavi":"https://www.youtube.com/watch?v=Qb_FkVTfDy0&list=PLkfpUmGJU_jZ-bd0GKgc0lGYBYNrSOPpi&index=34",
    "More Videos": "https://www.youtube.com/playlist?list=PLkfpUmGJU_jZ-bd0GKgc0lGYBYNrSOPpi"

}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


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
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- Publications ---
st.write('\n')
st.subheader("Publications")
st.write("---")
for project, link in publications.items():
    st.write(f"[{project}]({link})")

# --- Projects ---
st.write('\n')
st.subheader("Projects")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

image2 = Image.open('project.png')
st.image(image2)
# --- Videos ---
st.write('\n')
st.subheader("Tactical Analysis Videos")
st.write("---")
for project, link in videos.items():
    st.write(f"[{project}]({link})")

st.write('\n')
st.subheader("Twitter Data Visualization")
st.write("---")
image = Image.open('twitter.png')
st.image(image, caption='Twitter Posts')