from hashregate import MerkleTree

def run_tree():
	txs = [b'hello', b'there', b'you', b'king', b'no', b'bueno', b'tango', b'vial']
	mt = MerkleTree(txs)
	print(mt.tree[0].hex())

if __name__ == "__main__":
	run_tree()
