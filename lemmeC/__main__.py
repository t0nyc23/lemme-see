#!/usr/bin/python3
import sys
import os
import requests
import argparse
import datetime

from lemmeC.tools.subdomains import get_subdomains 
from lemmeC.tools.network import get_addresses, internetdb
from lemmeC.utils.banner import banner
from lemmeC.utils.utilities import Checks, Filesystem

def lemmec(options):
    get_request = requests.get
    target = options["domain"] # add check for valid domain
    report_time = datetime.datetime.now()

    #lemme_see_results = {}

    print(f"[+] Lemme see target: {target}")
    lemme_see_results = {"target":target,"time": report_time.strftime("%c")}
    lemme_see_results["addresses"] = get_addresses(target)
    lemme_see_results["internetdb"] = internetdb(get_request, lemme_see_results["addresses"])
    lemme_see_results["subdomains"] = get_subdomains(target, get_request)
    lemme_see_results["subdomain_count"] = str(len(lemme_see_results["subdomains"]))

    #print(lemme_see_results)

    if options["web"]:
        return lemme_see_results
    else:
        output_name        = Checks.check_output_name(options["output"])
        template_file_name = options["template"]
        filesystem_util    = Filesystem(output_name, template_file_name)
        filesystem_util.generate_html_report(lemme_see_results)

def main():
    parser = argparse.ArgumentParser(usage="python3 lemmeC.py -u <target domain> (options)")
    parser.add_argument("-d", "--domain", type=str,
        help="Target domain name to check (e.g. -d targetdomain.site)")
    parser.add_argument("-o", "--output", type=str, default="default",
        help="Name or path to save the results (e.g. -o results_for_domain)")
    parser.add_argument("-t", "--template", type=str,
        help="User specified HTML template (e.g. -t mytemplate.html)")
    parser.add_argument("-w", "--web", action="store_true",
        help="This option tells lemme-see to just return a Python dictionary with the results and does not generate a report")
    args = parser.parse_args()

    print(banner)
    if not args.domain:
        print()
        parser.print_help()
    else:
        results = lemmec(vars(args))
if __name__ == "__main__":
    main()
