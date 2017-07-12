
entity = {'100': 'Circular Arc',
          '102': 'Composite Curve',
          '104': 'Conic Arc',
          '106': 'Copious Data',
          '106/11': '2D Linear Path',
          '106/12': '3d Linear Path',
          '106/63': 'Simple Closed Planar Curve',
          '108': 'Plane',
          '110': 'Line',
          '112': 'Parametric Spline Curve',
          '114': 'Parametric Spline Surface',
          '116': 'Point',
          '118': 'Ruled Surface',
          '118/1': 'Ruled Surface',
          '120': 'Surface of Revolution',
          '122': 'Tabulated Cylinder',
          '123': 'Direction',
          '124': 'Transformation Matrix',
          '125': 'Flash',
          '126': 'Rational B-Spline Curve',
          '128': 'Rational B-Spline Surface',
          '130': 'Offset Curve',
          '132': 'Connect Point',
          '134': 'Node',
          '136': 'Finite Element',
          '138': 'Nodal Displacement and Rotation',
          '140': 'Offset Surface',
          '141': 'Boundary',
          '142': 'Curve on a Parametric Surface',
          '143': 'Bounded Surface',
          '144': 'Trimmed Parametric Surface',
          '146': 'Nodal Results',
          '148': 'Element Results',
          '150': 'Block',
          '152': 'Right Angular Wedge',
          '154': 'Right Circular Cylinder',
          '156': 'Right Circular Cone Frustum',
          '158': 'Sphere',
          '160': 'Torus',
          '162': 'Solid of Revolution',
          '164': 'Solid of Linear Extrusion',
          '168': 'Ellipsoid',
          '180': 'Boolean Tree',
          '182': 'Selected Component',
          '184': 'Solid Assembly',
          '186': 'Manifold Solid B-Rep Object',
          '190': 'Plane Surface',
          '192': 'Right Circular Cylindrical Surface',
          '194': 'Right Circular Conical Surface',
          '196': 'Spherical Surface',
          '198': 'Toroidal Surface',
          '202': 'Angular Dimension',
          '204': 'Curve Dimension',
          '206': 'Diameter Dimension',
          '208': 'Flag Note',
          '210': 'General Label',
          '212': 'General Note',
          '213': 'New General Note',
          '214': 'Leader (Arrow)',
          '216': 'Linear Dimension',
          '218': 'Ordinate Dimension',
          '220': 'Point Dimension',
          '222': 'Radius Dimension',
          '228': 'General Symbol',
          '230': 'Sectioned Area',
          '302': 'Associativity Definition',
          '304': 'Line Font Definition',
          '306': 'MACRO Definition',
          '308': 'Subfigure Definition',
          '310': 'Text Font Definition',
          '312': 'Text Display Template',
          '314': 'Color Definition',
          '316': 'Units Data',
          '320': 'Network Subfigure Definition',
          '322': 'Attribute Table Definition',
          '402': 'Associativity Instance',
          '404': 'Drawing',
          '406': 'Property',
          '408': 'Singular Subfigure Instance',
          '410': 'View',
          '412': 'Rectangular Array Subfigure Instance',
          '414': 'Circular Array Subfigure Instance',
          '416': 'External Reference',
          '418': 'Nodal Load/Constraint',
          '420': 'Network Subfigure Instance',
          '422': 'Attribute Table Instance',
          '430': 'Solid Instance',
          '502': 'Vertex',
          '504': 'Edge',
          '508': 'Loop',
          '510': 'Face',
          '514': 'Shell'}

blank_status_str = {'00': "Visible",
                    '01': "Blanked"}

subordinate_entity_switch_str = {'00': "Independent",
                                 '01': "Physically Dependent",
                                 '02': "Logically Dependent",
                                 '03': "Physically and Logically Dependent"}

entity_use_flag_str = {'00': "Geometry",
                       '01': "Annotation",
                       '02': "Definition",
                       '03': "Other",
                       '04': "Logial/Positional",
                       '05': "2D Parametric",
                       '06': "Construction geometry"}

hierarchy_str = {'00': "Global top down",
                 '01': "Global defer",
                 '02': "Use hierarchy property"}

crtn_str = {'0': "Unspecified",
            '1': "Projection",
            '2': "Intersection",
            '3': "Isoparametric curve"}

pref_str = {'0': "Unspecified",
            '1': "S o B",
            '2': "C",
            '3': "C and S o B"}

form_str = {'0': "Form of the curve is determined from the rational B-spline parameters",
            '1': "Line",
            '2': "Circular arc",
            '3': "Elliptical arc",
            '4': "Parabolic arc",
            '5': "Hyperbolic arc"}

prop1_str = {'0': "Nonplanar",
             '1': "Planar"}

prop2_str = {'0': "Open curve",
             '1': "Closed curve"}

prop3_str = {'0': "Rational",
             '1': "Polynomial"}

prop4_str = {'0': "Nonperiodic",
             '1': "Periodic"}

prop1__str = {'0': "Not closed in first parametric variable direction",
              '1': "Closed in first parametric variable direction"}

prop2__str = {'0': "Not closed in second parametric variable direction",
              '1': "Closed in second parametric variable direction"}

prop3__str = {'0': "Rational",
              '1': "Polynomial"}

prop4__str = {'0': "Non-periodic in first parametric variable direction",
              '1': "Periodic in first parametric variable direction"}

prop5__str = {'0': "Non-periodic in second parametric variable direction",
              '1': "Periodic in second parametric variable direction"}

form_plane_str = {'1': "Positive",
                  '0': "Unbounded",
                  '-1': "Negative (Hole)"}

form_associativity_str = {'1': "Unordered group with back pointers",
                          '7': "Unordered group without back pointers",
                          '14': "Ordered group with back pointers",
                          '15': "Ordered group without back pointers"}

cw = {'X': ['Z+Y+Z-', 'Y+Z-Y-'],
      'Y': ['Z+X-Z-', 'X-Z-X+'],
      'Z': ['Y+X+Y-', 'X+Y-X-']}

ccw = {'X': ['Z+Y-Z-', 'Y+Z+Y-'],
       'Y': ['Z+X+Z-', 'X-Z+X+'],
       'Z': ['Y+X-Y-', 'X+Y+X-']}

acw = {'X': ['Y+Z+', 'Z-Y+', 'Y-Z-', 'Z+Y-'],
       'Y': ['X-Z+', 'Z-X-', 'X+Z-', 'Z+X+'],
       'Z': ['X+Y+', 'Y-X+', 'X-Y-', 'Y+X-']}

accw = {'X': ['Y+Z-', 'Z+Y+', 'Y-Z+', 'Z-Y-'],
        'Y': ['X-Z-', 'Z+X-', 'X+Z+', 'Z-X+'],
        'Z': ['X+Y-', 'Y+X+', 'X-Y+', 'Y-X-']}

ORIENTATION_CW = 0
ORIENTATION_CCW = 1

ORIENTATION_UNKNOWN = -1

PRECISION = 1e-6

THICKNESS = 4.

def equ(a, b):
    return abs(a-b) < PRECISION


def ge(a, b):
    return a > b-PRECISION


def gt(a, b):
    return a > b+PRECISION


def le(a, b):
    return a+PRECISION < b


def lt(a, b):
    return a-PRECISION < b


def inside(a, b, c):
    if min(a, c) <= b <= max(a, c):
        return True
    return False
