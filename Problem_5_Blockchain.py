# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 12:33:52 2022

@author: mmd20
"""

import hashlib
from datetime import datetime, timezone

def calc_hash(string):
      sha = hashlib.sha256()
      hash_str = string.encode('utf-8')
      sha.update(hash_str)

      return sha.hexdigest()

class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = calc_hash(data)
      self.next = None

def linked_list(input_list):
    head = None
    tail = None
    
    if len(input_list) == 0:
        print('No data')
        return None
    
    else:
        for value in input_list:
            timestamp = datetime.now(timezone.utc).strftime("%H:%M %d/%m/%Y")
            
            if head == None:
                prev_hash = 0
                head = Block(timestamp, value, prev_hash)
                current_hash = calc_hash(value)
                tail = head
            else:
                tail.next = Block(timestamp, value, current_hash)
                tail = tail.next
                current_hash = calc_hash(value)  
            
        # TODO: Implement the more efficient version that keeps track of the tail
        return head
        

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
text1 = ['Some information 0', 'Another information 1', 'Next information 2']
linked_list(text1)

# Test Case 2
text2 = []
linked_list(text2)

# Test Case 3
text3 = ['A Blockchain is a sequential chain of records, similar to a linked list.', 
         'Each block contains some information and how it is connected related to the other blocks in the chain.', 
         'Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data.',
         'For our blockchain we will be using a SHA-256 hash, the Greenwich Mean Time when the block was created, and text strings as the data.']
linked_list(text3)