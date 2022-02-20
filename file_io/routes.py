# searches through multiple csvs to create possible airlines routes 
# and writes results to json.

import csv
import json
from os import read, getcwd
from pathlib import Path
import helper
import itertools

here = Path('.')
def read_airlines(filename='airlines.dat'):
    airlines = {}  # Map from code -> name
    with open(filename) as f:
        reader = csv.reader(f)
        for line in reader:
            airlines[line[4]] = line[1]
    return airlines

airlines = read_airlines(here/'airlines.dat')
airlines['CBG']

def read_airports(filename='airports.dat'):
    # Return a map of code -> name
    airports = {}
    with open(filename) as f:
        reader = csv.reader(f)
        for line in reader:
            airports[line[4]] = line[1]
    return airports

airports = read_airports(here/'airports.dat')

def read_routes(filename='routes.dat'):
    # Return a map from source -> list of destinations
    routes = {}
    with open(filename) as f:
        reader = csv.reader(f)
        for line in reader:
            if not line[2] in routes:
                routes[line[2]] = []
            routes[line[2]].append(line[4])
    return routes

routes = read_routes(here/'routes.dat')

def find_paths(routes, source, dest, max_segments = 5):
    # Run a graph search algorithm to find paths from source to dest.
    if max_segments == 0: return {}
    paths = {}
    paths['1'] = [[source, d] for d in routes[source]]
    # go deeper
    i = 1
    while i+1 <= max_segments-1:  
        for path in paths[str(i)]:
            if not str(i+1) in paths:
                paths[str(i+1)] = [path+[new] for new in routes[path[i]]]
            else:
                paths[str(i+1)].extend([path+[new] for new in routes[path[i]]])
        i += 1
    
    for key in paths:
        paths[key] = [path for path in paths[key] if path[int(key)] == dest]
        paths[key] = list(k for k,_ in itertools.groupby(paths[key]))
    return paths

def rename_path(path, airports):
    return tuple(map(airports.get, path))


def main(source, dest, max_segments):
    airlines = read_airlines(here/'airlines.dat')
    airports = read_airports(here/'airports.dat')
    routes = read_routes(here/'routes.dat')

    paths = find_paths(routes, source, dest, max_segments=3)
    for path_seg in paths.keys():
        for i in range(len(paths[path_seg])):
            paths[path_seg][i] = rename_path(paths[path_seg][i], airports)
    output = paths  # Build a collection of output paths!
    with open(here/'routes.json', 'w') as outfile:
        json.dump(output, outfile, indent=2)
    # Don't forget to write the output to JSON!
    

if __name__ == '__main__':
    parser = helper.build_parser()
    args = parser.parse_args()
    main(args.source, args.dest, args.max_segments)
