class HashTable:
    def __init__(self, size):
        pass

    def __repr__(self):
        """returns a formatted string containing the values in the hash table"""
        return f"HashTable {self.values}"

    def _hash(self, key: str) -> int:
        """
        Return the hashed value using the rolling polynomial algorithm.
        Further reading: https://cp-algorithms.com/string/string-hashing.html

        Note: 
        - The largest value to be returned will be less than size.   
        Remember to compress the return value to fit the table size (tip: You can use the mod operator once more)
       
        Parameters
        ---------
        - key: str
          The key to be hashed
        """
        pass

    def add(self, key: str, value: dict) -> str:
        """
        """
        pass

    def get(self, key: str):
        """
        """
        pass

    def update(self, key: str, value: dict) -> str:
        """
        """
        pass
        
    def remove(self, key: str) -> str:
        """
        """
        pass