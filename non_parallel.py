import time

def hitung_jumlah_kuadrat(n):
    total = 0
    for i in range(1, n + 1):
        total += i * i
    return total

if __name__ == "__main__":
    N = 10_000_000

    start = time.time()
    hasil = hitung_jumlah_kuadrat(N)
    end = time.time()

    print(f"Hasil: {hasil}")
    print(f"Waktu eksekusi: {end - start:.4f} detik")