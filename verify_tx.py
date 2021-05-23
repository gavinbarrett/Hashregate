from time import time
from os import urandom
from hashlib import sha256
from functools import reduce
from hashregate import MerkleTree

'''
def hash_tree():
	txs = [urandom(64) for i in range(4)]
	start = time()
	mt = MerkleTree(txs)
	print(f'{mt.get_root().hex()}\nRoot hash generated in {time() - start} seconds')
'''

def verify_tx(tx_id):
	''' Verify a transaction by computing its Merkle root hash '''
	path = mt.find_path(tx_id)
	# extract the root node
	exp_root = path.pop(-1)
	# check if the calculated root hash is correct
	return exp_root == reduce(lambda x, y: sha256(x + y).digest(), path)

if __name__ == "__main__":
	# create four random txs
	txs = [b' qhV\xd0\xd9H"\xc2M\x9c\xbd\x02\x1f\xc5\x0c', b'W\xc0x\xa1\x05\xc3V\x16\x8d\xa4]\xbf\xe5\xc1\x01$', b'Y\x91QK\xfc-\xe9ry\x05~7\xec\xbe\xae\xee', b'\x03\x88:\xc4\xd1jc\xe77&\xde\x89\\\x92D(']
	# instantiate a Merkle tree
	mt = MerkleTree(txs)
	# generate the transaction id for the fourth tx
	tx_id = sha256(b'\x03\x88:\xc4\xd1jc\xe77&\xde\x89\\\x92D(').digest()
	# verify the fourth tx in the tree
	verify_tx(mt)
