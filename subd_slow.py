import requests



def subdomains_slow(url1):
    file=open("subdomains.txt")
    content = file.read()
    subdomains = content.splitlines()
    for subdomain in subdomains:
        url=f"http://{subdomain}.{url1}"
        try:
            requests.get(url)
        except requests.ConnectionError:
            pass
        else:
            print("[+] Active subdomains: ",url)
