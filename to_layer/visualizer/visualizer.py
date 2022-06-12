import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

from to_layer.tomodel.tousermodel import TOModelBase
from to_layer.tomodel.to_reformulated_user_model import TOReformulatedUserModel
from to_layer.elements.element import Element
from to_layer.tomodel.subdomain import SubDomain


class Visualizer:
    # matplotlib properties
    fig = None
    ax = None

    # model properties
    dimension = 2
    nodes = {}
    fixed_nodes = []
    arr_nodes = []
    elements = {}

    # helpers
    __x_bound__ = []
    __y_bound__ = []
    __z_bound__ = []

    labels = None
    handles = None

    def __init__(self, ori_model: TOModelBase):
        # matplotlib section in init

        # node section in init
        self.nodes = ori_model.Nodes
        self.arr_nodes = self.__get_node_array__()
        self.__x_bound__ = [
            self.arr_nodes[:, 0].min(),
            self.arr_nodes[:, 0].max()
        ]
        self.__y_bound__ = [
            self.arr_nodes[:, 1].min(),
            self.arr_nodes[:, 1].max()
        ]

        self.fixed_nodes = ori_model.FEModel.boundary_conditions.fixed_nodes
        self.forced_nodes = ori_model.FEModel.boundary_conditions.outer_forces

        # element section in init
        self.elements = ori_model.elements

    def __store_original__(self, __ax):
        # draw nodes
        __ax.scatter(self.arr_nodes[:, 0], self.arr_nodes[:, 1], c='grey', s=90)
        # annotate nodes
        for _nnumber in range(1, len(self.arr_nodes)+1):
            __ax.annotate(str(_nnumber), (self.arr_nodes[_nnumber-1][0] + 0.1,
                          self.arr_nodes[_nnumber-1][1] + 0.1),
                          fontsize=15, ha='center', va='center')
        # draw elements
        for _it, _el in self.elements.items():
            self.__draw_element__(__ax, _el, _it)

        # draw boundaries
        self.__draw_fixations__(__ax)
        self.__draw_loads__(__ax)

    def __get_node_array__(self):
        al = []
        for _n_id, _n in self.nodes.items():
            al.append(_n.n_vec.tolist())
        return np.array(al)

    def __draw_element__(self, __ax, el: Element, el_id: int, displacement=(0, 0, 0)):
        # draw lines
        # lines are possible permutations of node indices
        arr_n = self.arr_nodes[np.array(list(el.Nodes.keys()))[:] - 1]
        arr_n[:] += np.array(displacement)
        for i in range(len(arr_n)):
            p1 = arr_n[i - 1]
            p2 = arr_n[i]
            __ax.plot([p1[0], p2[0]], [p1[1], p2[1]], c='grey')

        # write element number
        centroid = np.array(  # centroid of the element
            [
                sum(arr_n[:, 0]) / len(arr_n),
                sum(arr_n[:, 1]) / len(arr_n)
            ]
        )
        __ax.annotate(str(el_id), (centroid[0], centroid[1]), fontsize=20, ha='center', va='center')

    def __draw_fixations__(self, __ax, displacement=(0, 0, 0)):

        arr_fn = self.arr_nodes[np.array(self.fixed_nodes)[:] - 1]
        arr_fn[:] += np.array(displacement)

        __ax.scatter(arr_fn[:, 0], arr_fn[:, 1], c='green', marker='>', s=200, zorder=10, label='Fixations')

    def __draw_loads__(self, __ax):
        arr = None
        for _n, vec in self.forced_nodes.items():
            arr = plt.arrow(self.arr_nodes[_n - 1][0], self.arr_nodes[_n - 1][1], vec[0] * 0.5, vec[1] * 0.5,
                            edgecolor='navy', zorder=10, length_includes_head=True,
                            head_width=.1)
            arr.set_facecolor('navy')
            __ax.add_patch(arr)

        self.handles, self.labels = __ax.get_legend_handles_labels()
        self.handles.append(arr)
        self.labels.append("Loads")

    def __display_state_(self, _fig):

        plt.legend(handles=self.handles, labels=self.labels,
                   bbox_to_anchor=(0.5, -0.01), loc='lower center', ncol=2,
                   markerscale=1)

        plt.axis('equal')
        plt.axis('off')
        plt.tight_layout()

        # _fig.show()
        plt.show()

    def __draw_cell__(self, c: SubDomain, __ax, displacement: tuple, cutted_nodes: list):
        cn = self.arr_nodes[np.array(c.Nodes)[:] - 1]
        cn[:] += np.array(displacement)

        self.handles, self.labels = __ax.get_legend_handles_labels()
        __ax.scatter(cn[:, 0], cn[:, 1], c='grey')

        # annotate cell's nodes
        for _it, _n in enumerate(cn.tolist()):
            _nn = c.Nodes[_it]
            _coords = np.array(_n) + np.array(displacement)
            __ax.annotate(str(_nn), (_n[0]+0.1, _n[1]+0.1),
                          ha='center', va='center', fontsize=15)

        for e_id, el in c.Elements.items():
            self.__draw_element__(__ax, el, e_id, displacement)

        for nf in self.fixed_nodes:
            if nf in c.Nodes:
                coords = self.arr_nodes[nf - 1] + np.array(displacement)
                __ax.scatter(coords[0], coords[1], c='green', marker='>', s=200)

        for nl in self.forced_nodes:
            vec = self.forced_nodes[nl]
            if nl in c.Nodes:
                xyz = self.arr_nodes[nl - 1] + np.array(displacement)
                arr_fk = plt.arrow(xyz[0], xyz[1], vec[0] * 0.5, vec[1] * 0.5,
                                   edgecolor='navy', zorder=10, length_includes_head=True,
                                   head_width=.1, facecolor='navy')

                __ax.add_patch(arr_fk)

        # draw domain boundary forces
        arr_gk = None
        for n in cutted_nodes:
            if n in c.Nodes:
                _p0 = self.arr_nodes[n - 1] + np.array(displacement)
                _dx = 0.3 * (np.array(displacement)[0] * (-2) + 1)
                _dy = 0.3 * (np.array(displacement)[1] * (-2) + 1)
                arr_gk = plt.arrow(_p0[0], _p0[1], _dx, _dy,
                                   edgecolor='deepskyblue', facecolor='deepskyblue', zorder=10,
                                   length_includes_head=True, head_width=.1)
                __ax.add_patch(arr_gk)

    def display_original(self, size: tuple = (10, 10)):

        _fig, _ax = plt.subplots(figsize=size)
        self.__store_original__(_ax)

        plt.title("Original TO-Problem")

        self.__display_state_(_fig)

    def display_decomposer(self, cutting_lines: list):
        _fig, _ax = plt.subplots(figsize=(10, 10))

        plt.title("Decomposer applied to TO")

        self.__store_original__(_ax)

        for line in cutting_lines:
            arr_n = np.array(
                [
                    self.arr_nodes[np.array(line)[:] - 1][0],
                    self.arr_nodes[np.array(line)[:] - 1][1]
                ]
            )
            _ax.plot(arr_n[:, 0], arr_n[:, 1], c='r', label="Cutting Lines")
        self.handles.append(mpatches.Arrow(0, 0, 1, 0, width=1, color='r'))
        self.labels.append("Cutting Lines")

        self.__display_state_(_fig)

    def display_reformulated_model(self, ref_model: TOReformulatedUserModel, cell_displacements: dict):
        _fig, _ax = plt.subplots(figsize=(10, 10))
        # draw cell
        for cid, c in ref_model.sub_domains.items():
            self.__draw_cell__(c, _ax, cell_displacements[cid], ref_model.cutted_nodes)

        _ax.scatter([], [], c='green', marker='>', label='Fixations')
        _ax.scatter([], [], c='navy', marker=r'$\rightarrow$', label='Original Outer Forces $f_k$')
        _ax.scatter([], [], c='deepskyblue', marker=r'$\rightarrow$', label='Domain Boundary Forces $g_k$')
        self.handles, self.labels = _ax.get_legend_handles_labels()

        self.__display_state_(_fig)
