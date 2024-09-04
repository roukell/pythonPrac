# randomisation: python uses 'Mersenne Twister', a pseudorandom number generator (PRNG).
import random

# import own module
import modules.test_var as my_module

random_int = random.randint(1, 10)
print(random_int)

print(my_module.some_module_test_variable)

# generate floating point number in the range 0.0 <= X < 1.0
random_floating_num = random.random()
print(random_floating_num)

# generate floating point number N, such that a <= N <= b for a <= b
# random.uniform(a, b)
random_floating_num_with_range = random.uniform(1, 2)
print(random_floating_num_with_range)