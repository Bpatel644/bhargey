import os
import glob
import sys

from uuid import uuid4
from flask import Flask, render_template, request, redirect, url_for

reload(sys)
sys.setdefaultencoding("utf-8")

app = Flask(__name__,
            static_folder = "../dist/static",
            template_folder = "../dist")

@app.route('/', defaults={'path': ''})
def catch_all(path):
    """The default route for all mispelled address : the homepage"""
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    """Handle the upload of a file."""
    form = request.form

    # Create a unique "session ID" for this particular batch of uploads.
    upload_key = str(uuid4())

    # Target folder for these uploads.
    target = os.path.join(os.getcwd(),"static/uploads/{}".format(upload_key))
    if not os.path.exists(target):
        try:
            print("=== Folder creation ===")
            os.mkdir(target)
        except:
            return "Couldn't create upload directory: {}".format(target)      

    for file_uploaded in request.files.getlist("file"):
        filename = os.path.normcase(file_uploaded.filename)
        destination = "/".join([target, filename])
        print("Accept incoming file:", filename)
        print("Save it to:", destination)
        upload.save(destination)
        file_uploaded.save(destination)

    return redirect(url_for("upload_complete", uuid=upload_key))

@app.route("/files/<uuid>")
def upload_complete(uuid):
    """The location we send them to at the end of the upload."""

    # Get their files.
    root = "static/uploads/{}".format(uuid)
    if not os.path.isdir(root):
        return "Error: UUID not found!"

    files = []
    for file in glob.glob("{}/*.*".format(root)):
        fname = file.split(os.sep)[-1]
        files.append(fname)

    return render_template("files.html",
        uuid=uuid,
        files=files,
    )


''' @app.route("tts/<uuid>")
def tts(text, uuid):
    """The function handling the text-to-speech operation"""
    tts_result = gTTS(text=text, lang='en', slow=True)
    tts_result.save("{}.mp3".format(uuid))
    return render_template("tts.html") '''
