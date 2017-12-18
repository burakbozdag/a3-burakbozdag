
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
				<form action="/search" method="POST">
					<fieldset>
						<legend>Search menu:</legend>
						Search by country name:<br>
						<input type="text" name="country_name" value=""><br><br>
						or<br><br>
						Search by country code:<br>
						<input type="text" name="country_code" value=""><br><br>
						<input type="submit" value="Search"><br>
					</fieldset>
				</form>
	"""
	return site_form
	
@route('/search', 'POST')
def searching():
	country_name = request.forms.get('country_name')
	country_code = request.forms.get('country_code')
	row_data = """"""
	if str(country_name) != "":
		for i in range(1,52):
			if str(contents[i][0]).casefold() == str(country_name).casefold():
				for j in range(0,7):
					row_data += '\t\t\t\t\t\t<td>'+str(contents[i][j])+'</td>\n'
				break
	
	if str(country_code) != "":
		for i in range(1,52):
			if str(contents[i][1]).casefold() == str(country_code).casefold():
				for j in range(0,7):
					row_data += '\t\t\t\t\t\t<td>'+str(contents[i][j])+'</td>\n'
				break
	
	country_row = """
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
	return htmlify("Search result", str(country_row))


@route ('/')
def index():
	return htmlify("Internet usage percentages in countries", 
					str(form_of_site()) + 
					"""
						<br>
						<form action="/csv" method="POST" target="_blank">
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
