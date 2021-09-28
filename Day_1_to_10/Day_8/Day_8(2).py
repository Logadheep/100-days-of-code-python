# Error Handling with python
n = int(input())
for _ in range(n):
    try:
        a, b = map(int, input().split())
        d = a // b
        print(d)
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:",e)
