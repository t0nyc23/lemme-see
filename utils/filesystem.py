import os
import shutil
import jinja2
import datetime

CWD = os.getcwd()
TXT_REPORT_DIR = "txt_reports"
TXT_REPORT_DIR = "txt_reports"
HTML_TEMPLATE = "default.html"
HTML_TEMPLATES_DIR = "templates"

def generate_html_report(template, final_report_name):
	contents = {}
	if not template:
		template = HTML_TEMPLATE
	elif template[-5:] != ".html":
		template += ".html"
	if not final_report_name:
		timestamp = "{:%Y-%m-%d_%H-%M}".format(datetime.datetime.now())
		final_report_name = f"report_{timestamp}.html"
	elif final_report_name[-5:] != ".html":
		final_report_name += ".html"
	print(f"[+] Using {os.path.join(HTML_TEMPLATES_DIR, template)} as a template...")
	environment = jinja2.Environment(loader=jinja2.FileSystemLoader(HTML_TEMPLATES_DIR))
	html_template = environment.get_template(template)
	txt_files = os.listdir(TXT_REPORT_DIR)
	for file in txt_files:
		file_path = os.path.join(TXT_REPORT_DIR, file)
		jinja_name = file.replace(".txt", "")
		with open(file_path) as file2read:
			txt_contents = file2read.read()
			contents[jinja_name] = txt_contents
	report = html_template.render(contents)
	with open(final_report_name, "w") as final_report:
		final_report.write(report)
	print(f"[+] Saved report at {os.path.join(CWD, final_report_name)}")

def delete_dir(directory):
	try:
		shutil.rmtree(directory)
	except FileNotFoundError:
		print(f"[-] Could not find {os.path.join(CWD, directory)}")
	except PermissionError:
		print(f"[-] Permission Error for {os.path.join(CWD, directory)}")

def create_txt_report_dir():
	try:
		os.mkdir(TXT_REPORT_DIR)
	except FileExistsError:
		delete_dir(TXT_REPORT_DIR)
		create_txt_report_dir()

# {"filename":"contents"}
def write_txt_files(**kwargs):
	for filename, contents in kwargs.items():
		output_file = f"{TXT_REPORT_DIR}/{filename}.txt"
		with open(output_file, 'w') as file2write:
			file2write.write(contents)