from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<Eerste lijn>Hello, World!</Dit is mijn eerste Flask>'

if __name__ == '__main__':
    app.run()
    
 
