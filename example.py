from time import time
from os import urandom
from hashregate import MerkleTree

def run_tree():
	txs = [urandom(128) for i in range(4096)]
	start = time()
	mt = MerkleTree(txs)
	print(f'{mt.tree[0].hex()}\nRoot hash generated in {time() - start} seconds')

if __name__ == "__main__":
	run_tree()
