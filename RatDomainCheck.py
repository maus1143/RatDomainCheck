import os
import time
import threading

RatDomainCheckVersion = "0.0.1"

red = '\033[91m'
blue = '\033[94m'
green = '\033[92m'
white = '\033[97m'
yellow = '\033[93m'

def Rat_defined_print(message):
    print(f"{white}{message}")

os.system("cls" if os.name == "nt" else "clear")

def loading_screen(stop_event):
    while not stop_event.is_set():
        for char in "|/-\\":
            print(f"{white}Überprüfe Verfügbarkeit... {char}", end="\r")
            time.sleep(0.2)

def check_domain_availability(domain):
    Rat_defined_print(f"Überprüfe die Verfügbarkeit der Domain: {yellow}'{domain}'")
    stop_event = threading.Event()
    loading_thread = threading.Thread(target=loading_screen, args=(stop_event,))
    loading_thread.start()
    
    response = os.system(f"ping {domain} > nul")
    
    stop_event.set()
    loading_thread.join()
    
    if response == 0:
        Rat_defined_print(f"Die Domain '{yellow}{domain}{white}' ist aktiv {red}(nicht kaufbar){white}.")
        time.sleep(15)
    else:
        Rat_defined_print(f"Die Domain '{yellow}{domain}{white}' ist nicht erreichbar {green}(wahrscheinlich kaufbar){white}.")
        time.sleep(15)

if __name__ == "__main__":
    Rat_defined_print(f"RatDomainCheck | Version: {yellow}{RatDomainCheckVersion}")
    domain = input(f"{white}Gib die Domain ein (ohne http/https, z.B. example.com):{yellow} ")
    check_domain_availability(domain)
#By Mausi Schmausi