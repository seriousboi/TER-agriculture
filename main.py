from generator import *
from storage import *


tp = generate_random_instance("test plot",1,4,10)
tp.print()
save_instance(tp)
tpn = read_instance("test plot")
tpn.print()
