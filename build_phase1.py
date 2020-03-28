# Function that combines .html files to form complete webpages (blog, resume, about)
def main():
	# Create variables to represent each template file
	top = open('./templates/top.html').read()
	bottom = open('./templates/bottom.html').read()

	# Create variables to represent each file used-to form index.html
	blog_index = open('./content/blog_index.html').read()

	# Concatenate the 3 blog files together and write to index.html
	open('./docs/index.html', 'w+').write(top + blog_index + bottom)

	# Create variable to represent each file used-to form resume.html
	resume_index = open('./content/resume_index.html').read()

	# Concatenate the 3 resume files together and write to resume.html
	open('./docs/resume.html', 'w+').write(top + resume_index + bottom)

	# Create variables to represent each file used-to form about.html
	about_index = open('./content/about_index.html').read()

	# Concatenate the 3 about files together and write to about.html
	open('./docs/about.html', 'w+').write(top + about_index + bottom)

main()