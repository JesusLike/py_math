'''
Operations with vectors
'''

class Vector2:
    '''
    Two-dimensional vector
    '''
    def __init__(self, x, y):
        self.coord = (x, y)

    def x(self):
        '''
        Return X-axis coordinate
        '''
        return self.coord[0]

    def y(self):
        '''
        Return Y-axis coordinate
        '''
        return self.coord[1]

    def add(self, other):
        '''
        Addition of two 2D vectors
        '''
        return Vector2(self.x() + other.x(), self.y() + other.y())
