import functools
import time

def dec(func):
    @functools.wraps(func)
    def inner(*args,**kwrgs):
        start_zeit=time.perf_counter()
        value=func(*args,**kwrgs)
        ende_zeit=time.perf_counter()
        durchführungszeit=ende_zeit-start_zeit
        print(f"fertige Zeit:{func.__name__} in {durchführungszeit:.4}secunde")
        return value
    return inner

@dec
def verbrauchteZeit(nummer):
    for _ in range(nummer):
        sum([i**2 for i in range(1000)])

verbrauchteZeit(1)