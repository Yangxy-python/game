#coding:gbk
"""
���ߣ�������
Rock-paper-scissors-lizard-Spock��ʯͷ����������ʷ����
"""
import random
def number_to_name(number):#����Ϸ�����Ӧ����ͬ������
	if number==0:
		a="ʯͷ"
	elif number==1:
		a="ʷ����"
	elif number==2:
		a="ֽ"
	elif number==3:
		a="����"
	else:
		a="����"
	return a

def name_to_number(name):# ��������Ӧ����Ϸ�Ĳ�ͬ����
	if name==("ʯͷ"):
		b=0
	elif name==("ʷ����"):
		b=1
	elif name==("ֽ"):
		b=2
	elif name==("����"):
		b=3
	elif name==("����"):
		b=4
	
	else:
		print("Error: No Correct Name")
		b=5
	return b
		
def rpsls(player_choice):
	change1=name_to_number(player_choice)#�˹�����
	comp_number=random.randrange(0,4)#�������������
	change2=str(number_to_name(comp_number))
	print("�������ѡ���ǣ�")
	print(change2)
	if change1==comp_number:
		print("���ͼ��������һ����")
	elif (change1==0 and comp_number==3) or (change1==0 and comp_number==4):
		print("��Ӯ�ˣ�")
	elif (change1==2 and comp_number==1) or (change1==2 and comp_number==0): 
		print("��Ӯ�ˣ�")
	elif (change1==1 and comp_number==0) or (change1==1 and comp_number==4): 
		print("��Ӯ�ˣ�")
	elif (change1==3 and comp_number==2) or (change1==3 and comp_number==1): 
		print("��Ӯ�ˣ�")
	elif (change1==4 and comp_number==3) or (change1==4 and comp_number==2): 
		print("��Ӯ�ˣ�")
	elif change1==5:
		print("�޷�������Ϸ")
	else:
		print("�����Ӯ��!")

print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)

