# List of dictionaries to represent each webpage
pages = [
	{
		'template_top_filename': './templates/top.html',
		'template_bottom_filename': './templates/bottom.html',
		'content_filename': './content/blog_index.html',
		'output': './docs/index.html',
		'title': 'Blog',
	},
	{
		'template_top_filename': './templates/top.html',
		'template_bottom_filename': './templates/bottom.html',
		'content_filename': './content/resume_index.html',
		'output': './docs/resume.html',
		'title': 'Resume',		
	},
	{
		'template_top_filename': './templates/top.html',
		'template_bottom_filename': './templates/bottom.html',
		'content_filename': './content/about_index.html',
		'output': './docs/about.html',
		'title': 'About Me',		
	},
]


# Function that combines .html files to form complete webpages (blog, resume, about)
def main():
	# Loop through each variable in list
	for page in pages:
		# Create variables to open and read each template file
		template_top = open(page['template_top_filename']).read()
		template_bottom = open(page['template_bottom_filename']).read()
		# Create variables to open and read each content file
		content = open(page['content_filename']).read()
		# Create variables to create output files and write template and associated content files
		final_page = open(page['output'], 'w+').write(template_top + content + template_bottom)


main()
