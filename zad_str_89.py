def ksiezyc(w,p,l):
   for x in range(1,l):
    w=w+p
    waga_ksiezyc=w*0.165
    print(waga_ksiezyc)


waga=raw_input("Podaj swoja wage na ziemi")
rosnie=raw_input("Podaj ile rosnie Twoja waga kazdego roku")
lat=raw_input("Podaj liczbe lat")

ksiezyc(int(waga), int(rosnie), int(lat))
