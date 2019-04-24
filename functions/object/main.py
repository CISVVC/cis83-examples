count = 0
def print_face():
    global count
    # print face statements...
    count = count + 1
    print('The face will print here',count)
    return

def runme(f):
   f()

print_face()

func = print_face

func()
print_face()
runme(print_face)
runme(func)
