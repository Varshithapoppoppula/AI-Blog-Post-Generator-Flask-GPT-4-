import openai
import os
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv

# Load OpenAI API key from environment file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate_blog():
    data = request.json
    topic = data.get("topic", "")

    if not topic:
        return jsonify({"error": "Please provide a topic"}), 400

    # Generate blog post using GPT-4
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Write a detailed blog post about {topic}"}]
    )

    blog_post = response["choices"][0]["message"]["content"]
    return jsonify({"blog_post": blog_post})

if __name__ == "__main__":
    app.run(debug=True)
