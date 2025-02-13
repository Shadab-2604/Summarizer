# main.py
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure API Key securely
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("Missing GEMINI_API_KEY environment variable!")

genai.configure(api_key=api_key)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    try:
        data = request.json
        content = data.get("content")
        if not content:
            return jsonify({"error": "No content provided."}), 400

        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(content)
        summary = response.text if response else "Could not generate summary."

        return jsonify({"summary": summary})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=True)