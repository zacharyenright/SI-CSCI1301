def fibonacci(n):
    a=0
    b=1
    c=0
    
    if(n<0):
        return -1
    if(n==0 or n==1):
        return n
    for x in range(n-1):
        c=a+b
        a=b
        b=c
    return c

if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')
