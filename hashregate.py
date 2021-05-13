from hashlib import sha256

class MerkleTree:
	def __init__(self, txs):
		self.txs = txs
		self.tree = ([b''] * (len(txs) - 1)) + txs + ([None] * (len(txs) * 2))
		self.tree[0] = self.hash_up(0)

	def hash_up(self, i):
		''' Compute the root '''
		if self.tree[i] == None: return None
		left = self.hash_up(2*i + 1)
		right = self.hash_up(2*i + 2)
		self.tree[2*i + 1] = left
		self.tree[2*i + 2] = right
		if left == None and right == None:
			# hash transaction data
			return sha256(self.tree[i]).digest()
		# hash concatenated child hashes
		return sha256(left + right).digest()
