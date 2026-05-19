from paises import PaisesAPI


api = PaisesAPI()

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

print("PAISES")


for pais in paises:

    print(pais)


print("COMPARACION")
paises[0].comparar(paises[1:])