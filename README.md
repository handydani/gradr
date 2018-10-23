# gradr

Simple program which takes in a CSV file from zylabs and uses the canvas API to make a list of students by section number with their corresponding grade.

## Instructions:

1. Install python and the packages used
2. Set up environment variables
	Canvas API requires an API Key and API Url. You can generate tokens by going to your canvas profile and clicking on settings. Scroll down to find where you can get the token. Since it's not good practice to hard code tokens you should run the following commands so that API_KEY and API_URL are os environment variables:

	```export API_URL = 'https://ufl.instructure.com'```
	```export API_KEY = 'insert_your_key_here'```
3. Sample command line argument to the program looks like the following:
	```python gradr.py /Users/dtravie/Documents/code/Python/gradr/UFLCOP3503FoxFall2018_report_2018-09-30_2359.csv```

Reminder to change the sections to whatever your sections are!

Also you might have to change the scale and the assignment title based on what you're grading
## TODO

* checking if the canvas last name doesn't match the csv
* make this a class with functions
* use Submissions object from Canvas API to be able to change grade according to what the calculated grade ended up being
* ~~fix bug where students at the end of the list are printed 2-3 times~~
