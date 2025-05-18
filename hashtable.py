class HashTable:
    def __init__(self, size):
        pass

    def __repr__(self):
        """returns a formatted string containing the values in the hash table"""
        return f"HashTable {self.values}"

    def _hash(self, key):
        """
        Return the hashed value using the rolling polynomial algorithm.
        Further reading: https://cp-algorithms.com/string/string-hashing.html

        Note: 
        - p: int
          A parameter used in the rolling polynomial algorithm
        - size: int
          The largest value to be returned will be less than size
       
        Parameters
        ---------
        - key: str
          The key to be hashed
        """
        pass

    def add(self, key, value):
        """
        """
        index = self._hash(key)
        if self.values[index] is None:
            self.values[index] = value
        else:
            print("Unable to add. Destination not empty!")

    def get(self, key):
        """
        """
        pass

    def update(self, key, value):
        """
        """
        pass
        
    def remove(self, key):
        """
        """
        pass