# Payload_Generation_Automation_tool
This script automate payload generation process using Msfvenom exploit tool. We can generate payload for all plaforms. By simply add list (ex: win_list.txt) as input and generate payload as per our requirements.

# Requirement
Os: kalilinux
Programming language : Python3
Env: VM workstation

# Usage
msfvenom -p win_list -a <architecture(x86 or x64)> --enocoders LHOST=<local_ip> LPORT=<local_port> -formats
