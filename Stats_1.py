# Mean Function and MEDIAN FUNCTION

array_1=[2,5,3,6,4,1,9,7,8]
array_2=[2,5,3,6,4,1,9,7,8,10]


def mean(arr):
    return sum(arr)/len(arr)

print(mean(array_1))

def median(arr):
    arr.sort()
    length=len(arr)
    if length%2==0:
        length_1=length//2
        return '{} and {} are the median of the given array'.format(arr[length_1-1],arr[length_1])
    else:
        return '{} is the median of the given array'.format(arr[length//2])

print(median(array_2))