class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # Create difference array of indices
        # shiftFactor[i] = shift that we have to perform on s[i]
        shiftFactor = [0] * len(s)

        # Iterate through shifts array
        for l, r, factor in shifts:
            # As mentioned in the question we need to shift values by 1 from index l to index r includeing r
            # And here, factor signifies the backward or forward shif to be performed
            # So, we modify the conditions of difference array as such:
            #   shiftFactor[l] += 1 * ((-1) ** (factor==0)), shiftFactor[r+1] -= 1 * ((-1) ** (factor==0))
            # Here -ve values will signify we need to shift backwards
            shiftFactor[l] += 1 * ((-1) ** (factor==0))
            # To handle out of bound exception
            if r+1 < len(s):
                shiftFactor[r+1] -= 1 * ((-1) ** (factor==0))
        
        # Now do prefix sum on shiftFactor array to get shifts to be done on each indices
        for i in range(1, len(shiftFactor)):
            shiftFactor[i] += shiftFactor[i-1]
        
        # Now, shiftFactor[i] will represent shifts to be performed on s[i]
        # -ve values of shiftFactor[i] will signify backward shift, and forward shift otherwise

        # Strings are immutable, so convert to list
        s = list(s)

        # Traverse the list s
        for i in range(len(s)):
            # Do the shifting operation
            shift = (abs(shiftFactor[i]) % 26) * (-1 if shiftFactor[i] < 0 else 1)
            s[i] = chr(97 + ((ord(s[i])-97+shift+26)%26) )
        
        # Return the shifted list, by converting the list into string
        return "".join(s)