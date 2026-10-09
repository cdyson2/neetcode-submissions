class Solution:
    def calPoints(self, operations: List[str]) -> int:
    
        total = []

        for i in range(len(operations)):
            if operations[i] == "+":
                n = total[-2] + total[-1]
                total.append(n)
            elif operations[i] == "C":
                total.pop()
            elif operations[i] == "D":
                m = total[-1] * 2
                total.append(m)
            else:
                total.append(int(operations[i]))
        
        return sum(total)