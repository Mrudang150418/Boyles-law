from flask import Flask, request, render_template  
  
app = Flask(__name__)  
  
@app.route("/")  
def index():  
   return render_template("index.html")  
  
@app.route("/calculate", methods=["POST"])  
def calculate():  
   p1 = float(request.form["p1"])  
   v1 = float(request.form["v1"])  
   p2 = float(request.form["p2"])  
   v2 = float(request.form["v2"])  
  
   result = boyles_law(p1, v1, p2, v2)  
   return render_template("result.html", result=result)  
  
def boyles_law(p1, v1, p2, v2):  
   return (p1 * v1) / (p2 * v2)  
  
if __name__ == "__main__":  
   app.run(debug=True)