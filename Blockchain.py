
import json
import os


class Block:
    def __init__(self, mempool):
        self.TX_folder = mempool
    
    def open_TX(self):
        json_TX = os.listdir(self.TX_folder)
        # Print the contents of the directory
        for transaction_file in json_TX:
            try:
                with open(os.path.join(self.TX_folder, transaction_file), 'r') as file:
                    tx_details = json.load(file)
                    for item in tx_details['vin']:
                        print(item)
            except FileNotFoundError:
                print("Error: File not found.")


class hashblock:
    def __init__(self):
        pass


    
def main():
    # Assuming mempool directory is within the git repository
    directory = "/Users/alimansouri/Desktop/btc/rep_Clone/code-challenge-2024-eynmim/mempool"
    block_ = Block(directory)
    block_.open_TX()

if __name__ == '__main__':
    main()
