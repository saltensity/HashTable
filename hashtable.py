class HashTable:
    def __init__(self, size):
        self.size = size
        self.values = size*[None]

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
        p = 31
        m = 1000000009
        
        hashValue = 0
        pPow = 1
        
        for i in range(len(key)):
          charValue = ord(key[i]) - ord('a') + 1
          hashValue = (hashValue + charValue * pPow) % m
          pPow = (pPow * p) % m
        
        return hashValue % self.size

    def setitem(self, key: str, value: dict) -> None:
        """
        Adds / Updates the key in the hash table with the value.
        
        Parameters
        -----------
        - key: str
          The key to be used in the hash table.
        - value: dict
          The record to be inserted.
        """
        index = self._hash(key)
        if self.values[index] is None:
          print('Data successfully added!')
        else:
          print('Data successfully updated!')
          
        self.values[index] = value

    def getitem(self, key: str) -> 'dict | None':
        """
        Returns the value associated with the key in the hash table.
        
        Parameters
        -----------
        - key: str
          The key to be used in the hash table.
        """
        index = self._hash(key)
        if self.values[index] is None:
          print('Destination is empty!')
          return None
        
        return self.values[index]
        
    def delitem(self, key: str) -> None:
        """
        Deletes the key-pair value in the hash table, if it exists.
        
        Parameters
        -----------
        - key: str
          The key to be used in the hash table.
        """
        index = self._hash(key)
        if self.values[index] is None:
          print('Unable to remove. Destination is empty!')
          return
        
        self.values[index] = None
        print('Data successfully removed')
      