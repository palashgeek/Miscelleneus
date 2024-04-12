'''Given an integer array, find k'th smallest element in the array where k is a positive integer less than or equal to the length of array.

Input : [7, 4, 6, 3, 9, 1], k = 3
Output: 4
Explanation: The 3rd smallest array element is 4

Input : [1, 5, 2, 2, 2, 5, 5, 4], k = 5
Output: 4
Explanation: The 5th smallest array element is 4'''

def smallest(lst, k):
    if k>0&k<=len(lst):
        lst.sort()
        return lst[k-1]
        


if __name__ =='__main__':
    
    lst_len = int(input("Enter the length of list: "))
    lst = []
    for i in range(lst_len):
        a = int(input("Enter elements: "))
        lst.append(a)
    print(lst)
while True:
    k = int(input("Enter the value of k: "))
    if k > len(lst):
        print("Invalid input: k is greater than the length of the array.")
    else:
        result = smallest(lst, k)
        print("The smallest element is:", result)
        break
