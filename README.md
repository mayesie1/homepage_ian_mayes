# homepage_ian_mayes
# Run one of the following scripts to generate web pages:

1) build.sh script:
cat templates/top.html content/blog_index.html templates/bottom.html > docs/index.html
cat templates/top.html content/resume_index.html templates/bottom.html > docs/resume.html
cat templates/top.html content/about_index.html templates/bottom.html > docs/about.html

2) build.py script:
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
