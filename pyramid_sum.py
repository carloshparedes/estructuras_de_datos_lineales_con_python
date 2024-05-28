def pyramid_sum(lower, upper, margin=0):
    blank = '-' * margin
    print(blank, lower, upper)
    if lower > upper:
        print(blank, 0)
        return 0
    else:    
        result = lower + pyramid_sum(lower + 1, upper, margin + 4)
        print(blank, result)
        return result
    
print(pyramid_sum(1, 10))
    