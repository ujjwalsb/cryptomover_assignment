# There is mainly 3 ways to run this program of Stellar TestNet:

## 1. Run Directly -
		a. open the Terminal.
		b. $ cd cryptomover_assignment
		c. $ pip install -r requirements.txt
		d. $ python stellar.py 	  /	  python3 stellar.py

## 2. Use my virtual environment(stellarenv) -
		a. open the Terminal.
		b. $ cd cryptomover_assignment
		c. $ source stellarenv/bin/activate
		d. (stellarenv)$ python stellar.py    /	   python3 stellar.py

## 3. Create your own virtual environment and use -
		a. open the Terminal.
		b. $ cd cryptomover_assignment
		c. $ virtualenv myenv
		d. $ source myenv/bin/activate
		e. (myenv)$ pip install -r requirements.txt
		f. (myenv)$ python stellar.py    /	   python3 stellar.py

* We can use the 'confirmation Link' in the browser for more details as needed.


# The result will be shown as:

Creating users & Generating Keys......

	Sender's Address: SB5XWVUP76DCPGQMEMNRBYA7OHE7453VUV5SDUHZU2EMWTVX42Y4AKM4
	Receiver's Address: GA3SAM5J4VHMS7RQ66NNKARTQ6Y5MKMJDRSVO4HEWXKTWGA2CNVLQEOT

------------------------------------------------------------------------------

	Checking Initial Balance......
	Initial Balance of Sender: 10000.0000000
	Initial Balance of Receiver: 10000.0000000

------------------------------------------------------------------------------

	Enter the amount to be transferred(0-9998): 7495
	0.0000100 will be charged extra for the transaction
	Transferring the ammount to the Receiver......
	Transaction completed successfully.

Confirmation Link: https://horizon-testnet.stellar.org/transactions/feea8ccbe802ceb6ecc5c7021e599f235984d1f7630666a044cd118ab17ab6b0

------------------------------------------------------------------------------

	Checking the current balance......
	Current Balance of Sender: 2504.9999900
	Current Balance of Receiver: 17495.0000000

------------------------------------------------------------------------------