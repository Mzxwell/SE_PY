import concurrent.futures
import time

def cpu_intensive_task(start, end):
    result = 0
    for i in range(start, end):
        result += i**2
    return result

n = 10**6

if __name__ == "__main__":
    # 单进程执行
    start_time = time.time()
    result = cpu_intensive_task(0, 4 * n)
    print(f"Single process time: {time.time() - start_time:.4f} seconds")

    # 多进程执行
    start_time = time.time()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(cpu_intensive_task, i * n, (i + 1) * n) for i in range(4)]
        result = sum(future.result() for future in concurrent.futures.as_completed(futures))
    print(f"Multi-process time: {time.time() - start_time:.4f} seconds")
