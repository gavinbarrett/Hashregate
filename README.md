## Description
Hashregate is a Python implmentation of a [Merkle hash tree](https://en.wikipedia.org/wiki/Merkle_tree). Currently, the structure only work for transaction sizes in powers of two.

## Example
Here we will hash a Merkle tree containing 4096 distinct 128 byte transactions.

```bash
$ python example.py
7ff7f684dde7d59343ed918cf5f41b26318781f782b4e8e45cba844418d93653
Root hash generated in 0.019121408462524414 seconds
```
