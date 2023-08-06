def check_http_scheme(url):
	if not (url.startswith("http://") or url.startswith("https://")):
		url = f"http://{url}"
		print(f"[!] No http scheme supplied. Modified url to {url}.")
	if not url[-1] == '/':
		url += '/'
	return url
	
def check_host_alive(url, requests):
	print(f"[+] Checking if site exists...")
	check = requests.get(url)
	if not check.status_code == 200:
		print(f"[-] Site returned a non 200 status code (returned: {check.status_code})")
	else:
		print(f"[+] Site is Ok")