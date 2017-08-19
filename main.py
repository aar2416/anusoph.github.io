#!usr/bin/python
import webapp2
from google.appengine.ext import ndb
   
   
html = """ 
             <html>
            <body>
			<h1>Enter Patient details</h1>
            <form action = "/confirm" method = "POST">
	     
 Patient's Name:<input type = "text" name = "name" id="name" />
 <br>
 Disease:<textarea rows="4" cols="50" id="disease" name="disease"></textarea>
<input type = "submit"  value ="Save">
</form>
    <h1>Search Patient's Name</h1>
	        <form action="/search" method="POST">
Product:<input type="text" name="name">
<br>
<input type="submit" value="Search">
</form>
            </body>
            </html>   
 """  
   
   
class Hospital(ndb.Model):
     pname = ndb.StringProperty(indexed=True)
     pdisease = ndb.TextProperty(indexed=True)
     when = ndb.DateTimeProperty(auto_now_add=True)
	 
	 
	 
class MyHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(html)
		
		
		
		
class MainHandler(webapp2.RequestHandler):
   def post(self):
     name = self.request.get('name')
     disease = self.request.get('disease')
     patient = Hospital()
     patient.pname=name
     patient.pdisease=disease
     patient.put()
     self.response.out.write('Details entered into the datastore are')

class MainHandlers(webapp2.RequestHandler):
     def post(self):
        name = self.request.get('pname')
        patient = Hospital.query()
        searchquery = patient.filter(Hospital.pname==name)
        for i in searchquery:
            self.response.out.write('<b>The patient name is %s</b>' % i.pname)
	 
app = webapp2.WSGIApplication([('/', MyHandler),('/confirm', MainHandler),('/search', MainHandlers)], 
 debug=True)