## @defgroup Methods-Aerodynamics-Common-Fidelity_Zero-Drag Drag
# Aerodynamic methods contain the functions for the aerodynamic analyses.
# @ingroup Methods-Aerodynamics-Common-Fidelity_Zero


from parasite_drag_wing import parasite_drag_wing
from parasite_drag_fuselage import parasite_drag_fuselage
from parasite_drag_propulsor import parasite_drag_propulsor
from parasite_drag_pylon import parasite_drag_pylon
from parasite_total import parasite_total
from induced_drag_aircraft import induced_drag_aircraft
from compressibility_drag_wing import compressibility_drag_wing
from compressibility_drag_wing_total import compressibility_drag_wing_total
from miscellaneous_drag_aircraft_ESDU import miscellaneous_drag_aircraft_ESDU
from trim import trim
from spoiler_drag import spoiler_drag