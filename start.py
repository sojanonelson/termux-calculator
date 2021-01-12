import os,sys,time
os.system("clear")
BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33m"    # Yellow
G = "\033[32m"    # Green
W = "\033[0m"     # White
R = "\033[31m"    # Red
C = "\033[36m"    # Cyan

def load(word):
        for char in word:
                print(char,end="")
                sys.stdout.flush()
                time.sleep(0.02)
load(f"{CC}              _                          \n")
load(f"{GG}             | |                          \n")
load(f"{RR}__      _____| | ___ ___  _ __ ___   ___  \n")
load(f"{WW}\ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ \n")
load(f"{BB} \ V  V /  __/ | (_| (_) | | | | | |  __/  \n")
load(f"{CC}  \_/\_/ \___|_|\___\___/|_| |_| |_|\___| \n")
load(f"{GG}                          coded by SOJAN  \n")
load(f"{RR} Git hub: https://github.com/SOJAN-HACKER \n\n")
z = input("whats  is your name :")
print("calculator[Addition only now.next coming soon]")
a = input("Enter first number :")
b = input("Enter second number :")
print("Hai "+ z + " your answer is :")
sum =int(a) + int(b)
print(str(sum))
print("Thanku for useing me")
print("Have a nicec day " + str(z))
