def e_approx(n):
    e = 1
    count = 1
    for num in range(1, n + 1):
        count = count * num
        e += 1/count
    return e


def main():
    for n in range(15):
        curr_approx = e_approx(n)
        approx_str = "{:.15f}".format(curr_approx)
        print("n =", n, "Approximation:", approx_str)
