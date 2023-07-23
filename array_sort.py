def verify(array):
    end = True
    i = 0
    while i < len(array):
        if array[i] == array[-1]:
            end = end
        else:
            if array[i] > array[i+1]:
                end = False

        i += 1

    return end 

def sorting_lists(array):
    end = verify(array)
    while end == False:
        num_one = 0
        num_two = 0
        i = 0
        while i < len(array):
            if i != (len(array)-1):
                if (array[i] > array[i+1]):
                    num_one = array[i]
                    num_two = array[i+1]
                    array[i] = num_two
                    array[i+1] = num_one
            
            i += 1

        end = verify(array)

    return array

array = [1, 4, 5, 5, 3, 2]
array = [1, 2, 3, 4, 4, 6, 5, 5]
array = [4, 9, 0, 1]
print(sorting_lists(array))
