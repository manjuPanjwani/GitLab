#ImportError
#Since you haven't written the software and don't have access to the source code, you'll need to examine the environment where the software is running and try to work out what's going on. There's a python script named infrastructure in /usr/bin directory that reads data from a CSV file and prints them to the terminal in a nicely formatted manner. Let's run this script and see whether it generates any errors.
#Now change the directory to root, and run the script.

cd /
python3 /usr/bin/infrastructure
#The script crashed, displaying an ImportError. This error is raised when an import statement has trouble importing a specific module. You could also see the module that the import statement hasn't found (i.e. matplotlib). We'll need to import this module before we continue to run the script again.
#In order to fix this error, you first need to install pip3 which is a Python package installer. This downloads and configures new python modules with single-line commands.

sudo apt install python3-pip -y
#Now, install the matplotlib python library using pip3:

pip3 install matplotlib
#Matplotlib is a plotting library for the Python programming language and its numerical mathematics extension NumPy(installed upon installing matplotlib). It provides an object-oriented API for embedding plots into applications using general-purpose GUI toolkits. Even simpler, it's a visualization library in Python for 2D plots of arrays.
#After installing the necessary modules, run the script again.

python3 /usr/bin/infrastructure
#This time it returns a NoFileError with a message that it could not find data.csv file in the working directory. Try debugging this issue.

#Let's navigate to the working directory and see if the data.csv file exists.

cd ~
ls
#As you can see, the file data has the extension .bak. As we mentioned earlier, the script infrastructure works on CSV files. Interpret the error message, which also says that it didn't find a data.csv file. We've now found the root cause of the issue. Let's move forward by renaming the file data.bak to data.csv.

mv data.bak data.csv
#navigate back to the root directory and run the script again.

cd /
python3 /usr/bin/infrastructure
#This now gives a MissingColumnError. It says that it couldn't find a column named "company" within the data.csv file.

MissingColumnError
#Let's check the data.csv file for the missing column name.

cat ~/data.csv
#So, the column name is actually missing. Let's add the column name and run the script again.

#Grant the permissions to the data.csv file.

sudo chmod 777 ~/data.csv
#Open data.csv file using nano editor.

nano ~/data.csv
#Add the missing column name and save the file by clicking Ctrl-o, followed by Enter key and Ctrl-x.

#Now, run the script again:

python3 /usr/bin/infrastructure

#This time you fixed all the errors!
