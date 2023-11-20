class Solution(object):
    def merge(self, nums1, m, nums2, n):
        counter = m + n
        while n>0:
            if m>0 and nums1[m-1] > nums2[n-1]:
                nums1[counter-1] = nums1[m-1]
                m=m-1
            else:
                nums1[counter-1] = nums2[n-1]
                n=n-1
            counter=counter-1