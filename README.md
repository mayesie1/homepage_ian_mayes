1) build_phase1.py script (HW3, Phase1): Simple python script that performs the following:
	- Opens and reads template and content files
	- Concatenates and writes template and content files to output files that are created
	- Script contents are defined under function 'main'


2) build_phase2.py script (HW3, Phase2): Builds-from the script in HW3, Phase1
	- A list of dictionaries named 'pages' is created to represent template, content, and output files
	- A for loop is defined under function 'main' to loop through 'pages' to perform open / read / concatenation / write operations


3) build_phase3.py script (HW3, Phase3): Builds-from the script in HW3, Phase2
	- Combined template files into 'base.html'
	- Added html placeholder in 'base.html' to represent content to be added
	- Added step in for loop to replace html placeholders with data from content files


4) build_phase4.py script (HW3, Phase4): Builds-from the script in HW3, Phase3
	- Function 'main' is split-into (3) separate functions


5) build_phase5.py script (HW3, Phase5): Builds-from the script in HW3, Phase4
	- Added additional key:value pairs to 'pages' that represent titles and active link files for each webpage
	- Added html placeholders in 'base.html' to represent titles and active link to each webpage


6) build.py script: Final script; same-as build_phase5.py script (HW3, Phase5)
