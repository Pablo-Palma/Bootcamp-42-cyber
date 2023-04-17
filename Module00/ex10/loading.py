import time

def ft_progress(lst):
    total = abs(len(lst))
    start_time = time.time()
    prev_time = start_time

    for i, elem in enumerate(lst):
        curr_time = time.time()
        elapsed_time = curr_time - start_time
        delta_time = curr_time - prev_time

        if total == 1:
            print(f"ETA: 0.00s [100%][{'='*20}] 1/1 | elapsed time {elapsed_time:.2f}s", end='\r')
        else:
            eta = elapsed_time * (total - i) / (i + 1)
            print(f"ETA: {eta:3.2f}s [{int((i + 1) * 100 / total):3}%][{'='*int((i + 1) * 20 / total)}>{' '*(19-int((i + 1) * 20 / total))}] {i+1:4}/{total:4} | elapsed time {elapsed_time:2.2f}s", end='\r')
        prev_time = curr_time

        yield elem

    if total != 1:
        print(f"ETA: {eta:3.2f} [100%][{'='*20}] {total:5}/{total:5} | elapsed time {elapsed_time:3.2f}")

listy = range(3333)
ret = sum(listy)
for elem in ft_progress(listy):
    time.sleep(0.005)
print()
print(ret)

