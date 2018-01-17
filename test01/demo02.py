class Screen(object):
	@property
	def width(self):
		return self._width
	@width.setter
	def width(self,value):
		if isinstance(value,int) and value>0:
			self._width=value
		else:
			raise ValueError('width error')

	@property
	def height(self):
	    return self._height
	@height.setter
	def height(self,value):
		if isinstance(value,int) and value>0:
			self._height=value
		else:
			raise ValueError('height error')

	@property
	def resolution(self):
	    return self._width*self._height


s=Screen()
s.width=1024
s.height=768
print(s.resolution)