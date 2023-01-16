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

    sendToAddress = "nformntrCCWRSRApRFJDQs2YcrMEoy49CL"
    sendAmount = 6000
    sendFromAddress = "nZ3pBsb9ykUktJHqW5coo2ZkUa1WgZKK61"

    # Get List of UTXOs
    data = {}

    #"params": [1, 9999999, [] , true, { "minimumAmount": 5 } ]
    data = rpc.command("listunspent", params=[1, 9999999, [sendFromAddress] ])


    txin = []

    # verbose output (for debugging)
    verbose = 1
    curAmount = 0
    for line in data:
        if line["spendable"] is True:
            curAmount = curAmount + line["amount"]
            txin.append({"txid": line["txid"], "vout": line["vout"]})
            if curAmount > sendAmount:
                rawtx = {}
                change = (curAmount - sendAmount - 0.01)
                param = [txin, {sendToAddress: sendAmount, sendFromAddress: change}]
                rawtx = rpc.command("createrawtransaction", params=param)

                if verbose == 1:
                    print ("RAW TRANSACTION")
                    print (rawtx)

                # decode to extract size data
                decodedtx = {}
                decodedtx = rpc.command("decoderawtransaction", params=[rawtx])
                if verbose == 1:
                    print ("DECODED TRANSACTION")
                    print(json.dumps(decodedtx, indent=4))
                    # print(decodedtx)
                    # rather decode in the core wallet console for debugging

                signrawtx = rpc.command("signrawtransaction", params=[rawtx])
                if verbose == 1:
                    print ("SIGNED TRANSACTION")
                    print(json.dumps(signrawtx, indent=4))
                    #print(signrawtx)
                sendtx =""
                sendtx = rpc.command("sendrawtransaction", params=[signrawtx["hex"]])
                if verbose == 1:
                    print ("SENT TRANSACTION")
                    print(json.dumps(sendtx, indent=4))

                break
