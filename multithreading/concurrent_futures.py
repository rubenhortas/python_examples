#!/usr/bin/env python3

import concurrent.futures
import os
import time
import urllib.request

URLS = ["https://www.google.com/", "https://www.python.org/", "https://www.github.com/", "https://stackoverflow.com"]


def _load_url(url, timeout) -> bytes:
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()


def _main() -> None:
    # ThreadPoolExecutor for I/O bound tasks
    with concurrent.futures.ThreadPoolExecutor(max_workers=min(32, (os.cpu_count() or 1) + 4)) as executor:
        future_to_url = {executor.submit(_load_url, url, 60): url for url in URLS}

        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]

            try:
                data = future.result()
                print(f"Downloaded '{url}' ({len(data)} bytes)")
            except Exception as exc:
                print(f"ERROR: '{url}': {exc}")


if __name__ == "__main__":
    try:
        start_time = time.time()
        _main()
        print(f"Time: {time.time() - start_time:.2f}secs")
    except KeyboardInterrupt:
        pass
