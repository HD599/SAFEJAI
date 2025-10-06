from flask import Flask, render_template, redirect, url_for, session
from authlib.integrations.flask_client import OAuth
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "safejai-secret")
oauth = OAuth(app)

# Facebook OAuth
oauth.register(
    name='facebook',
    client_id=os.environ.get("FACEBOOK_CLIENT_ID"),
    client_secret=os.environ.get("FACEBOOK_CLIENT_SECRET"),
    access_token_url='https://graph.facebook.com/v10.0/oauth/access_token',
    authorize_url='https://www.facebook.com/v10.0/dialog/oauth',
    api_base_url='https://graph.facebook.com/',
    client_kwargs={'scope': 'email'}
)

# LINE OAuth
oauth.register(
    name='line',
    client_id=os.environ.get("LINE_CLIENT_ID"),
    client_secret=os.environ.get("LINE_CLIENT_SECRET"),
    access_token_url='https://api.line.me/oauth2/v2.1/token',
    authorize_url='https://access.line.me/oauth2/v2.1/authorize',
    api_base_url='https://api.line.me/v2/profile',
    client_kwargs={'scope': 'profile openid email'}
)

@app.route('/')
def index():
    user = session.get('user')
    return render_template('index.html', user=user)

@app.route('/auth/facebook')
def login_facebook():
    redirect_uri = url_for('facebook_callback', _external=True)
    return oauth.facebook.authorize_redirect(redirect_uri)

@app.route('/auth/facebook/callback')
def facebook_callback():
    token = oauth.facebook.authorize_access_token()
    resp = oauth.facebook.get('me?fields=id,name,email')
    session['user'] = resp.json()
    return redirect('/')

@app.route('/auth/line')
def login_line():
    redirect_uri = url_for('line_callback', _external=True)
    return oauth.line.authorize_redirect(redirect_uri)

@app.route('/auth/line/callback')
def line_callback():
    token = oauth.line.authorize_access_token()
    resp = oauth.line.get('profile')
    session['user'] = resp.json()
    return redirect('/')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
