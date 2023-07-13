import requests
import random
import hashlib
import string

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    sha256_hash = hashlib.sha256(random_string.encode()).hexdigest()
    return sha256_hash

def manual_auth(app_id, redirect_uri, code_challenge, nonce):
    url = "https://www.facebook.com/v17.0/dialog/oauth"
    params = {
        "client_id": app_id,
        "scope":"openid",
        "response_type":"code", 
        'redirect_uri': redirect_uri, 
        "code_challenge": code_challenge,
        "code_challenge_method":"S256",
        "nonce": nonce 
    }
    url = requests.Request('GET', url, params=params).prepare().url
    return url


def get_facebook_login_url(app_id, redirect_uri, scope):
    base_url = 'https://www.facebook.com/v17.0/dialog/oauth'
    params = {
        'client_id': app_id,
        'redirect_uri': redirect_uri,
        'scope': scope
    }
    url = requests.Request('GET', base_url, params=params).prepare().url
    return url


def get_user_access_token(app_id, app_secret, redirect_uri, code):
    url = 'https://graph.facebook.com/v17.0/oauth/access_token'
    params = {
        'client_id': app_id,
        'client_secret': app_secret,
        'redirect_uri': redirect_uri,
        'code': code
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        access_token = data['access_token']
        return access_token
    else:
        print('Error exchanging code for access token:', response.json())


def get_page_access_token(page_id , user_access_token):
    url = f"https://graph.facebook.com/v17.0/{page_id}"
    params = {
        'fields': 'access_token',
        'access_token': user_access_token
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        access_token = data['access_token']
        return access_token
    else:
        print('Error exchanging code for access token:', response.json())
