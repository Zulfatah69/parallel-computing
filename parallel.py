# parallel.py

import time
import multiprocessing

def hitung_sebagian(start, end):
    total = 0
    for i in range(start, end):
        total += i * i
    return total

if __name__ == "__main__":
    N = 10_000_000
    jumlah_proses = multiprocessing.cpu_count()

    pool = multiprocessing.Pool(jumlah_proses)

    chunk_size = N // jumlah_proses
    tasks = []

    for i in range(jumlah_proses):
        start = i * chunk_size + 1
        end = (i + 1) * chunk_size + 1 if i != jumlah_proses - 1 else N + 1
        tasks.append((start, end))

    start_time = time.time()

    results = pool.starmap(hitung_sebagian, tasks)
    pool.close()
    pool.join()

    total = sum(results)

    end_time = time.time()

    print(f"Hasil: {total}")
    print(f"Menggunakan {jumlah_proses} core CPU")
    print(f"Waktu eksekusi: {end_time - start_time:.4f} detik")