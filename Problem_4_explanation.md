Active Directory
In Windows Active Directory, a group can consist of user(s) and group(s) themselves. We can construct this hierarchy as such. Where User is represented by str representing their ids.

Objective:
	Write a function that provides an efficient look up of whether the user is in a group.
	 
Methodology:
	Use recursive method to loop over each sub_group in group, and return True if user is in target_folder. Otherwise return False

	

Time complexity:
	O(n)
	
Space complexity:
	O(n)

