app_id = 'YOUR_APP_ID'
app_secret = 'YOUR_APP_SECRET'
redirect_uri = 'http://localhost:8888/fb_tokens'
page_id = 'YOUR_PAGE_ID'

with open('config.txt', 'r') as f:
    app_id, app_secret, page_id =f.read().split('\n')

login_success = """<div class="container">
            <h3 class="pt-5 text-center pb-4">Facebook Access Token Graph API</h3>
            <div class="input-group mb-3">
                <input type="text" style="background-color: #fff" class="form-control" id="txt" placeholder="Access Token" aria-label="Access Token" aria-describedby="button-addon2" value="%val%" disabled>
                <button id="copy" class="btn btn-secondary" type="button">Copy</button>
            </div>
            <div class="container text-center">
                <a class="btn btn-primary" href="/" role="button">Regenerate</a>
                <button type="button" class="btn btn-warning" id="debug">DEBUG</button>
            </div>
            <br>
                <div id="table1" style="display: none;">
                    <div style="border: 1px solid #dddfe2; margin-bottom: -1px;">
                        <h5 style="margin: 10px 0px 10px 10px;">Access Token Info</h5>
                    </div>
                    <table id="at_info" class="table table-striped table-bordered caption-top" style="margin: 0px;">
                    </table>
                </div>
                <div id="table2" style="display: none;">
                    <div style="border: 1px solid #dddfe2; margin-top: -1px; margin-bottom: -1px;">
                        <h5 style="margin: 10px 0px 10px 10px;">Granular Scopes</h5>
                    </div>
                    <table id="granular_scopes" class="table table-striped table-bordered caption-top">
                    </table>
                </div>
            </div>
        
        <script src="https://cdnjs.cloudflare.com/ajax/libs/clipboard.js/2.0.11/clipboard.min.js"></script>
        
        <script>            
            function createTable(data, id) {
            let table = document.getElementById(id);
            let tbody = document.createElement('tbody');
            for (let key in data) {
                if (data.hasOwnProperty(key)) {
                    let row = document.createElement('tr');
                    let cell1 = document.createElement('td');
                    let cell2 = document.createElement('td');
                    let span1 = document.createElement('span')
                    let span2 = document.createElement('span')
                    
                    span1.textContent = key
                    span2.textContent = data[key];

                    cell1.appendChild(span1)
                    cell2.appendChild(span2)

                    row.appendChild(cell1);
                    row.appendChild(cell2);
                    tbody.appendChild(row);
                }
            }
            //console.log(table)
            table.appendChild(tbody);
            //document.body.appendChild(table);
            }
        </script>
        <script>
            //table_maker(data, "granular_scopes", "granular_scopes" )<script>
            function table_maker(jsoData, prm, id){
                if (prm === "at_info"){
                    createTable(jsoData.at_info, id);
                    table = document.getElementById("table1")
                }else{
                    createTable(jsoData.granular_scopes, id);
                    table = document.getElementById("table2")
                }
                table.removeAttribute('style');
            }
            debug = document.getElementById("debug")
            const token = document.getElementById('txt').value
            debug.addEventListener('click', function() {
                const requestData = {
                    token: token 
                };
                
                // Send a POST request to the Flask server
                fetch('/debug', {
                    method: 'POST',
                    headers: {
                    'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(requestData)
                })
                .then(response => response.json())
                .then(data => {
                    // Handle the response from the server
                    table_maker(data, "at_info", "at_info" );
                    table_maker(data, "granular_scopes", "granular_scopes" );
                })
                .catch(error => {
                    // Handle any errors
                    console.error('Error:', error);
                });            
            });
        </script>
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
            <h5><a type="button" class="btn btn-primary" href="%url%">Access Token</a></h5>
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

def parse_debug(data):
    x = data["data"]
    granular_scopes = {}
    for itm in x["granular_scopes"]:
        granular_scopes[itm["scope"]] = ",".join(itm["target_ids"])
    return { "at_info":{
        "App ID": x['app_id']+': '+x['application'],
        "Type": x['type'].title(),
        "Page ID": x['profile_id'],
        "App-Scoped User ID": x['user_id'],
        "Issued": x['issued_at'],
        "Expires": "Never" if 0 == x['expires_at'] else x['expires_at'],
        "Data Access Expires": x['data_access_expires_at'],
        "Valid": "True" if True == x['is_valid'] else "False",
        "Scopes": ", ".join(x['scopes']),
        },
        "granular_scopes": granular_scopes
        }