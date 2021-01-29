import jinja2
from datetime import datetime
from subprocess import PIPE, run
import os
from shutil import copyfile

now = datetime.now()
command = ['uptime', '-p']
uptime = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True)

style_name = "./docs/style.css"
os.makedirs(os.path.dirname(style_name), exist_ok=True)
copyfile("./style.css", "./docs/style.css")

templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "template.html"
template = templateEnv.get_template(TEMPLATE_FILE)
outputText = template.render({
    "time": now.strftime("%d/%m/%Y %H:%M:%S"),
    "head": "🌱",
    "loud": "33 Db",
    "cons": "115 W",
    "hum": "23.5 %",
    "temp": "39.5 C",
    "lum": "3400 L",
    "fan_led_1": 300,
    "fan_led_2": 300,
    "fan_in": 650,
    "fan_out": 650,
})  # this is where to put args to the template renderer

# print(outputText)

filename = "docs/index.html"
os.makedirs(os.path.dirname(filename), exist_ok=True)
with open(filename, "w", encoding="utf-8") as fh:
    fh.write(outputText)
