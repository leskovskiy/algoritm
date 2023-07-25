


def sort(numbers,i, n):
    i_left = i*2+1  #дочерний левый
    i_right = i*2+2 #дочерний правый
    i_max = i

    if i_left <= n and numbers[i_left] > numbers[i_max]:
        i_max = i_left
    
    if i_right <= n and numbers[i_right] > numbers[i_max]:
        i_max = i_right

    if i_max == i:
        return
    else:
        numbers[i_max], numbers[i] = numbers[i], numbers[i_max]  #если узел дочерний менялся рекурсией меняем
        sort(numbers,i_max,n)
    



def max_heap(numbers): #строим веришину
    i_midle = len(numbers)//2
    for i in reversed(range(0,i_midle +1)):
        sort(numbers,i,len(numbers)-1)


def start(numbers):
    max_heap(numbers) #строим пирамиду 
    for i in reversed(range(0,len(numbers))):  #переворачиваем элементы обратно в правильный порядок 
        numbers[0],numbers[i] = numbers[i],numbers[0]
        sort(numbers,0,i-1)



numbers = [2,6,5,34,20,45,6,2,8,6,5]
start(numbers)
print(numbers)
    
    