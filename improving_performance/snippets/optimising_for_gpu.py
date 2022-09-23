from numba import vectorize


@vectorize(["int64(int64, int64)"], target="cuda")
def add_gpu(x, y):
    return x + y


add_gpu(1, 2)
