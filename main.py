from paises import PaisesAPI

api = PaisesAPI()


# nombres de los paises
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

    print(pais)
    print()


print("COMPARACIÓN")


paises[0].comparar([
    paises[1],
    paises[2],
    paises[3],
    paises[4],
    paises[5],
    paises[6],
    paises[7],
    paises[8]
])