def test(out):
    def test_in(num_in):
        print("里面的内容是:%d"% num_in)
        return num_in + out
    return test_in
test1 = test(1)
test1(2)
tt = test1(1)
tt(2)
n = test(1)(2)
print(n)
