# Belajar Skills AI (Procedural Agent)

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Proyek ini adalah contoh nyata implementasi **Skills Prosedural** menggunakan AI Agent berbasis **DeepSeek API**. Agent ini tidak hanya menjawab teks, tetapi dapat menjalankan fungsi-fungsi terprogram secara otomatis berdasarkan logika prosedural.

## 🚀 Fitur Utama
- **Automated Workflow**: Agent dapat memutuskan langkah selanjutnya berdasarkan output fungsi sebelumnya.
- **Python-Based Skills**: Integrasi mudah dengan fungsi Python biasa.
- **Premium Documentation**: Halaman dokumentasi web modern dengan fitur Dark Mode.

## 📁 Struktur Folder
```text
belajar_skills_ai/
├── app.py              # Script utama AI Agent
├── requirements.txt    # Daftar dependensi
├── README.md           # Dokumentasi GitHub
└── docs/               # Dokumentasi Web
    ├── index.html
    ├── style.css
    └── script.js
```

## 🛠️ Cara Instalasi
1. Clone repositori ini.
2. Instal library yang dibutuhkan:
   ```bash
   pip install -r requirements.txt
   ```
3. Set Environment Variable untuk DeepSeek API:
   ```bash
   # Windows (CMD)
   set DEEPSEEK_API_KEY=your_api_key_here
   ```

## 📋 Cara Penggunaan
Cukup jalankan file `app.py`:
```bash
python app.py
```
Agent akan memproses prompt default dan mendemonstrasikan pemanggilan tool secara otomatis (cek stok, hitung diskon, kirim email).

## 🌙 Dokumentasi Web
Anda dapat membuka file `docs/index.html` di browser Anda untuk melihat panduan lengkap dalam format web interaktif yang mendukung mode gelap/terang.

---
Dibuat untuk keperluan belajar integrasi tool AI.
