from flask import Flask,request
from route import products
app=Flask(__name__)
products=[
  {
  "name":"vishal",
  "class":1
  },
  {
    "name":"basitha",
    "class":2
  }
]

@app.route("/family/<member>",methods=["POST"])
def clas(member):
  data=request.get_json()
  data["class"]=len(products)+1
  products.append(data)
  for i in products:
    if i["class"]==int(member):
      d=i
  return d
@app.route("/family",methods=["POST"])
def add():
  data=request.get_json()
  products.append(data)
  return products
@app.route("/family")
def update():
  data=request.get_json()
  for i in products:
    if i["class"]==data["class"]:
      products.remove(i)
  return products
app.run(debug=True)