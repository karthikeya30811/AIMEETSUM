import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import PyPDF2

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

st.title("🤖 AI- Kart27 Notes Summarizer")

uploaded_file = st.file_uploader("Upload transcript (txt/pdf)", type=["txt", "pdf"])


summary_style = st.selectbox(
    "Choose summary style",
    ["Executive (short & crisp)", "Detailed", "Action Items Only", "Custom Instruction"]
)

custom_prompt = ""
if summary_style == "Custom Instruction":
    custom_prompt = st.text_area(
        "Enter custom instruction",
        placeholder="e.g., Summarize in bullet points for executives"
    )

transcript = ""
if uploaded_file:
    if uploaded_file.name.endswith(".txt"):
        transcript = uploaded_file.read().decode("utf-8", errors="ignore")
    elif uploaded_file.name.endswith(".pdf"):
        reader = PyPDF2.PdfReader(uploaded_file)
        for page in reader.pages:
            transcript += page.extract_text() + "\n"


if st.button("Generate Summary"):
    if transcript.strip():
        model = genai.GenerativeModel("gemini-1.5-flash")

        # Choose summarization instruction
        if summary_style == "Executive (short & crisp)":
            instruction = "Summarize in 5 crisp bullet points highlighting only key decisions and outcomes."
        elif summary_style == "Detailed":
            instruction = "Summarize with detailed paragraphs covering all key points, context, and discussions."
        elif summary_style == "Action Items Only":
            instruction = "Extract only action items with owners and deadlines in bullet points."
        else:
            instruction = custom_prompt

        # Strong structured prompt
        prompt = f"""
        You are an expert meeting summarizer.
        Task:
        - Ignore greetings and small talk.
        - Focus on main discussion, decisions, and responsibilities.
        - Apply this summarization style: {instruction}

        Transcript:
        {transcript}
        """

        response = model.generate_content(prompt)
        st.session_state.summary = response.text
    else:
        st.warning("⚠ Please upload a file and enter a prompt.")


if "summary" in st.session_state:
    edited_summary = st.text_area(
        "Editable Summary",
        st.session_state.summary,
        height=300
    )

    recipient = st.text_input("Enter recipient email")

    if st.button("Send via Email"):
        if recipient:
            try:
                msg = MIMEMultipart()
                msg["From"] = EMAIL_USER
                msg["To"] = recipient
                msg["Subject"] = "Meeting Summary"
                msg.attach(MIMEText(edited_summary, "plain"))

                context = ssl.create_default_context()
                with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                    server.login(EMAIL_USER, EMAIL_PASS)
                    server.sendmail(EMAIL_USER, recipient, msg.as_string())

                st.success("✅ Email sent successfully!")
            except Exception as e:
                st.error(f"❌ Failed to send email: {e}")
        else:
            st.warning("⚠ Please enter recipient email.")