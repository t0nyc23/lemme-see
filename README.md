# Lemme See

### Installing prerequisites
```
$ sudo apt install python3-bs4 python3-jinja2 python3-requests
```

### Options list
```
-u --> target URL to check
-h --> prints this help message
-o --> (optional) file name for the saved output
-t --> (optional) name for the template to use from the templates directory
-hh --> show full help message
```

### Description about the tool

Using some OSINT, the tool gathers information for a target. The results will be saved 
in .txt files and then they will be parsed to an HTML reporting template. 
In essence the .txt results will be formated inside the html the same way that someone
would copy-paste a txt file inside a cherrytree file...or something like that.
  
Currently the sources that will be used are:
1. Shodan's [internetdb API](https://internetdb.shodan.io/)
2. [CentralOps](https://centralops.net/) for IP/DNS/WHOIS lookups, and more
3. [Toolsyep](https://toolsyep.com/en/webpage-to-plain-text/) to check for a robots.txt

### Description for flags
The target URL option (-u) is required (obviuslly), and it has to be a valid domain name
with or without an HTTP scheme. Just note that if no scheme is supplied,
the script will default to HTTP://

If no output file name is supplied (-o), the script will use
a default name with a timestamp that will be saved on the current directory
  
If no template file is supplied, the script will use the default template located
in the templates directory. To use a custom template, put such template in
the respective directory, then just specify the name for the template using -t

### Usage examples:
```Bash
$ python3 lemmec.py www.example.com
$ python3 lemmec.py example.com -t /home/user/Desktop/template.thml
$ python3 lemmec.py http://www.example.com -o example-com_results.html
```

  
