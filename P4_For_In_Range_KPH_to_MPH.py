print("------------------")
print("KPH \t MPH")
print("------------------")

for KPH in range(60,131,10):

    MPH = KPH * 0.6214

    print(KPH,"\t",format(MPH,"0.0f"))
