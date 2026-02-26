# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    profile_image = Image.open(profile_pic)  # Ensure this is only for the image
    st.image(profile_image, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.write(skills)
    st.write("📫", EMAIL)
    st.markdown("[📄 View Resume](?page=resume)", unsafe_allow_html=True)

# --- SOCIAL LINKS ---
st.write('\n')
SOCIAL_MEDIA["Resume"] = "?page=resume"  # Add resume link to social media
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- PAGE ROUTING ---
query_params = st.experimental_get_query_params()
if query_params.get("page") == ["resume"]:
    st.title("Resume")
    with open(resume_file, "rb") as pdf_file:
        PDFbyte = pdf_file.read()  # Ensure this is for the resume file
    st.download_button(
        label="📄 Download Resume",
        data=PDFbyte,
        file_name="Ana_Beatriz_Macedo_Resume.pdf",
        mime="application/pdf",
    )
    st.write("Use the button above to download the resume.")
