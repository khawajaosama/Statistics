# Range , MEAN , VARIANCE , AND STANDARD DEVIATION

array=[1,2,3,4,5,6,7]

def mean(arr):
    return sum(arr)/len(arr)

def range(x):
    return max(x)-min(x)

def variance(x,checker):
    de_mean=mean(x)
    diff=[(x_i - de_mean)**2 for x_i in x ]
    if checker=='population':
        return sum(diff)/len(diff)
    else:
        return sum(diff)/len(diff)-1

def standard(x,checker):
    return (variance(x,checker))**0.5

print(variance(array,'sample'))

print(variance(array,'population'))

print(standard(array,'population'))