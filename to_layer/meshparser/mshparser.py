import numpy as np
import os
# Functionality
# 1. Read File
# 2. Fill Container with Data about nodes elements and boundary conditions
# 2.1 Read components separate
# 2.2 Determine Boundary Elements
# 3. Write mesh file (and/or write msh file)
# 4. Parse Container data to TOBaseModel

from to_layer.meshparser.msh_boundary import MSHBoundary
from to_layer.meshparser.msh_element import MSHElement
from to_layer.utils.node import Node
from to_layer.tomodel.tousermodel import TOModelBase
from to_layer.tomodel.boundary_condition import BoundaryConditions
from to_layer.elements.element import Element

# TODO: Attention C2D4-Elements are only implemented now!!!
from to_layer.elements.C2D4Simple import ke

# Keys: MSH-Types; Values: MESH-Types
MAPTypes = {
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    15: 0
}


class MSHParser:
    original_file_name: str = ""
    dimension: int = 2
    # ----------------
    # Section Boundary Conditions
    ManualBoundaryConditions: bool = False
    BoundaryConditions: list = []
    boundary_number: int = 0
    boundary_start_index: int = 0
    boundary_tags: list = []
    boundary_elements: list = []
    boundary_indices: list = []
    boundary_elements_number: int = 0
    load_tags: list = []
    fix_tags: list = []
    # ----------------
    # ----------------
    # Section Nodes
    Nodes: dict = {}
    node_number: int = 0
    node_start_index: int = 0
    node_ids: list = []
    # ----------------
    # ----------------
    # Region Elements
    Elements: list = []
    element_number: int = 0
    element_start_index: int = 0

    # ----------------

    def __init__(self, file_name):

        __switch__ = 0

        self.original_file_name = file_name

        with open(self.original_file_name, 'r') as f:
            lines = f.readlines()
            # Get start indices for the different components in a msh file
            self.boundary_start_index, self.node_start_index, \
            self.element_start_index = self.__get_start_indices__(lines)
            # Read Boundary Conditions from file
            self.boundary_number, self.BoundaryConditions = self.__read_boundaries__(lines)
            # Read Nodes
            self.node_number, self.Nodes = self.__read_nodes__(lines)
            # Read Elements
            self.element_number, self.Elements = self.__read_elements__(lines)
        f.close()
        # Determine the boundary elements and remove them from Elements list
        self.__determine_boundary_elements__()
        self.__remove__none__fitting__elements()

    def __remove__none__fitting__elements(self):
        removals = []
        if self.dimension == 2:
            for i, e in enumerate(self.Elements):
                if e.etype in [1, 0]:
                    removals.append(i)
        elif self.dimension == 3:
            for i, e in enumerate(self.Elements):
                if e.etype in [0, 1, 2, 3]:
                    removals.append(i)
        else:
            print("Can not find the dimension of the model!")
        self.Elements = [_e for _i, _e in enumerate(self.Elements) if _i not in removals]
        self.element_number = len(self.Elements)

    def __determine_boundary_elements__(self):

        boundary_types = []

        if self.dimension == 2:
            boundary_types = [1, 15]
        elif self.dimension == 3:
            boundary_types = [2, 3]

        for i, e in enumerate(self.Elements):
            if any(_t in e.tags for _t in self.boundary_tags) and e.etype in boundary_types:
                self.boundary_elements.append(e)
                self.boundary_indices.append(i)
        self.Elements = [_e for _i, _e in enumerate(self.Elements) if _i not in self.boundary_indices]
        self.element_number = len(self.Elements)
        self.boundary_elements_number = len(self.boundary_elements)

        # remove 0 tag from boundary elements
        for i, e in enumerate(self.boundary_elements):
            if 0 in e.tags:
                e.tags = np.delete(e.tags, np.where(e.tags == 0), axis=0)

    def __read_elements__(self, lines):
        en = int(lines[self.element_start_index + 1])
        e_lines = lines[self.element_start_index + 2:self.element_start_index + 2 + en]
        e = []
        for e_line in e_lines:
            e_line = e_line.strip()
            arr_e = e_line.split(" ")
            eid = int(arr_e[0])
            etype = int(arr_e[1])
            if etype == 15:
                continue
            tag_number = int(arr_e[2])
            tags = np.array(arr_e[3:3 + tag_number], dtype=int)
            nodes = np.array(arr_e[3 + tag_number:], dtype=int)
            e.append(MSHElement(eid, etype, tag_number, tags, nodes))
        return en, e

    def __read_nodes__(self, lines):
        nn = int(lines[self.node_start_index + 1])
        n_lines = lines[self.node_start_index + 2:self.node_start_index + 2 + nn]
        n = {}

        for n_line in n_lines:
            arr_n = n_line.split(" ")
            n[int(arr_n[0])] = Node(int(arr_n[0]), float(arr_n[1]), float(arr_n[2]), float(arr_n[3]),
                                    index=n_lines.index(n_line))
            self.node_ids.append(int(arr_n[0]))

        return nn, n

    def __read_boundaries__(self, lines):
        bn = int(lines[self.boundary_start_index + 1])
        b_lines = lines[self.boundary_start_index + 2:self.boundary_start_index + 2 + bn]
        b = []
        for b_line in b_lines:
            arr_b = b_line.split(" ")
            b.append(MSHBoundary(int(arr_b[0]), int(arr_b[1]), arr_b[2].rstrip(r"\n")))
            self.boundary_tags.append(int(arr_b[1]))

        # determine load and fixation tag
        for _i, _b in enumerate(b):
            if "fix" in _b.name:
                self.fix_tags.append(_b.tag)
            elif "load" in _b.name:
                self.load_tags.append(_b.tag)

        return bn, b

    def __get_start_indices__(self, lines):
        bsi = nsi = esi = 0
        for line in lines:
            if "$PhysicalNames" in line:
                __switch__ = 1
                bsi = lines.index(line)
                continue
            elif "$Nodes" in line:
                __switch__ = 2
                nsi = lines.index(line)
                continue
            elif "$Elements" in line:
                __switch__ = 3
                esi = lines.index(line)
                continue
        return bsi, nsi, esi

    def write_mesh_file(self):
        output_file = self.original_file_name[:-3]
        output_file += 'mesh'

        with open(output_file, 'a') as f:
            f.truncate(0)
            f.write("MFEM mesh v1.0\n")
            f.write("\n")
            f.write("dimension\n")
            f.write(str(self.dimension) + "\n")
            f.write("\n")
            # write element section
            f.write("elements\n")
            f.write(str(self.element_number) + "\n")
            for i, e in enumerate(self.Elements):
                el_str = str(i + 1) + " " + str(e.etype)
                for j, n in enumerate(e.nodes):
                    el_str += " " + str(n - 1)
                f.write(el_str + "\n")
            # end element section
            f.write("\n")
            # write boundary section
            f.write("boundary\n")
            f.write(str(self.boundary_elements_number) + "\n")
            for i, e in enumerate(self.boundary_elements):
                el_str = str(e.tags[0]) + " " + str(e.etype)
                for j, n in enumerate(e.nodes):
                    el_str += " " + str(n - 1)
                f.write(el_str + "\n")
            # end boundary section
            f.write("\n")
            # write vertices section
            f.write("vertices\n")
            f.write(str(self.node_number) + "\n")
            f.write(str(self.dimension) + "\n")

            for i, n in enumerate(self.Nodes):
                n_str = ""
                for d in range(self.dimension):
                    n_str += str(n.n_vec[d]) + " "
                f.write(n_str.strip() + "\n")
            # end vertices section
        f.close()

    def __get_boundary_conditions__(self):
        loads = {}
        loads2 = {}
        fix = []
        for i, e in enumerate(self.boundary_elements):
            # fixation conditions
            if any(_t in e.tags for _t in self.fix_tags):
                for n in e.nodes:
                    if n not in fix:
                        fix.append(n)

            elif any(_t in e.tags for _t in self.load_tags):
                for n in e.nodes:
                    loads2[n] = np.array([0, -1])
                    _it = 0
                    for _i, d in enumerate(list(range(self.dimension * (n - 1), self.dimension * n))):
                        _it += 1
                        if _it == 2:
                            loads[d + 1] = -1
                        else:
                            loads[d + 1] = 0
        fix.sort()

        automatic_bc = BoundaryConditions(loads2, fix, self.node_ids)
        return automatic_bc

    def get_base_model(self, _bc: BoundaryConditions = None):

        to_elements = {}
        # Initialization of Elements!!!
        for i, e in enumerate(self.Elements):
            # TODO: ATTENTION Element is always the simplest C2D4 yet
            to_elements[e.eid] = Element(e.eid, {n_id: self.Nodes[n_id] for n_id in e.nodes.tolist()},
                                         ke(1, 0.3),
                                         dense_x=0.44)

        if _bc is not None:
            self.ManualBoundaryConditions = True
            bc = _bc
        else:
            self.ManualBoundaryConditions = False
            bc = self.__get_boundary_conditions__()

        m = TOModelBase(self.Nodes, to_elements, bc, 2)

        return m
