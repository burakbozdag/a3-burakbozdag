
#####################################################################
### Assignment skeleton
### You can alter the below code to make your own dynamic website.
### The landing page for assignment 3 should be at /
#####################################################################

from csv import reader

contents = []
input_file = open("a2_input.csv", "r")
for row in reader(input_file):
	contents = contents + [row]

import bottle
from bottle import route, run, Response, default_app, debug, template, get, post, request

def htmlify(title,text):
    page = """
        <!doctype html>
        <html lang="en">
            <head>
                <meta charset="utf-8" />
                <title>%s</title>
            </head>
            <body>
            %s
            </body>
        </html>
    """ % (title,text)
    return page
    
def contents_file():
	data = """"""
	for i in range(1,52):
		data += """\t\t\t\t\t<tr>\n"""
		for j in range(0,7):
			data += '\t\t\t\t\t\t<td>'+str(contents[i][j])+'</td>\n'
		data += """\t\t\t\t\t</tr>\n"""
	
	content_table = """
				<table>
					<tr>
						<th>Country Name</th>
						<th>Country Code</th>
						<th>2012</th>
						<th>2013</th>
						<th>2014</th>
						<th>2015</th>
						<th>2016</th>
					</tr>
%s
				</table>
	""" % (data)
	return content_table

def index():
    return htmlify("Internet usage percentages in countries",
                   str(contents_file()))

route('/', 'GET', index)


#####################################################################
### Don't alter the below code.
### It allows this website to be hosted on Heroku
### OR run on your computer.
#####################################################################

# This line makes bottle give nicer error messages
debug(True)
# This line is necessary for running on Heroku
app = default_app()
# The below code is necessary for running this bottle app standalone on your computer.
if __name__ == "__main__":
	run()
