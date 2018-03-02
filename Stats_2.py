#Mode

from collections import Counter

friends=[1,2,3,3,2,5,4,7,6]

def mode(x):
    counts=Counter(x)
    max_values=max(counts.values())
    return [x_i for x_i,count in counts.items()
            if count==max_values]

print(mode(friends))