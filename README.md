# aggUTXO
Add 100 outputs to one input

You must change in main.py your RPC user and password and maybe further stuff from your dogecoin.conf

Also make sure to add your address into the variable aggAddress in line 49.

No Guarantees or Warranties. Use at own risk!

# :rocket: sendFrom
Collects UTXO from an address stored in sendFromAddress using listunspent
```python
data = rpc.command("listunspent", params=[1, 9999999, [sendFromAddress] ])
```
https://github.com/nformant1/aggUTXO/blob/main/sendFrom.py#L31

creates a raw transaction
```python
data = rpc.command("listunspent", params=[1, 9999999, [sendFromAddress] ])
```
https://github.com/nformant1/aggUTXO/blob/main/sendFrom.py#L47

decodes, signes, and sends your funds:
```python
decodedtx = rpc.command("decoderawtransaction", params=[rawtx])
signrawtx = rpc.command("signrawtransaction", params=[rawtx])
sendtx = rpc.command("sendrawtransaction", params=[signrawtx["hex"]])
```
https://github.com/nformant1/aggUTXO/blob/main/sendFrom.py#L68

You must change in your RPC user and password and maybe further stuff from your dogecoin.conf

Also the amount and to addresses are in the code:
```python
sendToAddress = "nformntrCCWRSRApRFJDQs2YcrMEoy49CL"
sendAmount = 6000
sendFromAddress = "nZ3pBsb9ykUktJHqW5coo2ZkUa1WgZKK61"
```
https://github.com/nformant1/aggUTXO/blob/main/sendFrom.py#L23

This means `nZ3pBsb9ykUktJHqW5coo2ZkUa1WgZKK61` searches for UTXOs until 6000 are covered, send to `nformntrCCWRSRApRFJDQs2YcrMEoy49CL` and the change is send back to `nZ3pBsb9ykUktJHqW5coo2ZkUa1WgZKK61` (address reusage!)


The output should look like this:
```
python.exe C:/Users/nformant/PycharmProjects/pyTools/testagg.py
RAW TRANSACTION
01000000029078c26e10656e0badfcadd029a2415550fb620ee5a3a11b763fb0ced7d563f60100000000ffffffffe4bba206b6ccfc36b83341df2d51c9af2b14a2d4685a609ef5bfae1ba0f2920b0000000000ffffffff020070c9b28b0000001976a9147f69c1ea1d69a35552ea66416099a4925556f91e88ac8003346a740000001976a91435448af2ac3886f4458fa461b00282c84058ee3188ac00000000
DECODED TRANSACTION
{
    "txid": "b16c1f967397565e893c2fdf877b8c7fbb859c7f92cdbfaed1b13165402261d6",
    "hash": "b16c1f967397565e893c2fdf877b8c7fbb859c7f92cdbfaed1b13165402261d6",
    "size": 160,
    "vsize": 160,
    "version": 1,
    "locktime": 0,
    "vin": [
        {
            "txid": "f663d5d7ceb03f761ba1a3e50e62fb505541a229d0adfcad0b6e65106ec27890",
            "vout": 1,
            "scriptSig": {
                "asm": "",
                "hex": ""
            },
            "sequence": 4294967295
        },
        {
            "txid": "0b92f2a01baebff59e605a68d4a2142bafc9512ddf4133b836fcccb606a2bbe4",
            "vout": 0,
            "scriptSig": {
                "asm": "",
                "hex": ""
            },
            "sequence": 4294967295
        }
    ],
    "vout": [
        {
            "value": 6000.0,
            "n": 0,
            "scriptPubKey": {
                "asm": "OP_DUP OP_HASH160 7f69c1ea1d69a35552ea66416099a4925556f91e OP_EQUALVERIFY OP_CHECKSIG",
                "hex": "76a9147f69c1ea1d69a35552ea66416099a4925556f91e88ac",
                "reqSigs": 1,
                "type": "pubkeyhash",
                "addresses": [
                    "nformntrCCWRSRApRFJDQs2YcrMEoy49CL"
                ]
            }
        },
        {
            "value": 4999.98,
            "n": 1,
            "scriptPubKey": {
                "asm": "OP_DUP OP_HASH160 35448af2ac3886f4458fa461b00282c84058ee31 OP_EQUALVERIFY OP_CHECKSIG",
                "hex": "76a91435448af2ac3886f4458fa461b00282c84058ee3188ac",
                "reqSigs": 1,
                "type": "pubkeyhash",
                "addresses": [
                    "nZ3pBsb9ykUktJHqW5coo2ZkUa1WgZKK61"
                ]
            }
        }
    ]
}
SIGNED TRANSACTION
{
    "hex": "01000000029078c26e10656e0badfcadd029a2415550fb620ee5a3a11b763fb0ced7d563f6010000006b4830450221009a47ec77de124d9a81ed0b85bf61e2e092e738d9500c83547c907aed5d7dcf9702200e09d85e2a53353e7345bf7b6d09dc6dc0f97db0ab1f1caa98ee023b39defd12012103edbae0fc171e6c2fa681a9472a74e8f655d4ecb5d96517ba99995b7d1e1c0c62ffffffffe4bba206b6ccfc36b83341df2d51c9af2b14a2d4685a609ef5bfae1ba0f2920b00000000484730440220661d8947190ef7dca28470cf10fd7fa74641b71282dee9224ab8cfb8f7a7ea4f0220337775c275ef6fb480ed861cb9c7dedb2676046a36022d793ff75eae07bdcacc01ffffffff020070c9b28b0000001976a9147f69c1ea1d69a35552ea66416099a4925556f91e88ac8003346a740000001976a91435448af2ac3886f4458fa461b00282c84058ee3188ac00000000",
    "complete": true
}
SENT TRANSACTION
"cb2e93704e1bdd902fba4d1acfc954f7d6602573a8a841243af85fca59f52e83"

Process finished with exit code 0
```
Link to the transaction: https://chain.so/tx/DOGETEST/cb2e93704e1bdd902fba4d1acfc954f7d6602573a8a841243af85fca59f52e83

No Guarantees or Warranties. Use at own risk!
