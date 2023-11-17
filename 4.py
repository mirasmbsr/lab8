import time
import math

def invoke_square_root(num, milliseconds):
    start_time = time.time()
    while (time.time() - start_time) * 1000 < milliseconds:
        pass  

    result = math.sqrt(num)
    return result

num = input()
milliseconds = input()

result = invoke_square_root(num, milliseconds)
print(f"Square root of {num} after {milliseconds} milliseconds is {result}")