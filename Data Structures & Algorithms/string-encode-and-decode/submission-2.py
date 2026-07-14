class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        if the strs is empty, return an empty string
        declare an string1 empty
        traverse throug every str in strs:
            add the lenght of the curstr to string1
            add a ","
        add a # to the string1
        traverse trhough every str:
            add the curstr to string1
        return the string1
        """
        if strs == [""]:
            return ""
        
        string1 = ""
        for s in strs:
            string1 += str(len(s))
            string1 += ","
        
        string1 += "#"

        for s in strs:
            string1 += s
        
        return string1

    def decode(self, s: str) -> List[str]:
        """
        if the s is empty, return a list with and empty string
        declare an array1 (store the lengths)
        declare a left pointer as an int 0
        traverse while left is not an #:
            declare an string1 (store the number)
            traverse while left is not a ",":
                add the value that l is pointing in s
                add 1 to l
            convert string1 into int and appendit to array1
            add 1 to left
        add 1 to left
        declare an array2 (the response)
        traverse array1:
            append the string of s[left:curlenght + left] to array2
            add curlenght to left
        return the array2
        """
        if s == "":
            return [""]
        
        array1 = []
        left = 0
        while s[left] != "#":
            string1 = ""
            while s[left] != ",":
                string1 += s[left]
                left += 1
            array1.append(int(string1))
            left += 1
        
        left += 1
        array2 = []
        for length in array1:
            array2.append(s[left:left+length])
            left += length
        
        return array2


















