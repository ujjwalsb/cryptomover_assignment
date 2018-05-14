import time
import requests
from stellar_base.asset import Asset
from stellar_base.memo import TextMemo
from stellar_base.keypair import Keypair
from stellar_base.address import Address
from stellar_base.builder import Builder
from stellar_base.operation import Payment
from stellar_base.transaction import Transaction
from stellar_base.horizon import horizon_testnet
from stellar_base.transaction_envelope import TransactionEnvelope as Te


class stellar:
	def generate_account(self):
		kp1 = Keypair.random()
		kp2 = Keypair.random()
		self.publickey1 = kp1.address().decode()
		self.seed1 = kp1.seed().decode()
		self.publickey2 = kp2.address().decode()
		self.seed2 = kp2.seed().decode()

		print("\nCreating users & Generating Keys......")
		time.sleep(5)
		# print("Sender Public key: "+ publickey1)
		print("\nSender's Address: "+ self.seed1)
		print("Receiver's Address: "+ self.publickey2)
		# print("Receiver Private key: "+ seed2)
		print("\n------------------------------------------------------------------------------")

	def check_balance(self):
		print("\nChecking Initial Balance......")
		url = 'https://friendbot.stellar.org'
		req1 = requests.get(url, params={'addr': self.publickey1})
		req2 = requests.get(url, params={'addr': self.publickey2})
		self.address1 = Address(address = self.publickey1)
		self.address2 = Address(address = self.publickey2)
		self.address1.get()
		self.address2.get()

		# print("Initial Balance of Sender: {}".format(address1.balances[0]))
		for item in self.address1.balances:
			print("Initial Balance of Sender: "+item['balance'])
		for item in self.address2.balances:
			print("Initial Balance of Receiver: "+item['balance'])
		# print("Initial Balance of Receiver: {}".format(address2.balances[0]))
		print("\n------------------------------------------------------------------------------")

	def check_final_balance(self):
		self.address1.get()
		self.address2.get()

		# print("Current Balance of Sender: {}".format(address1.balances[0]))
		for item in self.address1.balances:
			print("Current Balance of Sender: "+item['balance'])
		for item in self.address2.balances:
			print("Current Balance of Receiver: "+item['balance'])
		# print("Current Balance of Receiver: {}".format(address2.balances[0]))
		print("\n------------------------------------------------------------------------------")


	def perform_transaction(self):
		send_seed = self.seed1
		recieve_address = self.publickey2

		amount = str(input("\nEnter the amount to be transferred(0-9998): "))
		print("0.0000100 will be charged extra for the transaction")

		send = Keypair.from_seed(send_seed)
		horizon = horizon_testnet()
		asset = Asset('XLM')

		op = Payment({
			'destination': recieve_address,
			'asset': asset,
			'amount': amount,
			})

		msg = TextMemo('Transaction Test')
		print("Transferring the ammount to the Receiver......")

		sequence = horizon.account(send.address()).get('sequence')

		tx = Transaction(
			source = send.address().decode(),
			opts = {
				'sequence': sequence,
				'memo': msg,
				'fee': 100,
				'operations': [
					op,
				],
			},
		)

		envelope = Te(tx=tx, opts={"network_id": "TESTNET"})
		envelope.sign(send)
		xdr = envelope.xdr()
		response = horizon.submit(xdr)
		print("Transaction completed successfully.\n")

		trans = response['_links']
		for values in trans.itervalues():
			for confirmation in values.itervalues():
				print("Confirmation Link: "+confirmation)
		print("\n------------------------------------------------------------------------------")
		print("\nChecking the current balance......")


result = stellar()
result.generate_account()
result.check_balance()
result.perform_transaction()
result.check_final_balance()






