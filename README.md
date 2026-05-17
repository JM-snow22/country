<<<<<<< HEAD
Proyecto API Countries

Proyecto realizado en Python usando Programación Orientada a Objetos y la API REST Countries.

Integrantes

- Jesus
- Juan

Países elegidos

Jesus

- J → Japan
- E → Egypt
- S → Spain
- U → Uruguay
- S → Sweden

Juan

- J → Jordan
- U → Uzbekistan
- A → Argentina
- N → Nepal

Archivos

- `paises.py` → clases Country y CountryAPI
- `main.py` → programa principal
- `requirements.txt` → dependencias

API utilizada

REST Countries API
=======
# Parcial — POO + APIs REST con Python
**Clase 08 · Programación Avanzada**
 
## Integrantes
| Nombre | Iniciales | Países asignados |
|--------|-----------|-----------------|
| Juan | J, U, A, N |jordan, uzbekistan, argentina, nepal   |
| Jesus | J, E, S, U, S | japan, egypt, spain, uruguay, sweden |
 
> La letra J se repite entre los dos nombres → Juan usa Jordan, Jesus usa Japan.  
> La letra U se repite → Juan usa uzbekistan, Jesus usa Uruguay.  
> La letra S se repite dos veces en Jesus → spain y Sweden.
 
## Archivos
```
country/
├── main.py    # Programa principal
├── paises.py  # Clases Country y CountryAPI
└── README.md    # Este archivo que dice que contiene el proyecto
```
 
## Cómo correr el proyecto
 
### 1. Instalar dependencias
```bash
pip install requests
```
 
### 2. Ejecutar
```bash
python main.py
```
 
## Descripción de las clases
 
### `Country`
Modela un país como objeto a partir del dict JSON que devuelve la API.
 
| Método | Descripción |
|--------|-------------|
| `__init__(data)` | Extrae nombre, capital, región, población y área |
| `__str__()` | Retorna cadena legible con todos los datos |
| `density()` | Calcula y retorna habitantes por km² |
| `comparar(otros)` | Imprime tabla comparativa e indica ganadores |
 
### `CountryAPI`
Encapsula todas las peticiones a [restcountries.com](https://restcountries.com).
 
| Método | Descripción |
|--------|-------------|
| `by_name(name)` | Busca país por nombre → retorna `Country` |
| `by_region(region)` | Busca por región → retorna `list[Country]` |
 
El manejo de errores (`Timeout`, `ConnectionError`, `HTTPError`) vive dentro de esta clase — el `main` no importa `requests`.
 
>>>>>>> 619068f9acc4d37311f330a1cf4e577fc82fab6a
