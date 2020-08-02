import time
import threading


def sleeper():
    print("sleeping 1 second..")
    time.sleep(1)


sleeper()
threads=[]
for _ in range(10):
    t = threading.Thread(target=sleeper)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

