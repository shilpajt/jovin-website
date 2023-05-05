from flask import Flask,render_template,jsonify
app = Flask(__name__)

JOBS =[
  {
    "id":1,
    "Title":"Data analyst",
    "location":"Bangalore,India",
    "salary":"Rs.4,50,000"
  },
  {
    "id":2,
    "Title":"Data Scientist",
    "location":"Delhi,India",
    "salary":"Rs.5,50,000"
  },
  {
    "id":3,
    "Title":"Frontend developer",
    "location":"Remote",
  },
  {
    "id":4,
    "Title":"Backend developer",
    "location":"San Fransisco,USA",
    "salary":"$150,000"
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html',jobs=JOBS,company_name ="JOVIAN")

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host="0.0.0.0",debug = True)
  