from flask import Flask, render_template, request, jsonify, session
from chatbot import get_lawbot_response, LANGUAGES

app = Flask(__name__)
app.secret_key = 'lawbot_secret_key'  # Required for session

@app.route('/')
def home():
    return render_template('index.html', languages=LANGUAGES)

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json['message']
    selected_lang = request.json.get('language')
    
    response = get_lawbot_response(user_input, selected_lang)
    detected_lang = response.get('detected_language', 'en')
    
    return jsonify({
        'reply': response['text'],
        'detected_language': detected_lang,
        'language_name': LANGUAGES.get(detected_lang, 'English')
    })

@app.route('/languages', methods=['GET'])
def get_languages():
    return jsonify(LANGUAGES)

if __name__ == '__main__':
    app.run(debug=True)
