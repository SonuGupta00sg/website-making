from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Logos',
    
  },
  {
    'id': 2,
    'title': 'Designs',
    
  },
  {
    'id': 3,
    'title': 'Drawing',
    
  },
  {
    'id': 4,
    'title': 'Emotes',
    
  }
]

@app.route("/")
def hello_jovian():
    return render_template('home.html', 
                           jobs=JOBS, 
                           company_name='The Creaphics')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)