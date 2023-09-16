def hcf(a,b):
    first = a
    second = b
    if second > first:
        a = second
        b = first
    else:
        a = first
        b = second
    while True:
        if a%b == 0:
            return(b)
        x = a%b
        a = b
        b = x

def lcm(a,b):
    first = a
    second = b
    if second > first:
        a = second
        b = first
    else:
        a = first
        b = second
    while True:
        if a%b == 0:
            return(first*second//b)
        x = a%b
        a = b
        b = x
