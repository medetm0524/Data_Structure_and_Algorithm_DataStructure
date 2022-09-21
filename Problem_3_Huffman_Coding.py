# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 00:33:10 2022

@author: mmd20
"""
import sys

class Node:
    def __init__(self, char):
        self.char = char
        self.value = 0
        self.left = None
        self.right = None
        self.bit = None
        
    def set_left_child(self, node):
        self.left = node
        
    def get_left_child(self):
        return self.left
    
    def set_right_child(self, node):
        self.right = node
        
    def get_right_child(self):
        return self.right
    
    def get_value(self):
        if self.bit is None:
            return self.char
        else:
            return [self.char, self.bit, self.value]

class PriorityQueue:

    def __init__(self):
        self.items = []
        
    def size(self):
        return len(self.items) 

    #Sort the queue besed on priority(value)
    def sort_queue(self):
        iter = 1
        while iter+1 <= self.size():
        #for i in range(self.size()):
            last_elem = self.items[-(iter)]
            second_last = self.items[-(iter+1)]
            
            if last_elem.value > second_last.value:
                self.items[-(iter+1)] = last_elem
                self.items[-(iter)] = second_last
                iter+=1
            else:
                break
            
            
    def list_of_freq(self):
        return [freq.value for freq in self.items]       
            
    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop()

class Tree:
    def __init__(self, Node):
        self.root = Node
    
    def get_root(self):
        return self.root

def huffman_encoding(data):
    frequency_dict = dict()
    for character in data:
        if character in frequency_dict.keys():
            frequency_dict[character]+=1            
        else:
            frequency_dict[character] = 1
    #Sort the dictionary
    frequency_dict = {k: v for k, v in sorted(frequency_dict.items(), key=lambda item: item[1])}
   
    
   #Build a Priority Queue    
    char_PQ = PriorityQueue()
    for item in reversed(frequency_dict.items()):
        item_node = Node(item[0])
        item_node.value = item[1]
        char_PQ.enqueue(item_node)
    
    while char_PQ.size() != 1:
        smallest_left = char_PQ.dequeue() 
        smallest_right = char_PQ.dequeue() #Pick 2 nodes with smallest value
        
        #Assign a bit value, 0 - left, 1 - right
        smallest_left.bit = 0
        smallest_right.bit = 1
        
        sum_value = smallest_left.value+smallest_right.value #Create a new node and assign sum value
        sum_node = Node(sum_value)
        sum_node.value = sum_value
        
        sum_node.set_left_child(smallest_left) #Assign children 

        sum_node.set_right_child(smallest_right)
        
        char_PQ.enqueue(sum_node)    
        char_PQ.sort_queue() #Perform sorting
    
    def pre_order(tree):
        visit_order = list()
        def traverse(node):
            if node:
                # visit the node
                visit_order.append(node.get_value())
                
                # traverse left subtree
                traverse(node.get_left_child())
                
                # traverse right subtree
                traverse(node.get_right_child())
        
        traverse(tree.get_root())
        
        return visit_order
    
    tree = Tree(char_PQ.items[0])
    visit_order = pre_order(tree)
    codes = dict()
    code = str()
    code_freq = list()
    
    for i in range(1,len(visit_order),1):
    #for i in range(1,10,1):
        elem = visit_order[i]

        if isinstance(elem[0], int)==False:

            while elem[2] >=code_freq[-1]:
                code = code[:-1]
                code_freq.pop()           
            
            char_code = code+str(elem[1])
            codes[elem[0]]=char_code
            
        else:
            
            if len(code)==0:
                code_freq.append(elem[0])
                code+=str(elem[1])
            
            
            #elif elem[0]<visit_order[i-1][2]:
            elif elem[0]<code_freq[-1]:   
                freq = elem[0]
                bit_code = elem[1]
                code+=str(elem[1])
                code_freq.append(elem[0])
            
            else:
                
                while elem[0]>code_freq[-1]:
                    code = code[:-1]
                    code_freq.pop()
                    if len(code_freq)==0:
                        break
                code = code[:-1]+str(elem[1])
                code_freq.append(elem[0])
                

    encoded_message = str()
    for char in data:
        for key, value in codes.items():
            if char == key:
                encoded_message+=value
    return encoded_message,tree

def huffman_decoding(data,tree):
    node = tree.get_root()
    decoded_message = str()

    for i in data:
        #print(node.value, node.bit, i)
        if int(i)==0:
            if node.get_left_child() !=None:
                node = node.get_left_child()
            else:
                char = node.char
                decoded_message+=char
                node = tree.get_root()
                node = node.get_left_child()
        
        else:
            if node.get_right_child() != None:
                node = node.get_right_child()
            else:
                char = node.char
                decoded_message+=char
                node = tree.get_root()
                node = node.get_right_child()
                
    decoded_message+=node.char
    return decoded_message
    


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
Test1 = "Hello world"
print ("The size of the data is: {}\n".format(sys.getsizeof(Test1)))
print ("The content of the data is: {}\n".format(Test1))

encoded_data, tree = huffman_encoding(Test1)
print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)
print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the encoded data is: {}\n".format(decoded_data))

# Test Case 2
Test2 = "AAAAAAABBBCCCCCCCDDEEEEEE"
print ("The size of the data is: {}\n".format(sys.getsizeof(Test2)))
print ("The content of the data is: {}\n".format(Test2))

encoded_data, tree = huffman_encoding(Test2)
print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)
print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the encoded data is: {}\n".format(decoded_data))

# Test Case 3
Test2 = "BIG BANG"
print ("The size of the data is: {}\n".format(sys.getsizeof(Test2)))
print ("The content of the data is: {}\n".format(Test2))

encoded_data, tree = huffman_encoding(Test2)
print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)
print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the encoded data is: {}\n".format(decoded_data))