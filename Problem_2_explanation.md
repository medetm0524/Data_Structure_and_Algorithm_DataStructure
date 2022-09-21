File Recursion problem

Objective:
	For this problem, the goal is to write code for finding all files under a directory (and all directories beneath it) that end with ".c"

	Python's os module will be useful—in particular, you may want to use the following resources:
	os.path.isdir(path)
	os.path.isfile(path)
	os.listdir(directory)
	os.path.join(...)

	Note: os.walk() is a handy Python method which can achieve this task very easily. However, for this problem you are not allowed to use os.walk().

Methodology:
	Use recursion method the loop thru folders and get files' name.
	

Time complexity:
	O(n)

Space complexity:
	O(n)


