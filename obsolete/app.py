
# app.py 
  
# import Template from jinja2 for passing the content 
from jinja2 import Template 
from jinja2 import Environment, BaseLoader, FileSystemLoader
import os
from csv import DictReader

here = os.path.dirname(os.path.abspath(__file__))

# Allow includes from this directory OR providing strings
template_dir = os.path.join(here, "templates")
env = Environment(loader=FileSystemLoader(template_dir))



# read table data file
with open("table_data.csv",'r') as file:
    dict_reader = DictReader(file)
    parsed_data = list(dict_reader)

# Render the template and pass the variables 
template = env.get_template("index_working.html")
rendered_form = template.render(data=parsed_data) 
  
  
# save the txt file in the form.html 
output = open('index3.html', 'w') 
output.write(rendered_form) 
output.close() 