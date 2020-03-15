# homepage_ian_mayes
# Run one of the following scripts to generate web pages:

1) build.sh script:
cat templates/blog_top.html content/blog_index.html templates/blog_bottom.html > docs/index.html
cat templates/resume_top.html content/resume_index.html templates/resume_bottom.html > docs/hw1_projects_page.html
cat templates/about_top.html content/about_index.html templates/about_bottom.html > docs/hw1_about_page.html

2) build.py script:
# Create variables to represent each file used-to form index.html
blog_top = open('./templates/blog_top.html').read()
blog_index = open('./content/blog_index.html').read()
blog_bottom = open('./templates/blog_bottom.html').read()

# Concatenate the 3 blog files together and write to index.html
open('./docs/index.html', 'w+').write(blog_top + blog_index + blog_bottom)

# Create variables to represent each file used-to form hw1_projects_page.html
resume_top = open('./templates/resume_top.html').read()
resume_index = open('./content/resume_index.html').read()
resume_bottom = open('./templates/resume_bottom.html').read()

# Concatenate the 3 resume files together and write to hw1_projects_page.html
open('./docs/hw1_projects_page.html', 'w+').write(resume_top + resume_index + resume_bottom)

# Create variables to represent each file used-to form hw1_about_page.html
about_top = open('./templates/about_top.html').read()
about_index = open('./content/about_index.html').read()
about_bottom = open('./templates/about_bottom.html').read()

# Concatenate the 3 about files together and write to hw1_about_page.html
open('./docs/hw1_about_page.html', 'w+').write(about_top + about_index + about_bottom)