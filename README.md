# beautifulworld

Package for visualizing data about cities

## Install beautifulworld
```
pip install beautifulworld
```

## Import beautifulworld
```python
from beautifulworld.city import City, climateGraph
```

## Instantiate a city
```python
istanbul = City('Istanbul')
print(istanbul)
Istanbul, Turkey
Time: 09 h 31 m 45
Date: jeudi 27 août 2020
Weather: Scattered clouds.
Temperature: 24 °C
Population: 10061000
Currency: <td>Turkish Lira (TRY)</td>
Coordinates: (41.105, 29.01)
```

## Draw climate graph of a city
```python
istanbul = City('Istanbul')
istanbul.climate_graph()
```
## Draw climate graphs of multiple cities
```python
istanbul, canberra, tokyo, sf, delhi, helsinki = City('Istanbul'), City('Canberra'), City('Tokyo'), City('San Francisco'), City('Delhi'), City('Helsinki')
climateGraph(istanbul, canberra, tokyo, sf, delhi, helsinki)

paris, lyon, nice = City('Paris'), City('Lyon'), City('Nice')
climateGraph(paris, lyon, nice)
```
