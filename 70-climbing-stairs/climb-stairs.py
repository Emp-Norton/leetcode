def climbStairs(n: int) -> int:
    """
    You are climbing a staircase. It takes n steps to reach the top.

    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

    :param n: Number of steps to reach the top
    :return:
    """
    solutions = [1,1]
    count = 0
    while count < n-1:
        solutions.append(solutions[count] + solutions[count+1])
        count+=1
    return solutions[-1]
