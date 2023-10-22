import os

bannereye = """=============================================================
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠛⢉⣉⣠⣤⣤⣤⣤⣤⣭⣉⡙⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢛⣁⣤⣴⣾⣿⡿⠿⠿⠟⠛⠛⠛⠻⠿⠿⢿⣿⣶⣬⣙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣋⣤⣾⣿⠿⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠈⠉⠛⠻⢿⣶⣬⣝⡛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣋⣴⣿⡿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠿⠛⠓⣦⣄⠀⠀⠀⠈⠙⠻⣿⣷⣬⣙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⣡⣾⡿⠛⢁⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⢸⣿⣷⢠⡀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡿⠿⣛⣫⣤⡾⠟⠉⣀⣼⣿⣿⠀⠀⣄⣀⣇⢰⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⢸⣷⡄⠀⣶⣤⣤⣀⡀⠈⠛⢿⣭⣙⢿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⢀⣤⣾⣿⣿⣿⣿⡄⠀⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⡿⣸⣿⠇⢰⣿⣿⣿⣿⣿⣷⣦⠄⣹⣿⣧⢹⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡿⠿⠋⢩⣴⣾⣿⣿⣿⣿⣿⣿⣿⣷⡀⠹⣿⣿⣿⣿⣿⣿⣦⣀⡀⠀⠀⠀⢀⣠⣾⣿⣿⣿⣳⣿⠏⢠⣿⣿⣿⣿⣿⣿⡿⢋⣼⣿⣿⠏⣸⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡏⠀⠾⢧⡀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠘⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⣰⣿⣿⣿⣿⣿⡿⢋⣤⣮⣿⠟⣣⣾⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣶⣶⣶⣦⣤⣄⡙⠛⢿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡈⠙⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⣠⣾⣿⣿⣿⡿⠟⢁⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⢿⣷⣆⡈⠙⠿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣄⣀⣉⠉⠛⠛⠛⠛⠉⣁⣠⣴⣿⣿⣿⣿⠿⠋⢀⣼⣿⠿⢛⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣦⣍⠻⢷⣦⡝⠻⢶⣄⡀⠈⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⣠⣾⠟⢋⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡙⣿⣿⣦⡙⠿⣦⣄⡀⠈⠉⠛⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠁⢀⣤⡾⠟⣡⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣮⡻⣿⣿⣷⣌⠛⠿⣷⣶⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣶⡶⠛⢉⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣉⠙⠛⠻⠿⠿⣿⣿⠿⠿⠿⠿⠿⠛⠛⣁⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣤⣤⣤⣤⣤⣤⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿"""

banner = """
=============================================================
~ -------- Lemme-See || version: 1.0.0 || by @n0n --------- ~
============================================================="""

# Remove the eye ascii art for windows, cause it's not printed correctly
if not os.name == "nt":
    banner = bannereye + banner


help_small = banner + """
Options list:
  -hh -->  show full help message
  -h  -->  show small help message
  -u  -->  target domain name to check
  -o  -->  (optional) name for the html report
  -t  -->  (optional) name for the template to use (from the templates directory)
"""

help_message = help_small + """
About Lemme-See:
  Lemme-See passively collects information for a domain name, utilizing 
  OSINT. The information gathered from each source, including
  IP addresses, open ports, subdomains, and more, is saved into text files
  and compiled into an HTML-formatted report.
  
Features:
  - Query https://internetdb.shodan.io/ for ports, vulnerabilities, and more (No API key required)
  - Check https://centralops.net/ for IP/DNS/WHOIS related information.
  - Check https://toolsyep.com/en/webpage-to-plain-text/ for a robots.txt
  - Query https://urlscan.io/ API for subdomains (No API key required)
  - Check https://crt.sh/ for subdomains
  - Query http://ci-www.threatcrowd.org/ API for subdomains (No API key required)
  - Save results in separate text files
  - Generate a single-page HTML report
  - Use a custom template for the HTML report

Description for flags:
  - The target URL option (-u) is required (obviuslly), and it has to be a valid domain name
    with or without an HTTP scheme. Just note that if no scheme is supplied,
    the script will default to HTTP://

  - If no output file name is supplied (-o), the script will use
    a default name with a timestamp that will be saved on the current directory
  
  - If no template file is supplied, the script will use the default template located
    in the templates directory. To use a custom template, put such template in
    the respective directory, then just specify the name for the template using -t
"""

examples = """
Usage examples:
  $ python3 lemmeC.py -u example.com
  $ python3 lemmeC.py -u example.com -t /home/user/Desktop/template.thml
  $ python3 lemmeC.py -u http://example.com -o example_results.html
"""

help_small += examples
help_message += examples