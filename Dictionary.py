'''
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 15, 'y': 30} ]

x[1][0] = 15

print(x)
'''

'''
def iterateDictionary(sum_dict_list):
    for item in sum_dict_list:
        print(item['first_name'])



def iterateDictionary1(students):
    for item in students:
        print(item['last_name'])


def main():
    students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

    iterateDictionary(students)
    iterateDictionary1(students)

if __name__ == "__main__":
    main()
'''


dojo= {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(sum_dict):
    for key in sum_dict.keys():
        length = len(sum_dict[key])
        print(str(length) + " " + key.upper())
        for item in sum_dict[key]:
            print(item)

printInfo(dojo)
