import requests
import threading

def check_url(url):

    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    }
    try:
        r = requests.get(url, timeout=3, headers=headers)
        if r.status_code == 200 or r.status_code == 301 or r.status_code == 302:
            print("[+]  Exists: " + url)
            with open('result.txt', 'a') as f:
                f.write("[+]  <" + str(r.status_code) + ">" + url + "\n")
    except:
        pass

def main():
    target_url = input("[*] Enter target URL: ")
    threads = int(input("[*] Enter number of threads: "))
    wordlist_file = "./dicc.txt"
    result_file = "./result.txt"

    print("[*] Starting path brute force...")
    print("[*] Target: " + target_url)
    print("[*] Wordlist file path: " + wordlist_file)

    with open(wordlist_file) as f:
        content = f.read()

    wordlist = content.splitlines()

    for word in wordlist:
        url = target_url + "/" + word
        t = threading.Thread(target=check_url, args=(url,))
        t.start()

if __name__ == '__main__':
    main()
