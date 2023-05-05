# Import necessary libraries
import openai
from flask import Flask, request, jsonify, render_template
import config

# Set up OpenAI API key
openai.api_key = config.API_KEY

# Initialize Flask app
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

# Define endpoint for chatbot
@app.route('/chatbot', methods=['POST'])
def chatbot():
    # Get user input from request
    input_text = request.json['text']

    prompt = f"{input_text}"

    # Use OpenAI API to generate response
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ]
    )

    # Extract chatbot response from OpenAI API response
    chatbot_response = response.choices[0].message.get("content")

    # Call your other API here with the prompt parameter
    # and store the response in the `other_api_response` variable
    other_api_response = "Your other API response here"

    # Return both responses as JSON
    return jsonify({
        'chatbot_response': chatbot_response,
        'other_api_response': other_api_response
    })

# Run Flask app
if __name__ == '__main__':
    app.run(debug=True)
