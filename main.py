from generator import *
from storage import *
from model import *
from mip import *

inst = generate_random_instance("test instance",1,24,6,6,4,10)
inst.print()
mod = create_model(inst)
mod.optimize(max_seconds=120)
print("Valeur de la fonction objectif ", mod.objective_value)
