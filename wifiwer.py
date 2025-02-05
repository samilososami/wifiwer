import os
from colorama import Fore, Style
import time
import platform
import subprocess

os.system("cls")
logo = r'''
 __      __.______________.___ __      ______________________ 
/  \    /  \   \_   _____/|   /  \    /  \_   _____|______   \.
\   \/\/   /   ||    __)  |   \   \/\/   /|    __)_ |       _/
 \        /|   ||     \   |   |\        / |        \|    |   \.
  \__/\  / |___|\___  /   |___| \__/\  / /_______  /|____|_  /
       \/           \/               \/          \/        \/ 
'''

command = "netsh wlan show profile"
result = subprocess.run(command, shell=True, capture_output=True, text=True)

try:
    profiles = []
    for line in result.stdout.splitlines():
        if "Perfil de todos los usuarios" in line:
            profile_name = line.split(":")[1].strip()
            profiles.append(profile_name)

    plataforma = platform.system()
    print(Fore.YELLOW + "[+] Resolving operative system...")
    time.sleep(1)
    print(Fore.GREEN + Style.BRIGHT + "[+]" + Style.RESET_ALL + Fore.GREEN + f" {plataforma} ✅")
    time.sleep(0.5)
    os.system("cls")

    is_running = True

    for line in logo.splitlines():
        print(Style.BRIGHT + f"{line}")
        time.sleep(0.05)

    usuario = input(Fore.LIGHTBLUE_EX + Style.BRIGHT + "\n[+] Press ENTER to show local wifis..." + Style.RESET_ALL)

except KeyboardInterrupt:
    is_running = False
    print(Fore.RED + "\n\n[!] Goodbye!" + Style.RESET_ALL)

try:
    while is_running:
        os.system("cls")
        print(Fore.GREEN + Style.BRIGHT + "[+] Local Wifis found: \n" + Style.RESET_ALL)
        for idx, profile in enumerate(profiles, start=1):
            print(Fore.GREEN + f"[{idx}] {profile}" + Style.RESET_ALL)
            time.sleep(0.05)

        try:
            selection = int(input(Fore.GREEN + Style.BRIGHT + "\nChoose an access point: " + Style.RESET_ALL))
            if 1 <= selection <= len(profiles):
                selected_profile = profiles[selection - 1]
                time.sleep(0.5)

                custom_command = f'netsh wlan show profile name="{selected_profile}" key=clear'
                wifi_result = subprocess.run(custom_command, shell=True, capture_output=True, text=True)

                ssid = None
                encryption = None
                security = None
                password = None
                name = None

                for line in wifi_result.stdout.splitlines():
                    if "Nombre de SSID" in line:
                        ssid = line.split(":")[1].strip()
                    if "Cifrado" in line:
                        encryption = line.split(":")[1].strip()
                    if "Autenticaci¢n" in line:
                        security = line.split(":")[1].strip()
                    if "Contenido de la clave" in line:
                        password = line.split(":")[1].strip()
                    if "Nombre" in line:
                        name = line.split(":")[1].strip()

                if security == "Abierta":
                    security = "OPEN!"
                elif encryption == "Ninguna":
                    encryption = "No encryption!"

                os.system("cls")
                print(Fore.GREEN + Style.BRIGHT + f"\n[+] Access point information --> " + Style.RESET_ALL + Fore.LIGHTCYAN_EX + f"{selected_profile}" + Style.RESET_ALL)
                time.sleep(0.5)
                print(Fore.GREEN + f"   Original name: " + Fore.LIGHTMAGENTA_EX + Style.BRIGHT + f"{name}" + Style.RESET_ALL)
                time.sleep(0.2)
                print(Fore.GREEN + f"   Encryption: {encryption}" + Style.RESET_ALL)
                time.sleep(0.2)
                if security == "OPEN!":
                    print(Fore.GREEN + f"   Security: " + Fore.LIGHTCYAN_EX + f"{security}" + Style.RESET_ALL)
                else:
                time.sleep(0.2)
                if password:
                    print(Fore.GREEN + f"   Password: " + Style.BRIGHT + Fore.LIGHTMAGENTA_EX + f"{password}" + Style.RESET_ALL)
                else:
                    print(Fore.RED + Style.BRIGHT + "   [!] No password found!" + Style.RESET_ALL)

            else:
                print(Fore.RED + "\n[!] Pick a valid number!" + Style.RESET_ALL)
                time.sleep(1)
        except ValueError:
            print(Fore.RED + "\n[!] That's not a number buddy!" + Style.RESET_ALL)
            time.sleep(1)
        again = input(Fore.YELLOW + Style.BRIGHT + "\n[i] Press ENTER to choose again...")
        os.system("cls")

except KeyboardInterrupt:
    is_running = False
    print(Fore.RED + "\n\n[!] Goodbye!" + Style.RESET_ALL)
