from flask import Flask, render_template, request
import requests

app = Flask(__name__)

LANGUAGES = {
    "English": "en",
    "Telugu": "te",
    "Hindi": "hi",
    "Tamil": "ta",
    "Kannada": "kn",
    "Malayalam": "ml",
    "French": "fr",
    "Spanish": "es",
    "German": "de"
}


@app.route("/", methods=["GET", "POST"])
def home():
    translated_text = ""
    error = ""

    if request.method == "POST":
        text = request.form.get("text")
        source = request.form.get("source")
        target = request.form.get("target")

        if not text:
            error = "Please enter some text."
        else:
            try:
                url = "https://api.mymemory.translated.net/get"

                params = {
                    "q": text,
                    "langpair": f"{source}|{target}"
                }

                response = requests.get(url, params=params, timeout=10)
                data = response.json()

                translated_text = data["responseData"]["translatedText"]

            except Exception:
                error = "Translation failed. Please try again."

    return render_template(
        "index.html",
        languages=LANGUAGES,
        translated_text=translated_text,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)