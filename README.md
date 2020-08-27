# beautifulworld

Package for visualizing data about cities

## Install beautifulworld
```
pip install beautifulworld
```

## Import beautifulworld
```
from beautifulworld.city import City, climateGraph
```

## Instantiate a city
```
istanbul = City('Istanbul')
print(istanbul)
```

## Draw climate graph of a city
```
istanbul = City('Istanbul')
istanbul.climate_graph()
```
## Draw climate graphs of multiple cities
```
istanbul, canberra, tokyo, sf, delhi, helsinki = City('Istanbul'), City('Canberra'), City('Tokyo'), City('San Francisco'), City('Delhi'), City('Helsinki')
climateGraph(istanbul, canberra, tokyo, sf, delhi, helsinki)

paris, lyon, nice = City('Paris'), City('Lyon'), City('Nice')
climateGraph(paris, lyon, nice)
```
