def binary_search(list_of_elements, n):
    low = 0
    high = len(list_of_elements) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list_of_elements[mid]
        if guess < n:
            low = mid + 1
        elif guess > n:
            high = mid - 1
        else:
            return mid
    return None

test = [8,3,12,6,34,876,45]
print(binary_search(test, 6))  #zwróciło 3
print(binary_search(test, 17)) #zwróciło None
#TODO obsługa błędu
#print(binary_search(test, "o")) 