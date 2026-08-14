import streamlit as st

st.set_page_config (
    page_icon="✨",
    page_title="Portfolio",
    layout="wide"
)


page = st.sidebar.selectbox("Select a page", ["Home", "About me", "Projects", "Contact"])

if page == ("Home"):
    st.title("Welcome to My Portfolio")
    col1, col2, col3, col4 = st.columns(4)
    with col2:
        st.image("My_image.png", caption= "MUHAMMAD NAEEM", width = 320)

if page == ("About me"):
    st.title("About Me")
    st.write("I am a passionate software developer with experience in building web applications and data analysis. I enjoy learning new technologies and applying them to solve real-world problems.")

if page == ("Projects"):
    st.title("Projects")
    st.write("Here are some of the projects I have worked on:")
    st.write("- Project 1: Description of project 1")
    st.write("- Project 2: Description of project 2")
    st.write("- Project 3: Description of project 3")

if page == ("Contact"):
    st.title("Contact")
    st.write("- Email: muhammadnaeemghulamyaseenawan@gmail.com")
    st.write("- LinkedIn: linkedin.com/in/example")
    st.write("- GitHub: github.com/example")

