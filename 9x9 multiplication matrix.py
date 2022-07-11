for i in range(1, 10):
    str = '\n'
    for j in range(1, 10):
        str += repr(j).rjust(2) + ' x' + repr(i).rjust(2) + ' = ' +repr(i*j).rjust(2) + '\t'
    print(str)