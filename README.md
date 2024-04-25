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

```bash
pip install tronpy