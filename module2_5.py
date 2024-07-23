def get_matrix(n, m, value):  #  объявляем функцию и задаем ей параметры
    matrix = []               #  создаем пустой список внутри функции
    for i in range(n):
        matrix.append([])     #  добавляем список
        for j in range(m):
            matrix[i].append(value)  # заполняем список значениями
    print(matrix)
result_1 = get_matrix(2,2,10)
result_2 = get_matrix(3, 5, 42)
result_3 = get_matrix(4, 2, 13)
