# Slicing and Striding

numbers = []
i = 0
while i < 21:
    numbers.append(i) 
    """
    TypeError: 'builtin_function_or_method' object is not subscriptable
    Line 5: changed [] to () around i
    """
    i = i + 1
print (numbers)

new = []
def squareList(listHere):
    for num in listHere:
        x = num ** 2 
        new.append(x)
    print (new)
squareList(numbers)

def first_fifteen(listHere):
    firstFifteen = []
    for i in range(15):
        firstFifteen.append(listHere[i])
    print (firstFifteen)
first_fifteen (new)

def every_fifth(listHere):
    print (listHere[4::5])
every_fifth(new)

def fancy_function(listHere):
    last_thirty = [listHere[-1::-3]]
    print (last_thirty)
fancy_function(new)


# 3D Lists

def create_2d_list():
    matrix = []
    for i in range(5):
        matrix.append([])
        for j in range(5):
            matrix[i].append(i * 5 + j + 1)
    return matrix
matrix = create_2d_list()
print(matrix)

def modified_2d(matrix):
    for i in range(5):
        for j in range(len(matrix[i])):
            if matrix[i][j] % 3 == 0:
                matrix[i][j] = "?"
    return matrix
matrix = modified_2d(matrix)
print (matrix)

def sum_non(new_matrix):
    total = 0
    for i in range(5):
        for j in range(len(matrix[i])):
            if matrix[i][j] != "?":
                total = total + matrix[i][j]
    print (total)
sum_non(matrix)