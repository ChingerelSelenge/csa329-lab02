# 1-ээс 100 хүртэлх бүх тооны нийлбэр
sum1 = 0
for number in range(1, 101):
    sum1 += number

# 1-ээс 100 хүртэлх сондгой тооны нийлбэр
sum2 = 0
number = 1
while number < 101:
    if number % 2 != 0:
        sum2 += number
    number += 1

# 1-ээс 100 хүртэлх тэгш тооны нийлбэр
sum3 = 0
for number in range(1, 101):
    if number % 2 == 0:
        sum3 += number

print("Бүх тооны нийлбэр:", sum1)
print("Сондгой тооны нийлбэр:", sum2)
print("Тэгш тооны нийлбэр:", sum3)