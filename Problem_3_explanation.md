Data Compression - Huffman Coding
	Data Compression
	In general, a data compression algorithm reduces the amount of memory (bits) required to represent a message (data). The compressed data, in turn, helps to reduce the transmission time from a sender to receiver. 
	The sender encodes the data, and the receiver decodes the encoded data. As part of this problem, you have to implement the logic for both encoding and decoding.
	A data compression algorithm could be either lossy or lossless, meaning that when compressing the data, there is a loss (lossy) or no loss (lossless) of information. 
	The Huffman Coding is a lossless data compression algorithm. Let us understand the two phases - encoding and decoding with the help of an example.
	
Objective:
	Implement Huffman Coding logic for both encoding and decoding the message. 
	 
Methodology:
	A. Message Encoding using Huffman Coding Logic
	Phase I, Build the Huffman Tree
		Use dictionary data structure to find the character as a key and frequency of character as a value.
		Convert dictionary to Priority Queue and sort each node (value, frequency). Pop-out two nodes with minimum frequency and merge them, create internal node with value as a sum of two frequency values of extracted 2 nodes.
		Repeat this process until 1 node left in PQ. Construct a Binary Huffman Tree, assign a bit value (0 for left child node, and 1 for right child node).
	
	Phase II - Generate the Encoded Data
		Based on the Huffman tree, generate unique binary code for each character of our string message. For this purpose, you'd have to traverse the path from root to the leaf node (pre-order traverse).
		
	B. Huffman Decoding
		Decode the code from encoding operation using Huffman Binary Tree. 
		
	

Time complexity:
	O(nlogn) - apply sorting algorithm and queue
	
Space complexity:
	O(nlogn) - apply sorting algorithm and queue

