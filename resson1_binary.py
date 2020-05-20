# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    
    # compute binary num
    rest = []
    
    while True:
        rest.append(N%2)
        N = N//2
        
        if N//2 == 1:
            rest.append(1)
            break
    
    # compute binary gap
    index_of_1 = [i for i, binary in enumerate(rest) if binary == 1]
    if len(index_of_1) == 1:
        return 0
    else :
        binary_gap = []
        
        for i in range(len(index_of_1)-1):
            binary_gap.append(index_of_1[i+1] - index_of_1[i])
        
        if max(binary_gap) == 1:
            return 0
        else:
            return max(binary_gap)