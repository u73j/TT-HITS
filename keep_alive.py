from flask import Flask
from threading import Thread

# المتغيرات المطلوبة
hit = 0
gg = 0
bb = 0
go = 0
bm = 0

app = Flask('')

@app.route('/')
def home():
    return f'''
    <pre>
    ━━━━━━━━━━━━━━━━━━━━━━━━━
    [0] Dev : @maho_s9 | @maho9s | TikTok Free Tool
    ━━━━━━━━━━━━━━━━━━━━━━━━━
    [1] HIT  -  تم الصيد    » 「{hit}」
    ━━━━━━━━━━━━━━━━━━━━━━━━━
    [2] Available Tik - متاح   » 「{gg}」
    ━━━━━━━━━━━━━━━━━━━━━━━━━
    [3] BAD Tik - مش متاح   » 「{bb}」
    ━━━━━━━━━━━━━━━━━━━━━━━━━
    [4] Good GM - جيميل صح » 「{go}」
    ━━━━━━━━━━━━━━━━━━━━━━━━━
    [5] BAD - ايميل خاطئ   » 「{bm}」
    ━━━━━━━━━━━━━━━━━━━━━━━━━
    </pre>
    '''

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
  
