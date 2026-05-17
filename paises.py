import requests
from requests.exceptions import (HTTPError,ConnectionError,Timeout)

BASE = "https://restcountries.com/v3.1"


class Pais:
    def __init__(self, data):

        self.name = data["name"]["common"]
        self.capital = data.get("capital", ["No tiene"])[0]
        self.population = data.get("population", 0)
        self.area = data.get("area", 0)
        self.region = data.get("region", "No tiene")

    def density(self):
        densidad = self.population / self.area
        return densidad

    def __str__(self):

        texto = ""
        texto += f"\nPais: {self.name}\n"
        texto += f"Capital: {self.capital}\n"
        texto += f"Poblacion: {self.population:,}\n"
        texto += f"Area: {self.area:,} km2\n"
        texto += f"Region: {self.region}\n"
        texto += f"Densidad: {self.density():.2f} hab/km2\n"

        return texto

    def comparar(self, otros):

        todos = [self] + otros

        print("\n")
        print("Comparacion de paises")
        print("-" * 60)

        print(f"{'Pais':15} {'Poblacion':15} {'Area':15} {'Densidad'}")

        print("-" * 60)

        for pais in todos:

            print(
                f"{pais.name:15} "
                f"{pais.population:<15,} "
                f"{pais.area:<15,.0f} "
                f"{pais.density():.2f}"
            )

        print("-" * 60)
        mas_poblacion = max(todos, key=lambda x: x.population)
        mas_area = max(todos, key=lambda x: x.area)
        mas_densidad = max(todos, key=lambda x: x.density())
        print(f"Mayor poblacion: {mas_poblacion.name}")
        print(f"Mayor area: {mas_area.name}")
        print(f"Mayor densidad: {mas_densidad.name}")


class PaisesAPI:
    def by_name(self, name):
        url = f"{BASE}/name/{name}"
        try:
            r = requests.get(url, timeout=5)
            r.raise_for_status()
            data = r.json()[0]
            pais = Pais(data)
            return pais
        except Timeout:
            print("La API tardo mucho")
        except ConnectionError:
            print("No hay internet")
        except HTTPError as e:
            print(f"Error: {e.response.status_code}")
        return None