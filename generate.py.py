#
#
import sys
import json
from jinja2 import Template 
from jinja2 import Environment, BaseLoader, FileSystemLoader
import os
from csv import DictReader

if (len(sys.argv) !=3):
    print("usage: generate.py [template filename] [output_filename]")
    
    exit()
    

here = os.path.dirname(os.path.abspath(__file__))

# Allow includes from this directory OR providing strings
template_dir = os.path.join(here, "templates")
env = Environment(loader=FileSystemLoader(template_dir))

with open('table_data.json', 'r') as table_datafile:
    table_data = json.load(table_datafile)


    

# Render the template and pass the variables 
template = env.get_template(sys.argv[1])
rendered_form = template.render() 
  
  
# save the txt file in the form.html 
output = open(sys.argv[2], 'w') 
output.write(rendered_form) 
output.close() 