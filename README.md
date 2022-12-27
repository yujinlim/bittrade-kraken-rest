ELM Bittrade's Kraken REST package & optional CLI
====

Install
---

`pip install bittrade-kraken-rest` or `poetry add bittrade-kraken-rest`

Not all Kraken endpoints are implemented yet.

Public endpoints
------

For all public endpoints, simply use `get_<endpoint>`.

Bring Your Own ~~Credentials~~ Signature (Private endpoints)
---

TLDR; Don't pass your API secret but sign the requests yourself, with your own code. It's safer.

This library doesn't want to ever access your Kraken secret keys.

Most libraries expect you to provide your api key and secret. I'm not comfortable doing that with third-party code, even open sourced.

Here instead, the library prepares the request, which you then sign using your own code and the library finishes the job. It has NO access to your secret.

Thankfully this is quite straightforward: you need to implement a `sign(request: RequestWithResponse) -> None` method which sets the correct headers and then follow a two step process:

```python
prep: RequestWithResponse
with get_websockets_token() as prep:
    sign(prep)  # copy `sign` from readme below or implement your own method.
# Once you exit the `with` context, the response object is available.
result: GetWebsocketsTokenResult = prep.response.get_result()
```

And here is a sample code for `sign` implementation. Feel free to copy it or implement your own signature function:

```python
from os import getenv
import urllib, hmac, base64, hashlib

# Taken (with a minor change on non_null_data) from https://docs.kraken.com/rest/#section/Authentication/Headers-and-Signature
def generate_kraken_signature(urlpath, data, secret):
    non_null_data = {k: v for k, v in data.items() if v is not None}
    post_data = urllib.parse.urlencode(non_null_data)
    encoded = (str(data['nonce']) + post_data).encode()
    message = urlpath.encode() + hashlib.sha256(encoded).digest()
    mac = hmac.new(base64.b64decode(secret), message, hashlib.sha512)
    signature_digest = base64.b64encode(mac.digest())
    return signature_digest.decode()


def sign(request):
    request.headers['API-Key'] = getenv('KRAKEN_API_KEY')  # this is just one example of how to read the API key/secret; alternatives include docker secrets and config files
    request.headers['API-Sign'] = generate_kraken_signature(request.url, request.data, getenv('KRAKEN_API_SECRET'))
```


When using the CLI, simply put the above code (or your own) inside a file called `sign.py` at the root of the library (same level as `kraken.py`).


CLI
---

To use the CLI, clone/fork this repo then:

`python kraken.py <command>`

List of commands `python kraken.py --help`

Auto complete can be achieved using [Google Fire's commands](https://google.github.io/python-fire/using-cli/#-completion-generating-a-completion-script)

### Authenticated Websocket

`python kraken.py authenticated_websocket`

You will need to have set up the `sign.py` file as described 