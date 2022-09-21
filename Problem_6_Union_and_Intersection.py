# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 13:45:06 2022

@author: mmd20
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    head_llist_1 = llist_1.head
    head_llist_2 = llist_2.head

    union_list = []
    while head_llist_1 !=None:
        if head_llist_1.value not in union_list:
            union_list.append(head_llist_1.value)
        head_llist_1 = head_llist_1.next 
        
    while head_llist_2 !=None:
        if head_llist_2.value not in union_list:
            union_list.append(head_llist_2.value)
        head_llist_2 = head_llist_2.next
        
    return union_list

def intersection(llist_1, llist_2):
    # Your Solution Here
    head_llist_1 = llist_1.head
    head_llist_2 = llist_2.head
    
    List_1 = []
    intersection_list = []
    while head_llist_1 !=None:
        if head_llist_1.value not in List_1:
            List_1.append(head_llist_1.value)
        head_llist_1 = head_llist_1.next 
        
    while head_llist_2 !=None:
        if head_llist_2.value in List_1:
            intersection_list.append(head_llist_2.value)
        head_llist_2 = head_llist_2.next
        
    return intersection_list

# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)
print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [1,2,3,4,5,6]
element_2 = [4,5,6,7,8,9]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print (union(linked_list_5,linked_list_6))
print (intersection(linked_list_5,linked_list_6))

# Test Case 2
linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = [3,33, 241, 15, 21, 21, 415, 33, 1, 5]
element_2 = [215, 33, 215, 21, 1, 16, 49]

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print (union(linked_list_7,linked_list_8))
print (intersection(linked_list_7,linked_list_8))
# Test Case 3
linked_list_9 = LinkedList()
linked_list_10 = LinkedList()

element_1 = [1,2,3,4,5]
element_2 = []

for i in element_1:
    linked_list_9.append(i)

for i in element_2:
    linked_list_10.append(i)

print (union(linked_list_9,linked_list_10))
print (intersection(linked_list_9,linked_list_10))
