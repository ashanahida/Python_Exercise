birth_year ={'Asha':1999,
             'Nahida':1999,
             'Akhi':2004,
             'Asha':2000
             }
print(birth_year)
#len
print(len(birth_year))
#key value print
print(birth_year['Nahida'])
#updating 
birth_year['Nahida']=1555
print(birth_year)
#adding new item list in dict 
birth_year['nabin']=[1111,4444,6666]
print(birth_year)

#nasted dict
birth_year['salam']={'home':1111,'office':555}
print(birth_year)
#access key
print([birth_year['salam']['office']])
#get() method
print([birth_year.get('asha')])
#keys()
print(birth_year.keys())
#values()
print(birth_year.values())
#items
print(birth_year.items())
#copy
birth_year2 = birth_year.copy()
print(birth_year2)
#for loop in dict
for i in birth_year:
    print(i)            #to access keys
    print(birth_year[i])# to access values corosponding to keys
for i in birth_year.items():
    print(i)            #to access key&value pair

#example
data ={1: 'jenny',
       2: 'jabir',
       0: 'jhon',
}
print(data[0])

#delete item
bit_coin = {'56mp':133,
            '23np':889,
            '55pl':991,
            '67hp':542,
            '88yt':432
            }
del bit_coin['56mp']
print(bit_coin.pop('67hp'))
print(bit_coin.popitem())
bit_coin.clear()
print(bit_coin)
