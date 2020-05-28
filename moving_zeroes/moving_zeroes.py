'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # First pass
    # zeroes = []
    # others = []
    # for num in arr:
    #     if num == 0:
    #         zeroes.append(num)
    #     else:
    #         others.append(num)

    
    # return others + zeroes
    # Reflecting+refining; aim is single pass using O(1) space
    last_index = len(arr) - 1
    for i in range(len(arr)):
        if last_index == i:
            return arr
        if arr[i] == 0:
            while arr[last_index] == 0:
                last_index -= 1
            arr[i], arr[last_index] = arr[last_index], arr[i]
            last_index -= 1
        print(i, arr, last_index)
    return arr

    
    


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")