import csv

#precision 2

with open('mpg.csv') as csvfile:
    mpg=list(csv.DictReader(csvfile))

#print(len(mpg))
#print(mpg[0].keys())
#print(sum(float(d['hwy']) for d in mpg) / len(mpg))
cylinders=set(d['cyl'] for d in mpg)
#print(cylinders)

CtyMpgByCyl = []

for c in cylinders:
    summpg = 0
    cyltypecount = 0
    for d in mpg:
        if d['cyl'] == c:
            summpg += float(d['cty'])
            cyltypecount += 1
    CtyMpgByCyl.append((c, summpg /cyltypecount))

CtyMpgByCyl.sort(key=lambda x: x[0])
print(CtyMpgByCyl)

vehicleClass=set(d['class'] for d in mpg)
print(vehicleClass)