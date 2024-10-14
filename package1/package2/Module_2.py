from package1.package2.Module_1 import hello
import Module_1
print(Module_1)


def good_word(name):
    hello(name)
    print("You're the best, ", name)

if __name__ == '__main__':
    good_word('Urban')