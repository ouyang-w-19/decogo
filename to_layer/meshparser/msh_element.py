from typing import List


class MSHElement:
    """
    Just stores data for a msh element from the file
    """
    eid: int = 0
    etype: int = 0
    tag_number: int = 0
    tags: List[int] = []
    nodes: List[int] = []

    def __init__(self, eid, etype, tag_number, tags, nodes):
        self.eid = eid
        self.etype = etype
        self.tag_number = tag_number
        self.tags = tags
        self.nodes = nodes
