from operator import itemgetter
from itertools import groupby
'''
根据字段将记录分组，使用groupby要先排序，因为groupby只能检查连续的项
'''
rows=[{'address':'5412 N CLARK','date':'07/01/2012'},
      {'address':'5148 N CLARK','date':'07/04/2012'},
      {'address':'5800 E 58TH','date':'07/02/2012'},
      {'address':'2122 N CLARK','date':'07/03/2012'},
      {'address':'5646 N RAVENSWOOD','date':'07/02/2012'},
      {'address':'1062 W ADDISON','date':'07/02/2012'},
      {'address':'4801 N BROADWAY','date':'07/01/2012'},
      {'address':'1039 W CLARK','date':'07/04/2012'},
      ]

rows.sort(key=itemgetter('date'))
print(rows)
for date,items in groupby(rows,key=itemgetter('date')):
    print(date)
    for i in items:
        print('',i)