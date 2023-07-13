from flask import Flask, request, redirect
from api import get_user_access_token, get_facebook_login_url, get_page_access_token
import config

app = Flask(__name__)

@app.route('/')
def home():
    url = get_facebook_login_url(
        config.app_id, config.redirect_uri, ''
    )
    code = config.Template.replace('/*start*/', config.home.replace(r"%url%", url))
    return code

@app.route('/fb_tokens')
def facebook_red():
    if "code" not in request.query_string.decode():
        return 'Login Failed. Please try again, Facebook!'
    app_id = config.app_id
    app_secret = config.app_secret
    redirect_uri = config.redirect_uri
    authorization_code = request.query_string.decode().split('=')[1]
    user_access_token = get_user_access_token(app_id, app_secret, redirect_uri, authorization_code)
    if config.page_id == 'YOUR_PAGE_ID':
        return config.Template.replace('/*start*/', config.login_success.replace('%val%', user_access_token))
    page_access_token = get_page_access_token(config.page_id, user_access_token)
    return config.Template.replace('/*start*/', config.login_success.replace('%val%', page_access_token))


if __name__ == '__main__':
    app.run(host='localhost', port=8888)