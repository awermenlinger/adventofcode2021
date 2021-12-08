def check_if_present(integers, even):
    answer = False
    if len(integers)%2 == 1:
        if sum(integers)%2 == 0:
            answer =  True
        else:
            if sum(integers)%2 == 1:
                answer =  True
    else:
        if len(integers)%2 == 1:
            if sum(integers)%2 == 1:
                answer =  True
        else:
            if sum(integers)%2 == 0:
                answer = True
    return answer

def find_outlier(integers):  
    def recurse(integers, even):
        if len(integers) == 1:
            if even:
                if integers[0]%2 == 0:
                    return integers[0]
            else:
                if integers[0]%2 == 1:
                    return integers[0]
        else:
            front = integers[:int(len(integers)/2)]
            back = integers[int(len(integers)/2):]            
            
            if check_if_present(front, even):
                print("recursing front", front, even)
                return recurse(front, even)
            else:
                print("recursing back", back, even)
                return recurse(back, even)
            
    if sum(integers)%2 == 0:
        if len(integers)%2 == 1:
            return recurse(integers, True)
        else:
            return recurse(integers, False)
    else:
        if len(integers)%2 == 1:
            return recurse(integers, False)
        else:
            return recurse(integers, True)

#find_outlier([2, 4, 6, 8, 10, 3])
#find_outlier([2, 4, 0, 100, 4, 11, 2602, 36])
print(find_outlier([1, 1, 1, 1, 1, 44, 7, 7, 7, 7, 7, 7, 7, 7]))
#print(160%2)