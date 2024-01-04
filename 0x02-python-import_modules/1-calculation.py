#!/usr/bin/python3
a = 10
b = 5
calculator_1 = __import__("calculator_1")

result_add = calculator_1.add(a, b)
result_sub = calculator_1.sub(a, b)
result_mul = calculator_1.mul(a, b)
result_div = calculator_1.div(a, b)

print(result_add)
print(result_sub)
print(result_mul)
print(result_div)
