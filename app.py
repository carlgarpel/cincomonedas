from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
   
   )
    return 'Aplicación para resolver un acertijo con 5 monedas. -En desarrollo.- '

if __name__ == '__main__':
    app.run()
