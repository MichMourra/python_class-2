'''
NAME
	ejercicio_porcentajeAminoacidos.py
    
VERSION
    1.0
    
AUTHOR
	Lot Hernandez	
    
DESCRIPTION
    Da el porcentaje de un cierto aminoacido de una secuencia dada
        
CATEGORY
	Genomic Sequence
    
USAGE
'''

import argparse

# parser = argparse.ArgumentParser(
#    description="Da el porcentaje de un aminoacido especifico de una secuencia dada")

# parser.add_argument("-sec", "--secuencia",
#                    help="Tu secuencia",
#                    required=True)
# parser.add_argument("-l", "--lista",
#                    help="Lista de aminoacidos de la que quieres saber el porcentaje",
#                    required=False)
#args = parser.parse_args()

# Se meten los argumentos a variables
#sec = args.secuencia
#amin = list(args.lista)


# Se checa que la longitud de secuencia no sea 0 y que solo se haya pedido el porcentaje de 1 aminoacido
# if(len(sec) == 0):
#    print("Error: No introdujiste una secuencia")
#    quit()


# Funcion con la que se saca el porcentaje
def porcentajeamin(sec, amin=['A', 'I', 'L', 'M', 'F', 'W', 'Y', 'V']):
    sum = 0
    for aminoacido in amin:
        sum += (sec.upper().count(aminoacido.upper()))
    porcentaje = round((sum / len(sec)) * 100)
    return(porcentaje)


assert porcentajeamin("MSRSLLLRFLLFLLLLPPLP", ["M"]) == 5
assert porcentajeamin("MSRSLLLRFLLFLLLLPPLP", ['M', 'L']) == 60
assert porcentajeamin("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L']) == 70
assert porcentajeamin("MSRSLLLRFLLFLLLLPPLP") == 65

#print(f"El porcentaje en tu secuencia es:\n{porcentajeamin(sec, amin)} %")