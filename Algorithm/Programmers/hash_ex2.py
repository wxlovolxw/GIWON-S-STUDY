
def solution(phone_book):
    phone_book.sort()
    for i in phone_book:
        if list(map(lambda x: list(str(x))[:len(list(str(i)))], phone_book)).count(list(str(i))) >= 2:
            return False
        else: return True


print(solution([123, 12,567,88]))