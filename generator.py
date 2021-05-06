from structures import *
from random import randint



def generate_random_instance(instance_name,period_duration,planning_duration,rest_duration,fallow_duration,crop_species_amount,plots_amount):

    crop_families_amount = randint(1,crop_species_amount)

    rand_inst = Instance(instance_name,period_duration,planning_duration,rest_duration,fallow_duration,crop_species_amount,crop_families_amount,[],plots_amount,[],[])

    for crop_index in range(crop_species_amount):
        family = randint(0,crop_families_amount-1)
        if randint(0,1) == 1:
            fertilizer = True
            rand_inst.fertilizers_list + [crop_index]
        else:
            fertilizer = False
        planting_season_beginning = randint(0,11) #toujour représenté en mois
        planting_season_ending = randint(0,11)
        cycle_duration = randint(1,12)
        productivity = randint(1,10)
        price = randint(1,10)

        rand_inst.crop_species_list += [Crop_Species(family,fertilizer,planting_season_beginning,planting_season_ending,cycle_duration,productivity,price)]

    rand_inst.crop_species_list += [Crop_Species(-1,False,0,11,fallow_duration,0,0)] #ajout la pseudo culture jachère

    for plot_index in range(plots_amount):
        area = randint(1,100)
        neighbors_amount = randint(1,8)

        rand_inst.plots_list += [Plot(area,neighbors_amount,[])]

        for neighbor_index in range(neighbors_amount):
            neighbor = randint(0,plots_amount-1)
            if (neighbor == plot_index) or (neighbor in rand_inst.plots_list[plot_index].neighbors_list):
                rand_inst.plots_list[plot_index].neighbors_amount -= 1
            else:
                rand_inst.plots_list[plot_index].neighbors_list += [neighbor]

    return rand_inst
