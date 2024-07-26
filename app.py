from flask import Flask, render_template, request, jsonify
from RecognizeVoice import recognize
import webbrowser
app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/voice-command', methods=['POST'])
def voice_command():
    command, coordinates = recognize()
    return jsonify({'command': command, 'coordinates': coordinates})

if __name__ == '__main__':
    webbrowser.open("http://127.0.0.1:5000")
    app.run(debug=True)