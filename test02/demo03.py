'''找到最大或最小的N个元素'''
import heapq
nums=[1,8,2,23,7,-4,18,23,42,37,2]
print(heapq.nlargest(3,nums))
print(heapq.nsmallest(3,nums))