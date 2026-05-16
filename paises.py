import requests
from requests.exceptions import (HTTPError,ConnectionError,Timeout)

BASE = "https://restcountries.com/v3.1"


class Country:

    def __init__(self, data: dict):
        self.name = data["name"]["common"]
        self.capital = data.get("capital", ["—"])[0]
        self.population = data.get("population", 0)
        self.area = data.get("area", 0)
        self.region = data.get("region", "—")

    def density(self):
        if self.area == 0:
            return 0
        return self.population / self.area

    def __str__(self):
        return (
            f"{self.name} ({self.region})\n"
            f"  Capital: {self.capital}\n"
            f"  Población: {self.population:,}\n"
            f"  Área: {self.area:,.0f} km²\n"
            f"  Densidad: {self.density():.2f} hab/km²"
        )

    def comparar(self, otros: list):

        todos = [self] + otros

        print("\n")
        print(f"{'País':15} {'Población':15} {'Área':12} {'Densidad'}")
        print("-" * 65)

        for p in todos:
            print(
                f"{p.name:15} "
                f"{p.population:15,} "
                f"{p.area:12,.0f} "
                f"{p.density():10.2f} hab/km²"
            )

        print("-" * 65)

        mayor_poblacion = max(todos, key=lambda p: p.population)
        mayor_area = max(todos, key=lambda p: p.area)
        mayor_densidad = max(todos, key=lambda p: p.density())

        print(f"Mayor población : {mayor_poblacion.name}")
        print(f"Mayor área      : {mayor_area.name}")
        print(f"Mayor densidad  : {mayor_densidad.name}")


# =========================
# CLASE COUNTRY API
# =========================
class CountryAPI:

    def by_name(self, name):

        url = f"{BASE}/name/{name}"

        try:
            r = requests.get(url, timeout=5)
            r.raise_for_status()

            data = r.json()[0]

            return Country(data)

        except Timeout:
            print("⏱ La API tardó demasiado")

        except ConnectionError:
            print("📡 Sin conexión a internet")

        except HTTPError as e:
            print(f"❌ Error {e.response.status_code}: país no encontrado")

        return None

    def by_region(self, region):

        url = f"{BASE}/region/{region}"

        try:
            r = requests.get(url, timeout=5)
            r.raise_for_status()

            data = r.json()

            return [Country(pais) for pais in data]

        except Timeout:
            print("⏱ La API tardó demasiado")

        except ConnectionError:
            print("📡 Sin conexión a internet")

        except HTTPError as e:
            print(f"❌ Error {e.response.status_code}")

        return []


# =========================
# MAIN
# =========================

api = CountryAPI()

# =====================================
# JESUS
# J = Japan
# E = Egypt
# S = Spain
# U = Uruguay
# S = Sweden (segunda S, país distinto)
# =====================================

japan   = api.by_name("japan")
egypt   = api.by_name("egypt")
spain   = api.by_name("spain")
uruguay = api.by_name("uruguay")
sweden  = api.by_name("sweden")

print("\n===== PAÍSES DE JESUS =====\n")

for pais in [japan, egypt, spain, uruguay, sweden]:
    print(pais)
    print()


# =====================================
# JUAN
# J = Jordan
# U = Uzbekistan
# A = Argentina
# N = Nepal
# =====================================

jordan      = api.by_name("jordan")
uzbekistan  = api.by_name("uzbekistan")
argentina   = api.by_name("argentina")
nepal       = api.by_name("nepal")

print("\n===== PAÍSES DE JUAN =====\n")

for pais in [jordan, uzbekistan, argentina, nepal]:
    print(pais)
    print()


# =========================
# COMPARACIÓN
# =========================

print("\n===== COMPARACIÓN =====")

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