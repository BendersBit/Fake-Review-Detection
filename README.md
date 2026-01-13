# Fake Review Detection

This project demonstrates a machine learning-based fake review detection system integrated with blockchain storage for secure and immutable record-keeping.

## Features

- **Dataset Generation**: Creates a synthetic dataset of product reviews with genuine/fake labels.
- **Machine Learning Model**: Uses Naive Bayes classifier to predict whether reviews are fake.
- **Blockchain Integration**: Stores review predictions on an Ethereum-compatible blockchain using a Solidity smart contract.

## Requirements

- Python 3.x
- scikit-learn
- pandas
- web3.py
- solcx
- Ganache (for local blockchain testing)

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd FakeReviewDetection
   ```

2. Install Python dependencies:
   ```
   pip install pandas scikit-learn web3 solcx
   ```

3. Ensure Ganache is running on `http://127.0.0.1:7545` with the default account unlocked.

## Usage

1. **Generate Dataset**:
   Run `generate_reviews.py` to create `reviews.csv` with sample reviews.

2. **Train Model and Predict**:
   Run `ml_model.py` to train the model and generate predictions in `reviews_with_predictions.csv`.

3. **Store on Blockchain**:
   Run `blockchain_interact.py` to deploy the contract and store predictions on the blockchain.

## Files

- `generate_reviews.py`: Generates synthetic review dataset.
- `ml_model.py`: Trains ML model and makes predictions.
- `blockchain_interact.py`: Interacts with blockchain to store reviews.
- `ReviewStorage.sol`: Solidity smart contract for review storage.
- `ReviewStorage_abi.json`: Contract ABI.
- `reviews.csv`: Generated dataset.
- `reviews_with_predictions.csv`: Dataset with predictions.

## License

MIT License