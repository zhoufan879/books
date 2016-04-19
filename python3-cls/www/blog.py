
class Blog(object):

	def __init__(self):
		self.list = [
			{'id': 1001, 'title': 'JavaScript教程', 'cd': '2015-08-30', 'content': '111111......' },
			{'id': 1002, 'title': 'Python教程', 'cd': '2016-01-10', 'content': '222222......' },
			{'id': 1003, 'title': 'Git教程', 'cd': '2016-04-15', 'content': '333333......' },
		]

	def get(self, id=None):
		if id:
			for x in self.list:
				print (id, x)
				if x['id'] == id:
					return x

		return self.list

	def new(self, blog):
		self.list.append(blog)
		return True

	def remove(self, id):
		if id:
			for index, x in enumerate(self.list):
				if x['id'] == id:
					self.list.pop(index)
		
		return True

	def edit(self, blog):
		if blog:
			for index, x in enumerate(self.list):
				if x['id'] == blog['id']:
					self.list.pop(index)

		# print ( self.list )
		self.new(blog)

		return True

blog = Blog()

# print ( blog.get(1001) )

# blog.remove(1001)

# blog.new({'id': 1004, 'title': '《好好学习》', 'cd': '2016-04-15', 'content': '4444444......' })

# blog.edit({'id': 1004, 'title': '《好好学习2》', 'cd': '2016-04-15', 'content': '555555......' })

# print ( blog.get() )