import concurrent.futures
import time

def print_test():
    time.sleep(1)
    print("Hi")

def main():
    stop_watch = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        for _ in range(10):
            executor.submit(print_test)


    print(f"finished in {time.perf_counter()-stop_watch:.6f}")

if __name__ == "__main__":
    main()