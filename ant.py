__author__ = 'Inigo'

from lxml import etree
import os
import numpy as np


class Ant():
    def __init__(self):
        self.tour_length = 0
        self.path = []
        self.current_node = ''
        self.visited = []

    def choose_node(self):
        for i in self.memory:
            self.memory[i][0] = self.heuristic(self.current_node)

class Graph():
    def __init__(self, fname):
        self.filename = fname
        with open(self.filename) as f:
            xml = etree.fromstring(f.read())  # Initialize the graph
        self.vertices = xml.find('graph').findall('vertex')
        self.n = len(self.vertices)
        self.distance_matrix = self.create_distance_matrix()
        self.pheromone_matrix = np.zeros((self.n, self.n))
        self.choice_info = np.zeros((self.n, self.n))

    def create_distance_matrix(self):
        m = np.zeros((self.n, self.n))
        for i in range(self.n):
            for j in range(self.n - 1):
                edge = int(self.get_target_vertex(i, j))
                m[i][edge] = self.get_cost(i, j)
        return m

    def get_edges(self, vertex):
        return self.vertices[vertex].findall('edge')

    def get_cost(self, vertex, edge):
        return self.get_edges(vertex)[edge].get('cost')

    def get_target_vertex(self, vertex, edge):
        return self.get_edges(vertex)[edge].text


def get_file():
    script_dir = os.path.dirname(__file__)  #<-- absolute dir the script is in
    rel_path = "problems/"
    abs_file_path = os.path.join(script_dir, rel_path)
    onlyfiles = [f for f in os.listdir(abs_file_path) if os.path.isfile(os.path.join(abs_file_path, f))]
    print "Introduce the number corresponding to the desired file to perform the algorithm on it :"
    count = 1
    for i in onlyfiles:
        print count, " --> ", i
        count += 1
    findex = raw_input("\nType the number and press 'Enter' : ")
    while True:
        try:
            findex = int(findex)
            if findex in range(1,count):
                break
            else:
                print findex, "is not in among the proposed numbers. Please introduce a number within the range ",
                print "[", 1, ", ", count -1, "]"
        except:
            print findex, "is not an integer. Please introduce an integer"
        findex = raw_input("\nType the number and press 'Enter' : ")
    f = onlyfiles[findex - 1]
    return os.path.join(abs_file_path, f)


if __name__ == "__main__":

    fname = get_file()
    g = Graph(fname)
