import time

num_apto = input("n: ")

start1 = time.perf_counter()
num_apto = num_apto.zfill(3)
end1 = time.perf_counter()
t1 = end1 - start1

start2 = time.perf_counter()
num_apto = "00" + num_apto
end2 = time.perf_counter()
t2 = end2 - start2

print(f"zfill: {t1}")
print(f"puro: {t2}")
print(f"menor: {min(t1, t2)}")
