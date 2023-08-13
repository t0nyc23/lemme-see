# Lemme-See quick recon using OSINT

![lemme see gif](img/lemmesee.gif)

# About Lemme-See

"Lemme-See" passively collects information for a domain name, utilizing OSINT.
The information gathered from each source, including IP addresses, open ports, subdomains, and more, 
is saved into text files and compiled into an HTML-formatted report.

### Features:
* Query Shodan's [internetdb API](https://internetdb.shodan.io/) for open ports, vulnerabilities, hostnames, and more (No API key required)
* Check [CentralOps](https://centralops.net/) for IP/DNS/WHOIS related information.
* Check [Toolsyep](https://toolsyep.com/en/webpage-to-plain-text/) for a robots.txt
* Query [Urlscan](https://urlscan.io/) API for subdomains (No API key required)
* Check [crt.sh](https://crt.sh/) for subdomains
* Query [Threat Crowd](http://ci-www.threatcrowd.org/) API for subdomains (No API key required)
* Save results in separate text files
* Generate a single-page HTML report
* Use a custom template for the HTML report

### Installing prerequisites (for Debian based systems)
```
$ sudo apt install python3-bs4 python3-jinja2 python3-requests
```

### Options list
```
-hh  -->  show full help message
-h   -->  show small help message
-u   -->  target target domain name to check
-o   -->  (optional) name for the html report
-t   -->  (optional) name for the template to use (from the templates directory)
```

### Usage examples:
```Bash
$ python3 lemmeC.py -u target.com
$ python3 lemmeC.py -u target.com -t /home/user/Desktop/template.thml
$ python3 lemmeC.py -u http://target.com -o target_results.html
```

  
