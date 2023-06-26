# Задача №36

def print_operation_table(operation, num_rows=6, num_columns=6) -> None:
    for i in range(1, num_columns + 1):
        for j in range(1, num_rows + 1):
            print(operation(i, j), end='\t')
        print()


print_operation_table(lambda x, y: x * y, num_rows=8, num_columns=6)