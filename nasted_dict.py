worker_info ={
    'Neela':{'job':'python developer',
             'age':25,
             'certificate':{'SSC','HSC','Honors'}},

    'Milon':{'job':'SQA engineer',
             'age':24,
             'phone_no':{'Home':198334,'Bussiness':61973682}},

    'Tuhin':{'job':'Electronies Engineer',
             'age':27,
             'university':{'BSc':'AIUB','MSC':'UTS'},
             'phone_no':6134865}
}
#print(worker_info)
print(worker_info['Milon'])
print(worker_info['Tuhin']['phone_no'])

#adding 
worker_info['Neela']['phone_no']=234782
print(worker_info['Neela'])
#deleting
del worker_info['Milon']['phone_no']['Home']
print(worker_info['Milon'])

#nesting a list to dict
student_marks={
    'asha':[32,243,34,54,34,78],
    'gini':[34,57,56,24,98,56]}
print(student_marks)

#nested a dict to list
worker =[
    {'name':'Nella',
     'job':'python developer',
     'certificate':{'SSC','HSC','Honors'}},

    {'name':'milon',
     'job':'SQA engineer',
     'phone_no':{'Home':198334,'Bussiness':61973682}}]
print(worker)
#access item in list by indexing
print(worker[0]['certificate'])
             