## Hash Table Practice

A Hash Table is implemented with a fixed-size array.

**Reminder:** A hash table **does NOT do a linear search** to locate the item! If you are looking to implement a linear search algorithm within the hash table, think twice!

### Task

With reference to the **algorithm** given in the [notes](https://docs.google.com/document/d/18-ROQl3yrCsoCzIDRKCvKqx82IprpE5UoxTVyPfw8bo/edit?tab=t.0#heading=h.n8aq0nk6ho4p), you are required to Implement a **Hash Table** class (in the **hashtable.py file**)  

with the attributes:  
- `size` - size of the hash table
- `values` - a Python list spanning the size of the hash table, pre-filled with the **None** placeholder

and the following methods:  
- `repr` - returns a formatted string containing the values in the hash table
- `_hash`
    - takes in the argument `key`
    - returns the hashed value using the rolling polynomial algorithm below:  
      (Further reading: https://cp-algorithms.com/string/string-hashing.html)  
        
      $`hash(s) = (s[0] + s[1].p + s[2].p^2 + ... + s[n-1].p^{n-1})\ mod\ m = (\sum_{i=0}^{n-1} s[i].p^i)\ mod\ m`$  
      where
      - `s[0]` indicates the integer representation of a character at index 0 of the string (remember to convert it accordingly)
      - `p` - a small prime number (if the input is composed of only lowercase letters of the English alphabet,  
        $p = 31$  is a good choice. If the input may contain both uppercase and lowercase letters, then  
        $p = 53$  is a possible choice.)
      - `m` - a large prime number (we will use $`10^9+9`$ for this implementation)

    - You can use the following sample in `pseudocode`, of calculating the hash of a string 
    $s$ , which contains only lowercase letters. We convert each character of  
    $s$  to an integer. Here we use the conversion  
    $a \rightarrow 1$ ,  
    $b \rightarrow 2$ ,  
    $\dots$ ,  
    $z \rightarrow 26$ . Converting  
    $a \rightarrow 0$  is not a good idea, because then the hashes of the strings  
    $a$ ,  
    $aa$ ,  
    $aaa$ ,  
    $\dots$  all evaluate to  
    $0$ .
    ```code
    FUNCTION ComputeHash(S : STRING) RETURNS INTEGER
        DECLARE p : INTEGER
        DECLARE m : INTEGER
        DECLARE HashValue : INTEGER
        DECLARE pPow : INTEGER
        DECLARE i : INTEGER
        DECLARE CharValue : INTEGER

        p ← 31
        m ← 1000000009
        HashValue ← 0
        pPow ← 1

        FOR i ← 1 TO LENGTH(S)
            CharValue ← ASCII(S[i]) - ASCII('a') + 1
            HashValue ← (HashValue + CharValue * pPow) MOD m
            pPow ← (pPow * p) MOD m
        NEXT i

        RETURN HashValue
    END FUNCTION
    ```
    `NOTE:` The largest value to be returned will be less than size.   
    Remember to compress the return value to fit the table size 
- `add`
    - adds an item to the hash table
    - displays the string
        - `Unable to add. Destination not empty!` if there is already an item at the destination or
        - `Data successfully added` otherwise
- `get` - returns
    - an item within the hash table
    - or the string `Destination is empty!` otherwise
- `update`
    - updates an item in the hash table
    - displays the string
        - `Unable to update. Destination is empty!` if there is no item at the destination or
        - `Data successfully updated` otherwise
- `remove`
    - removes the item at the destination
    - returns the string
        - `Unable to remove. Destination is empty!` if there is no item at the destination or
        - `Data successfully removed` otherwise

**NOTE: Remember to include the docstrings for the above methods**