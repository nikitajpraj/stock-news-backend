from flask import Flask, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = "YOUR_OPENAI_KEY"  # Replace later using environment variable

@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.json
    news_text = data.get("text", "")

    if not news_text:
        return jsonify({"error": "No text provided"}), 400

    prompt = f"Summarize this financial news in simple terms: {news_text}"
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=150
    )
    summary = response.choices[0].text.strip()
    return jsonify({"summary": summary})

@app.route("/")
def home():
    return "Stock News Backend is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
