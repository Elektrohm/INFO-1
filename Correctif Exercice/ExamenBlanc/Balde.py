

class A:
    def sum(self, lst):
        sum = 0
        for i in lst:
            sum += i
        return sum


class B:
    def sum_A(self, lst):
        a = A()
        return A().sum(lst)


if __name__ == '__main__':
    b = B()
    print(b.sum_A([1,2,3,4,5]))