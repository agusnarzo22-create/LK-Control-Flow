from flask import Flask, render_template  # <-- Pastikan ada ini

app = Flask(__name__)

@app.route("/")
def home():
    # Pastikan nama file di sini sama dengan nama file di folder templates
    return render_template("portofolio.html", user="Agus")

if __name__ == "__main__":
    app.run(debug=True)