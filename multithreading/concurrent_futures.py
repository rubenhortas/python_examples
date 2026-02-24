import concurrent.futures
import os
import time
import urllib.request

URLS = ["https://www.google.com/", "https://www.python.org/", "https://www.github.com/", "https://stackoverflow.com"]


def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()


def run_concurrent_tasks():
    # ThreadPoolExecutor for I/O bound tasks
    with concurrent.futures.ThreadPoolExecutor(max_workers=min(32, os.cpu_count() + 4)) as executor:
        future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}

        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]

            try:
                data = future.result()
                print(f"Downloaded '{url}' ({len(data)} bytes)")
            except Exception as exc:
                print(f"ERROR: '{url}': {exc}")


if __name__ == "__main__":
    start_time = time.time()
    run_concurrent_tasks()
    print(f"Time: {time.time() - start_time:.2f}secs")
