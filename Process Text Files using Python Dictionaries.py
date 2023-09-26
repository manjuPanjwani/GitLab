#Web server corpweb
#Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. A Web framework is a set of components that provide a standard way to develop websites quickly and easily.
#For this lab, a Django web server corpweb is already configured under /projects/corpweb directory. You can check it out by visiting the external IP address of the corpweb VM. The external IP address can be found in the connection details panel. Enter the corpweb external IP address in a new separate browser tab.
#Append /feedback to the external IP address of corpweb VM opened in the browser tab.
#This is a web interface for a REST end-point. Through this end-point, you can enter feedback that can be displayed on the company's website. You can use this end-point in the example below. Start by copying and pasting the following JSON to the Content field on the website, and click POST.
#{"title": "Experienced salespeople", "name": "Alex H.", "date": "2020-02-02", "feedback": "It was great to talk to the salespeople in the team, they understood my needs and were able to guide me in the right direction"}
#The whole website is stored in /projects/corpweb. You're free to look around the configuration files. Also, there's no need to make any changes to the website; all interaction should be done through the REST end-point.
#Process text files and upload to running web server
#Navigate to /data/feedback directory, where you'll find a few .txt files with customer reviews for the company.

cd /data/feedback
ls
Copied!
cat 007.txt
#They're all written in the same format (i.e. title, name, date, and feedback).
cd ~
nano run.py

#Grant executable permission to the run.py script.

chmod +x ~/run.py
./run.py
