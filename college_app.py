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

    cic_number = st.text_input("Enter your CIC Number")

    if cic_number:
        try:
            # Read Google Sheet directly as CSV
            url = "https://docs.google.com/spreadsheets/d/1JP7N0ZQS0lL3FeEiOvIz813XqS4N6UIqahlLw6M5sNg/export?format=csv&id=1JP7N0ZQS0lL3FeEiOvIz813XqS4N6UIqahlLw6M5sNg&gid=982647782"
            df = pd.read_csv(url)

            # Assuming 'cic' is the column name in the sheet
            result = df[df['cic'] == cic_number]

            if not result.empty:
                st.success("✅ Student found!")
                st.write(result)  # or format nicely using st.info()
            else:
                st.error("❌ CIC number not found.")

        except Exception as e:
            st.error(f"⚠️ Error reading Google Sheet: {e}")

elif menu == "Contact":
    st.subheader("📞 Contact")
    st.write("For help, contact your class tutor.")
