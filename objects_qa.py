
while True:
    value = input("Write some input, q to quit:")
    if value == 'q':
        break

    result = eval (value)

    print (result, type(result))
