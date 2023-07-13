# Facebook Graph API Access Token Generator with Python Flask #

This repository contains a Python Flask application that utilizes the Facebook Graph API to generate access tokens. The access tokens are required to make authenticated requests to the Facebook Graph API and access various features and data on the Facebook platform.

## Prerequisites ##

To run this application, you need to have the following installed:

- `Python (version 3.6 or higher)`
- `Flask (version 2.0.1 or higher)`
- `Requests (version 2.26.0 or higher)`
- `Virtualenv (version 20.14.1 or higher)`

You also need to have a Facebook Developer account and an app created on the Facebook Developer platform. You will need the app ID, app secret, and other necessary credentials to authenticate and generate access tokens.

## Getting Started ##

1. Clone this repository to your local machine or download the ZIP file.

2. Install the required dependencies by running the following command in your terminal or command prompt:

```markdown
pip install -r requirements.txt
```

3. Open the config file and replace the placeholders with your Facebook app credentials:


```python
app_id = 'YOUR_APP_ID'
app_secret = 'YOUR_APP_SECRET'
```

`Note: If you want to generate "Page Access Token" give your page id in:`  

```python
page_id = 'YOUR_PAGE_ID'
```  

4. Save the changes and run the Flask application by executing the following command:

```markdown
python app.py
```

5. Open your web browser and navigate to <http://localhost:8888>. You should see the access token generator interface.

6. Enter click on the "Access Token" button. Follow the authentication flow, and upon successful authentication, you will receive an access token.

## Facebook Credentials ##

1. [APP_ID][app_id]
2. [APP_SECRET][app_secret]
3. [PAGE_ID][page_id]
4. [Access Tokens][access_tokens]

![Screenshot 1](https://github.com/Tonmoy-abc/facebook-manual-login/blob/main/img/sc1?raw=true)

![Screenshot 1](https://github.com/Tonmoy-abc/facebook-manual-login/blob/main/img/sc2?raw=true)

## Contributing ##

Contributions to this project are welcome! If you find any issues or want to add new features, feel free to open a pull request or submit an issue.

## License ##

This project is licensed under the [`MIT License`][license]. Feel free to modify and use it for your own purposes.

Repository Link: <https://github.com/Tonmoy-abc/facebook-manual-login.git>

[app_id]:https://goldplugins.com/documentation/wp-social-pro-documentation/how-to-get-an-app-id-and-secret-key-from-facebook/
[app_secret]:https://goldplugins.com/documentation/wp-social-pro-documentation/how-to-get-an-app-id-and-secret-key-from-facebook/
[access_tokens]:https://developers.facebook.com/tools/accesstoken/
[page_id]:https://www.facebook.com/business/help/2814101678867149
[license]:https://github.com/Tonmoy-abc/facebook-manual-login/blob/main/LICENSE
