def tip( bill,Tipperc):
    total=bill*(1+0.01*Tipperc)
    total=round(total,2)
    print("please pay",total)
tip(150,20)