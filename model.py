from structures import *
from datatools import *
from mip import *




def create_model(instance):

    mod = Model(name = instance.name, sense = mip.MAXIMIZE, solver_name="CBC")

    Maj = (instance.crop_species_amount+1)*instance.plots_amount*instance.planning_duration

    x = [[[mod.add_var(name="X"+str(c)+","+str(p)+","+str(t),lb=0, ub= 1,var_type=INTEGER) for t in range(instance.planning_duration) ] for p in range(instance.plots_amount) ] for c in range(instance.crop_species_amount+1) ]

    for c in range(instance.crop_species_amount+1):
        for p in range(instance.plots_amount):
            for t in range(instance.planning_duration):

                mod += (x[c][p][t]<=is_season_for_crop(instance,c,t)) #(1)

                cycle = instance.crop_species_list[c].cycle_duration
                mod += (xsum(xsum(  x[c2][p][k]  for c2 in range(instance.crop_species_amount+1) )   for k in range(t,min(t+cycle,instance.planning_duration))) <= 1 + Maj*(1-x[c][p][t]) ) #(2)

                d = instance.rest_duration
                mod += (xsum(xsum(  x[c2][p][k]*is_crop_in_family(instance,c2,instance.crop_species_list[c].family)  for c2 in range(instance.crop_species_amount+1)) for k in range(t,min(t+d+1,instance.planning_duration))) <= 1 + Maj*(1-x[c][p][t])) #(3)

                mod += (xsum(xsum(xsum( x[c2][p2][k]*are_neighbors(instance,p,p2)*is_crop_in_family(instance,c2,instance.crop_species_list[c].family)   for p2 in range(instance.plots_amount)) for c2 in range(instance.crop_species_amount+1)) for k in range(t,min(t+cycle,instance.planning_duration))) <= 1 + Maj*(1-x[c][p][t])) #4

    for p in range(instance.plots_amount):

        mod += (xsum(xsum(   x[cf][p][t]   for cf in instance.fertilizers_list) for t in range(instance.planning_duration)) >= 1) #5

        mod += (xsum(   x[-1][p][t]   for t in range(instance.planning_duration)) >= 1)

    mod.objective = maximize(xsum(xsum(xsum(   x[c][p][t]*instance.crop_species_list[c].price*instance.crop_species_list[c].productivity*instance.plots_list[p].area   for c in range(instance.crop_species_amount+1)) for p in range(instance.plots_amount)) for t in range(instance.planning_duration)))

    return mod
