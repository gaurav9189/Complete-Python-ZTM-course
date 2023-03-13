import hashlib
import sys
import requests


def request_response(query_char, tail):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    # print(url)
    resp = requests.get(url)
    if resp.status_code != 200:
        print(f'Something wrong with the API check again {resp.status_code}')
    return check_leaks(resp, tail)


def sha_gen(password):
    hash_obj = hashlib.sha1(f'{password}'.encode())
    back_5 = hash_obj.hexdigest().upper()[5:]
    front_5 = hash_obj.hexdigest().upper()[:5]
    return request_response(front_5, back_5)

    # print(hash_dict)


def check_leaks(resp, tail):
    # print(resp)
    response_list = [i.decode().split(':') for i in resp.iter_lines()]
    # print(response_list)
    for i in response_list:
        if i[0] == tail:
            return i[1]


def main(passwords):
    for i in passwords:
        count = sha_gen(i)
        if count:
            print(f'{i} was used {count} times')
        else:
            print(f'your password {i} is good')


passwords = sys.argv[1:]
main(passwords)
