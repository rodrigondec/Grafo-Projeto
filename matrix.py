import pandas as pd
import numpy as np


class Matrix:
    def __init__(self):
        self.connections = None
        self.connections_normalize = None
        self.nodes = None
        self.type = None
        self.name = None
        self.weight = None

    def build(self, filename):
        flag_matrix = True
        self.connections = []
        with open(filename, 'r') as f:
            for line in f:
                if line.strip() and flag_matrix:
                    line = [int(x) for x in line.strip().strip('\n').split(',')]
                    self.connections.append(line)
                elif not line.strip() or not flag_matrix:
                    flag_matrix = False
                    label = line.split(':')
                    if label[0] == "nodes":
                        self.nodes = label[1].strip().strip('\n').split(',')
                    elif label[0] == "type":
                        self.type = label[1].strip().strip('\n')
                    elif label[0] == "name":
                        self.name = label[1].strip().strip('\n')
                    elif label[0] == "weight":
                        self.weight = float(label[1].strip().strip('\n'))
        self.connections = np.matrix(self.connections)

    def cost_normalize(self, v):
        max = float(self.connections.max())
        min = float(self.connections.min())
        return (max - v) / (max - min)

    def normalize(self):
        func = None
        if self.type == 'cost':
            func = self.cost_normalize
        else:
            pass

        func = np.vectorize(func)
        self.connections_normalize = func(self.connections)
        print(self.connections_normalize)

if __name__ == '__main__':
    m = Matrix()
    m.build('cost.txt')
    m.normalize()
