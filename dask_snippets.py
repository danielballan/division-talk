import dask.array as da

a = da.random.random((100_000, 100_000, 10))
b = (da.arcsin(a) + da.arccos(a)).sum(axis=(1, 2))
result = b.compute()

x = da.random.random(100_000, chunks=(10,))
x.sum().compute()  # Slow
y = x.rechunk((1000,))
y.sum().compute()