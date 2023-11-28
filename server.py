from flask import Flask
from app import app

if __name__ == '__main__':
    app.run(debug=True,host='192.168.0.113',port=5000)