from subprocess import Popen
# thanks to https://github.com/holoviz-demos/clifford

def load_jupyter_server_extension(nbapp):
    Popen(["panel", "serve", "bangkok.ipynb", "--allow-websocket-origin=*"])
    #Popen(["panel", "serve", "preview1.ipynb", "--allow-websocket-origin=*"])
    #panel serve --show --port 5009 bangkok.ipynb
