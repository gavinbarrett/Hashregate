from time import time
from os import urandom
from hashregate import MerkleTree

def run_tree():
	tx = urandom(64)
	txs = [tx] * 4096
	start = time()
	mt = MerkleTree(txs)
	print(f'{mt.tree[0].hex()}\nRoot hash generated in {time() - start} seconds')

if __name__ == "__main__":
	run_tree()
