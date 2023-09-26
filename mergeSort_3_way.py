"""
Title: Three Way Merge Sort
Description:
Sorts an array of numbers in descending order in O(n log_3[n]) time.
Utilizes regular merge sort methods, but splits array into thirds
as apposed to halves.
Author: Owen Raftery
Date: 9/24/2023
"""


def mergeSort_3_way(alist):
    if len(alist) > 1:
        if len(alist) == 2:
            # account for array of size 2 special case
            left = [alist[0]]
            mid = [alist[1]]
            right = []
            mergeSort_3_way(left)
            mergeSort_3_way(mid)
        else:
            # find separation points
            first = len(alist)//3
            second = (len(alist)-first)//2+first

            # divide into three arrays
            left = alist[:first]
            mid = alist[first:second]
            right = alist[second:]
            mergeSort_3_way(left)
            mergeSort_3_way(mid)
            mergeSort_3_way(right)

        # --- sort the arrays ---
        # initialize counters for each array
        l = 0
        m = 0
        r = 0
        count = 0

        # loop for when left, mid, and right contain unsorted values
        while l < len(left) and m < len(mid) and r < len(right):
            if left[l] > mid[m]:
                if left[l] > right[r]:
                    alist[count] = left[l]
                    l += 1
                    count += 1
                else:
                    alist[count] = right[r]
                    r += 1
                    count += 1
            elif mid[m] > right[r]:
                alist[count] = mid[m]
                m += 1
                count += 1
            else:
                alist[count] = right[r]
                r += 1
                count += 1

        # loop for when only left and mid contain unsorted values
        while l < len(left) and m < len(mid):
            if left[l] > mid[m]:
                alist[count] = left[l]
                l += 1
                count += 1
            else:
                alist[count] = mid[m]
                m += 1
                count += 1

        # loop for when only mid and right contain unsorted values
        while m < len(mid) and r < len(right):
            if mid[m] > right[r]:
                alist[count] = mid[m]
                m += 1
                count += 1
            else:
                alist[count] = right[r]
                r += 1
                count += 1

        # loop for when only left and right contain unsorted values
        while l < len(left) and r < len(right):
            if left[l] > right[r]:
                alist[count] = left[l]
                l += 1
                count += 1
            else:
                alist[count] = right[r]
                r += 1
                count += 1

        # loop for when only left has unsorted values
        while l < len(left):
            alist[count] = left[l]
            l += 1
            count += 1

        # loop for when only mid has unsorted values
        while m < len(mid):
            alist[count] = mid[m]
            m += 1
            count += 1

        # loop for when only right has unsorted values
        while r < len(right):
            alist[count] = right[r]
            r += 1
            count += 1


# test method on below array
arr = [5, -10, 90, -6, 83, 23, 16, 4, -2, 73]
mergeSort_3_way(arr)
print(arr)
