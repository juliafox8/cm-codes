def cumulative_product_helper(nums, subtotal):
    #base case
    if nums == []:
        return []
    #recursive
    return [nums[0] * subtotal] + cumulative_product_helper(nums[1:], subtotal * nums[0])




def cumulative_product(nums):
    return cumulative_product_helper(nums, 1)
