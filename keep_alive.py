from flask import Flask
from threading import Thread

# المتغيرات المطلوبة
hit = 0

app = Flask('')

@app.route('/')
def home():
    return f'''
    <h1>Hit Count</h1>
    <p>Number of Hits: {hit}</p>
    '''

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
