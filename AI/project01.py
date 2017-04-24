# -*- coding: utf-8 -*-
# @Author: AengusMa
# @Date:   2017-04-24 19:42:48
# @Last Modified by:   AengusMa
# @Last Modified time: 2017-04-24 21:40:02


import numpy as np
import operator
class State:
	def __init__(self, state, directionFlag=None, parent=None):
		self.state = state        
		self.direction = ['up', 'down', 'right', 'left']
		if directionFlag:
			self.direction.remove(directionFlag)  
		self.parent = parent
		self.val1 = 0
		self.val2 = 0
	#得到可以移到的方向
	def getDirection(self):
		return self.direction
	#得到0的位置
	def getZeroPos(self):
		postion = np.where(self.state == 0)
		return postion
	#移动
	def generateSubStates(self):
		if not self.direction:
			return []
		subStates = []
		boarder = len(self.state) - 1         
		row, col = self.getZeroPos()
		if 'left' in self.direction and col > 0:
			s = self.state.copy()
			tmp = s.copy()
			s[row, col] = s[row, col-1]
			s[row, col-1] = tmp[row, col]
			news = State(s, directionFlag='right', parent=self)
			news.val1 = news.cal1()
			news.val2 = news.cal2()
			subStates.append(news)
		if 'up' in self.direction and row > 0:    
		#it can move to upper place
			s = self.state.copy()
			tmp = s.copy()
			s[row, col] = s[row-1, col]
			s[row-1, col] = tmp[row, col]
			news = State(s, directionFlag='down', parent=self)
			news.val1 = news.cal1()
			news.val2 = news.cal2()
			subStates.append(news)
		if 'down' in self.direction and row < boarder:     
			s = self.state.copy()
			tmp = s.copy()
			s[row, col] = s[row+1, col]
			s[row+1, col] = tmp[row, col]
			news = State(s, directionFlag='up', parent=self)
			news.val1 = news.cal1()
			news.val2 = news.cal2()
			subStates.append(news)
		if self.direction.count('right') and col < boarder:   
			s = self.state.copy()
			tmp = s.copy()
			s[row, col] = s[row, col+1]
			s[row, col+1] = tmp[row, col]
			news = State(s, directionFlag='left', parent=self)
			news.val1 = news.cal1()
			news.val2 = news.cal2()
			subStates.append(news)
		return subStates
	#估价函数一：不在位的数字的个数
	def cal1(self):
		n = 0
		for i in range(3):
			for j in range(3):
				if(State.answer[i][j]!=self.state[i][j]):
					n+=1
		return n
	#估价函数二：不在位的数字移动到正确位置需要的最小步数
	def cal2(self):
		n = 0
		for i in range(3):
			for j in range(3):
				if(State.answer[i][j]!=self.state[i][j]):
					k,l = np.where(self.state == State.answer[i][j])
					n += abs(k-i)+abs(l-j)

		return n
	#宽度优先搜索
	def solve(self):
		openTable = []                  
		closeTable = []      
		openTable.append(self)    
		steps = 0
		path = []
		while len(openTable) > 0:      
			n = openTable.pop(0)
			flag = 0 
			for item in closeTable:
				if (item.state==n.state).all():
					flag = 1
					break
			if(flag==1):
				continue
			steps += 1
			closeTable.append(n)
			subStates = n.generateSubStates()
			for s in subStates:
				if (s.state == s.answer).all():
					path.append(s)
					while s.parent and s.parent != originState:
						path.append(s.parent)
						s = s.parent
					path.reverse()
					return path, steps
			openTable.extend(subStates)
		return path, steps
	#使用估价函数1，遇到相同的时都添加进open表
	def solve1(self):
		openTable = []                  
		closeTable = []      
		openTable.append(self)    
		steps = 0
		path = []
		while len(openTable) > 0:      
			n = openTable.pop(0)
			flag = 0 
			for item in closeTable:
				if (item.state==n.state).all():
					flag = 1
					break
			if(flag==1):
				continue
			steps += 1
			closeTable.append(n)
			subStates = n.generateSubStates()
			min = 1024
			for n in subStates:
				if(n.val1<min):
					min = n.val1
			for s in subStates:
				if (s.state == s.answer).all():
					path.append(s)
					while s.parent and s.parent != originState:
						path.append(s.parent)
						s = s.parent
					path.reverse()
					return path, steps
				if(min == s.val1):
					openTable.append(s)
		return path, steps
	#使用估价函数1所有都添加进open表，然后排序
	def solve2(self):
		openTable = []                  
		closeTable = []      
		openTable.append(self)    
		steps = 0
		path = []
		while len(openTable) > 0:      
			n = openTable.pop(0)
			flag = 0 
			for item in closeTable:
				if (item.state==n.state).all():
					flag = 1
					break
			if(flag==1):
				continue
			steps += 1
			closeTable.append(n)
			subStates = n.generateSubStates()
			for s in subStates:
				if (s.state == s.answer).all():
					path.append(s)
					while s.parent and s.parent != originState:
						path.append(s.parent)
						s = s.parent
					path.reverse()
					return path, steps
			openTable.extend(subStates)
			cmpfun = operator.attrgetter('val1')
			openTable.sort(key = cmpfun)  
		return path, steps
	#使用估价函数2，遇到相同的时都添加进open表
	def solve3(self):
		openTable = []                  
		closeTable = []      
		openTable.append(self)    
		steps = 0
		path = []
		while len(openTable) > 0:      
			n = openTable.pop(0)
			flag = 0 
			for item in closeTable:
				if (item.state==n.state).all():
					flag = 1
					break
			if(flag==1):
				continue
			steps += 1
			closeTable.append(n)
			subStates = n.generateSubStates()
			min = 1024
			for n in subStates:
				if(n.val2<min):
					min = n.val2
			for s in subStates:
				if (s.state == s.answer).all():
					path.append(s)
					while s.parent and s.parent != originState:
						path.append(s.parent)
						s = s.parent
					path.reverse()
					return path, steps
				if(min == s.val2):
					openTable.append(s)
		return path, steps
	#使用估价函数2所有都添加进open表，然后排序
	def solve4(self):
		openTable = []                  
		closeTable = []      
		openTable.append(self)    
		steps = 0
		path = []
		while len(openTable) > 0:      
			n = openTable.pop(0)
			flag = 0 
			for item in closeTable:
				if (item.state==n.state).all():
					flag = 1
					break
			if(flag==1):
				continue
			steps += 1
			closeTable.append(n)
			subStates = n.generateSubStates()
			for s in subStates:
				if (s.state == s.answer).all():
					path.append(s)
					while s.parent and s.parent != originState:
						path.append(s.parent)
						s = s.parent
					path.reverse()
					return path, steps
			openTable.extend(subStates)
			cmpfun = operator.attrgetter('val2')
			openTable.sort(key = cmpfun)  
		return path, steps
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
if __name__ == '__main__':
	#originState = State(np.array([[8,6, 3], [1, 2 , 4], [7, 0, 5]])) 
	tmp = input("输入一个数组：")
	originState = State(np.array([
		[int(tmp[0]),int(tmp[2]), int(tmp[4])], 
		[int(tmp[6]), int(tmp[8]) , int(tmp[10])], 
		[int(tmp[12]), int(tmp[14]), int(tmp[16])]])) 
	State.answer = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])
	s1 = State(state=originState.state)
	s1.val1 = s1.cal1()
	s1.val2 = s1.cal2()
	if(caljie(s1.state)==1):
		path, steps = s1.solve()
		print ("宽度优先搜索 移到步数："+str(len(path))+"\t扩展节点个数："+str(steps))
		path1, steps1 = s1.solve1()
		print ("启发1 移动步数："+str(len(path1))+"\t扩展节点个数："+str(steps1))
		path2, steps2 = s1.solve2()
		print ("启发2 移动步数："+str(len(path2))+"\t扩展节点个数："+str(steps2))
		path3, steps3 = s1.solve3()
		print ("启发3 移动步数："+str(len(path3))+"\t扩展节点个数："+str(steps3))
		path4, steps4 = s1.solve4()
		print ("启发4 移动步数："+str(len(path4))+"\t扩展节点个数："+str(steps4))
	
	else:
		print ('无解')