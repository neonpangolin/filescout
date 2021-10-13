
# Import libraries and modules
import webbrowser, requests

c_red   =   "\033[01;31m"
c_clear   =   "\033[0m"

print('')
print('\033[01;31m   /$$$$$$$$$/$$$$/$$$$    /$$$$$$$$')
print('\033[01;31m  | $$$$$$$$$ $$$$ $$$$   | $$$$$$$$')
print('\033[01;31m  | $$$$   /| $$$$ $$$$   | $$$$   /')
print('\033[01;31m  | $$$$$$$$| $$$$ $$$$   | $$$$$$$$')
print('\033[01;31m  | $$$$$$$$| $$$$ $$$$   | $$$$$$$$')
print('\033[01;31m  | $$$$___/| $$$$ $$$$   | $$$$   /')
print('\033[01;31m  | $$$$    | $$$$ $$$$$$$$ $$$$$$$$')
print('\033[01;31m  | $$$$    | $$$$ $$$$$$$$ $$$$$$$$')
print('\033[01;31m  |/___/    |/___//______/|/_______/')
print('')
print('\033[01;31m   /$$$$$$$$/$$$$$$$$/$$$$$$$$$$$$/$$$$   /$$$$/$$$$$$$$$$$$')
print('\033[01;31m  | $$$$$$$$ $$$$$$$$ $$$$$$$$$$$$ $$$$  | $$$$ $$$$$$$$$$$$')
print('\033[01;31m  | $$$$   | $$$$___/ $$$$__/ $$$$ $$$$  | $$$$/__/ $$$$___/')
print('\033[01;31m  | $$$$$$$$ $$$$   | $$$$  | $$$$ $$$$  | $$$$   | $$$$')
print('\033[01;31m  |/___ $$$$ $$$$   | $$$$  | $$$$ $$$$  | $$$$   | $$$$')
print('\033[01;31m   /$$$$$$$$ $$$$$$$$ $$$$$$$$$$$$ $$$$$$$$$$$$   | $$$$')
print('\033[01;31m  | $$$$$$$$ $$$$$$$$ $$$$$$$$$$$$ $$$$$$$$$$$$   | $$$$')
print('\033[01;31m  |/_______/________//___________//__________/    |/___/')
print('"\033[0m"')

# Name of target website
print('Please enter the name of the target website')
target = input('... ')

print('Please select the filetypes you would like to search for')
print('-d (documents) -p (passwords) -e (emails)')
print('-b (databases) -s (software) -c (configurations)')   
print('or -m (microsoft)')

# Defines action to take
flag = input('... ')

keyword = input('... ')

# Document files
docs = ['txt','rtf','odt','csv','xls','xlsx','odp','ppt','html','mht','xml']

# Passwords, usernames and login items
passwords = ['htpasswd', 'pass','password','pem','csr','netrc','key','pgp','asc']

# Email files
emails = ['eml','mbx','wab']

# Database files
databases = ['sql','nsf','php','mdb','fp3','fp5','fp7','ldb','ora','myd']

# Software and application files
software = ['env','inf','cfg','log','dotenv','inf','ini','lic','blt','conf','log','reg','env', 'mdb', 'cfm', 'config','avastlic']

# Systems, wireless and networks
configurations = ['ns1','pac','pcf','cfm','axd','cgi','cnf','jnlp','pcmcfg''mobileconfig']

# Microsoft files
microsoft = ['lit','lit','ldb','mdb','mny','pdb','bkf']


# Push list in exploits_list.py to function parameters
def search(docs):
    for i in docs:
        url = 'http://google.com/search?q=site%3A' + target + '+filetype%3A' + i + '+%22'+ keyword + '%22'
        webbrowser.open(url)

def search(passwords):
    for i in passwords:
        url = 'http://google.com/search?q=site%3A' + target + '+filetype%3A' + i + '+%22'+ keyword + '%22'
        webbrowser.open(url)

def search(emails):
    for i in emails:
        url = 'http://google.com/search?q=site%3A' + target + '+filetype%3A' + i + '+%22'+ keyword + '%22'
        webbrowser.open(url)


def search(databases):
    for i in databases:
        url = 'http://google.com/search?q=site%3A' + target + '+filetype%3A' + i + '+%22'+ keyword + '%22'
        webbrowser.open(url)


def search(software):
    for i in software:
        url = 'http://google.com/search?q=site%3A' + target + '+filetype%3A' + i + '+%22'+ keyword + '%22'
        webbrowser.open(url)

def search(configurations):
    for i in configurations:
        url = 'http://google.com/search?q=site%3A' + target + '+filetype%3A' + i + '+%22'+ keyword + '%22'
        webbrowser.open(url)

def search(mirosoft):
    for i in mirosoft:
        url = 'http://google.com/search?q=site%3A' + target + '+filetype%3A' + i + '+%22'+ keyword + '%22'
        webbrowser.open(url)

if '-d' in flag:
        search(docs)
elif '-p' in flag:
    search(passwords)
elif '-e' in flag:
    search(emails)
elif '-b' in flag:
    search(databases)
elif '-s' in flag:
    search(software)
elif '-c' in flag:
    search(configurations)    
elif '-m' in flag:
    search(microsoft)
else:
    print('"\033[01;31m"')
    print('Please pass a valid argument')

