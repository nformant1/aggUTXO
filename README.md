# aggUTXO
Add 100 outputs to one input

You must change in main.py your RPC user and password and maybe further stuff from your dogecoin.conf

Also make sure to add your address into the variable aggAddress in line 49.

No Guarantees or Warranties. Use at own risk!

# sendFrom
Collects UTXO from an address stored in sendFromAddress and creates a raw transaction, decodes it and print it to screen.

You must change in your RPC user and password and maybe further stuff from your dogecoin.conf

Also the amount and to address are in the code.

To Do:
* Create a reusable function
* Check size of TX (fee)
* Add advanced logic to choose best fitting inputs


No Guarantees or Warranties. Use at own risk!
