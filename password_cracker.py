import hashlib

def crack_sha1_hash(hash, use_salts=False):
    with open('top-10000-passwords.txt') as f:
        passwords = [line.strip() for line in f]
    if not use_salts:
        for pw in passwords:
            if hashlib.sha1(pw.encode('utf-8')).hexdigest() == hash:
                return pw
        return "PASSWORD NOT IN DATABASE"

    with open('known-salts.txt') as f:
        salts = [line.strip() for line in f]
    for pw in passwords:
        for salt in salts:
            combo = salt + pw + salt
            if hashlib.sha1(combo.encode('utf-8')).hexdigest() == hash:
                return pw
            combo = salt + pw
            if hashlib.sha1(combo.encode('utf-8')).hexdigest() == hash:
                return pw
            combo = pw + salt
            if hashlib.sha1(combo.encode('utf-8')).hexdigest() == hash:
                return pw
    return "PASSWORD NOT IN DATABASE"
