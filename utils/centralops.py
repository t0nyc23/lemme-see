from bs4 import BeautifulSoup
#import requests
import time
import sys
import re

def is_ipv4(ip_str):
    # Regular expression for IPv4 address
    ipv4_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    return re.match(ipv4_pattern, ip_str) is not None

def is_ipv6(ip_str):
    # Regular expression for IPv6 address
    ipv6_pattern = r'^(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,6}:|:[0-9a-fA-F]{1,4}|:)$'
    return re.match(ipv6_pattern, ip_str) is not None

# Address Lookup
def address_lookup(soup):
	addresses_lookup_txt = ""
	canonical_name = soup.find('td', string='canonical name')

	if canonical_name:
	    canonical_name = canonical_name.find_next('td').find('a').text.strip()
	    addresses_lookup_txt += f"{'='*80}\n\nAddress Lookup\n{'-'*15}\nCanonical Name: {canonical_name}"

	addresses = soup.find('td', string='addresses')
	if addresses:
	    addresses = addresses.find_next('td').find_all('span', class_='ipaddr')
	    for address in addresses:
	    	addr_string = f"{addresses}"
	    	addresses_list = list(addr_string.replace('[<span class="ipaddr">', '').replace('<br/></span>]', '').strip().split("<br/>"))

	    
	    for ip in addresses_list:
	    	if is_ipv4(ip):
	    		addresses_lookup_txt += f"\nIPv4 Address: {ip}"
	    	elif is_ipv6(ip):
	    		addresses_lookup_txt += f"\nIPv6 Address: {ip}"
	    		addresses_list.remove(ip)

	
	return addresses_list, addresses_lookup_txt

# Domain Whois Record
def domain_whois_record(soup):
	spacer = '   '
	domain_whois_txt = "\n" + "="*80
	domain_whois_txt += "\n\nDomain Whois Record\n"
	domain_whois_txt += "-"*19
	domain_whois = soup.find('h3', string='Domain Whois record')
	if domain_whois:
		domain_whois = domain_whois.find_next('pre').text.strip()
		#print("Domain Whois Record:", domain_whois)
		domain_whois = domain_whois.replace(spacer, "- ")
		domain_whois_txt += "\n" + domain_whois
		return domain_whois_txt

# Network Whois Record
def network_whois_record(soup):
	net_whois_txt = "\n" + "="*80
	net_whois_txt += "\n\nNetwork Whois Record\n"
	net_whois_txt += "-"*20
	network_whois = soup.find('h3', string='Network Whois record')
	if network_whois:
		network_whois = network_whois.find_next('pre').text.strip()
		net_whois_txt += "\n" + network_whois
		return net_whois_txt

# Service Scan
def service_scan(soup):
	scan_results = "\n" + "=" * 80
	scan_results += "\n\nService/Port Scan\n"
	scan_results += "-"*17
	service_scan_table = soup.find('h3', string='Service scan')
	if service_scan_table:
		for i in range(6):
			service_scan_table = service_scan_table.find_next('table')
			string = f"\n{'* '*40}\n{service_scan_table}"
			string = string.replace('<table border="0" cellpadding="5" cellspacing="0">\n<tr><td valign="top" width="100"><b>', "")
			string = string.replace('</b></td><td valign="top"><tt>', '\n')
			string = string.replace('</tt></td></tr></table>', '').replace("<br/>", "")
			if '<font color="gray">' in string:
				string = string.replace('<font color="gray">', '')
				string = string.replace("</font>", '')
			scan_results += string
			string = ""
		scan_results += f"\n\n{'='*80}"
		return scan_results

def generate_txt_report(html_report):
	txt_report = "\nInvestigate domains and IP addresses using CentralOps Domain Dossier."
	txt_report += "\nCheck https://centralops.net/ for more."
	soup = BeautifulSoup(html_report, 'html.parser')
	# return addresses list for use on other tools
	addresses_list, addresses_lookup_txt = address_lookup(soup)
	txt_report += "\n" + addresses_lookup_txt

	domain_whois_txt = domain_whois_record(soup)
	txt_report += "\n" + domain_whois_txt
	
	net_whois_txt = network_whois_record(soup)
	txt_report += "\n" + net_whois_txt
	
	service_scan_txt = service_scan(soup)
	txt_report += "\n" + service_scan_txt + "\n"
	return txt_report, addresses_list

def centralops_query(target, get_request):
	opts = "&dom_whois=true&dom_dns=true&traceroute=true&net_whois=true&svc_scan=true"
	cops = "https://centralops.net/co/DomainDossier.aspx?addr=" + target + opts
	c_headers = {
		'Host': 'centralops.net',
		'Cookie': 'tool-settings=DD-dd=1&DD-dw=1&DD-nw=1&DD-ss=0&DD-tr=0&dn=google.com',	
		'Sec-Ch-Ua': '"Not A(Brand";v="24", "Chromium";v="110"',
		'Sec-Ch-Ua-Mobile': '?0',
		'Sec-Ch-Ua-Platform': "Windows",
		'Upgrade-Insecure-Requests': '1',		
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		'Sec-Fetch-Site': 'none',
		'Sec-Fetch-Mode': 'navigate',
		'Sec-Fetch-User': '?1',
		'Sec-Fetch-Dest': 'document',
		'Accept-Encoding': 'gzip, deflate',
		'Accept-Language': 'en-US,en;q=0.9',
		'Connection': 'close'
	}
	#r = requests.get(cops, headers=headers)
	r = get_request(cops, headers=c_headers)
	print("wait a bit.")
	time.sleep(10)
	html_report = r.text

	if "Could not find an IP address for this domain name." in html_report:
		addresses_list = False
		txt_report = False
		return txt_report ,addresses_list
	else:
		txt_report, addresses_list = generate_txt_report(html_report)
		return txt_report ,addresses_list