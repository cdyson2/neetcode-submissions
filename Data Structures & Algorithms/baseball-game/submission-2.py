class Solution:
    def calPoints(self, operations: List[str]) -> int:
    
        record = []

        for i in range(len(operations)):
            if operations[i] == "1":
                record.append(1)
            elif operations[i] == "2":
                record.append(2)
            elif operations[i] == "+":
                plus = record[-1] + record[-2]
                record.append(plus)
            elif operations[i] == "C":
                record.pop()
            elif operations[i] == "5":
                record.append(5)
            elif operations[i] == "D":
                mult = record[-1] * 2
                record.append(mult)
            else:
                record.append(int(operations[i]))

        total = sum(record)
               

            

        return total