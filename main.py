import sys
import os
from flask import Flask, render_template
import webview
import threading



if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    static_folder = os.path.join(sys._MEIPASS, 'static')
    print(template_folder)
    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)

else:
    app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

def start_server():
    app.run(host='127.0.0.1', port=5050)

if __name__ == "__main__":
    
    t = threading.Thread(target=start_server)
    t.daemon = True
    t.setDaemon(True)
    t.start()
    title = 'Flask Desktop Template'

    webview.create_window(title, url='http://127.0.0.1:5050/', html='', js_api=None, width=800, height=600,
                      x=None, y=None, resizable=True, fullscreen=False, \
                      min_size=(200, 100), hidden=False, frameless=False, \
                      minimized=False, confirm_close=False, background_color='#FFF', \
                      text_select=False)
    webview.start()
    sys.exit()
