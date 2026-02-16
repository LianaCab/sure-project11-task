
---

## backend/app.py

```python
import os
import base64
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from openai import OpenAI
from ambiguity import detect_ambiguity
from dialogue import DialogueManager

load_dotenv()

app = Flask(__name__)
CORS(app)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

dialogue_manager = DialogueManager()


def encode_image(image_file):
    return base64.b64encode(image_file.read()).decode("utf-8")


def analyze_image(image_base64):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": """
                        Analyze this image and return structured JSON:
                        {
                          objects: [
                            {
                              name: "",
                              count: number,
                              attributes: "",
                              location: ""
                            }
                          ]
                        }
                        """
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_base64}"
                        }
                    }
                ]
            }
        ],
        max_tokens=800
    )

    return response.choices[0].message.content


@app.route("/analyze", methods=["POST"])
def analyze():
    image = request.files["image"]
    question = request.form["question"]
    mode = request.form["mode"]

    image_base64 = encode_image(image)
    structured_data = analyze_image(image_base64)

    ambiguity = detect_ambiguity(structured_data, question)

    if mode == "onepass":
        return jsonify({
            "response": ambiguity["full_response"]
        })

    elif mode == "iterative":
        reply = dialogue_manager.handle_turn(
            structured_data,
            question
        )
        return jsonify({
            "response": reply
        })


if __name__ == "__main__":
    app.run(debug=True)
