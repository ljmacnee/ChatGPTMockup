# Import necessary libraries
import openai
from flask import Flask, request, jsonify
import config

# Set up OpenAI API key
openai.api_key = config.API_KEY

# Initialize Flask app
app = Flask(__name__)

# Define endpoint for chatbot
@app.route('/chatbot', methods=['POST'])
def chatbot():
    # Get user input from request
    input_text = request.json['text']

    # Set up OpenAI GPT-3 parameters
    model_engine = "text-davinci-002"
    prompt = f"User: {input_text}\nChatbot:"

    # Use OpenAI API to generate response
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Extract chatbot response from OpenAI API response
    chatbot_response = response.choices[0].text.strip()

    # Return chatbot response as JSON
    return jsonify({'response': chatbot_response})

# Run Flask app
if __name__ == '__main__':
    app.run(debug=True)
