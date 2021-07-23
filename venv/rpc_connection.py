import base64, json
from http.client import HTTPConnection


class RPC_Connection:
    def __init__(self, user, password, host="127.0.0.1", port=44555):
        creds = bytes(f"{user}:{password}", "ascii")
        self.auth = f"Basic {base64.b64encode(creds).decode('ascii')}"
        self.conn = HTTPConnection(host, port, 30.0)

    def command(self, method, params=None):
        obj = {
            "jsonrpc": "1.0",
            "method": method,
        }

        if params is None:
            obj["params"] = []
        else:
            obj["params"] = params

        #print ("POST "+"/ "+ str(json.dumps(obj)) )
        self.conn.request(
            "POST",
            "/",
            json.dumps(obj),
            {"Authorization": self.auth, "content-type": "application/json"},
        )

        resp = self.conn.getresponse()
        if resp is None:
            print("JSON-RPC: no response")
            return None

        body = resp.read()
        resp_obj = json.loads(body)

        if resp_obj is None:
            print("JSON-RPC: cannot JSON-decode body")
            return None

        if "error" in resp_obj and resp_obj["error"] != None:
            return resp_obj["error"]

        if "result" not in resp_obj:
            print("JSON-RPC: no result in object")
            return None

        return resp_obj["result"]
