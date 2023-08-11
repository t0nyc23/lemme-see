def format_list(list2format):
	formated_text = "  "
	coutner = 0
	if len(list2format) == 0:
		formated_text = "  Nothing here..."
		return formated_text
	elif len(str(list2format[0])) < 6:
		row_length = 5
	else:
		row_length = 3
	for list_item in list2format:
		coutner += 1
		formated_text += f"{list_item}, "
		if coutner == row_length:
			coutner = 0
			formated_text += "\n  "
	return formated_text


def internetdb_query(get_request, addresses):
	result_txt  = f"\nQuery results from Shodan's InternedDB API\n"
	for target in addresses:
		print(f"[+] Checking target addess: {target} on InternedDB.")
		url = "https://internetdb.shodan.io/" + target
		query_results = get_request(url).json()
		result_txt += f"\n{'='*42}\nInternetdb Query:\n  {url}\n"
		if "detail" in query_results:
			result_txt += f"\nValidation Error:\n  {query_results['detail']}\n"
		else:
			result_txt += f"\nTarget IP:\n  {query_results['ip']}\n"
			result_txt += f"\nTarget Ports:\n{format_list(query_results['ports'])}\n"
			result_txt += f"\nTarget Tags:\n{format_list(query_results['tags'])}\n"
			result_txt += f"\nTarget Hostnames:\n{format_list(query_results['hostnames'])}\n"
			result_txt += f"\nTarget Vulns:\n{format_list(query_results['vulns'])}\n"
			result_txt += f"\nTarget CPEs:\n{format_list(query_results['cpes'])}\n"
	return result_txt