import os

app_id = 'YOUR_APP_ID'
app_secret = 'YOUR_APP_SECRET'
redirect_uri = 'localhost:8888/fb_tokens'
page_id = 'YOUR_PAGE_ID'

login_success = """<div class="container">
            <h3 class="pt-5 text-center pb-4">Facebook Access Token Graph API</h3>
            <div class="input-group mb-3">
                <input type="text" style="background-color: #fff" class="form-control" id="txt" placeholder="Access Token" aria-label="Access Token" aria-describedby="button-addon2" value="%val%" disabled>
                <button id="copy" class="btn btn-secondary" type="button">Copy</button>
            </div>
            <div class="container text-center"><a class="btn btn-primary" href="/" role="button">Regenerate</a></div>
        </div>

        <script src="https://cdnjs.cloudflare.com/ajax/libs/clipboard.js/2.0.11/clipboard.min.js"></script>
        <script type="text/javascript">
        const target = document.getElementById('txt');
        const button = document.getElementById('copy');
        var clipboard = new ClipboardJS(button, {
            target: target,
            text: function() {
                return target.value;
            }
        });

        // Success action handler
        clipboard.on('success', function(e) {
            const currentLabel = button.innerHTML;

            // Exit label update when already in progress
            if(button.innerHTML === 'Copied!'){
                return;
            }

            // Update button label
            button.innerHTML = 'Copied!';

            // Revert button label after 3 seconds
            setTimeout(function(){
                button.innerHTML = currentLabel;
            }, 3000)
        });
        </script>
        """

home = r"""<div class="container text-center">
            <h2><u>Welcome To Facebook Access Token Generator</u></h2>
            <a type="button" class="btn btn-primary" href="%url%">Access Token</a>
        </div>
"""

Template = """<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Facebook Access Token</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
  </head>
  <body>
    <div class="container-lg" style="overflow: hidden">
    /*start*/
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-geWF76RCwLtnZ8qwWowPQNguL3RmwHVBC9FhGdlKrxdiJJigb/j/68SIy3Te4Bkz" crossorigin="anonymous"></script>
  </body>
</html>
"""