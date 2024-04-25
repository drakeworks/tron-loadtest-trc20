# Tron Loadtest USDT-TRC20
Script to automate USDT TRC-20 transactions on Tron testnet.

The key components of the project are:

- **Tron Network**: We use the Tron test network, known as "Nile," to send transactions.
- **Private Keys**: Transactions are sent from randomly selected private keys.
- **Recipient Addresses**: Transactions are sent to a list of predetermined recipient addresses.
- **Transaction Variability**: The amount and interval between transactions are random to simulate real transactions.

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

## Notes

- This project is designed for the Tron test network. Using mainnet keys or sending transactions to production addresses can result in loss of funds.
- Be sure to use appropriate safety measures when handling private keys. Keep them secure and do not share them publicly.
- The random transaction sending function runs in a separate thread and can continue sending transactions until stopped manually.
