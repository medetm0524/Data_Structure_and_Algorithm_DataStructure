# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 10:59:37 2022

@author: mmd20
"""

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.cache_dict = dict()
        self.entry_order = list()
        self.size = len(self.cache_dict)
        

    def get(self, key):
        
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key in self.cache_dict.keys(): #cache hit
            return self.cache_dict[key]
        else: # cache miss
            return -1
        

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if value not in self.cache_dict.values():
            if len(self.entry_order) == self.capacity: # cache reaches it's upper limit, rewrite last entry with value
                index = self.entry_order[-1]    #find last entry's index
                self.cache_dict[key] = self.cache_dict.pop(index)
                self.cache_dict[key] = value
                self.entry_order[-1] = key
            
            else:
                self.cache_dict[key] = value
                self.entry_order.append(key)
        else:
            pass
        
        

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
our_cache.set(4,4)
our_cache.set(123,123)
print(our_cache.get(4))     #Return 4
# Test Case 2
print(our_cache.get(123))   #Return 123

# Test Case 3
print(our_cache.get(14))    #Return -1