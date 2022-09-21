# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 13:33:21 2022

@author: mmd20
"""

# importing os module 
import os 

def recurse_files(syntax, folder_path):
    folder_in = os.listdir(folder_path)
    path_len = len(folder_path)
    for f_inside in folder_in:
        if f_inside.count('.')>=1:
            if syntax in f_inside:
                [print(folder_path[len(folder_path):]+"\\"+ sub_files) for sub_files in folder_in] #print all folders and files in directory of extension is found
        else:
            subfolder_path = folder_path+"\\"+ f_inside
            recurse_files(syntax, subfolder_path) # Run recursive function for subfolder
                
#path = r"C:\Users\mmd20\PycharmProjects\pythonProject1\Udacity\DataStructure_and_Algorithms\2_DataStructure\Project\Task2"
path = os.path.dirname(os.path.realpath(__file__))

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
print('\n Test 1')
recurse_files('.c', path)

# Test Case 2
print('\n Test 2')
recurse_files('.h', path)

# Test Case 3
print('\n Test 3')
recurse_files('.py', path)





