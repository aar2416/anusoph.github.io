import cgi
import HTML
#calling form values
form = cgi.FieldStorage()

with open ('fileToWrite.txt','w') as fileOutput:
    fileOutput.write(form.getValue('name'))
    fileOutput.write(form.getValue('email'))
