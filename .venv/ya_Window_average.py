import time

set_1 = []
set_1_inp = []
time_in_sec = float
window_size = int
windows = np.array([1, 2, 3])
result = []

time_in_sec = float(input())
set_1 = list(map(int, input().split()))
window_size = int(input())

started_at = time.time()

i = 0
j = 1 + len(set_1) - window_size
#started_at = time.time()
result = [str(sum(set_1[i: i + window_size]) / window_size) for i in range (0, j)]
print(' '.join(result))

ended_at = time.time()
elapsed = round(ended_at - started_at, 10)
print(f"Function's work time is {elapsed} sec")
