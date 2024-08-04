# import sys
# input_func = sys.stdin.readline



# num_of_order = int(input_func())

# def get_input():
#     return sys.stdin.readline().strip().split()

# items = []

# for i in range(num_of_order):
#     try:
#         line = get_input()

#         if not line:
#             break

#         command = line[0]
#         value = line[1] if len(line) > 1 else None

#         if command == 'push_front':
#             items.insert(0, value)
#         elif command == 'push_back':
#             items.append(value)
#         elif command == 'front':
#             print(items[0] if items else 'No job')
#         elif command == 'back':
#             print(items[-1] if items else 'No job')
#         elif command == 'reverse':
#             items.reverse()

#     except EOFError:
#         break


num_of_order = int(input())

def get_input():
    return input().strip().split()

items = []
print_order = []
for i in range(num_of_order):
    try:
        line = get_input()

        if not line:
            break

        command = line[0]
        value = line[1] if len(line) > 1 else None

        if command == 'push_front':
            items.insert(0, value)
        elif command == 'push_back':
            items.append(value)
        elif command == 'front':
            # print(items[0] if items else 'No job')
            if items:
                print_order.append(items[0])
                items.pop(0)
            else:
                print_order.append('No job')

        elif command == 'back':
            # print(items[-1] if items else 'No job')
            if items:
                print_order.append(items[-1])
                items.pop(-1)

            else:
                print_order.append('No job')

        elif command == 'reverse':
            items.reverse()

    except EOFError:
        break

for i in print_order:
    print(i)