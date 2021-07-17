from flask import Flask , render_template,request,redirect
import speech_recognition as sr
app=  Flask(__name__)



@app.route("/", methods=['GET','POST'])
def index():
    transcript =''
    if request.method == 'POST':
        print("form data received")
        if "file" not in request.files:
            return redirect(request.url)
        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)
        is_audio_file=file.filename.endswith("wav") or file.filename.endswith("mp3")
        if not is_audio_file:
            print("this is not an audio file")
            return redirect(request.urls)
        if file:
            recognizer = sr.Recognizer()
            audio_file = sr.AudioFile(file)
            with audio_file as source:
                data=recognizer.record(source)
            transcript = recognizer.recognize_google(data , key=None)

            print("Good!  you have upload an audio file")


    return render_template("index.html", transcript=transcript)


if __name__ == "__main__":
    app.run(debug=True , threaded = True)
