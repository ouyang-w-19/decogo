# Short Guide of TO-Layer to apply column generation methods to TO-Problem

## Model Creation
### Manual Model
- example is provided in models/manual_model.py 
- a dictionary of nodes
  - Dict[int, Node]
- a dictionary of elements
  - Dict[int, Type[FiniteElement]]
- boundaries can be mappped by BoundaryCondition-object
  - fixed nodes: List["node_ids"]
  - loads: Dict["node_id": force_vector: np.array]

--> Create an instance of TOModelBase

### Using GMSH
- Create a Geometry and mesh using "GMSH"
- export mesh as .msh-file
- "meshparser" is used to load a Meshfile
- Defining Boundary Conditions:
  - "physical entities"
  - name "load" all nodes will be loaded
  - name "fix" all nodes are fixed
- example is provided in "Geometry"