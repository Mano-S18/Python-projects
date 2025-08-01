import requests
import hashlib
import sys

def resquest_api_data(password):
    url = 'https://api.pwnedpasswords.com/range/' + password
    req = requests.get(url)
    return req

def password_count(hashes,hastochk):
    hashes = (lines.split(':') for lines in hashes.text.splitlines())
    for h,count in hashes:
        if h==hastochk:
            return count
    return 0

def pwned_api_chk(password):
    hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    head, tail = hash[:5],hash[5:]
    resp = resquest_api_data(head)
    return password_count(resp,tail)
    
def main(argv):
    for password in argv:
        count = pwned_api_chk(password)
        if count:
            print(f'your password is pawned {count} times, change it')
        else:
            print(f'your password is gud')
    


main(sys.argv[1:])