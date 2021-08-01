import sys, zipfile
from termcolor import *

passwd_file = "rockyou.txt"
zip_file = ""

def crack_passwd(passwd_list, zip_obj):
    with open(passwd_list, 'rb') as file:
        for line in file:
            for word in line.split():
                try:
                    cprint("[-] Password failed - %s" % word.decode("utf-8"), 'red', attrs=['bold'])
                    sys.stdout.write("\033[F")
                    sys.stdout.write("\033[K")
                    zip_obj.extractall(pwd=word)
                    cprint("[+] Password found - %s" % word.decode("utf-8"), 'green', attrs=['bold'])
                    return True
                except:
                    continue
    cprint("[-] Password cannot be found. Try other wordlist.", 'white', 'on_red', attrs=['bold'])
    return False


def print_usage():
    cprint("Usage: python3 crack.py <zip file> <password file>", 'white')

def print_files(zip_obj):
    for file in zip_obj.namelist():
        print('File name: ', file, '\tFile size: ', zip_obj.getinfo(file).file_size)

if ( len(sys.argv) == 2 ):
    cprint("[INFO] Using rockyou.txt as password list.", 'green')
    zip_file = sys.argv[1]
elif ( len(sys.argv) == 3):
    cprint("[INFO] Using %s as password list." % (sys.argv[2]), 'green')
    zip_file = sys.argv[1]
    passwd_file = sys.argv[2]
else:
    print_usage()
    sys.exit()


zip_obj = zipfile.ZipFile(zip_file)

if crack_passwd(passwd_file, zip_obj):
    print_files(zip_obj)