import sys
from math import floor
from hashlib import sha256

class MerkleTree:
	def __init__(self, txs):
		try:
			self.blk_size = 4
			self.txs = self.enforce_block_length(txs)
			self.tree = ([b''] * (len(self.txs) - 1)) + self.txs
			self.tree[0] = self.hash_txs(0)
			self.id_map = {sha256(tx).digest():(idx + len(self.txs) - 1) for idx, tx in enumerate(self.txs)}
		except ValueError as err:
			print(f"Error: {err}")
			sys.exit(1)
	
	def __str__(self):
		''' Print out the heap structure '''
		return '\n'.join([f'tree[{idx}]: {elem}' for idx, elem in enumerate(self.tree)])

	def get_root(self):
		''' Return the Merkle root hash of the tree '''
		return self.tree[0]

	def enforce_block_length(self, txs):
		txs_len = len(txs)
		if txs_len <= self.blk_size:
			return txs + ([b''] * (self.blk_size - txs_len))
		raise ValueError(f"Block size is {self.blk_size}")
			
	def hash_txs(self, i):
		''' Compute the root hash '''
		if i >= len(self.tree): return None
		left = self.hash_txs(2*i + 1)
		right = self.hash_txs(2*i + 2)
		if left == None and right == None:
			# hash transaction data
			return sha256(self.tree[i]).digest()
		self.tree[2*i + 1] = left
		self.tree[2*i + 2] = right
		# hash concatenated child hashes
		return sha256(left + right).digest()
	
	def find_path(self, tx_id):
		''' Verify the root node '''
		# retrieve the index of the transaction
		index = self.id_map[tx_id]
		path = [self.tree[index]]
		# iterate from the transaction to the root node
		while index > 0:
			# identify parent node
			parent = floor((index - 1) /2)
			# retrieve the parent's other child node
			if not index % 1:
				path += [self.tree[(parent * 2) + 2]]
			elif index % 1:
				path += [self.tree[(parent * 2) + 1]]
			# set the index to be the new parent
			index = parent
		# add the root node digest
		path += [self.tree[index]]
		return path
