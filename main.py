from paises import PaisesAPI


api = PaisesAPI()


#nombres de los paises
nombres = [

    # jesus
    "japan",
    "egypt",
    "spain",
    "uruguay",
    "sweden",

    # juan
    "jordan",
    "uzbekistan",
    "argentina",
    "nepal"
]



paises = api.varios_paises(nombres)


print("PAÍSES ELEGIDOS")


for pais in paises:

    if pais is not None:

        print(pais)
        print()


print("COMPARACIÓN")

paises_validos = []

for pais in paises:

    if pais is not None:
        paises_validos.append(pais)



if len(paises_validos) > 0:
    primer_pais = paises_validos[0]
    otros_paises = paises_validos[1:]
    primer_pais.comparar(otros_paises)

else:
    print("No se pudieron cargar paises")