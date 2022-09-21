Least Recently Used Cache problem

There are 2 loop up operation with cache, get() and set()
While doing the get() operation, if the entry is found in the cache, it is known as a cache hit. If, however, the entry is not found, it is known as a cache miss.
- In case of cache hit, get() operation returns appropriate value
- In case of cache miss, get() operaiton returns -1

Cache has upper limit on the size of the cache (capacity). If we want to insert new element but cache is full, last inserted element (LI) will be removed and replaced by new one. 

Time complexity:
- get() operation - O(1)
- set() operation - O(1)

Space complexity:
- get() operation - O(n)
- set() operation - O(n)


