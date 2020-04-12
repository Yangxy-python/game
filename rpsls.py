#coding:gbk
"""
作者：阳新月
Rock-paper-scissors-lizard-Spock，石头剪刀布蜥蜴史波克
"""
import random
def number_to_name(number):#将游戏对象对应到不同的整数
	if number==0:
		a="石头"
	elif number==1:
		a="史波克"
	elif number==2:
		a="纸"
	elif number==3:
		a="蜥蜴"
	else:
		a="剪刀"
	return a

def name_to_number(name):# 将整数对应到游戏的不同对象
	if name==("石头"):
		b=0
	elif name==("史波克"):
		b=1
	elif name==("纸"):
		b=2
	elif name==("蜥蜴"):
		b=3
	elif name==("剪刀"):
		b=4
	
	else:
		print("Error: No Correct Name")
		b=5
	return b
		
def rpsls(player_choice):
	change1=name_to_number(player_choice)#人工所猜
	comp_number=random.randrange(0,4)#机器所随机产生
	change2=str(number_to_name(comp_number))
	print("计算机的选择是：")
	print(change2)
	if change1==comp_number:
		print("您和计算机出的一样呢")
	elif (change1==0 and comp_number==3) or (change1==0 and comp_number==4):
		print("您赢了！")
	elif (change1==2 and comp_number==1) or (change1==2 and comp_number==0): 
		print("您赢了！")
	elif (change1==1 and comp_number==0) or (change1==1 and comp_number==4): 
		print("您赢了！")
	elif (change1==3 and comp_number==2) or (change1==3 and comp_number==1): 
		print("您赢了！")
	elif (change1==4 and comp_number==3) or (change1==4 and comp_number==2): 
		print("您赢了！")
	elif change1==5:
		print("无法参与游戏")
	else:
		print("计算机赢了!")

print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
rpsls(choice_name)

