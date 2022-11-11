
def recursive_pow():
    """
    returns power of number, *use recursion
    :return:
    """

def recursive_factorial(n):
    """
    Calculates n! recursivly
    :param n:
    :return:
    """
    if n <=1:
        return 1
    """ n! = n*(n-1)!"""
    pass

def non_recursive_factorial(n):
    """

    :param n:
    :return:
    """
    pass

def task_1_reversed_recursive(n, final_n = 0):
    """

    :param n:
    :param final_n:
    :return:
    """
    if n == 0:
        return final_n
    return task_1_reversed_recursive(n//10, final_n*10+n%10)

def task_1_reversed_nonrecursive(n):
    """using string method"""
    return (int(str(n)[::-1]))

def task_2_number_q_rec():
    """

    :param n:
    :return:
    """

def taks_2_number_q_nonrec():
    pass