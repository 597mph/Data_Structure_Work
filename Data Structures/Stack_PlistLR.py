class Empty(Exception): 
	"""Error attempting to access an element from an empty container.""" 
	pass

class Stack_PlistLR: 
	def __init__ (self): 
		"""Create an empty stack.""" 
		self._data = [ ] # nonpublic list instance 
 
	def __len__(self): 
		"""Return the number of elements in the stack."""
		return len(self._data)
 
	def isEmpty(self): 
		"""Return True if the stack is empty.""" 
		return len(self._data) == 0
 
	def push(self, e): 
		"""Add element e to the top of the stack.""" 
		self._data.append(e)	# new item stored at end of list
 
	def top(self): 
		"""Return (but do not remove) the element at the top of the stack. Raise Empty exception if the stack is empty. """ 
		if self.isEmpty():
			raise Empty('Stack is empty') 
		return self._data[-1] # the last item in the list
 
	def pop(self): 
		"""Remove and return the element from the top of the stack (i.e., LIFO). Raise Empty exception if the stack is empty. """ 
		if self.isEmpty():
			raise Empty("Stack is empty") 
		return self._data.pop( )	# remove last item from list

	
	def __str__(self):
		str_s = ""
	    
		for e in self._data:
			str_s+=str(e)+" "
		
		return str_s.strip() 	

