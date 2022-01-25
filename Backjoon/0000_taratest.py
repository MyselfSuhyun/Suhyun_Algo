def sum_of_repeat_number(numbers):
    result = 0

    for i in numbers:  # numbers리스트를 돈다.
        print(numbers)
        print(i)
        if numbers.count(i) >= 2:  # 만약 해당 원소의 개수가 2개 이상이라면
            for _ in range(numbers.count(i)):  # 해당 개수 만큼 반복문을 돌아
                numbers.remove(i)  # 계속 삭제 해준다.

    for j in numbers:  # 그 후 다시 반복문을 돌아
        result += j  # 값을 더해준다.

    return result

print(sum_of_repeat_number([4, 4,4,4,4, 7,8, 7,10])) #25 출력