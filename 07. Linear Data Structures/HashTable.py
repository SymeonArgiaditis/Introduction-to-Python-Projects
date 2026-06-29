from collections import defaultdict

class HashTable:
    def __init__(self):
        self.collection = defaultdict(dict)

    def hash(self, hash_key: str) -> int:
        hashed_value = 0
        for s in hash_key:
            hashed_value += ord(s)

        return hashed_value
    
    def add(self, hash_key: str, hash_value) -> None:
        computed_hash_value: int = self.hash(hash_key)

        #If the computed hash value doesn't exist, defaultdict creates {}
        self.collection[computed_hash_value][hash_key] = hash_value

    def remove(self, hash_key: str) -> None:
        computed_hash_value: int = self.hash(hash_key)

        if (computed_hash_value in self.collection) and (hash_key in self.collection[computed_hash_value]):
            del self.collection[computed_hash_value][hash_key]
            print(f"Deleted key-value pair at key [{computed_hash_value}]")

        #If the nested dict is now empty remove the hash bucket entirely.
        if not self.collection[computed_hash_value]:
            del self.collection[computed_hash_value]

    def lookup(self, hash_key: str):
        computed_hash_value: int = self.hash(hash_key)

        return self.collection.get(computed_hash_value, {}).get(hash_key)