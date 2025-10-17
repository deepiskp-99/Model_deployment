import streamlit as st

st.set_page_config(page_title="📞 Contact Page", layout="wide")

st.title("📞 Contact Page")
st.write("If you’d like to get in touch, fill in your details below 👇")

name = st.text_input("Your Name")
email = st.text_input("Your Email")
message = st.text_area("Your Message")

if st.button("Send Message"):
    if name and email and message:
        st.success(f"Thank you {name}! Your message has been sent successfully.")
    else:
        st.warning("⚠️ Please fill in all fields before submitting.")