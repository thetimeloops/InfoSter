import requests
from threading import Thread
from queue import Queue

q= Queue()

url1 = input("Enter URL ?>: " )
threads = int(input("Threads (max-100) ?>:"))
wordlist = input("Filename ?>:")
def subdomains_fast(url1):
    global q
    while True:
        subdomain=q.get()
        url=f"http://{subdomain}.{url1}"
        try:
            requests.get(url)
        except requests.ConnectionError:
            pass
        else:
            print("[+] Active subdomains: ",url)

        q.task_done()

def main(url1,n_threads,subdomains):
    global q;

    for subdomain in subdomains:
        q.put(subdomain)

    for i in range(n_threads):
        worker = Thread(target=subdomains_fast,args=(url1,))
        worker.daemon=True
        worker.start()





main(url1=url1, n_threads=threads, subdomains=open(wordlist).read().splitlines())
q.join()
