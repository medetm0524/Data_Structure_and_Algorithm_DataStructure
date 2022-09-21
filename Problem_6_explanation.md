Union and Intersection of Two Linked Lists
	Your task for this problem is to fill out the union and intersection functions. The union of two sets A and B is the set of elements which are in A, in B, or in both A and B. 
	For example, the union of A = [1, 2] and B = [3, 4] is [1, 2, 3, 4].
	The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members of both sets A and B. For example, the intersection of A = [1, 2, 3] and B = [2, 3, 4] is [2, 3].

Objective:
	You will take in two linked lists and return a linked list that is composed of either the union or intersection, respectively. 
	Once you have completed the problem you will create your own test cases and perform your own run time analysis on the code.
	 
Methodology:
	Iterate thru each node of each linked lists, and create 2 different lists - union_elements_list and intersection_elements_list
Result:
	return union list and intersection list 
	

Time complexity:
	O(n^2) - iterate thru both of linkedList
	
Space complexity:
	O(n)

