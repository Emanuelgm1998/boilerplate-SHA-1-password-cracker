import hashlib

def crack_sha1_hash(hash, use_salts=False):
    with open('top-10000-passwords.txt') as f:
        passwords = [line.strip() for line in f]
    if use_salts:
        with open('known-salts.txt') as sf:
            salts = [line.strip() for line in sf]
        for salt in salts:
            for pw in passwords:
                if hashlib.sha1((salt + pw + salt).encode('utf-8')).hexdigest() == hash:
                    return pw
    else:
        for pw in passwords:
            if hashlib.sha1(pw.encode('utf-8')).hexdigest() == hash:
                return pw
    return "PASSWORD NOT IN DATABASE"
