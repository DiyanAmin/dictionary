#Write a program to check the frequency of a value in a dictionary - {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}
please_give_me_name={'Codingal':2,'is':2,'best':2,'for':2,'Coding':1}#-->Repeated value:2
count2=2
val=0
for keys in please_give_me_name:
    if please_give_me_name[keys]==count2:
        val+=1
print(f'Number of times value is repeated: {val}')