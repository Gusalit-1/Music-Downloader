# 🎵 Music Downloader & Audio Processor

[![Python Version](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/)
[![Framework](https://img.shields.io/badge/framework-Flask-lightgrey.svg)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Music Downloader** adalah aplikasi berbasis Web (Flask) yang dirancang untuk mengunduh audio dari berbagai platform dan melakukan pemrosesan awal (preprocessing) agar kompatibel dengan model AI Detection.

---

## 🚀 Fitur Utama
* **High-Quality Download:** Mengunduh audio dengan format terbaik menggunakan engine `yt-dlp`.
* **Auto-Conversion:** Mengonversi hasil unduhan langsung ke format `.wav` (Lossless) agar akurasi deteksi AI lebih maksimal.
* **Simple Dashboard:** Antarmuka web yang bersih dan mudah digunakan.
* **Integrated Workflow:** Hasil unduhan dapat langsung digunakan sebagai input untuk model **AudioLens AI**.

---

## 🛠️ Arsitektur Teknologi
Aplikasi ini dibangun menggunakan *stack* teknologi berikut:
* **Backend:** Python 3.11 & Flask
* **Engine Unduh:** yt-dlp
* **Processing:** Librosa & FFmpeg
* **Frontend:** HTML5, CSS (Tailwind), dan JavaScript (Fetch API)



---

## 📋 Prasyarat Sistem
Sebelum menjalankan aplikasi, pastikan perangkat Anda sudah terinstal:
1. **Python 3.11** (Sangat disarankan untuk stabilitas library).
2. **FFmpeg** (Wajib terinstal di sistem PATH untuk proses konversi audio).

---

## ⚙️ Cara Instalasi

1. **Clone Repository**
   ```bash
   git clone [https://github.com/Gusalit-1/Music-Downloader.git](https://github.com/Gusalit-1/Music-Downloader.git)
   cd Music-Downloader
2. **Buat & Aktifkan Virtual Environment**
3. **Instal Library yang Dibutuhkan**

   
## 🏃 Cara Menjalankan
1. **Jalankan server Flask:**
2. **Buka browser dan akses:**
3. **Masukkan link musik, klik download, dan file akan tersimpan di folder downloads/.**

## 📂 Struktur Folder
Music-Downloader/
├── app.py              # Logika Backend Flask
├── static/             # File CSS & JavaScript
├── templates/          # Tampilan HTML (index.html)
├── downloads/          # Tempat penyimpanan hasil unduhan (ignored)
├── .gitignore          # File pengecualian Git
└── README.md           # Dokumentasi Project
