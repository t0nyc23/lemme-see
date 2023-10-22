#!/usr/bin/python3
import sys
import os
import requests
import argparse

from utils.robots import get_robots
from utils.centralops import centralops_query, is_ipv4
from utils.internetdb import internetdb_query
from utils.passif import passif_scan
from utils.banner import banner, help_message, help_small
from utils.utilities import Checks, Filesystem

def lemmec(options):
	get_request			= requests.get
	target_url			= Checks.check_http_scheme(options['target_url'])
	output_name	= Checks.check_output_name(options['output_file'])
	template_file_name	= options['template_file']
	filesystem_util		= Filesystem(output_name, template_file_name)
	
	print(f"[+] Lemme see target: {target_url}")
	centralops_results_txt, centralops_addresses_list = centralops_query(target_url, get_request)
	internetdb_results_txt = internetdb_query(get_request, centralops_addresses_list)
	robots_file = get_robots(target_url, get_request)
	subdomains = passif_scan(target_url, get_request)
	
	filesystem_util.write_txt_files(robots=robots_file, centralops=centralops_results_txt, internetdb=internetdb_results_txt, subdomains=subdomains)
	filesystem_util.generate_html_report()

if __name__ == "__main__":
	parser = argparse.ArgumentParser(add_help = False)
	parser.add_argument('-u', dest='target_url', type=str, help='Target URL to check')
	parser.add_argument('-o', dest='output_file', type=str, help='Output file name', default="default")
	parser.add_argument('-t', dest='template_file', type=str, help='Template file to use')
	parser.add_argument('-h', '--help', action='store_true')
	parser.add_argument('-hh', '--help_full', action='store_true')
	args = parser.parse_args()

	if args.help_full and not args.help:
		print(help_message)
	elif not args.target_url or args.help:
		print(help_small)
	else:
		print(banner)
		lemmec(vars(args))
