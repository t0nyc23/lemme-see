import os
import sys
import shutil
import jinja2
import datetime

class Checks:
	def check_http_scheme(url):
		if url.startswith("https://"):
			url = url.replace("https://", "")
		elif url.startswith("http://"):
			url = url.replace("http://", "")
		url = url.replace("/", "")
		return url

	def check_template_name(templates_dir, template):
		msg = f"[+] Using {template} as a template..."
		if not template:
			template = "default.html"
		elif template[-5:] != ".html":
			template += ".html"
			if not os.path.isfile(os.path.join(templates_dir, template)):
				msg = f"[Warnning] Could not find template: {template}, using default template instead..."
				template = "default.html"
		print(msg)
		return template

	def check_output_name(dir_name):
		if dir_name == "default" or os.path.isdir(dir_name):
			#------MONTH-DAY-YEAR_HOUR:MINUTE:SECOND
			timestamp = "{:%m-%d-%Y_%H:%M:%S}".format(datetime.datetime.now())
			dir_name = f"lemme-see_report_{timestamp}"
			dir_name = os.path.join(os.path.expanduser("~"), dir_name)
		return dir_name
	
class Filesystem:
	def __init__(self, output_dir, template_file):
		self.STARTING_DIR          = os.getcwd()
		self.REPORT_DIR            = os.path.join(self.STARTING_DIR, output_dir)
		self.REPORT_DIR_TXT        = f"{self.REPORT_DIR}/txt"
		os.chdir(os.path.dirname(__file__))
		self.TOOL_HOME             = os.path.abspath(os.pardir)
		self.HTML_TEMPLATES_DIR    = os.path.abspath(os.path.join(os.pardir, "templates"))
		self.HTML_TEMPLATE         = template_file
		self.FINAL_REPORT_NAME     = f"{output_dir}.html"
		self.create_report_dir()

	def create_report_dir(self):
		os.mkdir(self.REPORT_DIR)
		os.mkdir(self.REPORT_DIR_TXT)

	def delete_dir(self, directory):
		try:
			shutil.rmtree(directory)
		except FileNotFoundError:
			print(f"[-] Could not find {directory}")
		except PermissionError:
			print(f"[-] Permission Error for {directory}")

	def write_txt_files(self, **kwargs):
		for filename, contents in kwargs.items():
			output_file = f"{self.REPORT_DIR_TXT}/{filename}.txt"
			with open(output_file, 'w') as file2write:
				file2write.write(contents)

	def write_report_file(self):
		file2write = f"{self.REPORT_DIR}/lemme-see_report.html"
		msg = f"[+] Saving to {file2write}"
		print(msg)
		try:
			with open(file2write, "w") as final_report:
				final_report.write(self.report)
		except FileNotFoundError:
			print(f"[Warnning] Could not write to: {self.FINAL_REPORT_NAME}")
			default_name = Checks.check_output_name("default")
			msg = f"[+] Saving to {default_name} instead..."
			self.write_report_file(default_name)

	def generate_html_report(self):
		contents = {}
		environment = jinja2.Environment(loader=jinja2.FileSystemLoader(self.HTML_TEMPLATES_DIR))
		html_template_check = Checks.check_template_name(self.HTML_TEMPLATES_DIR, self.HTML_TEMPLATE)
		html_template = environment.get_template(html_template_check)
		txt_files = os.listdir(self.REPORT_DIR_TXT)
		for file in txt_files:
			file_path = os.path.join(self.REPORT_DIR_TXT, file)
			jinja_name = file.replace(".txt", "")
			with open(file_path) as file2read:
				txt_contents = file2read.read()
				contents[jinja_name] = txt_contents
		self.report = html_template.render(contents)
		os.chdir(self.STARTING_DIR)
		self.write_report_file()
