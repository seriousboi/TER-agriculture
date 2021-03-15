from structures import *
from random import randint



def generate_random_instance(instance_name,max_rest_duration,max_crop_species_amount,max_plots_amount):
    rest_duration = randint(1,max_rest_duration)
    crop_species_amount = randint(1,max_crop_species_amount)
    print()
    print(crop_species_amount)
    print()
    crop_families_amount = randint(1,crop_species_amount)
    plots_amount = randint(1,max_plots_amount)

    rand_inst = Instance(instance_name,rest_duration,crop_species_amount,crop_families_amount,[],plots_amount,[])

    for crop_index in range(crop_species_amount):
        family = randint(0,crop_families_amount-1)
        if randint(0,1) == 1:
            fertilizer = True
        else:
            fertilizer = False
        planting_season_beginning = randint(0,11) #éventuellement à changer si on prend une période autre que les mois#
        planting_season_ending = randint(0,11)
        cycle_duration = randint(1,12)
        productivity = randint(1,10)
        price = randint(1,10)

        rand_inst.crop_species_list += [Crop_Species(family,fertilizer,planting_season_beginning,planting_season_ending,cycle_duration,productivity,price)]

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
