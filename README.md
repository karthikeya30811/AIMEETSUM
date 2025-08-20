
# 🤖 AI-Powered Meeting Notes Summarizer

An intelligent Streamlit app that:

* 📂 Uploads **TXT/PDF transcripts**
* 🧠 Summarizes meetings using **Google Gemini API**
* ✍️ Lets you **edit summaries** before sharing
* 📧 Sends meeting notes directly via **Email**

---

## 🚀 Features

* Supports **TXT** & **PDF** input
* Multiple summary styles:

  * Executive (short & crisp)
  * Detailed
  * Action Items Only
  * Custom instruction
* Built-in **editor** to refine summaries
* **Email integration** with Gmail (App Password required)

---

## 📂 Project Structure

```
AI-Summarizer/
├─ main.py                # Streamlit app
├─ requirements.txt       # Dependencies
├─ .gitignore             # Ignore secrets & junk
└─ README.md              # Project info
```

---

## 🛠️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/<your-username>/AI-Summarizer.git
cd AI-Summarizer
```

### 2️⃣ Create Virtual Environment (Optional but Recommended)

```bash
python -m venv .venv
source .venv/bin/activate   # On Linux/Mac
.venv\Scripts\activate      # On Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Secrets

Create a **`.env`** file (for local dev):

```
GEMINI_API_KEY=your_gemini_api_key
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_gmail_app_password
```

⚠️ On **Streamlit Cloud**, add the same values under **App → Settings → Secrets** instead of `.env`.

---

## ▶️ Run the App Locally

```bash
streamlit run main.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🌐 Deploy to Streamlit Cloud

1. Push your project to GitHub.
2. Go to [Streamlit Community Cloud](https://share.streamlit.io/).
3. Create a **New App** → connect your repo → select **main.py**.
4. Add your secrets (API key & email) under **App → Settings → Secrets**.
5. Deploy 🚀

---

## 📧 Gmail Setup

* Enable **2FA** on your Google Account.
* Generate a **Gmail App Password** (16-character) from [Google App Passwords](https://myaccount.google.com/apppasswords).
* Use it as `EMAIL_PASS` instead of your real password.

---

## 📝 Example Usage

Upload a meeting transcript like:

```
Manager: Let's finalize Q3 targets.
Team: Marketing will focus on social campaigns.
Action: Dev team to release new feature by August 15.
```

➡️ **Executive Summary Output:**

```
• Q3 targets finalized
• Marketing → social campaigns
• Dev team → release feature by Aug 15
```

---

## ⚠️ Known Issues

* **429 Quota Errors** → Free Gemini tier limit (15 requests/min). Enable billing for higher quota.
* **PDF parsing** → Some scanned PDFs may extract poorly (use OCR before upload).

---
