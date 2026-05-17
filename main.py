from paises import CountryAPI

#Jesus 
api = CountryAPI()
japan   = api.by_name("japan")
egypt   = api.by_name("egypt")
spain   = api.by_name("spain")
uruguay = api.by_name("uruguay")
sweden  = api.by_name("sweden")


#JUAN
jordan      = api.by_name("jordan")
uzbekistan  = api.by_name("uzbekistan")
argentina   = api.by_name("argentina")
nepal       = api.by_name("nepal")


print("PAÍSES ELEGIDOS")
paises = [
    japan,
    egypt,
    spain,
    uruguay,
    sweden,
    jordan,
    uzbekistan,
    argentina,
    nepal
]

for pais in paises:
    print(pais)
    print()

print("COMPARACIÓN")

japan.comparar([
    egypt,
    spain,
    uruguay,
    sweden,
    jordan,
    uzbekistan,
    argentina,
    nepal
])