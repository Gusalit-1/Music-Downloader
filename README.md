# AudioGrab - YouTube Music Downloader 🎵

Aplikasi berbasis web sederhana untuk mengunduh audio dari YouTube dalam format MP3 atau WAV menggunakan **Flask** dan **yt-dlp**. Proyek ini dikembangkan sebagai bagian dari pembelajaran pengembangan perangkat lunak dan implementasi library Python.

## 🚀 Fitur
- Unduh audio langsung dari URL YouTube.
- Pilihan format output: **MP3** atau **WAV**.
- Proses konversi otomatis menggunakan **FFmpeg**.
- Tampilan antarmuka yang bersih dengan **Tailwind CSS**.

## 🛠️ Prasyarat
Sebelum menjalankan proyek ini, pastikan kamu sudah menginstal:
- [Python 3.10+](https://www.python.org/)
- [FFmpeg](https://ffmpeg.org/download.html) (Wajib ada di PATH sistem)

## 📦 Instalasi

1. **Clone repositori ini:**
   ```bash
   git clone [https://github.com/Gusalit-1/Music-Downloader.git](https://github.com/Gusalit-1/Music-Downloader.git)
   cd Music-Downloader

   
2. **Buat dan aktifkan Virtual Environment:**
  PowerShell
   python -m venv .venv
   .\venv\Scripts\activate
   
3.**Instal library yang dibutuhkan:**
   Bash
   pip install flask yt-dlp
   
4.**Cara Menjalankan**
   Pastikan venv sudah aktif.
   Jalankan server Flask:
   python app.py
   Buka browser dan akses: http://127.0.0.1:5000


