class Node():
	"""docstring for Node"""
	def __init__(self, data=None):
		self.data = data
		self.next = None

class SLinkedList():
	"""
	doctring for Single Linked List
	"""
	def __init__(self, head=None):
		self.head = head

	def print_linked_list(self, head):
		temp = head
		while(temp):
			print(temp.data, end="->")
			temp = temp.next
		print("")

if __name__ == "__main__":
  n1 = Node(1)
  n2 = Node(2)
  n3 = Node(3)
  head = n1
  head.next = n2
  head.next.next = n3
  l = SLinkedList(None)
  l.print_linked_list(head=head)