'''实现一个队列以给定的优先级排序每次pop操作时都会返回优先级最高那个元素'''
#这主要是利用了heapq模块的作用，将queue变成了堆，堆的特征就是永远弹出最小的元素
import heapq
class PriorityQueue:
	def __init__(self):
		self.queue=[] #一个队列
		self._index=0 #设置一个记录放入元素的顺序，当优先级一样时对比放入顺序
	def push(self,item,priority):#priority是优先级
		heapq.heappush(self.queue,(-priority,self._index,item))
		self._index+=1
	def pop(self):
		return heapq.heappop(self.queue)[-1]

class Item:
	def __init__(self,name):
		self.name=name
	def __repr__(self):
		return 'Item({!r})'.format(self.name)

if __name__=='__main__':
	q=PriorityQueue()
	q.push(Item('foo'),1)
	q.push(Item('bar'),5)
	q.push(Item('spam'),4)
	q.push(Item('grok'),1)
	print(q.pop())
	print(q.pop())
	print(q.pop())
	print(q.pop())