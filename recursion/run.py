import tasks

assert tasks.non_recursive_factorial(5) == tasks.recursive_factorial(5)
assert tasks.task_1_reversed_nonrecursive(32050) == tasks.task_1_reversed_recursive(32050)
assert tasks.recursive_pow(2) == 4
assert tasks.recursive_pow(5) == 25
#assert tasks.task_2_number_q_rec() ==