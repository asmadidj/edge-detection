# 🔍 Edge Detection — OpenCV (Python)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green?logo=opencv)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%2010%20%7C%20Anaconda%20%7C%20VSCode-lightgrey)

---

## Deskripsi Proyek
Proyek ini merupakan tugas mata kuliah **Pengolahan Citra Digital / Computer Vision**  
pada **S2 Teknik Informatika UNPAM**.

Tujuan proyek ini adalah **mendeteksi tepi pada citra digital** menggunakan beberapa metode populer di bidang *image processing*, yaitu:
- **Sobel Operator**
- **Laplacian Operator**
- **Canny Edge Detection**

Hasil deteksi divisualisasikan dalam satu gambar perbandingan untuk memudahkan analisis visual terhadap perbedaan metode.

---

## Contoh Hasil Deteksi Tepi
> Gambar di bawah memperlihatkan hasil deteksi tepi dari citra daun menggunakan metode Sobel, Laplacian, dan Canny.

![Contoh Output](docs/gambar_comparison.png)

---

## Teknologi yang Digunakan
- **Python 3.10+**
- **OpenCV (cv2)**
- **NumPy**
- **Matplotlib**

---

## Fitur Utama
1.Konversi gambar ke **grayscale**  
2.Deteksi tepi dengan **Sobel**, **Laplacian**, dan **Canny**  
3.Penyimpanan hasil otomatis ke folder `outputs/`  
4.Visualisasi hasil menggunakan **matplotlib**

---

## Instalasi & Cara Menjalankan

### 1️⃣ Clone repository
```bash
git clone https://github.com/asmadidj/edge-detection.git
cd edge-detection
