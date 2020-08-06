# Copyright (C) 2020 TANMAY PRABHAKAR THAG. All Rights Reserved.


from flask import Flask, render_template , request

app = Flask(__name__)


# This is the route to main ask  questions section 
# It renders the applicaion interface.
@app.route("/")
def input():
	return render_template("input.html")
    
    
 #this rout respond to sucessful submit of questions 
@app.route("/done", methods=["POST"])
def done():
    return render_template("done.html")


#this route is meant to store the input data
@app.route("/teacher", methods=["GET"])
def teacher():
    question = request.form.get("question")
    image = request.form.get("image")
    return render_template("teacher.html", question=question , image=image)
    

  

    
if __name__ == '__main__':
      
    app.run(debug=True)