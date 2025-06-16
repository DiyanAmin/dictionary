#First, create a dictionary that consists of - id, name, class and subject integration of students. Then, write a program to retrieve unique entries and eliminate the rest
student_details={'ID 1':
                 {'Name':'Zprichye','Grade':3,'Age':'6','Subjects':['English Literature','English Language','French','Kannnada']},
                 'ID 2':#Second ID
                 {'Name':'Zaonchrance','Grade':9,'Age':20,'Subjects':['English','Art','French','Hindi']},
                 'ID 3':
                 {'Name':'Zjekreyink','Grade':3,'Age':'6','Subjects':['English Literature','English Language','French','Kannnada']}}
unknown_name={}
for key,value in student_details.items():
    if value not in unknown_name.values():
        unknown_name[key]=value
print(f'{unknown_name}')
