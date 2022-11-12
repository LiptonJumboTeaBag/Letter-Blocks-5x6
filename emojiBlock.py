import random, sys


def letter_to_5x6(letter, f = "1", s=':0:'):
    output = []
    match letter: 
        case 'a': 
            output = [
                s + s + f + s + s, 
                s + f + s + f + s, 
                s + f + s + f + s, 
                f + f + f + f + f, 
                f + s + s + s + f,
                f + s + s + s + f]
        case 'b':
            output = [
                f + f + f + f + s,
                f + s + s + f + s,  
                f + f + f + f + f,
                f + s + s + s + f,
                f + s + s + s + f,
                f + f + f + f + f]
        case 'c':
            output = [
                f + f + f + f + f,
                f + s + s + s + f,
                f + s + s + s + s,
                f + s + s + s + s,
                f + s + s + s + f,
                f + f + f + f + f]
        case 'd':
            output = [
                f + f + f + f + s,
                f + s + s + s + f,
                f + s + s + s + f,
                f + s + s + s + f,
                f + s + s + s + f,
                f + f + f + f + s]
        case 'e':
            output = [
                f + f + f + f + f,
                f + s + s + s + s,
                f + f + f + s + s,
                f + s + s + s + s,
                f + s + s + s + s,
                f + f + f + f + f]
        case 'f':
            output = [
                f + f + f + f + f,
                f + s + s + s + s,
                f + f + f + s + s,
                f + s + s + s + s,
                f + s + s + s + s,
                f + s + s + s + s]
        case 'g':
            output = [
                f + f + f + f + f,
                f + s + s + s + f,
                f + s + s + s + s,
                f + s + s + f + f,
                f + s + s + s + f,
                f + f + f + f + f]
        case 'h':
            output = [
                f + s + s + s + f,
                f + s + s + s + f,
                f + f + f + f + f,
                f + s + s + s + f,
                f + s + s + s + f,
                f + s + s + s + f]
        case 'i':
            output = [
                f + f + f + f + f,
                s + s + f + s + s,
                s + s + f + s + s,
                s + s + f + s + s,
                s + s + f + s + s,
                f + f + f + f + f]
        case 'j':
            output = [
                s + s + s + s + f,
                s + s + s + s + f,
                s + s + s + s + f,
                s + s + s + s + f,
                f + s + s + s + f,
                f + f + f + f + f]
        case 'k':
            output = [
                f + s + s + s + f,
                f + s + s + s + f,
                f + s + s + f + s,
                f + f + f + s + s,
                f + s + s + f + s,
                f + s + s + s + f]
        case 'l':
            output = [
                f + s + s + s + s,
                f + s + s + s + s,
                f + s + s + s + s,
                f + s + s + s + s,
                f + s + s + s + s,
                f + f + f + f + f]
        case 'm':
            output = [
                f + s + s + s + f,
                f + f + s + f + f,
                f + s + f + s + f,
                f + s + f + s + f,
                f + s + s + s + f,
                f + s + s + s + f]
        case 'n':
            output = [
                f + s + s + s + f,
                f + f + s + s + f,
                f + s + f + s + f,
                f + s + s + f + f,
                f + s + s + s + f,
                f + s + s + s + f]
        case 'o':
            output = [
                f + f + f + f + f,
                f + s + s + s + f,
                f + s + s + s + f,
                f + s + s + s + f,
                f + s + s + s + f,
                f + f + f + f + f]
        case 'p':
            output = [
                f + f + f + f + s,
                f + s + s + s + f,
                f + f + f + f + s,
                f + s + s + s + s,
                f + s + s + s + s,
                f + s + s + s + s]
        case 'q':
            output = [
                s + f + f + f + s,
                f + s + s + s + f,
                f + s + s + s + f,
                f + s + f + s + f,
                f + s + s + f + s,
                s + f + f + s + f]
        case 'r':
            output = [
                f + f + f + f + s,
                f + s + s + s + f,
                f + f + f + f + s,
                f + s + s + s + f,
                f + s + s + s + f,
                f + s + s + s + f]
        case 's':
            output = [
                s + f + f + f + f,
                f + s + s + s + s,
                s + f + f + f + s,
                s + s + s + s + f,
                s + s + s + s + f,
                f + f + f + f + s]
        case 't':
            output = [
                f + f + f + f + f,
                s + s + f + s + s,
                s + s + f + s + s,
                s + s + f + s + s,
                s + s + f + s + s,
                s + s + f + s + s]
        case 'u':
            output = [
                f + s + s + s + f,
                f + s + s + s + f,
                f + s + s + s + f,
                f + s + s + s + f,
                f + s + s + s + f,
                s + f + f + f + s]
        case 'v':
            output = [
                f + s + s + s + f,
                f + s + s + s + f,
                f + s + s + s + f,
                s + f + s + f + s,
                s + f + s + f + s,
                s + s + f + s + s]
        case 'w':
            output = [
                f + s + s + s + f,
                f + s + s + s + f,
                f + s + f + s + f,
                f + s + f + s + f,
                f + s + f + s + f,
                s + f + s + f + s]
        case 'x':
            output = [
                f + s + s + s + f,
                s + f + s + f + s,
                s + s + f + s + s,
                s + f + s + f + s,
                f + s + s + s + f,
                f + s + s + s + f]
        case 'y':
            output = [
                f + s + s + s + f,
                s + f + s + f + s,
                s + s + f + s + s,
                s + s + f + s + s,
                s + s + f + s + s,
                s + s + f + s + s]
        case 'z':
            output = [
                f + f + f + f + f,
                s + s + s + f + s,
                s + s + f + s + s,
                s + f + s + s + s,
                f + s + s + s + s,
                f + f + f + f + f]
        case ' ':
            output = [
                s + s + s + s + s,
                s + s + s + s + s,
                s + s + s + s + s,
                s + s + s + s + s,
                s + s + s + s + s,
                s + s + s + s + s]
        case '.':
            output = [
                s + s + s + s + s,
                s + s + s + s + s,
                s + s + s + s + s,
                s + s + s + s + s,
                s + s + s + s + s,
                f + s + s + s + s]
        case '!':
            output = [
                f + s + s + s + s,
                f + s + s + s + s,
                f + s + s + s + s,
                f + s + s + s + s,
                s + s + s + s + s,
                f + s + s + s + s]
        case '?':
            output = [
                f + f + f + f + f,
                f + s + s + s + f,
                s + s + f + f + f,
                s + s + f + s + s,
                s + s + s + s + s,
                s + s + f + s + s]
        case _:
            output = [
                f + f + f + f + f,
                f + f + f + f + f,
                f + f + f + f + f,
                f + f + f + f + f,
                f + f + f + f + f,
                f + f + f + f + f]




    return output
def main():
    args = sys.argv[1:]
    if len(args) == 0:
        print('usage: word1 word2 word3 ...')
        sys.exit(1)
    fill = ""
    space = ""
    replace = False
    match args[0]:
        case '-r' | '--replace':
            fill = args[1]
            space = args[2]
            args = args[3:]
            replace = True
        case '-f' | '--fill':
            fill = args[1]
            space = " " * len(fill)
            args = args[2:]
            replace = True
        case '-s' | '--space':
            space = args[1]
            fill = " " * len(space)
            args = args[2:]
            replace = True
        case '-c' | '--character':
            fill = args[1]
            space = " " * 2 * len(fill)
            args = args[2:]
            replace = True

    output = []

    for word in args:
        length = 1
        output.append([space]*6)
        for letter in word:
            if replace:
                output.append(letter_to_5x6(letter, fill, space))
            else:
                output.append(letter_to_5x6(letter))
            output.append([space]*6)
            length += 6
        outputWord = ""
        printedTop = False
        for i in range(6):
            for j in range(len(output)):
                outputWord += output[j][i]
            if printedTop == False:
                print(space * length)
                printedTop = True
            print(outputWord)
            outputWord = ""
        print(space * length)
        output = []

if __name__ == '__main__':
    main()
