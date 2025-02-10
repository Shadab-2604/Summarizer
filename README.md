# Summarizer
# Content Summarizer

## 📌 Overview
The **Content Summarizer** is a web application that uses the **Gemini API** to generate concise summaries of user-provided text. It is built using **Flask** for the backend and a clean **Bootstrap-based UI** for user interaction.

## 🚀 Features
- ✅ Summarizes long text content using Gemini AI
- ✅ Interactive and responsive UI
- ✅ Easy-to-use web interface
- ✅ Error handling for invalid input
- ✅ Lightweight and fast API response

## 🛠️ Tech Stack
- **Backend:** Flask (Python)
- **API:** Google Gemini API
- **Frontend:** HTML, CSS, Bootstrap, JavaScript

## 🔧 Installation & Setup
### **1️⃣ Install Dependencies**
Ensure you have **Python 3.x** installed. Then, install the required packages:
```sh
pip install flask google-generativeai
```

### **2️⃣ Set Up Gemini API Key**
Replace `YOUR_GEMINI_API_KEY` in `app.py` with your actual Google Gemini API key:
```python
import google.generativeai as genai

genai.configure(api_key="YOUR_GEMINI_API_KEY")
```

### **3️⃣ Run the Application**
Start the Flask server:
```sh
python app.py
```

### **4️⃣ Access the Web App**
Open your browser and visit:
```
http://127.0.0.1:5000/
```

## 📄 Usage Guide
1. Enter or paste text into the provided input field.
2. Click the **Summarize** button.
3. View the AI-generated summary below the input field.

## 🎯 Example Input & Output
### **Input:**
```
Artificial Intelligence (AI) is a branch of computer science that aims to create machines that can perform tasks that typically require human intelligence...
```

### **Generated Summary:**
```
AI is a field of computer science focused on creating machines that mimic human intelligence. It includes learning, reasoning, and problem-solving...
```

## 🛠️ Future Enhancements
- 📂 File upload support (PDF, TXT summarization)
- ⬇️ Download summary as a text file
- 🌙 Dark mode for UI
- 🏷️ Keyword extraction

## 🤝 Contribution
Feel free to contribute! Fork the repo, make changes, and submit a pull request.

## 📜 License
This project is open-source and available under the MIT License.

---

⚡ **Developed by:** Shadab 🚀

