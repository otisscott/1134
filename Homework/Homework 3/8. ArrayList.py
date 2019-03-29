import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()


class ArrayList:
    def __init__(self):
        self.data_arr = make_array(1)
        self.n = 0
        self.capacity = 1

    def __len__(self):
        return self.n

    def append(self, val):
        if(self.n == self.capacity):
            self.resize(2 * self.capacity)
        self.data_arr[self.n] = val
        self.n += 1

    def resize(self, new_size):
        new_arr = make_array(new_size)
        for i in range(self.n):
            new_arr[i] = self.data_arr[i]
        self.data_arr = new_arr
        self.capacity = new_size

    def __getitem__(self, ind):
        if not(0 <= abs(ind) <= (self.n - 1)):
            raise IndexError("Invalid Index")
        if ind < 0:
            return self.data_arr[self.n + ind]
        else:
            return self.data_arr[ind]

    def __setitem__(self, ind, val):
        if not(0 <= abs(ind) <= (self.n - 1)):
            raise IndexError("Invalid Index")
        if ind < 0:
            self.data_arr[self.n + ind] = val
        else:
            self.data_arr[ind] = val

    def __iter__(self):
        for i in range(self.n):
            yield self.data_arr[i]

    def extend(self, other_iterable):
        for elem in other_iterable:
            self.append(elem)

    def __repr__(self):
        final = "["
        for num in range(self.n):
            if num == self.n - 1:
                final += str(self.data_arr[num])
            else:
                final += str(self.data_arr[num]) + ", "
        return final + "]"

    def __add__(self, other):
        new_arr = ArrayList()
        for item in range(len(self)):
            new_arr.append(self[item])
        for item in range(len(other)):
            new_arr.append(other[item])
        return new_arr

    def __iadd__(self, other):
        for item in other:
            self.append(item)
        return self

    def __mul__(self, n):
        new_arr = ArrayList()
        for item in range(self.n * n):
            new_arr.append(self[item % self.n])
        return new_arr

    def __rmul__(self, n):
        new_arr = ArrayList()
        for item in range(self.n * n):
            new_arr.append(self[item % self.n])
        return new_arr
