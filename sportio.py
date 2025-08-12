# sports_platform_prototype.py
import random
import streamlit as st
from streamlit_option_menu import option_menu
from database import create_table, add_profile, get_profiles, get_training_data, get_milestones, get_profile

# Set page configuration
st.set_page_config(page_title="Sportio-Hub", layout="wide")

# Custom background styling
st.markdown("""
    <style>
        .stApp {
            background-image: url('https://wallpapercave.com/wp/wp2675414.jpg');
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-position: center;
        }

        .block-container {
            background-color: transparent;
        }

        .main-header {
            font-size: 36px;
            font-weight: bold;
            color: black;
            padding: 20px 0;
            text-align: center;
        }

        .info-box {
            background-color: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border-radius: 15px;
            padding: 1rem;
            margin-bottom: 1rem;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# Header function
def top_header():
    st.markdown("""
    <div style='text-align: center;'>
        <div class='main-header'>Sportio-Hub</div>
    </div>
    """, unsafe_allow_html=True)

# Profile card function
def profile_card(name, sport, location, bio, achievements, skills):
    st.markdown(f"""
    <div class="info-box">
        <strong>Name:</strong> {name}<br>
        <strong>Sport:</strong> {sport}<br>
        <strong>Location:</strong> {location}<br>
        <strong>Bio:</strong> {bio}<br>
        <strong>Achievements:</strong> {achievements}<br>
        <strong>Skills:</strong> {skills}
    </div>
    """, unsafe_allow_html=True)

# Initialize database
create_table()

# Sidebar navigation
with st.sidebar:
    selected = option_menu(
        "Main Menu",
        ["\U0001F3E0 Home", "\U0001F3C5 Profile", "\U0001F4C8 Training", "\U0001F916 AI Assistant", "\U0001F4B0 Crowdfunding", "\U0001F9ED Career Guide", "\U0001F4CA Milestones"],
        icons=["house", "person", "bar-chart", "robot", "cash-coin", "compass", "graph-up"],
        menu_icon="list",
        default_index=0
    )

# Page: Home
if selected == "\U0001F3E0 Home":
    top_header()
    st.title("Welcome to Sportio-Hub \U0001F3CB️")
    st.markdown("""
        ## About the Project
        Sportio-Hub is a cutting-edge platform designed to empower athletes by bridging the gap between talent and opportunity.

        We offer:
        - Personalized training plans
        - Real-time AI coaching and communication support
        - Blockchain-powered crowdfunding
        - Career recommendations and progress tracking

        ## What we are doing
        As we seeing the results of olympics on our country. We saw that as a too hilarious problem, that when comparing to other small countries we are more lesser than them in exhibiting the skills on young athletes and sports person.
        Many talented athletes face obstacles such as financial constraints, lack of exposure, and limited access to professional training. 
        Sportio-Hub addresses these challenges by providing a unified digital space to showcase talent, receive support, and grow professionally.

        **Our mission is to unlock every athlete's full potential regardless of their background or location.**
    """)
    st.markdown("[our experienced hackathon on Sportio-Hub](https://devfolio.co/projects/sportio-hub-a-platform-for-career-and-skill-growth-1148)", unsafe_allow_html=True)
    st.markdown("[github link of Sportio-Hub](https://github.com/jothiprakasam/SportioHub/)")
    st.video("https://www.youtube.com/watch?v=V9R8R-_2ie8")

# Page: Profile
elif selected == "\U0001F3C5 Profile":
    top_header()
    st.title("Athlete Profile")
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://via.placeholder.com/150", caption="Profile Photo")
        name = st.text_input("Full Name")
        sport = st.selectbox("Sport", ["Football", "Cricket", "Tennis", "Athletics", "Other"])
        location = st.text_input("Location")
    with col2:
        bio = st.text_area("Bio")
        achievements = st.text_area("Achievements")
        skills = st.text_area("Skills")

    if st.button("\U0001F4BE Save Profile"):
        if name:
            add_profile(name, sport, location, bio, achievements, skills)
            st.success(f"Profile saved for {name}.")
        else:
            st.warning("Please enter at least a name to save the profile.")

    st.write("---")
    st.subheader("All Athlete Profiles")
    profiles = get_profiles()
    for prof in profiles:
        profile_card(prof[1], prof[2], prof[3], prof[4], prof[5], prof[6])

# Page: Training
elif selected == "\U0001F4C8 Training":
    top_header()
    st.title("Intelligent Training Dashboard")
    st.subheader("Enter Your Weekly Training Data")

    monday_time = st.number_input("\U0001F3CB️ Monday: Time spent on Strength Training (in minutes)", 0, 300, step=10)
    tuesday_distance = st.number_input("\U0001F3C3 Tuesday: Distance in Endurance Drills (km)", 0.0, 100.0, step=0.1)
    wednesday_hours = st.number_input("\U0001F3CB Wednesday: Flexibility & Recovery (hours)", 0.0, 10.0, step=0.5)
    thursday_time = st.number_input("\U0001F6B4 Thursday: Cardio (minutes)", 0, 300, step=10)
    friday_intensity = st.number_input("\U0001F4A5 Friday: HIIT Intensity (1-10)", 1, 10, step=1)
    friday_duration = st.number_input("\U0001F4A5 Friday: HIIT Duration (minutes)", 0, 180, step=5)
    saturday_activity = st.selectbox("\U0001F6CC Saturday: Rest or Active Recovery", ["Rest", "Active Recovery"])

    if st.button("Generate Training Plan"):
        plan = []
        plan.append("\U0001F7E2 Monday: Regular strength training." if monday_time <= 120 else "\U0001F534 Monday: Reduce intensity.")
        plan.append("\U0001F7E2 Tuesday: Moderate pace endurance." if tuesday_distance <= 10 else "\U0001F534 Tuesday: Add recovery.")
        plan.append("\U0001F7E2 Wednesday: Good flexibility." if wednesday_hours >= 1 else "\U0001F7E1 Wednesday: Increase recovery.")
        plan.append("\U0001F7E2 Thursday: Balanced cardio." if thursday_time <= 150 else "\U0001F534 Thursday: Reduce time.")
        plan.append("\U0001F7E2 Friday: Suitable HIIT." if friday_intensity <= 8 or friday_duration <= 60 else "\U0001F534 Friday: HIIT too intense.")
        plan.append("\U0001F7E2 Saturday: Enjoy rest." if saturday_activity == "Rest" else "\U0001F7E1 Saturday: Light recovery work.")
        st.markdown("### Adaptive Training Plan:")
        for p in plan:
            st.markdown(p)

    st.markdown("### Weekly Summary")
    st.write(f"\U0001F3CB️ Monday: {monday_time} min Strength")
    st.write(f"\U0001F3C3 Tuesday: {tuesday_distance} km Endurance")
    st.write(f"\U0001F3CB Wednesday: {wednesday_hours} hrs Flexibility")
    st.write(f"\U0001F6B4 Thursday: {thursday_time} min Cardio")
    st.write(f"\U0001F4A5 Friday: {friday_duration} min HIIT @ {friday_intensity}")
    st.write(f"\U0001F6CC Saturday: {saturday_activity}")

# Page: AI Assistant
elif selected == "\U0001F916 AI Assistant":
    top_header()
    st.title("AI Strategy Assistant")
    st.subheader("Get training insights using AI")

    user_query = st.text_area("Ask a question or describe your training strategy:")

    if st.button("Get Advice"):
        if user_query:
            st.info("Analyzing... (NLP model placeholder)")
            if "bowling" in user_query.lower():
                response = "\U0001F3B3 Focus on explosive starts, grip technique, and visualization."
            elif "running" in user_query.lower():
                response = "\U0001F3C3‍♂ Try intervals, posture focus, and hydration."
            elif "injury" in user_query.lower():
                response = "\U0001FA7A Use load management, physiotherapy, and recovery."
            elif "flexibility" in user_query.lower():
                response = "\U0001F9D8 Stretching, dynamic warm-ups, and yoga are key."
            else:
                response = "\U0001F9E0 Focus on technique, recovery cycles, and mindset."

            st.success("AI Suggestion:")
            st.markdown(response)
        else:
            st.warning("Please enter a training-related question or strategy.")

# Page: Crowdfunding
elif selected == "\U0001F4B0 Crowdfunding":
    top_header()
    st.title("Crowdfunding Campaigns")
    campaign_name = "Journey to Paris Olympics 2028"
    goal = 10000
    raised = 4000
    supporter_count = 87

    st.markdown(f"### \U0001F680 Campaign: {campaign_name}")
    st.markdown(f"<div class='info-box'><strong>Raised:</strong> ${raised} / ${goal}<br><strong>Supporters:</strong> {supporter_count}</div>", unsafe_allow_html=True)
    st.progress(raised / goal)

    contribution = st.number_input("Enter your contribution amount (USD):", min_value=1, max_value=goal - raised, step=10)

    if st.button("Contribute Now"):
        if contribution > 0:
            raised += contribution
            supporter_count += 1
            st.success(f"Thank you for your support! You contributed ${contribution}.")
            st.write("Simulating blockchain update... Contribution processed.")
            st.markdown(f"**Updated Raised:** ${raised} / ${goal}")
            st.markdown(f"**Supporters:** {supporter_count}")
            st.progress(raised / goal)
        else:
            st.warning("Please enter a valid contribution amount.")

# Page: Career Guide
elif selected == "\U0001F9ED Career Guide":
    top_header()
    st.title("Career Recommendation")

    performance = st.slider("Athletic Performance (1-10)", 1, 10, 5)
    education = st.selectbox("Education Level", ["High School", "Diploma", "Bachelor's", "Master's"])

    def recommend_career(performance, education):
        recommendations = []
        if performance >= 8:
            if education == "High School":
                recommendations.extend(["Sports Coaching", "Therapy Assistant"])
            elif education == "Diploma":
                recommendations.extend(["Personal Trainer", "Analyst"])
            elif education == "Bachelor's":
                recommendations.extend(["Manager", "Pro Athlete"])
            else:
                recommendations.extend(["Researcher", "Psychologist"])
        elif performance >= 5:
            if education == "High School":
                recommendations.extend(["Coach", "Fitness Instructor"])
            elif education == "Diploma":
                recommendations.extend(["Trainer", "Nutritionist"])
            elif education == "Bachelor's":
                recommendations.extend(["Event Coordinator", "Marketing"])
            else:
                recommendations.extend(["Manager", "Data Analyst"])
        else:
            recommendations.extend(["Assistant Coach", "Fitness Assistant"])
        return recommendations

    if st.button("Get Recommendations"):
        st.info("Analyzing your profile...")
        for rec in recommend_career(performance, education):
            st.markdown(f"- **{rec}**")

# Page: Milestones
elif selected == "\U0001F4CA Milestones":
    top_header()
    st.title("Milestone Tracker")
    milestone = st.text_input("Milestone Description")
    date = st.date_input("Date")
    if st.button("Add Milestone"):
        st.info("Milestones will appear in timeline format in full version.")
