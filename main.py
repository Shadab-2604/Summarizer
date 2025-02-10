from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure API Key securely
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

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

# Vercel requires a 'handler' function
def handler(request, *args, **kwargs):
    return app(request.environ, start_response)

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
