def floor(number: int) -> int:
    """
    floor()

    Like round(), but always rounds down.
    """
    number_round = round(number)
    if number > 0:
        if number_round > number: number_round -= 1
    else:
        if number_round < number: number_round += 1
    return number_round
    
def floor_l(num: int) -> int:
    """
    floor_l()

    Like floor(), but written by [L_](https://github.com/hbgda).
    """
    is_neg = False
    if num < 0:
        num = -num
        is_neg = True
    number_round = round(num)
    if number_round > num:
        number_round -= 1
    return number_round if not is_neg else -number_round

def top(number: int) -> int:
    """
    top()

    Like round(), but always rounds up.
    """
    number_round = round(number)
    if number > 0:
        if number_round < number:
            number_round += 1
    else:
        if number_round > number:
            number_round -= 1
    return number_round

def sqr(number, times=2):
    ognum = number
    for x in range(times-1):
        number = number*ognum
    return number

