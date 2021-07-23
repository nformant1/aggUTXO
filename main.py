from rpc_connection import RPC_Connection
import math
import time

# we need math for the fee calculation
# we need time to sleep (wait for next block)
# rpc_connection wraps our calls nicely


if __name__ == '__main__':
    # I assume the node runs local (127.0.0.1)
    # This should match your dogecoin.conf
    testnet = 1 # optional if "dogecoin-qt.texe -testnet" is used
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

    # only send n transactions
    maxloops = 1

    # declare some vars
    loops = 0
    sumamount = 0
    counter = 0
    param = ""
    txin = []

    # verbose output (for debugging)
    verbose = 0

    # aggregate n (txcount) inputs into one output, sent to nformntrCCWRSRApRFJDQs2YcrMEoy49CL (aggAddress)
    txcount = 100
    aggAddress = "YOUR_DOGECOIN_ADDRESS" #"nformntrCCWRSRApRFJDQs2YcrMEoy49CL"

    for line in data:
        # each line is one UTXO
        # print (line)
        if line["address"] == aggAddress:
           # this is the address we want to aggregate to (sitting in the same wallet)
           # in that case we don't want to do anything...
           if verbose == 1:
               print ("UTXO from aggregate ("+aggAddress+") address")
        else:
            counter = counter +1

            if verbose == 1:
                print ("txid:   " + line["txid"])
                print ("vout:   " +str(line["vout"]))
                print ("amount: " + str(line["amount"]))

            # cummulate inputs to use it as one output
            sumamount = sumamount + line["amount"]

            if verbose == 1:
                print ("sumamount:" + str(sumamount))
                print ("counter:  " + str(counter))

            # comma separator only after the first tx
            comma = ""
            if counter > 1:
                comma = ","

            # create the tx
            # template
            # dogecoin-cli createrawtransaction "[{\"txid\":\"myid\",\"vout\":0}]" "{\"address\":0.01}"
            txin.append({"txid": line["txid"], "vout": line["vout"]})
            param = param + comma + "{\"txid\":\""+line["txid"]+"\",\"vout\":"+str(line["vout"])+"}"
            if verbose == 1:
                print (param)

            # amount of inputs to aggregate is satisfied
            if counter == txcount:
                # build output of the tx
                # remove tx count as fee (=5 Doges for 5 TXs)
                # just add 1 Doge fee per TX input, will be overwritten later...
                sumamountorg = sumamount
                sumamount = round(sumamount - txcount, 0)

                # create raw transaction to get size of tx
                rawtx = {}
                param = [txin, {aggAddress: sumamount}]
                rawtx = rpc.command("createrawtransaction" , params=param)
                # decode to extract size data
                decodedtx = {}
                decodedtx = rpc.command("decoderawtransaction", params=[rawtx])
                # 1 Doge per kB - if you want to handle dust you need to add 1 Doge per dust output
                fee = math.ceil(decodedtx["size"]/1000)

                # create raw transaction again with correct fee
                sumamount = round(sumamountorg - fee, 0)
                rawtx = {}
                param = [txin, {aggAddress: sumamount}]
                rawtx = rpc.command("createrawtransaction", params=param)

                # sign raw transaction
                signtx = rpc.command("signrawtransaction", params=[rawtx])
                """try:
                    print ("sign: "+signtx["hex"])
                except:
                    print ("no hex?")
                    print ("return")
                    print (signtx)
                    print ("rawtx")
                    print (rawtx)
                    print("param")
                    print(param)"""

                # not more txs then we defined erlier
                if loops < maxloops:
                    sendtx = rpc.command("sendrawtransaction", params=[signtx["hex"]])
                    print("send: " + sendtx)
                    # wait 20 sec to add a ~3 txs to a block
                    if maxloops > 1:
                        time.sleep(20)

                # reset vars and counters
                counter = 0
                param = ""
                sumamount = 0
                txin = []
                loops = loops + 1

