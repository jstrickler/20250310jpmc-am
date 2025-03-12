
def find_word(search_term, *file_paths, ignore_case=False):
    for file_path in file_paths:
        print(f"{file_paths = }")
        
        with open(file_path) as file_in:
            for raw_line in file_in:
                if search_term in raw_line:
                    print(raw_line.rstrip())
find_word('hatter', 'DATA/words.txt', 'DATA/parrot.txt', 'DATA/mary.txt', ignore_case=True)
print('-' * 60)
find_word('arm', 'DATA/alice.txt')
print('-' * 60)

def doit(p1, *, p2, p3):
    pass

doit(10, p2=20, p3=30)
doit("abc", p3="wombat", p2="spam")

def wacky(p1, p2, *p3, p4, p5, **p6):
    pass

wacky(10, 20, 30, 40, 50, p5="spam", p4="ham", animal="wombat", country="Poland", sport="soccer")


def spam(foo: int, bar: int, blah: float):
    print(f"{foo = }")
    print(f"{bar = }")
    print(f"{blah = }")
    
# python type hints
# mypy for checking types

spam([1, 2, 3], 20, "abc")

dev = [5, 10, 15]
staging = [8, 9, 10]
production = [100, "200", 300]

spam(*dev)
spam(*staging)
spam(*production)
