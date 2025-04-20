import streamlit as st
import pandas as pd

st.set_page_config(page_title="My College App", layout="centered")

st.title("🎓 My College App")

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
