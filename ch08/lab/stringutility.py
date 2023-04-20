class StringUtility:
    def __init__(self, string) -> None:
        self.string = string
    def __str__(self) -> str:
        return self.string
    def vowels(self) -> str:
        return [i for i in self.string if i in 'aeiou']
    def bothEnds(self) -> str:
        pass
    def fixStart(self) -> str:
        pass
    def asciiSum(self) -> int:
        pass
    def cipher(self) -> str:
        pass
