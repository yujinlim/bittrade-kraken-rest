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

Thankfully this is quite straightforward: you need to implement a `sign(request: PreparedRequest) -> None` method which sets the correct headers and then follow a two step process:

```python
request: PreparedRequest = get_websockets_token()
sign(request)
result = get_result(request)
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


CLI
---

The CLI has been moved to [its own repo](https://github.com/TechSpaceAsia/bittrade-kraken-cli)
