import numpy as np
x = np.array(['heLLo woRLd', 'Say sOmething'], dtype=str)

Capitalized  = np.char.capitalize(x)
lowered = np.char.lower(x)
uppered = np.char.upper(x)
Swapcased = np.char.swapcase(x)
titlecased = np.char.title(x)

print("Capitalized:", Capitalized)
print("Lowered:", lowered)
print("Uppered:", uppered)
print("Swapcased:", Swapcased)
print("Titlecased:", titlecased)





