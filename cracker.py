import hashlib
import argparse
import os

def crack_hash(hash_to_crack, wordlist_path, algorithm='sha256'):
    if not os.path.exists(wordlist_path):
        print(f"[!] Wordlist file not found: {wordlist_path}")
        return

    try:
        hash_func = getattr(hashlib, algorithm)
    except AttributeError:
        print(f"[!] Unsupported hash algorithm: {algorithm}")
        return

    with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as file:
        for word in file:
            word = word.strip()
            hashed_word = hash_func(word.encode()).hexdigest()
            if hashed_word == hash_to_crack:
                print(f"[+] Password found: {word}")
                return

    print("[-] Password not found in wordlist.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Hashed Password Cracker")
    parser.add_argument("-H", "--hash", required=True, help="Hashed password to crack")
    parser.add_argument("-w", "--wordlist", required=True, help="Path to password wordlist")
    parser.add_argument("-a", "--algorithm", default="sha256", help="Hash algorithm (default: sha256)")
    args = parser.parse_args()

    crack_hash(args.hash, args.wordlist, args.algorithm.lower())
