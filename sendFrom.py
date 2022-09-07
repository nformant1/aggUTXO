from rpc_connection import RPC_Connection

if __name__ == '__main__':
    # I assume the node runs local (127.0.0.1)
    # This should match your dogecoin.conf
    testnet = 1  # optional if "dogecoin-qt.texe -testnet" is used
    server = 1
    rpcuser = "YourRPCUser"
    rpcpassword = "YourRPCPassword"

    # port standard values if not defined
    # use them if you or dont assign those variables at all
    # if you are not merged mining on this node
    # rpcport = 44555
    # port = 44556
    # my non standard ports for merged mining
    rpcport = 7332
    port = 7333
    # End of dogecoin.conf

    rpc = RPC_Connection(rpcuser, rpcpassword, "127.0.0.1", rpcport)
    # Get List of UTXOs
    data = {}
    data = rpc.command("listunspent")

    # declare some vars
    txin = []
    vout = []
    # dogecoin-cli createrawtransaction "[{\"txid\":\"myid\",\"vout\":0}]" "{\"address\":0.01}"
    sendToAddress = "nformntrCCWRSRApRFJDQs2YcrMEoy49CL"
    sendAmount = 100
    sendFromAddress = "nj7nsJmY7uk5xJEmtZvBTanC8z1ohjGqcJ"
    counter = 0
    param = ""

    # verbose output (for debugging)
    verbose = 1
    curAmount = 0
    for line in data:
        if line["spendable"] is True and line["address"] != sendToAddress and line["address"] == sendFromAddress:
            curAmount = curAmount + line["amount"]
            counter = counter + 1
            comma = ""
            if counter > 1:
                comma = ","
            txin.append({"txid": line["txid"], "vout": line["vout"]})
            param = param + comma + "{\"txid\":\"" + line["txid"] + "\",\"vout\":" + str(line["vout"]) + "}"
            if curAmount > sendAmount:
                rawtx = {}
                change = (curAmount - sendAmount - 0.01)
                param = [txin, {sendToAddress: sendAmount, sendFromAddress: change}]
                rawtx = rpc.command("createrawtransaction", params=param)
                # decode to extract size data
                decodedtx = {}
                decodedtx = rpc.command("decoderawtransaction", params=[rawtx])
                print(decodedtx)
                break
