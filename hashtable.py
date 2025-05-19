class HashTable:
    def __init__(self, size):
        pass

    def __repr__(self):
        """returns a formatted string containing the values in the hash table"""
        return f"HashTable {self.values}"

    def _hash(self, key: str) -> int:
        """
        Return a hashed location using the rolling polynomial algorithm.
        Further reading: https://cp-algorithms.com/string/string-hashing.html

        Note: 
        - The largest value to be returned will be less than size.   
        Remember to compress the return value to fit the table size.
       
        Parameters
        ---------
        - key: str
          The key to be hashed
        """
        pass

    def setitem(self, key: str, value: dict) -> None:
        """
        """
        pass

    def getitem(self, key: str) -> 'dict | None':
        """
        """
        pass
        
    def delitem(self, key: str) -> None:
        """
        """
        pass