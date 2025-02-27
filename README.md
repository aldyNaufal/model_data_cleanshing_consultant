# FastAPI Consultant Name Cleaner

## Deskripsi
FastAPI Consultant Name Cleaner adalah sebuah API berbasis FastAPI yang dirancang untuk membersihkan dan menstandarkan nama konsultan. API ini memanfaatkan data referensi yang disimpan dalam file CSV dan menggunakan teknik fuzzy matching untuk mengoreksi kesalahan penulisan nama konsultan sehingga menghasilkan data yang lebih konsisten dan akurat.

## Fitur
- **Pembersihan Nama Konsultan:** Memperbaiki kesalahan penulisan pada nama konsultan.
- **Standarisasi Data:** Menstandarkan format nama konsultan berdasarkan data referensi.
- **Fuzzy Matching:** Menggunakan algoritma fuzzy matching (dengan RapidFuzz) untuk mencocokkan nama konsultan meskipun terdapat variasi penulisan.
- **Integrasi Cepat dengan FastAPI:** API siap digunakan dengan dokumentasi interaktif melalui Swagger UI dan Redoc.

## Persyaratan
Pastikan Anda telah menginstal:
- Python 3.8 atau versi lebih baru.
- pip (Python package manager).

## Instalasi
1. **Clone Repository (Opsional, jika menggunakan repo GitHub)**
   ```sh
   git clone https://github.com/username/repo-name.git
   cd repo-name
   ```

2. **Buat dan Aktifkan Virtual Environment**
   ```sh
   python -m venv venv
   source venv/bin/activate  # Untuk Linux/Mac
   venv\Scripts\activate     # Untuk Windows
   ```

3. **Install Dependensi**
   ```sh
   pip install -r requirements.txt
   ```
   Jika tidak terdapat file `requirements.txt`, Anda dapat menginstal paket secara manual:
   ```sh
   pip install fastapi uvicorn pandas rapidfuzz
   ```

## Struktur File
```
project-directory/
│── train_data.csv          # Dataset berisi daftar nama konsultan dan nomor konsultan
│── main.py                 # File utama aplikasi FastAPI
│── requirements.txt        # Daftar dependensi proyek
│── README.md               # Dokumentasi proyek
```

## Menjalankan Aplikasi
### Pengembangan Lokal
Jalankan aplikasi dengan auto-reload (berguna saat pengembangan):
```sh
uvicorn main:app --reload
```
Aplikasi akan berjalan di `http://127.0.0.1:8000`  
Dokumentasi API dapat diakses melalui:
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### Akses dari Host Lain (Remote)
Untuk menjalankan API agar dapat diakses dari perangkat lain, jalankan:
```sh
uvicorn main:app --host 0.0.0.0 --port 8080
```
Pastikan:
- Port 8080 tidak diblokir oleh firewall.
- Jika menggunakan NAT atau router, lakukan konfigurasi port forwarding sesuai kebutuhan.

## Cara Menggunakan API
### Endpoint: `/clean/`
- **Method:** `POST`
- **Request Body:**  
  Kirim data dalam format JSON seperti berikut:
  ```json
  {
    "Nama_Konsultan": "Nama konsultan yang ingin dibersihkan",
    "No_Konsultan": "Nomor konsultan asli",
    "Alamat_Korespondensi": "Alamat korespondensi",
    "Email": "Alamat email",
    "No_Telp": "Nomor telepon"
  }
  ```
- **Response:**  
  API akan mengembalikan response JSON dengan data yang telah dibersihkan:
  ```json
  {
    "clean_text_nama": "Nama konsultan yang telah dibersihkan",
    "clean_no_konsultan": "Nomor konsultan sesuai data referensi"
  }
  ```

## Deployment (Opsional)
### Menjalankan dengan Docker
1. **Buat Dockerfile** di dalam direktori proyek:
   ```dockerfile
   FROM python:3.9
   WORKDIR /app
   COPY . /app
   RUN pip install --no-cache-dir -r requirements.txt
   CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
   ```
2. **Bangun dan Jalankan Container:**
   ```sh
   docker build -t fastapi-consultant-cleaner .
   docker run -p 8080:8080 fastapi-consultant-cleaner
   ```

## Lisensi
Proyek ini dilisensikan di bawah lisensi MIT. Silakan gunakan dan modifikasi sesuai kebutuhan Anda.
