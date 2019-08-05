'''You are given an array of integers. You should find the sum of the integers with even indexes (0th, 2nd, 4th...). Then multiply this summed number and the final element of the array together. Don't forget that the first element has an index of 0.

For an empty array, the result will always be 0 (zero).

Input: A list of integers.

Output: The number as an integer.

Example:

checkio([0, 1, 2, 3, 4, 5]) == 30
checkio([1, 3, 5]) == 30
checkio([6]) == 36
checkio([]) == 0
1
2
3
4
How it is used: Indexes and slices are important elements of coding. This will come in handy down the road!'''

def checkio(nums):
    if len(nums) == 0 :
        return 0
    else:
        evans = nums[::2]
        last = nums[-1]

        return sum(evans) * last











checkio([-37,-36,-19,-99,29,20,3,-7,-64,84,36,62,26,-76,55,-24,84,49,-65,41])

