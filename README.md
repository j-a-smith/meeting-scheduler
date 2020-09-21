# meeting-scheduler
Python script for evaluating different meeting schedules based on individuals' availability. Uses formatted CSV as input and outputs report for each potential meeting schedule.

Set-up:
- Download this project as a zip file and unzip it on your computer
- Download Python here: https://www.python.org/downloads/ \
  (the latest version is fine, or anything that starts with 3 (NOT 2.something) \
  An installation wizard should pop up, go through the steps to install Python 
 
 Usage:
 - Send out a Google Form with a format like this example: https://docs.google.com/forms/d/e/1FAIpQLScoOpDdBQn5FCR2TmUAUMUhRJm7GfIUoXEXMHeaPXUsOqZ7Hg/viewform
 - Open up the responses to the Google Form in Google Sheets
 - Go to File->Download and download the responses as a CSV file. Give it a name without spaces.
 - Place the downloaded CSV file in the same folder where your unzipped meeting-scheduler folder is
 - In your meeting-scheduler folder, double click on the file "meeting-scheduler.py" \
   A command prompt window should open with the following text: \
   "Enter the name of the schedule file: "
 - Type in "../" (without the quotes), followed by the name of the CSV file you downloaded, including the ".csv" file extension (ex: "../schedules.csv" without the quotes) \
   Then press enter. The following text should appear: \
   "Enter the name for the report file: "
 - Type in the name of the file where you want the script to put your results. (ex: results.txt) WARNING: If you choose a file name that is already taken by a file in the same folder (the meeting-scheduler folder), it will overwrite that file! \
   Press enter again. The command prompt window should close.
 - In the meeting-scheduler folder, you should see a new file with the name that you chose in the previous step. Open the file with Notepad. It should contain a numbered list of options, where each option has two possible meeting times, the number of people who would not be available for either of those times, and a list of those people who are unavailable. \
   Note: the list is sorted from the least number of unavailable people to the greatest.
   
