"""Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10
 and
, the first
 terms will be:
 1,2,3,5,8,13,21,34,55,89

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms."""

fibonacci_array = [0,1,1,2]
result = 0
first_number = 1
second_number = 2


sum = 0


while True:

    if result >= 4000000:
        break


    result = first_number + second_number
    fibonacci_array.append(result)
    first_number = second_number

    second_number = result



for number in fibonacci_array:
    if number % 2 == 0 and number < 4000000:
        sum += number


print(fibonacci_array)
print(sum)
