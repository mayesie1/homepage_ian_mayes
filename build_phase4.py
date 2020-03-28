# List of dictionaries that represent each webpage
pages = [
	{
		'template_filename': './templates/base.html',
		'content_filename': './content/blog_index.html',
		'output': './docs/index.html',
		'title': 'Blog',
	},
	{
		'template_filename': './templates/base.html',
		'content_filename': './content/resume_index.html',
		'output': './docs/resume.html',
		'title': 'Resume',		
	},
	{
		'template_filename': './templates/base.html',
		'content_filename': './content/about_index.html',
		'output': './docs/about.html',
		'title': 'About Me',		
	},
]



# Function that opens and reads each template & content file; replaces html placeholder with content
def apply_template(page):
	# Create variables that open and read each template file
	template = open(page['template_filename']).read()
	# Create variables that open and read each content file
	content = open(page['content_filename']).read()
	# Create variables that replace html placeholder with content
	complete_page = template.replace('{{content}}', content)
	# Send data output from 'complete_page' variable back to 'write_page' function to be written to output files
	return complete_page

# Function that writes template and associated content files to form complete webpages (blog, resume, about)
def write_page(page):
	# Create variables that create output files
	output_page = open(page['output'], 'w+')
	# Create variables that call 'apply_template' function (refer-to function comments for additional info)
	complete_page = apply_template(page)
	# Write template and associated content files returned-from 'apply_template' function to form complete webpages
	output_page.write(complete_page)

# Function that starts the process of combining .html files to form complete webpages (blog, resume, about)
def main():
	# Loop through each variable in 'pages' list
	for page in pages:
		# Call 'write_page' function (refer-to function comments for additional info)
		write_page(page)


# Invokes 'main' function (refer-to function comments for additional info)
main()





