import streamlit as st
import pandas as pd


# Set the theme, page title, and layout
st.set_page_config(
    page_title="College App",
    page_icon="🎓",  # You can change the icon
    layout="wide",  # You can also try "centered"
    initial_sidebar_state="expanded"  # Sidebar settings: "expanded", "collapsed"
)

st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #1c1c1c;  # Dark background for buttons
        color: white;  # White text
    }
    </style>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    st.header("Admin Tools")
    st.button("Upload Materials")

with col2:
    st.header("Student Resources")
    st.button("Download Notes")


st.title("🎓 Darussalam")

menu = st.sidebar.radio("📋 Menu", ["Home", "Announcements", "Timetable", "Materials", "Fee Status", "Contact"])

if menu == "Home":
    st.write("Welcome to the official app of our college. ✨")

elif menu == "Announcements":
    st.subheader("📢 Announcements")
    st.write("No announcements yet.")

elif menu == "Timetable":
    st.subheader("📅 Timetable")
    st.write("Timetable coming soon.")

elif menu == "Materials":
    st.subheader("📁 Study Materials")
    st.write("Materials will be added soon.")

elif menu == "Fee Status":
    st.subheader("🧾 Check Fee Status")

    student_id = st.text_input("Enter your Student ID")

    if student_id:
        try:
            df = pd.read_csv("fees.csv")  # This is where you’ll later add fee data
            student_id = int(student_id)
            result = df[df['student_id'] == student_id]

            if not result.empty:
                row = result.iloc[0]
                st.success(f"👤 Name: {row['name']}")
                st.info(f"💰 Total Fee: ₹{row['total_fee']}")
                st.info(f"✅ Paid: ₹{row['paid_fee']}")
                st.warning(f"🕗 Pending: ₹{int(row['total_fee']) - int(row['paid_fee'])}")
            else:
                st.error("❌ Student ID not found.")
        except:
            st.error("⚠️ Error reading fee data.")

elif menu == "Contact":
    st.subheader("📞 Contact")
    st.write("For help, contact your class tutor.")
