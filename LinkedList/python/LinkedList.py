class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

class LinkedList:
	def __init__(self, value):
		self.head = Node(value)
	
	def insert(self, idx, value):
		new_node = Node(value)
		temp = self.head
		if idx == 0:
			self.head = new_node
			self.head.next = temp
			return True
		else:
			index = 1
			while temp:
				if index == idx:
					next_temp = temp.next
					temp.next = new_node
					new_node.next = next_temp
					return True
				temp = temp.next
			return False

	# O(n) insert at end
	def append(self, value):
		temp = self.head
		while temp.next:
			temp = temp.next
		temp.next = Node(value)

	# O(n) search, returns index if found, -1 otherwise
	def search(self, value):
		temp = self.head
		index = 0
		while temp:
			if temp.value == value:
				return index
			index += 1
			temp = temp.next
		# If not found return -1
		return -1

	# Updates value of node at certain index to value
	# Returns True on success
	def update(self, idx, value):
		temp = self.head
		index = 0

		while temp:
			if index == idx:
				temp.value = value
				return True
			index += 1
			temp = temp.next
		# Return False if index not in list
		return False

	def delete(self, idx):
		temp = self.head
		
		if idx == 0:
			if temp.next:
				self.head = temp.next
			else:
				self.head = None
			return True

		else:
			index = 1
			while temp.next:
				if index == idx:
					# Update link between nodes to ignore node at idx
					temp.next = temp.next.next
					return True
				index += 1
				temp = temp.next
			# If index not found
			return False

	def __str__(self):
		temp = self.head
		retval = ''
		while temp:
			retval += str(temp.value) + ' -> '
			temp = temp.next
		return retval
