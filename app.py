from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from youtube_dl import youtube_dl

app = Flask(__name__)


@app.route("/")
@app.route("/home/")
@app.route("/index/")
def home():
    return render_template("index.html")


@app.route("/terms-conditions/")
def terms():
    return render_template("terms-conditions.html")


@app.route("/privacy-policy/")
def privacy():
    return render_template("privacy-policy.html")


@app.route("/download/", methods=["GET","POST"])
def download():
    uLink = request.form['url']
    with youtube_dl.YoutubeDL() as ydl:
        url = ydl.extract_info(uLink, download=False)
        downloadLink = (url["formats"][-1]["url"])
        
    return redirect(downloadLink+"&dl=1")


if __name__ == "__main__":
    app.run(debug=True)