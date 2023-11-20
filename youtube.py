from flask import Flask,redirect,request,render_template,send_file,send_from_directory
import os
from pytube import YouTube
from werkzeug.utils import secure_filename

app=Flask(__name__)

app.config['video_folder']="uploads/"

@app.route("/")
def home():


    return render_template("ytube.html")

@app.route("/user",methods=['POST','GET'])
def search():
        video_file=os.listdir(app.config['video_folder'])
        for i in video_file:
         os.remove(app.config['video_folder']+i)

        video_links=request.form['video_link']
        print(video_links)
        
        url =video_links
        
        filename = "downloaded_video.mp4"  # Choose a filename for the downloaded video
        
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download(app.config['video_folder'])
        print(f"Video downloaded as {filename}")


        return redirect("/")
    
@app.route("/video")
def server():
    filename=''
    video=os.listdir(app.config['video_folder'])
    for i in video:
         filename=i
    return send_from_directory(app.config['video_folder'],filename)

@app.route("/download")
def down():
    filename=''
    video=os.listdir(app.config['video_folder'])
    for i in video:
         filename=i
    return send_file(app.config['video_folder']+filename,as_attachment=True)


if __name__=='__main__':
    app.run(debug=True)
    