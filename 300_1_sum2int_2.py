def two_sum(nums, target):
    # tao dic chua number
    num_dict = {}
    for i, num in enumerate(nums):
        com = target - num

        #kiem tra com co trong num_dict ko
        #neu chua lam tiep
        #neu co ket thuc
        if com in num_dict: #so sanh value co giong ko
            #vd num_dict = {2:0, 7:1}
            return [num_dict[com], i] # [0, i=1]

        # neu ko co
        num_dict[num] = i
    # neu ko co tim thay
    return "ko tim thay"
# Example usage
nums = [2, 9, 7, 15]
target = 9
result = two_sum(nums, target)
print(result)
