 # 人工智能课程的作业



 ## 实验一（代码project.py，版本为python3.5）

 #### 遇到过以下几个问题

1. 根据类的属性排序：

```

cmpfun = operator.attrgetter('val2') #按照类属性val2进行排序，小的在前面。需要import operator

openTable.sort(key = cmpfun)    #对openTable按照属性val2进行从小到大排序

```

2. 二维数组转一维数组：

arr为3*3,转tmp的为一维数组

```

tmp = arr.reshape(1,9)[0]

```

3. 八数码是否有解问题

一个状态表示成一维的形式，求出除0之外所有数字的逆序数之和，也就是每个数字前面比它大的数字的个数的和，称为这个状态的逆序。

+ 若两个状态的逆序奇偶性相同，则可相互到达，否则不可相互到达。

+ 由于原始状态的逆序为0（偶数），则逆序为偶数的状态有解。

代码：

```

def caljie(arr):

	tmp = arr.reshape(1,9)[0]

	n = 0

	for i in range(1,9):

		for j in range(i):

			if(tmp[i]==0):

				continue

			if(tmp[i]<tmp[j]):

				n = n^1

	return n

```




