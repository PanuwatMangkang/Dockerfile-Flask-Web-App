from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Good morning!'

@app.route('/bye')  # Corrected route to '/bye'
def bye():
    return 'Goodbye, World'  # Changed message for the '/bye' endpoint

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)






