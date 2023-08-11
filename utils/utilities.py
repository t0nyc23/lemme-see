import os
import shutil
import jinja2
import datetime
import sys

class Checks:
	def check_http_scheme(url):
		if url.startswith("https://"):
			url = url.replace("https://", "")
		elif url.startswith("http://"):
			url = url.replace("http://", "")
		url = url.replace("/", "")
		return url

	def check_template_name(template):
		if not template:
			template = "default.html"
		elif template[-5:] != ".html":
			template += ".html"
		print(f"[+] Using {template} as a template...")
		return template

	def check_output_file_name(file_name):
		if not file_name:
			timestamp = "{:%Y-%m-%d_%H-%M}".format(datetime.datetime.now())
			file_name = f"report_{timestamp}.html"
		elif file_name[-5:] != ".html":
			file_name += ".html"
		return file_name
	
class Filesystem:
	def __init__(self, output_file, template_file):
		self.CWD = os.getcwd()
		self.TXT_REPORT_DIR = "txt_reports"
		self.HTML_TEMPLATES_DIR = "templates"
		self.HTML_TEMPLATE = template_file
		self.FINAL_REPORT_NAME = output_file

		#DEBUG print(self.HTML_TEMPLATE, self.OUTPUT_FILE);sys.exit()
		self.create_txt_report_dir()

	def create_txt_report_dir(self):
		try:
			os.mkdir(self.TXT_REPORT_DIR)
		except FileExistsError:
			self.delete_dir(self.TXT_REPORT_DIR)
			os.mkdir(self.TXT_REPORT_DIR)

	def delete_dir(self, directory):
		try:
			shutil.rmtree(directory)
		except FileNotFoundError:
			print(f"[-] Could not find {os.path.join(self.CWD, directory)}")
		except PermissionError:
			print(f"[-] Permission Error for {os.path.join(self.CWD, directory)}")
	
	# {"filename":"contents"}
	def write_txt_files(self, **kwargs):
		for filename, contents in kwargs.items():
			output_file = f"{self.TXT_REPORT_DIR}/{filename}.txt"
			with open(output_file, 'w') as file2write:
				file2write.write(contents)

	def generate_html_report(self):
		contents = {}
		environment = jinja2.Environment(loader=jinja2.FileSystemLoader(self.HTML_TEMPLATES_DIR))
		html_template = environment.get_template(self.HTML_TEMPLATE)
		txt_files = os.listdir(self.TXT_REPORT_DIR)
		for file in txt_files:
			file_path = os.path.join(self.TXT_REPORT_DIR, file)
			jinja_name = file.replace(".txt", "")
			with open(file_path) as file2read:
				txt_contents = file2read.read()
				contents[jinja_name] = txt_contents
		report = html_template.render(contents)
		with open(self.FINAL_REPORT_NAME, "w") as final_report:
			final_report.write(report)
		print(f"[+] Saved report at {os.path.join(self.CWD, self.FINAL_REPORT_NAME)}")
		self.delete_dir(self.TXT_REPORT_DIR)
