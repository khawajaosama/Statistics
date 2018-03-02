#PERCENTILE

array=[22,44,55,66,34,88,11,44,5,96,34]

def percentile(arr_x,pth):

    length=len(array)*pth
    return sorted(arr_x)[length]

print(percentile(array,0.56))