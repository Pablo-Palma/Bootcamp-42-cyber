import time

def ft_progress(lst):
    total = len(lst)
    start_time = time.time()
    prev_time = start_time

    for i, elem in enumerate(lst):
        curr_time = time.time()
        elapsed_time = curr_time - start_time
        delta_time = curr_time - prev_time
        eta = elapsed_time * (total - i) / (i + 1)
        prev_time = curr_time

        if i == 0:
            pass
        else:
            print(f"ETA: {eta:.2f}s [{int((i + 1) * 100 / total)}%][=>{' '*(18-int((i + 1) * 20 / total))}] {i+1}/{total} | elapsed time {elapsed_time:.2f}", end='\r')
            print(f"ETA: {eta:.2f}s [{int((i + 1) * 100 / total)}%][{'='*int((i + 1) * 20 / total)}>{' '*(19-int((i + 1) * 20 / total))}] {i+1}/{total} | elapsed time {elapsed_time:.2f}s", end='\r')

        yield elem

    print(f"ETA: {eta:.2f} [100%][{'='*20}] {total}/{total} | elapsed time {elapsed_time:.2f}")

listy = range(3333)
ret = sum(listy)
for elem in ft_progress(listy):
    time.sleep(0.005)
print()
print(ret)

