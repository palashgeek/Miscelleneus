'''.Given an array nums, write a function to move all zeroes to the end of it while maintaining the relative order of the non-zero elements.
Input: [0,1,0,3,12]
Output: [1, 3, 12, 0, 0]

Input: [1,7,0,0,8,0,10,12,0,4]
Output: [1, 7, 8, 10, 12, 4, 0, 0, 0, 0]'''

def movezeros(input_arr, n):
    count = 0
    for i in range(n):
        if input_arr[i] != 0:
            input_arr[count] = input_arr[i]
            count+=1


    while count <n:
        input_arr[count] = 0
        count += 1

input_arr = [0,1,0,3,12]
n = len(input_arr)
movezeros(input_arr, n)
print(input_arr)