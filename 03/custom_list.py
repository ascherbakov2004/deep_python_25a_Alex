class CustomList(list):
    def __lt__(self, other):
        return sum(self) < sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)

    def __extend_zeros(self, other):
        l_list = CustomList(self)
        r_list = CustomList(other)
        diff = len(l_list) - len(r_list)
        if diff != 0:
            if diff > 0:
                r_list.extend([0] * diff)
            else:
                l_list.extend([0] * (-diff))
        return r_list, l_list

    def __add__(self, other):
        r_list, l_list = self.__extend_zeros(other)
        return CustomList([l_elem + r_elem for l_elem, r_elem in zip(l_list, r_list)])

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        r_list, l_list = self.__extend_zeros(other)
        return CustomList([l_elem - r_elem for l_elem, r_elem in zip(l_list, r_list)])

    def __rsub__(self, other):
        l_list, r_list = self.__extend_zeros(other)
        return CustomList([l_elem - r_elem for l_elem, r_elem in zip(l_list, r_list)])

    def __str__(self):
        return f"elements: {super().__str__()} sum: {sum(self)}"