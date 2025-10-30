import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse

# === FUNGSI: memastikan folder output tersedia ===
def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

# === FUNGSI UTAMA ===
def main():
    parser = argparse.ArgumentParser(description="Program Deteksi Tepi pada Citra (Sobel, Laplacian, Canny)")
    parser.add_argument('--input', '-i', required=True, help='Path gambar input (contoh: examples/gambar.jpg)')
    parser.add_argument('--out', '-o', default='outputs', help='Folder output')
    args = parser.parse_args()

    # --- 1. Baca gambar ---
    img = cv2.imread(args.input)
    if img is None:
        print(f"[ERROR] Gambar '{args.input}' tidak ditemukan.")
        return
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # --- 2. Deteksi tepi ---
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    sobel = cv2.magnitude(sobelx, sobely)

    laplacian = cv2.Laplacian(gray, cv2.CV_64F)
    laplacian = cv2.convertScaleAbs(laplacian)

    canny = cv2.Canny(gray, 100, 200)

    # --- 3. Pastikan folder output ada ---
    ensure_dir(args.out)

    # --- 4. Simpan hasil ---
    base = os.path.splitext(os.path.basename(args.input))[0]
    cv2.imwrite(os.path.join(args.out, f"{base}_gray.jpg"), gray)
    cv2.imwrite(os.path.join(args.out, f"{base}_sobel.jpg"), sobel)
    cv2.imwrite(os.path.join(args.out, f"{base}_laplacian.jpg"), laplacian)
    cv2.imwrite(os.path.join(args.out, f"{base}_canny.jpg"), canny)

    # --- 5. Tampilkan hasil ---
    titles = ['Asli', 'Grayscale', 'Sobel', 'Laplacian', 'Canny']
    images = [img[..., ::-1], gray, sobel, laplacian, canny]

    plt.figure(figsize=(12,6))
    for i in range(5):
        plt.subplot(2,3,i+1)
        plt.imshow(images[i], cmap='gray')
        plt.title(titles[i])
        plt.axis('off')

    plt.tight_layout()
    plt.savefig(os.path.join(args.out, f"{base}_comparison.png"))
    plt.show()

    print(f"\n✅ Proses selesai! Hasil disimpan di folder: '{args.out}'")

if __name__ == "__main__":
    main()
