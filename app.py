import os
from flask import Flask

app = Flask('hello-app')

@app.route('/')
def hello():
  return f"Hello from {os.getenv('MY_NODE_NAME')}!\n"

if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 8080)
