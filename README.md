# Eye4AnEye

![](resized-icon.png)

## A tool for asynchronous and automated eye diagnosis

-This is a simple tool that can be used by anyone in order to
send an automated diagnosis for cataract and blood presense *(for now)* in the eye.
And can later be reviewed by an actual doctor.

### Setup
You simply have to have python 3.7.9 installed on you computer.
Additionally you have to have the packages in the requirements.txt file installed with their specified version.
To do that you can simply run the following command on your command line shell (e.g. For Windows: cmd.exe)
command: pip install -r requirements

After you have completed the setup process you can run the main.pyw file.

### Usage
Firstly click on the "Select File" button and navigate to the directory the file of the eye you want to process is in
and select it.
Make sure you have selected the correct file. You can do that by checking the full path of your file displayed just above the button.
Then you can now press the "Start" button and let python do its magic!
Wait for a couple of seconds and a new comma separated file is going to be generated with your results.
You can now use the program again without worrying about the results.csv file as it is going to append any changes.
After you are finished you can send the results.csv and image files that you have processed.

