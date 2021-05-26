
def solution(genres, plays) :
    dict = {}
    a = list(map(lambda x, y: dict.update(x, y, enumerate(x))), genres, plays)

    return a


print(solution(['classic', 'pop', 'classic', 'classic', 'pop'],[500, 600, 150, 800, 2500]))