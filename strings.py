new_file = open('write.txt', "w")
with open('test.sql', 'r') as s:
    print(type(s))
    print(s)
    for line in s:
        print(type(line))
        print(line)
        new_file.write(line)

