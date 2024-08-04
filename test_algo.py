import string
import random
import time

searched = ["D", "J", "P", "N"]
chars = string.ascii_letters + string.digits
generated_list = ""
start_time = time.perf_counter()

for _ in range(random.randint(10000000, 999999999)):
    generated_list += random.choice(chars)

searched_found = {"D": 0, "J": 0, "P": 0, "N": 0}

for c in generated_list:
    if c in searched:
        searched_found[c] += 1

print(searched_found, " | Took: "+str(time.perf_counter() - start_time)+"s")
