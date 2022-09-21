# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 11:22:43 2022

@author: mmd20
"""

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    user_in_group = False
    if len(group.get_users())!=0:
        if user in group.get_users():
            return True
    else:
        for sub_group in group.get_groups():
            user_in_group = is_user_in_group(user, sub_group)
            
    return user_in_group
    


print(is_user_in_group(sub_child_user, parent))  
# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
test1_user = 'Neighbour'
print(is_user_in_group(test1_user, parent)) #False
# Test Case 2
test2_user = 'Neighbour'
child.add_user(test2_user)
print(is_user_in_group(test1_user, parent)) #True

# Test Case 3
test2_user = 'Neighbour'
child.add_user(test2_user)
print(is_user_in_group(test1_user, sub_child)) #False
