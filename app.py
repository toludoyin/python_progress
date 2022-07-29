from flask import Flask, render_template
app = Flask(__name__, template_folder = 'template')

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/show_text", methods=['GET'])
def show_text():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug = True)