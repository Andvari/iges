
entity = {}

entity['100'] = 'Circular Arc'
entity['102'] = 'Composite Curve'
entity['104'] = 'Conic Arc'
entity['106'] = 'Copious Data'
entity['106/11'] = '2D Linear Path'
entity['106/12'] = '3d Linear Path'
entity['106/63'] = 'Simple Closed Planar Curve'
entity['108'] = 'Plane'
entity['110'] = 'Line'
entity['112'] = 'Parametric Spline Curve'
entity['114'] = 'Parametric Spline Surface'
entity['116'] = 'Point'
entity['118'] = 'Ruled Surface'
entity['118/1'] = 'Ruled Surface'
entity['120'] = 'Surface of Revolution'
entity['122'] = 'Tabulated Cylinder'
entity['123'] = 'Direction'
entity['124'] = 'Transformation Matrix'
entity['125'] = 'Flash'
entity['126'] = 'Rational B-Spline Curve'
entity['128'] = 'Rational B-Spline Surface'
entity['130'] = 'Offset Curve'
entity['132'] = 'Connect Point'
entity['134'] = 'Node'
entity['136'] = 'Finite Element'
entity['138'] = 'Nodal Displacement and Rotation'
entity['140'] = 'Offset Surface'
entity['141'] = 'Boundary'
entity['142'] = 'Curve on a Parametric Surface'
entity['143'] = 'Bounded Surface'
entity['144'] = 'Trimmed Parametric Surface'
entity['146'] = 'Nodal Results'
entity['148'] = 'Element Results'
entity['150'] = 'Block'
entity['152'] = 'Right Angular Wedge'
entity['154'] = 'Right Circular Cylinder'
entity['156'] = 'Right Circular Cone Frustum'
entity['158'] = 'Sphere'
entity['160'] = 'Torus'
entity['162'] = 'Solid of Revolution'
entity['164'] = 'Solid of Linear Extrusion'
entity['168'] = 'Ellipsoid'
entity['180'] = 'Boolean Tree'
entity['182'] = 'Selected Component'
entity['184'] = 'Solid Assembly'
entity['186'] = 'Manifold Solid B-Rep Object'
entity['190'] = 'Plane Surface'
entity['192'] = 'Right Circular Cylindrical Surface'
entity['194'] = 'Right Circular Conical Surface'
entity['196'] = 'Spherical Surface'
entity['198'] = 'Toroidal Surface'
entity['202'] = 'Angular Dimension'
entity['204'] = 'Curve Dimension'
entity['206'] = 'Diameter Dimension'
entity['208'] = 'Flag Note'
entity['210'] = 'General Label'
entity['212'] = 'General Note'
entity['213'] = 'New General Note'
entity['214'] = 'Leader (Arrow)'
entity['216'] = 'Linear Dimension'
entity['218'] = 'Ordinate Dimension'
entity['220'] = 'Point Dimension'
entity['222'] = 'Radius Dimension'
entity['228'] = 'General Symbol'
entity['230'] = 'Sectioned Area'
entity['302'] = 'Associativity Definition'
entity['304'] = 'Line Font Definition'
entity['306'] = 'MACRO Definition'
entity['308'] = 'Subfigure Definition'
entity['310'] = 'Text Font Definition'
entity['312'] = 'Text Display Template'
entity['314'] = 'Color Definition'
entity['316'] = 'Units Data'
entity['320'] = 'Network Subfigure Definition'
entity['322'] = 'Attribute Table Definition'
entity['402'] = 'Associativity Instance'
entity['404'] = 'Drawing'
entity['406'] = 'Property'
entity['408'] = 'Singular Subfigure Instance'
entity['410'] = 'View'
entity['412'] = 'Rectangular Array Subfigure Instance'
entity['414'] = 'Circular Array Subfigure Instance'
entity['416'] = 'External Reference'
entity['418'] = 'Nodal Load/Constraint'
entity['420'] = 'Network Subfigure Instance'
entity['422'] = 'Attribute Table Instance'
entity['430'] = 'Solid Instance'
entity['502'] = 'Vertex'
entity['504'] = 'Edge'
entity['508'] = 'Loop'
entity['510'] = 'Face'
entity['514'] = 'Shell'

blank_status = {}
blank_status['00'] = "Visible"
blank_status['01'] = "Blanked"

subordinate_entity_switch = {}
subordinate_entity_switch['00'] = "Independent"
subordinate_entity_switch['01'] = "Physically Dependent"
subordinate_entity_switch['02'] = "Logically Dependent"
subordinate_entity_switch['03'] = "Physically and Logically Dependent"

entity_use_flag = {}
entity_use_flag['00'] = "Geometry"
entity_use_flag['01'] = "Annotation"
entity_use_flag['02'] = "Definition"
entity_use_flag['03'] = "Other"
entity_use_flag['04'] = "Logial/Positional"
entity_use_flag['05'] = "2D Parametric"
entity_use_flag['06'] = "Construction geometry"

hierarchy = {}
hierarchy['00'] = "Global top down"
hierarchy['01'] = "Global defer"
hierarchy['02'] = "Use hierarchy property"

CRTN = {}
CRTN['0'] = "Unspecified"
CRTN['1'] = "Projection"
CRTN['2'] = "Intersection"
CRTN['3'] = "Isoparametric curve"

PREF = {}
PREF['0'] = "Unspecified"
PREF['1'] = "S o B"
PREF['2'] = "C"
PREF['3'] = "C and S o B"

FORM = {}
FORM['0'] = "Form of the curve is determined from the rational B-spline parameters"
FORM['1'] = "Line"
FORM['2'] = "Circular arc"
FORM['3'] = "Elliptical arc"
FORM['4'] = "Parabolic arc"
FORM['5'] = "Hyperbolic arc"

PROP1 = {}
PROP1['0'] = "Nonplanar"
PROP1['1'] = "Planar"

PROP2 = {}
PROP2['0'] = "Open curve"
PROP2['1'] = "Closed curve"

PROP3 = {}
PROP3['0'] = "Rational"
PROP3['1'] = "Polynomial"

PROP4 = {}
PROP4['0'] = "Nonperiodic"
PROP4['1'] = "Periodic"

PROP1_ = {}
PROP1_['0'] = "Not closed in first parametric variable direction"
PROP1_['1'] = "Closed in first parametric variable direction"

PROP2_ = {}
PROP2_['0'] = "Not closed in second parametric variable direction"
PROP2_['1'] = "Closed in second parametric variable direction"

PROP3_ = {}
PROP3_['0'] = "Rational"
PROP3_['1'] = "Polynomial"

PROP4_ = {}
PROP4_['0'] = "Non-periodic in first parametric variable direction"
PROP4_['1'] = "Periodic in first parametric variable direction"

PROP5_ = {}
PROP5_['0'] = "Non-periodic in second parametric variable direction"
PROP5_['1'] = "Periodic in second parametric variable direction"
