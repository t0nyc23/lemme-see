import jinja2
import os


TXT_REPORT_DIR = "txt_reports_EXAMPLE"
HTML_TEMPLATE = "lemmeC_template.html"
HTML_TEMPLATES_DIR = "templates"

def generate_html_report(template):
	contents = {}
	environment = jinja2.Environment(loader=jinja2.FileSystemLoader(HTML_TEMPLATES_DIR))
	html_template = environment.get_template(template)
	txt_files = os.listdir(TXT_REPORT_DIR)
	for file in txt_files:
		file_path = os.path.join(TXT_REPORT_DIR, file)
		jinja_name = file.replace(".txt", "")
		with open(file_path) as file2read:
			txt_contents = file2read.read()
			#print(txt_contents)
			contents[jinja_name] = txt_contents
		report = html_template.render(contents)
		with open("report.html", "w") as final_report:
			final_report.write(report)

generate_html_report(HTML_TEMPLATE)