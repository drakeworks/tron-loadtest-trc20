import random
import time
import threading
from tronpy import Tron
from tronpy.keys import PrivateKey
from tronpy.providers import HTTPProvider

# Token Configuration
TOKEN_CONFIG = {
    "contract_address": "TOKEN_CONTRACT_ADDRESS",  # Replace with your TRC20 token contract address
    "decimals": 6,  # Number of decimal places (USDT=6, most others=18)
    "symbol": "TOKEN",  # Token symbol for logging (e.g., "USDT", "TRX", "BTT")
    "min_amount": 10,  # Minimum transaction amount in token units
    "max_amount": 100,  # Maximum transaction amount in token units
}

# Network Configuration
NETWORK_CONFIG = {
    "network": "nile",  # "nile" for testnet, "mainnet" for mainnet DON'T USE MAINNET
    "provider_url": "https://nile.trongrid.io",  # Testnet URL, SERIOUSLY DON'T USE MAINNET UNLESS YOU KNOW WHAT YOU ARE DOING
}

# Transaction Configuration
TX_CONFIG = {
    "min_interval": 0.001,  # Minimum seconds between transactions
    "max_interval": 0.05,   # Maximum seconds between transactions
    "timeout": 30,          # Transaction confirmation timeout
    "confirmation_interval": 2,  # Seconds between confirmation checks
}

# List of Private Keys and Corresponding Addresses
private_keys_hex = [
    "PRIVATE_KEY_1", #Public address XXXX
    "PRIVATE_KEY_2", #Public address XXXX
    "PRIVATE_KEY_3", #Public address XXXX
    "PRIVATE_KEY_4", #Public address XXXX
]

# List of Potential Recipients
recipient_addresses = [
    "ADDRESSS 1",
    "ADDRESSS 2",
    "ADDRESSS 3",
    "ADDRESSS 4",
]

# Initialize Tron client with custom provider
tron = Tron(network=NETWORK_CONFIG["network"])
tron.provider = HTTPProvider(NETWORK_CONFIG["provider_url"])

def validate_token_contract():
    """Validate that the contract address is a valid TRC20 token"""
    try:
        contract = tron.get_contract(TOKEN_CONFIG["contract_address"])
        
        # Check if the contract has the standard TRC20 transfer function
        if hasattr(contract.functions, 'transfer'):
            print(f"Valid TRC20 token contract found: {TOKEN_CONFIG['symbol']}")
            return True
        else:
            print(f"Contract does not have transfer function. Not a valid TRC20 token.")
            return False
    except Exception as e:
        print(f"Error validating token contract: {e}")
        return False

def send_random_transactions():
    """Send random TRC20 token transactions"""
    try:
        # Validate token contract first
        if not validate_token_contract():
            print("Token validation failed. Please check your contract address.")
            return

        # Get token contract
        token_contract = tron.get_contract(TOKEN_CONFIG["contract_address"])
        
        print(f"Starting {TOKEN_CONFIG['symbol']} load test...")
        print(f"Token: {TOKEN_CONFIG['symbol']}")
        print(f"Decimals: {TOKEN_CONFIG['decimals']}")
        print(f"Amount range: {TOKEN_CONFIG['min_amount']} - {TOKEN_CONFIG['max_amount']} {TOKEN_CONFIG['symbol']}")
        print(f"Network: {NETWORK_CONFIG['network']}")
        print("-" * 50)

        while True:
            # Select a random private key and derive the public key and address
            random_private_key_hex = random.choice(private_keys_hex)
            private_key = PrivateKey(bytes.fromhex(random_private_key_hex))
            address = private_key.public_key.to_base58check_address()

            # Generate a random token amount and convert it to the appropriate precision
            random_amount = random.randint(TOKEN_CONFIG["min_amount"], TOKEN_CONFIG["max_amount"])
            amount_in_wei = int(random_amount * (10 ** TOKEN_CONFIG["decimals"]))

            # Choose a random recipient from the list
            recipient_address = random.choice(recipient_addresses)

            # Create a transfer transaction
            transaction = (
                token_contract.functions.transfer(recipient_address, amount_in_wei)
                .with_owner(address)
                .memo("")
                .build()
            )

            # Sign and broadcast the transaction
            signed_txn = transaction.sign(private_key)
            txn_response = signed_txn.broadcast()

            # Confirm the transaction on-chain
            confirmation = txn_response.wait(
                timeout=TX_CONFIG["timeout"], 
                interval=TX_CONFIG["confirmation_interval"], 
                solid=False
            )

            print(f"✓ Transaction sent: {random_amount} {TOKEN_CONFIG['symbol']} from {address[:8]}... to {recipient_address[:8]}... | Response: {confirmation}")

            # Random interval before the next transaction
            random_interval = random.uniform(TX_CONFIG["min_interval"], TX_CONFIG["max_interval"])
            time.sleep(random_interval)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("TRC20 Token Load Test Script")
    print("=" * 50)
    print(f"Token: {TOKEN_CONFIG['symbol']}")
    print(f"Contract: {TOKEN_CONFIG['contract_address']}")
    print(f"Network: {NETWORK_CONFIG['network']}")
    print("=" * 50)
    
    # Start the function in a separate thread
    thread = threading.Thread(target=send_random_transactions)
    thread.start()
    
    try:
        # Keep the main thread alive
        thread.join()
    except KeyboardInterrupt:
        print("\nLoad test stopped by user.")
