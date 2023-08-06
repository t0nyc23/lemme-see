def get_robots(url, get_request):
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.78 Safari/537.36',}
	print("[+] Checking for a robots.txt file...")
	toolsyep = "https://toolsyep.com/en/webpage-to-plain-text/?u="
	url = url.replace("/", "%2F").replace(":", "%3A") + "%2Frobots.txt"
	target_url = f"{toolsyep}{url}"
	req = get_request(target_url, headers=headers).text
	robots_file = ""
	for line in req.split("\n"):
		if not line.startswith("<"):
			robots_file += f"\n{line}"
	if "User-agent:" in robots_file:
		robots_file = robots_file.replace("</pre>", "").replace(" ", "").replace("\n", "")
		robots_file = robots_file.replace("User-agent:", "\n\nUser-Agent: ")
		robots_file = robots_file.replace("Disallow:", "\nDisallow: ")
		robots_file = robots_file.replace("Allow:", "\nAllow: ")
		robots_file = robots_file.replace("Sitemap:", "\n\nSitemap: ")
		robots_file = robots_file.replace("Host:", "\n\nHost: ")
		robots_file = robots_file.replace("-------------------", "\n-------------------\n")
	return robots_file