def solution(clothes):
    a = list(map(lambda x: [1, x[1]], clothes))
    b = list(set(list(map(lambda x: (x[1], a.count(x)), a))))

    answer = 1
    for num in b :
        answer = answer * (num[1]+1)

    return (answer-1)
print(solution([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]))