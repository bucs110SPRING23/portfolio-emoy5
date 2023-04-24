class StringUtility:
    
    def __init__(self, string) -> None:
        self.string = string
    
    def __str__(self) -> str:
        return self.string
    
    def vowels(self) -> str:
        count = 0
        for i in self.string:
            if i in 'aeiouAEIOU':
                count += 1
        if count < 5:
            return str(count)
        else:
            return str("many")
    
    def bothEnds(self) -> str:
        bothends = ""
        if len(self.string) <= 2:
            return str("")
        else:     
            for i in range(2):
               bothends+=self.string[i]
            bothends+=self.string[-2]
            bothends+=self.string[-1]
            return str(bothends)
    
    def fixStart(self) -> str:
        if len(self.string) <= 1:
            return self.string
        else:
            start = self.string[0]
            
            for i in range(1,len(self.string)):
                if self.string[i] == self.string[0]:
                    start += "*"
                else:
                    start += self.string[i]
            return start
    
    def asciiSum(self) -> int:
        count = 0
        for i in range(len(self.string)):
            count += ord(self.string[i])
        return int(count)
    
    def cipher(self) -> str:
        shift = len(self.string)
        encrypted = ""
        for i in range(len(self.string)):
            if self.string[i].isalpha():
                start = ord('A') if self.string[i].isupper() else ord('a')
                if self.string[i-1] == "" or " ":
                    new_pos = (ord(self.string[i]) - start + shift) % 26
                elif self.string[i].isalpha():
                    new_pos = (ord(self.string[i-1]) - start + shift) % 26
                encrypted += chr(start + new_pos)
            else:
                encrypted += " "
        return encrypted

                 
        
