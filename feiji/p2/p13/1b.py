def test(out=1):
    out_list = [out]
    def test_in():
        out_list[0] += 1
        print(out_list[0])
        return out_list[0]
    return test_in
test()()
test()()
test1 = test()
test1()
test1()
