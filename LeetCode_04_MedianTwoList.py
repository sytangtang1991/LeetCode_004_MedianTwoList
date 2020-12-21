#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 18:33:45 2020

@author: yangsong
"""
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# Follow up: The overall run time complexity should be O(log (m+n)).
                                                      
# With Sort Function
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num = nums1 + nums2
        num.sort()
        
        if len(num)==1:
            return num[0]
        
        elif len(num)%2==1:
            return num[int((len(num)+1)/2-1)]
        
        else:
            a=num[int(len(num)/2-1)]
            b=num[int(len(num)/2)]
            return(float((a+b)/2))



#Withour Sort Function
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num = nums1 + nums2
        # Bubble Sort
        for i in range(1, len(num)):
            for j in range(0, len(num)-i):
                if num[j] > num[j+1]:
                    num[j], num[j + 1] = num[j + 1], num[j]
        
        
        if len(num)==1:
            return num[0]
        
        elif len(num)%2==1:
            return num[int((len(num)+1)/2-1)]
        
        else:
            a=num[int(len(num)/2-1)]
            b=num[int(len(num)/2)]
            return(float((a+b)/2))


