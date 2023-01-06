from os import getenv
import urllib, hmac, base64, hashlib
from pathlib import Path
from reactivex import operators
from bittrade_kraken_rest import get_account_balance, send


# Taken (with a minor change on non_null_data) from https://docs.kraken.com/rest/#section/Authentication/Headers-and-Signature
def generate_kraken_signature(urlpath, data, secret):
    non_null_data = {k: v for k, v in data.items() if v is not None}
    post_data = urllib.parse.urlencode(non_null_data)
    encoded = (str(data["nonce"]) + post_data).encode()
    message = urlpath.encode() + hashlib.sha256(encoded).digest()
    mac = hmac.new(base64.b64decode(secret), message, hashlib.sha512)
    signature_digest = base64.b64encode(mac.digest())
    return signature_digest.decode()


def sign(request):
    # request = original_request.copy()
    request.headers["API-Key"] = Path("./config_local/key").read_text()
    request.headers["API-Sign"] = generate_kraken_signature(
        request.url, request.data, Path("./config_local/secret").read_text()
    )
    return request.prepare()


def test_get_account_balance():
    result = (
        get_account_balance()
        .pipe(
            operators.map(sign),
            operators.flat_map(send),
        )
        .run()
    )
    assert result
