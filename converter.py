class ConvertToDecimal:
    def convert(self, base, getal):
        result = 0
    
        for index, getal_part in enumerate(reversed(getal)):
         
            getal_part = int(getal_part, base)
           
            if (getal_part != 0):
                result = result + (getal_part * (base ** index))

        return result