a = float(input("প্রথম সংখ্যা: "))
op = input("অপারেটর (+ - * /): ")
b = float(input("দ্বিতীয় সংখ্যা: "))

if op == "+":
    print("ফলাফল:", a + b)
elif op == "-":
    print("ফলাফল:", a - b)
elif op == "*":
    print("ফলাফল:", a * b)
elif op == "/":
    print("ফলাফল:", "শূন্য দিয়ে ভাগ করা যায় না" if b == 0 else a / b)
else:
    print("ভুল অপারেটর")
