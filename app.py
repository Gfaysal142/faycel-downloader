from flask import Flask, render_template, request, send_file
import yt_dlp
import os
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form.get('url')
    if not url:
        return "يرجى إدخال رابط!"

    filename = f"video_{int(time.time())}.mp4"
    ydl_opts = {
        'format': 'best',
        'outtmpl': filename,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        # هذي تبعث الفيديو للمتصفح باش يتشارجي
        return send_file(filename, as_attachment=True)
    except Exception as e:
        return f"خطأ: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000))

