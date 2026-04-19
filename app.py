from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    print("\n  Huella de Carbono Digital")
    print("  Abre tu navegador en: http://localhost:5000\n")
    app.run(debug=True, host='0.0.0.0', port=5000)
