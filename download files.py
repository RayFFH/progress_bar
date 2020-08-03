from tqdm
import tqdm
import requests
import time

def downloader(url)
chunk = 1024
r-requests.get(url, stream = True)

total_size = int(r.headers['content-length'])

    with open("python.pdf",'wb') as f:
        for data in tqdm(itera = r.iter_content(chunk = chunk)), total = total_size/chunk, unit = 'KB')

t1 = time.perf_counter()

with concurrent.futures.ThreadPoolExectuor() as executor:
        executor.map(downloader, urls)

t2 = time.perf_counter()