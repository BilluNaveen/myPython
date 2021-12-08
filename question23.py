class Practice:
    def sub_sets(self, values):
        print(self.subsetsRecur([], values))

    def subsetsRecur(self, current, values):
        if values:
            return self.subsetsRecur(current, values[1:]) + self.subsetsRecur(current + [values[0]], values[1:])
        return [current]

list_a = [4, 5, 6]

Practice().sub_sets(list_a)