"""
Reverse bits of a given 32 bits unsigned integer.

Note:

Note that in some languages, such as Java, there is no unsigned integer type. In this case, 
both input and output will be given as a signed integer type. They should not affect your implementation, 
as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above, 
the input represents the signed integer -3 and the output represents the signed integer -1073741825.
 

Example 1:

Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
Example 2:

Input: n = 11111111111111111111111111111101
Output:   3221225471 (10111111111111111111111111111111)
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.
 

Constraints:

The input must be a binary string of length 32
"""

from soupsieve import SoupSieve


class Solution:
    def reverseBits(self, n: int) -> int:
        """
        :type n: int
        :rtype
        """
        #the input will be int and needs to be returned as an int 
        #int(x,2) converts back to an interger from bitwise 
        #need to consider that it can be int 32, which means there are 32 zeros to be fliped 

        if not int: return None

        x = bin(n).replace('0b', '')
        32 - len(x)
        zeros = '' 
        for _ in range(32-len(x)): 
            zeros += '0'
        x = zeros + x 
        y = x[::-1]
        
        return int(y,2)
        
        

print(Solution().reverseBits(8))


"""
x = 8 
x = bin(x).replace('0b', '')
print(x)
print(int(x,2))
"""