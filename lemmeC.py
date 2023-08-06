#!/usr/bin/python3
import sys
import requests
import argparse

from termcolor import colored
from utils.robots import get_robots
from utils.centralops import centralops_query, is_ipv4
from utils.internetdb import internetdb_query
from utils.checks import check_http_scheme, check_host_alive
from utils.banner import banner, help_message, help_small
from utils.filesystem import create_txt_report_dir, delete_dir, write_txt_files, generate_html_report

def lemmec(options):
	get_request   = requests.get
	target        = options["target_url"]
	output_file   = options["output_file"]
	template_file = options["template_file"]
	create_txt_report_dir()
	print(f"[+] Doing checks for supplied target: {target}")
	target_url = check_http_scheme(target)
	print(f"[+] Checking target on CentralOps...", end="")
	centralops_results_txt, centralops_addresses_list = centralops_query(target_url, get_request)
	if not centralops_results_txt:
		print(f"[-] There was a problem with: {target_url} while using CentralOps. Exiting...")
		sys.exit(-1)
	internetdb_results_txt = internetdb_query(get_request, centralops_addresses_list)
	robots_file = get_robots(target_url, get_request)
	write_txt_files(robots=robots_file, centralops=centralops_results_txt, internetdb=internetdb_results_txt)
	generate_html_report(template_file, output_file)
	delete_dir("txt_reports")

if __name__ == "__main__":
	parser = argparse.ArgumentParser(add_help = False)
	parser.add_argument('-u', dest='target_url', type=str, help='Target URL to check')
	parser.add_argument('-o', dest='output_file', type=str, help='Output file name')
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