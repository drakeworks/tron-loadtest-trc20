import random
import time
import threading
from tronpy import Tron
from tronpy.keys import PrivateKey
from tronpy.providers import HTTPProvider

# Initialize Tron client with custom provider
tron = Tron(network="nile")  # Specifying 'nile' for the test network
tron.provider = HTTPProvider("https://nile.trongrid.io")

# List of Private Keys and Corresponding Addresses
private_keys_hex = [
    "PRIVATE_KEY_1", #Public address XXXX
    "PRIVATE_KEY_2", #Public address XXXX
    "PRIVATE_KEY_3", #Public address XXXX
    "PRIVATE_KEY_4", #Public address XXXX
]

# USDT Contract Address and List of Potential Recipients
token_address = "USDT_TOKEN_CONTRACT_ADDRESS"  # Verify this address for USDT on your testnet
recipient_addresses = [
    "ADDRESSS 1",
    "ADDRESSS 2",
    "ADDRESSS 3",
    "ADDRESSS 4",
]

# Function to send random transactions
def send_random_transactions():
    try:
        while True:
            # Select a random private key and derive the public key and address
            random_private_key_hex = random.choice(private_keys_hex)
            private_key = PrivateKey(bytes.fromhex(random_private_key_hex))
            address = private_key.public_key.to_base58check_address()

            # Generate a random USDT amount and convert it to the appropriate precision
            random_amount = random.randint(10, 100)  # Random amount in int
            amount_in_wei = int(random_amount * 10**6)  # USDT has 6 decimals

            # Choose a random recipient from the list
            recipient_address = random.choice(recipient_addresses)

            # Obtain the USDT contract and create a transfer transaction
            token_contract = tron.get_contract(token_address)
            transaction = (
                token_contract.functions.transfer(recipient_address, amount_in_wei)
                .with_owner(address)  # Owner of the transaction
                .memo("")  # Can add a memo to transaction
                .build()  # Build the transaction
            )

            # Sign and broadcast the transaction
            signed_txn = transaction.sign(private_key)  # Correct signing
            txn_response = signed_txn.broadcast()  # Broadcast to Tron network

            # Confirm the transaction on-chain
            confirmation = txn_response.wait(timeout=30, interval=2, solid=False)

            print(f"Transaction sent: {random_amount} USDT from {address} to {recipient_address} | Response: {confirmation}")

            # Random interval before the next transaction
            random_interval = random.uniform(0.001, 0.05)  # Adjusted interval in seconds
            time.sleep(random_interval)

    except Exception as e:
        print("An error occurred:", e)

# Start the function in a separate thread
thread = threading.Thread(target=send_random_transactions)
thread.start()
