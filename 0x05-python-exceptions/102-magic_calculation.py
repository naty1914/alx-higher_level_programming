
#!/usr/bin/python3
def magic_calculation(a, b):
    number_result = 0
    for x in range(1, 3):
        try:
            if x > a:
                raise Exception
            number_result += a ** b / x
        except Exception as e:
            print(e)
            number_result = b + a
            break
    return number_result
