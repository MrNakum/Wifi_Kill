

import os

print("*" * 60)
print("[+] Installing Dependencies ...")
print("*" * 60)
os.system("sudo apt-get install git")
print("*" * 60)
print("[+] Dependencies Download")
print("*" * 60)

if os.path.exists("wificurse"):
	os.chdir("wificurse")
	print("*" * 60)

	print("[+] Directory Changed.")
	print("[+] Ready For Compile.")
	print("*" * 60)

	os.system("make");
	print("*" * 60)

	print("[+] Compilation Done.")
	os.system("sudo make install");

	print("*" * 60)
	print("""[+] Code Compile and set into system Succefully.")
[+] You are ready to jammed all wifi within limited redius.
[+] Run Wifi_Jammer Script To test and Jammed.""")
	print("*" * 60)
else: 
	print("*" * 60)
	print("[-] Unknown Error occured.")
	print("*" * 60)
