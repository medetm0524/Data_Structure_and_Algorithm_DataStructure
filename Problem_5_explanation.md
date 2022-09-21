Blockchain
A Blockchain is a sequential chain of records, similar to a linked list. Each block contains some information and how it is connected related to the other blocks in the chain. 
Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. For our blockchain we will be using a SHA-256 hash, the Greenwich Mean Time when the block was created, and text strings as the data.

Objective:
	Use your knowledge of linked lists and hashing to create a blockchain implementation.
	 
Methodology:
	Use LinkedList data srtucture as append each block. Each block has the following attributes, timestamp UTC, message, privious block's hash message. Apply SHA-256 hash for each block.  

Result:
	Returns linkedlist with blockchain. Tested on 3 cases. 
	

Time complexity:
	O(n)
	
Space complexity:
	O(n)

