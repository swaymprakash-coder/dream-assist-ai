import urllib.parse
import streamlit as st
from youtubesearchpython import VideosSearch
st.set_page_config(
    page_title="Dream Assist AI",
    page_icon="🤖",
    layout="wide"
)
st.sidebar.title("🚀 Dream Assist AI")

st.sidebar.write("Learn Skills • Solve Problems • Grow 🚀")

st.sidebar.info("Powered by Dream Global Tech")
# WELCOME MESSAGE
st.title("🤖 Dream Assist AI")
st.write("Learn Skills • Solve Problems • Grow 🚀")

# About Section
st.subheader("🤖 About Dream Assist AI")
st.write("Dream Assist AI is a smart assistant designed to help you learn new skills and solve real-life problems easily.")
st.write("You can ask anything — from coding, designing, and career guidance to everyday challenges.")
st.write("🚀 Features:")
st.write("- Step-by-step learning guidance For New Skills")
st.write("- Instant YouTube tutorials")
st.write("- Beginner friendly")    
st.write("🎯 Mission:")
st.write("To make learning and problem-solving simple, fast, and accessible for everyone.")
st.write("🌟 Vision:")
st.write("To build a powerful AI platform that helps people grow, learn, and solve problems anytime.")
st.write("🔹Powered by Dream Global Tech")

# 📚 Skills data
skills_data = {
    "python": [
        "Step 1: Install Python from python.org",
        "Step 2: Learn variables and data types",
        "Step 3: Learn loops and functions",
        "Step 4: Practice small projects",
        "Step 5: Learn libraries like numpy and pandas"
    ],
    "graphic designing": [
        "Step 1: Learn basics of color and typography",
        "Step 2: Start using Canva or Photoshop",
        "Step 3: Practice poster and logo design",
        "Step 4: Learn advanced tools",
        "Step 5: Build portfolio"
    ],
    "web development": [
        "Step 1: Learn HTML basics",
        "Step 2: Learn CSS styling",
        "Step 3: Learn JavaScript basics",
        "Step 4: Build small websites",
        "Step 5: Learn frameworks"
    ]
}

# 🤖 Function
def get_skill_solution(skill):
    skill = skill.lower()

    if skill in skills_data:
        steps = skills_data[skill]
    else:
        steps = [
    "🤖 Is topic ke liye main aapko simple aur useful guidance de raha hoon👇",
    "🎥 Saath Hi Ek Best Learning Video Ka Link Bhi Add kiya hai 👇"
]

    try:
        videosSearch = VideosSearch(skill + " tutorial for beginners", limit=1)
        video_result = videosSearch.result()
        video_link = video_result["result"][0]["link"]
    except:
        video_link = None

    return steps, video_link


# 🧠 User Input
query = st.text_input("🤖 Aap Kya Seekhna YAA Jaanna Chahte Hain? ---> OR Apni Chat Close Karne Ke Liye Type Exit")

if st.button("Search"):

    if query.lower() == "exit":
        st.success("🌟 Thank you for using Dream Assist AI! Keep learning, keep growing… Phir milenge! 🚀👋")
        st.stop()

    steps, video = get_skill_solution(query)

    st.subheader("📚 Learning Steps")

    for step in steps:
        st.write(step)

    st.subheader("🎥 Recommended Video")

    if video:
        st.video(video)
    else:
        # 🔥 fallback (important fix)
        fallback_link = fallback_link = f"https://www.youtube.com/results?search_query={urllib.parse.quote(query + ' tutorial')}"
        st.warning("🎥 Aapke liye video link ready hai Please Link Pr Click Kare 👇")
        st.markdown(f"[👉 Click here to watch videos]({fallback_link})")

