from flask import Flask, render_template, request, jsonify
import yt_dlp
import os

app = Flask(__name__)

def get_tiktok_video(url):
    ydl_opts = {
        'format': 'best',
        'quiet': True,
        'no_warnings': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(url, download=False)
            return {
                'title': info.get('title', 'TikTok Video'),
                'url': info.get('url'),
                'thumbnail': info.get('thumbnail'),
                'duration': info.get('duration')
            }
        except Exception as e:
            return {"error": str(e)}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    video_url = request.json.get('url')
    if not video_url:
        return jsonify({"error": "URL tidak boleh kosong"}), 400
    
    result = get_tiktok_video(video_url)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
  
