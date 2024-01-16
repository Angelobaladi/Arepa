print("Bienvenido, hoy haremos unas ricas arepas!")
print("Introduzca las cantidades de cada uno de los ingredientes.")

agua = input("Cuantas tazas de agua son?\n ")
harina_pan = input("Cuantas tazas de harina pan son?\n")
sal = input("Cuantas cucharaditas de sal son?\n")
aceite = input("Cuantas cucharadas de aceite son?\n")

agua = float(agua)
harina_pan = float(harina_pan)
sal = float(sal)
aceite = float(aceite)

cantidad_de_tzs_de_sal = (sal/3)/16

cantidad_de_tzs_de_aceite = aceite/16

print("Son: ", agua, "tazas de agua")
print("Son: ", harina_pan, "tazas de harina PAN")
print("Son: ", cantidad_de_tzs_de_sal, "tazas de sal")
print("Son: ", cantidad_de_tzs_de_aceite, "tazas de aceite")

bol= agua + harina_pan + cantidad_de_tzs_de_sal

print("Se mezcla hasta que quede uniforme y de esa forma se obtiene", bol, "de masa para hacer arepas")
print("Se le da a la mezcla forma de disco")
print("Se coloca", cantidad_de_tzs_de_aceite, "tazas de aceite en un budare hasta dorar")
print("Se voltea y repite")
print("Se sirve en un plato")