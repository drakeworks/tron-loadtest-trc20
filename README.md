# Tron Loadtest TRC-20
Script to automate TRC-20 token transactions on Tron testnet for system load testing purposes.

The key components of the project are:

- **Tron Network**: Uses the Tron test network (Nile) to send transactions safely
- **TRC20 Tokens**: Supports most TRC-20 tokens (including USDT), with configurable contract addresses
- **Private Keys**: Transactions are sent from randomly selected private keys
- **Recipient Addresses**: Transactions are sent to a list of predetermined recipient addresses
- **Transaction Variability**: Random amounts and intervals between transactions simulate real network activity

## Requirements

To run this project, you'll need:

- Python 3.7 or later
- The following Python packages:
  - `tronpy`
  - `random`
  - `threading`
  - `time`

Install the necessary Python packages with:

`pip install tronpy`

## Configuration

Before running, update the configuration in `main.py`:

- Set your TRC-20 token contract address
- Configure token decimals and symbol
- Add your private keys and recipient addresses
- Adjust transaction amounts and intervals as needed

## Usage

Run the script with:

`python main.py`

The script will continuously send random transactions until stopped with Ctrl+C.

## Notes

- This project is designed for the Tron test network. Using mainnet keys or sending transactions to production addresses can result in loss of funds.
- Be sure to use appropriate safety measures when handling private keys. Keep them secure and do not share them publicly.
- The random transaction sending function runs in a separate thread and can continue sending transactions until stopped manually.
