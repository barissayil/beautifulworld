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
