class TreeNode:
	def __init__(self, key):
		self.val = key
		self.left = None
		self.right = None

class CheckFormat:
	def acceptInput(self, root : TreeNode):
		print(vars(root.left.left))

if __name__ == '__main__':
	node = TreeNode(2)
	node.left = TreeNode(5)
	node.left.left = TreeNode(15)
	node.right = TreeNode(4)
	Caller = CheckFormat()
	Caller.acceptInput(node)

