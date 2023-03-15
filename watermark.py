from PIL import Image

def znakWodny(nazwa):
    znakwodny = Image.open("znakwodny.png") #otwiera obraz
    tlo = Image.open(nazwa)
    tlo_wymiary = tlo.size
    znakwodny_wymiary = znakwodny.size  #wrzuca obrazka w prawy dolny rog
    y_poczatek = tlo_wymiary[0]-znakwodny_wymiary[0]
    x_poczatek = tlo_wymiary[1]-znakwodny_wymiary[1]
    znakwodny.putalpha(50)
    nowe = Image.new("RGB", tlo.size, (0,0,0,0))
    nowe.paste(tlo, (1,1))
    nowe.paste(znakwodny,(y_poczatek,x_poczatek),mask=znakwodny)
    nowe.save("nowe.jpg")   #zapisuje wodno oznaczony obraz



