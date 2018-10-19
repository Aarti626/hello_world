from flask import Flask
from flask import render_template
from flask import request
import os
from os import listdir, rename, remove
import sys

# from heapq import nlargest
# from heapq import nsmallest
app = Flask(__name__, template_folder='templates')
# app = Flask(__name__)
# global identifier


@app.route("/")
def index():
   print("Render")
   return render_template("./templates/index.html")

@app.route("/sum",methods=["GET"])
def sum():
#     num1=request.args.get("num1", "")
#     num2=request.args.get("num2", "")  
#     sum = int(num1) + int(num2)
    
# Display the sum
#     print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))

    return render_template("./templates/login.html")
    
        
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port,debug=True)
    # sentiment_anlysis()
