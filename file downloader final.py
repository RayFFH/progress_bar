from tqdm import tqdm
import requests
import time
import concurrent.futures

urls = [
'https://unsplash.com/photos/ErhaVPCytew','https://unsplash.com/photos/ygC8YJvaR1Y']


def downloader(url):
    print("Downloading file...")
    size = 1024
    r=requests.get(url, stream = True)

    total = int(r.headers['content-length'])

    with open("output.pdf",' wb') as f:
        for data in tqdm(iterable = r.iter_content(chunk_size = size), total =total/size, unit ='Kb'):
            f.write(data)


t1 = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(downloader, urls)

t2 = time.perf_counter()

print(f'Finished in {t2-t1} seconds')
print("Download is complete")