def KtoF(Temperature):
    assert(Temperature >= 0),"Sangat dingin melebihi nol derajat"
    return((Temperature-273)*1.8)+32

print (KtoF(273))
print (int(KtoF(505.78)))
print (KtoF(-5))
