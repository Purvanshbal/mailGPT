from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/send_prompt', methods=['POST'])
def send_prompt():
    prompt = request.form['prompt']
    print("PRomPT MIL GAYA BRO", prompt)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)