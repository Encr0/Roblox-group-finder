import os import threading import requests import random from dhooks
import Webhook import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("Encr0 Group Finder")

hook_url = input("[-] Enter your webhook URL: ")
threads = int(input("[-] How many threads: "))

hook = Webhook(hook_url)

def groupfinder():
    try:
        id = random.randint(13000000, 20000000)
        r = requests.get(f"https://www.roblox.com/groups/group.aspx?gid={id}", timeout=30)
        if 'owned' not in r.text:
            re = requests.get(f"https://groups.roblox.com/v1/groups/{id}", timeout=30)
            if re.status_code != 429:
                if 'errors' not in re.json():
                    if 'isLocked' not in re.json() and 'owner' in re.json() and re.json()['publicEntryAllowed'] == True and re.json()['owner'] == None:
                        hook.send(f'Hit: https://www.roblox.com/groups/group.aspx?gid={id}')
                        print(f"[+] Hit: {id}")
                    else:
                        if 'isLocked' in re.json() and re.json()['isLocked'] == True:
                            print(f"[-] Group Locked: {id}")
                        else:
                            print(f"[-] No Entry Allowed: {id}")
                else:
                    print(f"[-] Group Already Owned: {id}")
            else:
                print(f"[-] Group API Rate Limited")
        else:
            print(f"[-] Group Already Owned: {id}")
    except Exception as e:
        print(f"[-] Error: {e}")

print("""

░▒▓████████▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓████████▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓██████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░ 
                                                                   
""")

while True:
    if threading.active_count() <= threads:
        threading.Thread(target=groupfinder).start()
