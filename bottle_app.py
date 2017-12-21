
#####################################################################
### Assignment skeleton
### You can alter the below code to make your own dynamic website.
### The landing page for assignment 3 should be at /
#####################################################################

from csv import reader
from bottle import *

contents = []
input_file = open("a2_input.csv", "r")
for row in reader(input_file):
	contents = contents + [row]

import bottle
from bottle import route, run, Response, default_app, debug, template, get, post, request, static_file


def htmlify(title,text):
    page = """
        <!doctype html>
        <html lang="en">
            <head>
                <meta charset="utf-8" />
                <link rel="stylesheet" href="styling.css" type="text/css">
                <title>%s</title>
            </head>
            <body class="bodyy">
            %s
            </body>
        </html>
    """ % (title,text)
    return page
    
    
@get('/<filename:re:.*\.css>')
def static_stylesheets(filename):
	return static_file(filename, root='./')
	
@get('/<filename:re:.*\.png>')
def static_image(filename):
	return static_file(filename, root='./', mimetype='image/png')


@route('/csv', 'POST')
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
	return htmlify("Internet usage percentages in countries",
                   str(content_table))


def form_of_site():
	site_form = """
				<form class="forms" action="/search" method="POST" target="_blank">
					<fieldset>
						<legend>Search menu</legend>
						Search:<br>
						<input type="text" name="country_value" value="Turkey"><br><br>
						<input type="radio" name="country_type" value="name" checked>Search by country name<br>
						<input type="radio" name="country_type" value="code">Search by country code<br><br>
						<input type="submit" value="Search"><br>
					</fieldset>
				</form>
	"""
	return site_form
	
@route('/search', 'POST')
def searching():
	country_value = request.forms.get('country_value')
	country_type = request.forms.get('country_type')
	row_data = """"""
	counter_if = 0
	if str(country_type) == "name":
		for i in range(1,52):
			if str(contents[i][0]).casefold() == str(country_value).casefold():
				counter_if = 1
				for j in range(0,7):
					row_data += '\t\t\t\t\t\t<td>'+str(contents[i][j])+'</td>\n'
				break
	
	if str(country_type) == "code":
		for i in range(1,52):
			if str(contents[i][1]).casefold() == str(country_value).casefold():
				counter_if = 1
				for j in range(0,7):
					row_data += '\t\t\t\t\t\t<td>'+str(contents[i][j])+'</td>\n'
				break
				
	if counter_if == 0:
		return htmlify("404 NOT FOUND", 
						"""
							<div>
								<h1>ERROR 404: SEARCH RESULT NOT FOUND!</h1>
								<h2>Please enter a valid value and try again.</h2>
								<h3>(The search engine is not case-sensitive.)</h3>
							</div>
						""")
	
	country_row = """
				<h2 class="search">Search results:</h2>
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
	""" % (row_data)
	return htmlify("Search results", str(country_row))

### CURRENTLY MODIFYING ###
#@route('/sort', 'POST')
#def sorting():
#	sort_type = request.forms.get('sort_type')
#	if str(sort_type) == "ascending"


#	<form class="forms" action="/sort" method="POST" target="_blank">
#					<fieldset>
#						<legend>Sort menu</legend>
#						Sort in:<br>
#						<select required>
#							<option name="sort_type" value="ascending">Ascending</option>
#							<option name="sort_type" value="descending">Descending</option>
#						</select>order<br><br>
#						<input type="submit" value="Sort">
#					</fieldset>
#				</form>
###

@route ('/')
def index():
	return htmlify("Internet usage percentages in countries", 
					"""
						<div class="header">
							<h1>Internet Usage Percentages in Countries</h1>
						</div>
					""" + 
					str(form_of_site()) + 
					"""
						<br>
						<form class="csv" action="/csv" method="POST" target="_blank">
							<input type="submit" value="Show the csv file">
						</form>
					""")



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
