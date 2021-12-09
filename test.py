def find_outlier(integers):  
    def check_if_present(integers, even):
        answer = False
        if even:
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
                print("Recursing front", front, int(len(integers)/2))
                return recurse(front, even)
            else:
                print("Recursing back", back, int(len(integers)/2))
                return recurse(back, even)
            
    if sum(integers)%2 == 0:
        if len(integers)%2 == 1:
            print(True)
            return recurse(integers, True)
        else:
            print(False)
            return recurse(integers, False)
    else:
        if len(integers)%2 == 1:
            print(False)
            return recurse(integers, False)
        else:
            print(True)
            return recurse(integers, True)

#find_outlier([2, 4, 6, 8, 10, 3])
#find_outlier([2, 4, 0, 100, 4, 11, 2602, 36])
print(find_outlier([7381188, -5133920, 5543136, 7280902, -2172560, -7220844, 2692982, 5141562, 7203186, -4153848, -6965830, -7577934, -8033452, 751490, -6521840, 488584, -9326392, 8880590, -6871030, -766308, -7097028, -2168356, 7230086, -1690030, 4773470, 2167730, -2060709, 6491682, 7500658, -8571752, -9050634, -9788178, 3282124, -1613272, 985516, -9549312, 9035110, -6373168, 3525822, 506168, 3195698]))
print(len([7381188, -5133920, 5543136, 7280902, -2172560, -7220844, 2692982, 5141562, 7203186, -4153848, -6965830, -7577934, -8033452, 751490, -6521840, 488584, -9326392, 8880590, -6871030, -766308, -7097028, -2168356, 7230086, -1690030, 4773470, 2167730, -2060709, 6491682, 7500658, -8571752, -9050634, -9788178, 3282124, -1613272, 985516, -9549312, 9035110, -6373168, 3525822, 506168, 3195698]))
print(sum([7381188, -5133920, 5543136, 7280902, -2172560, -7220844, 2692982, 5141562, 7203186, -4153848, -6965830, -7577934, -8033452, 751490, -6521840, 488584, -9326392, 8880590, -6871030, -766308, -7097028, -2168356, 7230086, -1690030, 4773470, 2167730, -2060709, 6491682, 7500658, -8571752, -9050634, -9788178, 3282124, -1613272, 985516, -9549312, 9035110, -6373168, 3525822, 506168, 3195698]))
#print(160%2)