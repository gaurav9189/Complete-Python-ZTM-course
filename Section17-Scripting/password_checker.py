import requests
import hashlib
import sys

password = sys.argv[1:]
url = 'https://api.pwnedpasswords.com/range/'


def hash_gen(password):
    hash_dict = {}
    for i in password:
        hash_obj = hashlib.sha1(f'{i}'.encode())
        hash_5 = hash_obj.hexdigest().upper()[5:]
        front_5 = hash_obj.hexdigest().upper()[:5]
        # print(f'hash5 for {i} is: {hash_5}')
        hash_dict[f'{i}'] = [hash_5, front_5]
        # print(hash_dict)
    return hash_dict


def check_pwned(dict):
    # print(dict)
    final_repsonse = {}
    for k, v in dict.values():
        burl = url + v
        res = requests.get(burl).iter_lines()
        for i in res:
            hash_resp = i.decode().split(':')[0]
            if k == hash_resp:
                times = i.decode().split(':')[1]
                # print(f'You have been pwned {times} times with password {v}')
                final_repsonse[v] = times
    return final_repsonse


def main(pwned, hash):
    for k, v in hash.items():
        f5 = v[1]
        if f5 in pwned:
            print(f'"{k}" password has been used {pwned[f5]} times')
        else:
            print(f'"{k}" password is safe')


hashed = hash_gen(password)
pwned = check_pwned(hashed)
main(pwned, hashed)
