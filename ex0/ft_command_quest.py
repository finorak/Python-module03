import sys

if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv)
    counter = 0
    if argc == 1:
        print("No arguments provied!")
    print(f"Program name: {argv[0]}")
    if argc > 1:
        for arg in argv[1:]:
            print(f"Argument {counter + 1}: {arg}")
            counter += 1
    print(f"Total arguments: {argc}")
