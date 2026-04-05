from flask import Flask, render_template, request, send_file
import yt_dlp
import os

app = Flask(__name__)
DOWNLOAD_DIR = 'downloads'

if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    link = request.form.get('url')
    ext = request.form.get('format', 'mp3')
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{DOWNLOAD_DIR}/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': ext,
            'preferredquality': '192',
        }],
        'quiet': False, # Ubah ke False agar kita bisa lihat prosesnya di terminal
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(link, download=True)
            filename = ydl.prepare_filename(info).rsplit('.', 1)[0] + '.' + ext
            
        return send_file(filename, as_attachment=True)
    except Exception as e:
        return f"Error: {str(e)}"

# BAGIAN INI WAJIB ADA DAN TIDAK BOLEH TYPO
if __name__ == '__main__':
    print("Server sedang berjalan di http://127.0.0.1:5000")
    app.run(debug=True, port=5000)