import streamlit as st

st.set_page_config(
    page_icon="✨",
    page_title="Muhammad Naeem | Portfolio",
    layout="wide"
)

page = st.sidebar.selectbox(
    "Select a page",
    ["Home", "About me", "Projects", "Skills", "Contact"]
)

if page == "Home":
    st.title("Welcome to My Portfolio")

    col1, col2, col3, col4 = st.columns(4)

    with col2:
        st.image(
            "My_image.png",
            caption="MUHAMMAD NAEEM",
            width=320
        )

    st.write("")
    st.subheader("AI & Data Science Student")

    st.write(
        "I am a passionate Python developer and AI & Data Science student "
        "interested in Machine Learning, Data Science, Artificial Intelligence "
        "and building practical applications with Streamlit and FastAPI."
    )

    st.write("Karachi, Pakistan")

elif page == "About me":
    st.title("About Me")

    st.write(
        "I am an AI and Data Science student currently developing my skills "
        "in Python, Machine Learning, Data Analysis and Artificial Intelligence."
    )

    st.write(
        "I enjoy transforming data analysis and machine learning workflows "
        "into interactive applications using Streamlit and FastAPI."
    )

    st.write(
        "My goal is to become a professional Data Scientist, AI Developer "
        "or Python Developer."
    )

    st.subheader("Education")

    st.write("🎓 AI & Data Science — Saylani Mass IT Training (SMIT)")
    st.write("🎓 Higher Secondary School Certificate")
    st.write("🎓 Secondary School Certificate")

elif page == "Projects":
    st.title("Projects")

    st.write("Here are some of the projects I have worked on:")

    st.subheader("1. Simple Arithmetic Calculator")
    st.write(
        "A simple Python application for performing basic arithmetic "
        "operations."
    )
    st.write(
        "GitHub Link: https://github.com/muhammadnaeemghulamyaseen/Simple-Arithmetic-Calculator.git"
    )
    st.write(
        "Live Link: https://simple-arithmetic-calculator.streamlit.app/"
    )

    st.subheader("2. Simple-LangChain-Chatbot")
    st.write(
        "A simple AI chatbot built with Streamlit, LangChain, and Groq."
    )
    st.write(
        "GitHub Link: https://github.com/muhammadnaeemghulamyaseen/Simple-LangChain-Chatbot.git"
    )
    st.write(
        "Live Link: https://muhammadnaeemghulamyaseenchatbot.streamlit.app/)"
    )

elif page == "Skills":
    st.title("Skills")

    st.subheader("Programming")

    st.write("🐍 Python")

    st.subheader("Data Science")

    st.write("NumPy")
    st.write("Pandas")
    st.write("Matplotlib")
    st.write("Seaborn")
    st.write("Exploratory Data Analysis")

    st.subheader("Machine Learning")

    st.write("Scikit-Learn")
    st.write("TensorFlow")
    st.write("Data Preprocessing")
    st.write("Feature Engineering")
    st.write("Model Training")
    st.write("Model Evaluation")
    st.write("Classification Algorithms")

    st.subheader("Web & API")

    st.write("Streamlit")
    st.write("FastAPI")
    st.write("Pydantic")
    st.write("REST API Development")

    st.subheader("Tools")

    st.write("Git")
    st.write("GitHub")
    st.write("API Integration")
    st.write("Problem Solving")

elif page == "Contact":
    st.title("Contact")

    st.write(
        "📧 Email: muhammadnaeemghulamyaseenawan@gmail.com"
    )

    # st.write(
    #     "💼 LinkedIn: linkedin.com/in/example"
    # )

    st.write(
        "🐙 GitHub: https://github.com/muhammadnaeemghulamyaseen"
    )

    st.write("Karachi, Pakistan")
