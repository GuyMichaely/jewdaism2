import os
from flask import Flask, Response, abort, request
from flask.helpers import redirect

app = Flask(__name__)

REMOTE_FILE_URL = 'https://scontent-atl3-1.xx.fbcdn.net/v/t1.6435-9/62305197_689453418177959_639826170052870144_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=a5f93a&_nc_ohc=bx07z8CxhGgQ7kNvwHewC0Z&_nc_oc=Adkrhoet9i67f_K66EHpYK4kpUYkoGl09D12WW7r1bUkQMM81RIIV7XGtVTdZfa0jAor3WFBTxrOk9FAie9LI2OI&_nc_zt=23&_nc_ht=scontent-atl3-1.xx&_nc_gid=jDXBdaGSfdO33b64B1Lgwg&oh=00_AfNNL9qMPOdMP3wixAx2rCWbjIyPsfT9ekHCw-3uj5V4UA&oe=68866E0A'
SECRET = 'guy_michaely_owns_jewdaism_k66ehpyk4kpuy'

'''@app.route(SECRET_PATH)
def proxy_file():
    return redirect(REMOTE_FILE_URL)
    r = requests.get(REMOTE_FILE_URL, stream=True)
    if r.status_code != 200:
        return '', 404
    return Response(
        r.iter_content(chunk_size=8192),
        content_type=r.headers.get('Content-Type')
    )'''

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    # abort(404)
    ref = request.referrer
    if ref and any(v in ref for v in [SECRET, 'guytest']):
        print(f'{ref=}')
        return redirect(REMOTE_FILE_URL)
    return '', 404

if __name__ == '__main__':
    print('hello world')
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000))
