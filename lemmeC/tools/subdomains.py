import re
import sys
import json
import requests

def search_dict(key2search, dictionary):
    if isinstance(dictionary, dict):
        for key, value in dictionary.items():
            if key == key2search:
                yield value
            elif isinstance(value, dict):
                for result in search_dict(key2search, value):
                    yield result
            elif isinstance(value, list):
                for domain in value:
                    for result in search_dict(key2search, domain):
                        yield result

def process_subdomains(domain, subdomains):
    sorted_unique = []
    for subdomain in subdomains:
        if subdomain.endswith(domain) and subdomain not in sorted_unique:   
            subdomain = re.sub(r'^[\.\*]\.?', '', subdomain)
            sorted_unique.append(subdomain.strip())

    return sorted(sorted_unique)


def get_subdomains(domain, get_request):
    subdomains = []
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1"}
    apis = {
        "urlscan": f"https://urlscan.io/api/v1/search/?q=domain:{domain}",
        "crtsh": f"https://crt.sh/?q={domain}&output=json",
        "threatc" : f'http://ci-www.threatcrowd.org/searchApi/v2/domain/report/?domain={domain}'
    }
    print(f"[+] Checking for subdomains for target: {domain}")
    for api_name, api_url in apis.items():
        api_response = json.loads(get_request(api_url, headers=headers).text)
        if api_name == "urlscan":
            subdomains += search_dict("domain", api_response)
        elif api_name == "crtsh":
            for data in api_response:
                for subdomain in data['name_value'].split('\n'):
                    subdomains.append(subdomain)
        elif api_name == "threatc":
            subdomains += api_response['subdomains']
    clean_subdomains = process_subdomains(domain, subdomains)
    return clean_subdomains
