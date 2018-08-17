from sentai.vectors.Vector3 import Vector3
from sentai.dynamics.DynamicBody import centre_of_mass, DynamicBody


class Cell:

    def __init__(self, x, y, z, length, width, height):
        """
        Class to represent a 3-dimensional region of space containing a given number of bodies.
        :param x: The x location of the bottom, close, left corner.
        :param y: The y location of the bottom, close, left corner.
        :param z: The z location of the bottom, close, left corner.
        :param length: The length (in the x-direction) of the Octree
        :param width: The width (in the y-direction) of the Octree.
        :param height: The height (in the z-direction) of the Octree.
        """
        self.x = x
        self.y = y
        self.z = z
        self.length = length
        self.width = width
        self.height = height
        self.bodies = []
        self.centre_of_mass = self.get_centre_of_mass()
        self.id = None

    def get_centre_of_mass(self):
        return centre_of_mass(self.bodies)

    def total_mass(self):
        tot_mass = 0
        if len(self.bodies) == 0:
            return 0
        for body in self.bodies:
            tot_mass += body.mass
        return tot_mass

    def as_dynamic_body(self):
        return DynamicBody(self.centre_of_mass(), Vector3(0, 0, 0), self.total_mass())

    def populate(self, body_list=None):
        self.bodies.extend(body_list)

    def add_body(self, body):
        self.bodies.append(body)

    def body_count(self):
        return len(self.bodies)

    def divide(self):
        """ Divide the cell into 8 sub-cellls and place the bodies into the appropriate cells."""
        new_length, new_width, new_height = self.length / 2, self.width / 2, self.height / 2
        low_close_left = Cell(self.x, self.y, self.z, new_length, new_width, new_height)
        low_close_right = Cell(self.x + new_length, self.y, self.z, new_length, new_width, new_height)
        low_far_left = Cell(self.x, self.y + new_width, self.z, new_length, new_width, new_height)
        low_far_right = Cell(self.x + new_length, self.y + new_width, self.z, new_length, new_width, new_height)

        high_close_left = Cell(self.x, self.y, self.z + new_height, new_length, new_width, new_height)
        high_close_right = Cell(self.x + new_length, self.y, self.z + new_height, new_length, new_width, new_height)
        high_far_left = Cell(self.x, self.y + new_width, self.z + new_height, new_length, new_width, new_height)
        high_far_right = Cell(self.x + new_length, self.y + new_width, self.z + new_height,
                              new_length, new_width, new_height)

        for body in self.bodies:
            x, y, z = body.position.x, body.position.y, body.position.z
            if z < self.z + new_height:
                if y < self.y + new_width:
                    if x < self.x + new_length:
                        low_close_left.add_body(body)
                        continue
                    else:
                        low_close_right.add_body(body)
                        continue
                elif x < self.x + new_length:
                    low_far_left.add_body(body)
                    continue
                else:
                    low_far_right.add_body(body)
                    continue
            else:
                if y < self.y + new_width:
                    if x < self.x + new_length:
                        high_close_left.add_body(body)
                        continue
                    else:
                        high_close_right.add_body(body)
                        continue
                elif x < self.x + new_length:
                    high_far_left.add_body(body)
                    continue
                else:
                    high_far_right.add_body(body)
                    continue

        sub_cells = [low_close_left, low_close_right, low_far_left, low_far_right,
                     high_close_left, high_close_right, high_far_left, high_far_right]

        return sub_cells


def generate_root_cell(bodies):
    min_x, max_x = bodies[0].position.x, bodies[0].position.x
    min_y, max_y = bodies[0].position.y, bodies[0].position.y
    min_z, max_z = bodies[0].position.z, bodies[0].position.z

    for ind in range(1, len(bodies)):
        if bodies[ind].position.x < min_x:
            min_x = bodies[ind].position.x
        elif bodies[ind].position.x > max_x:
            max_x = bodies[ind].position.x

        if bodies[ind].position.y < min_y:
            min_y = bodies[ind].position.y
        elif bodies[ind].position.y > max_y:
            max_y = bodies[ind].position.x

        if bodies[ind].position.z < min_z:
            min_z = bodies[ind].position.z
        elif bodies[ind].position.z > max_z:
            max_z = bodies[ind].position.z
    root_cell = Cell(min_x, min_y, min_z, abs(max_x - min_x), abs(max_y - min_y), abs(max_z - min_z))
    root_cell.bodies = bodies
    return root_cell


def split_cells(root_cell: Cell, max_contained_bodies=5):
    cells = []

    if root_cell.body_count() <= max_contained_bodies:
        cells.append(root_cell)
        return cells

    for cell in root_cell.divide():
        if cell.body_count() > max_contained_bodies:
            cells.extend(split_cells(cell, max_contained_bodies=max_contained_bodies))

    for cell in cells:
        if cell.body_count() == 0:
            cells.remove(cell)

    return cells
