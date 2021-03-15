from structures import *



def save_instance(instance):
    file= open("instances/"+instance.name+".txt","w")

    lines = []
    lines += [str(instance.rest_duration)+"\n"]
    lines += [str(instance.crop_species_amount)+"\n"]
    lines += [str(instance.crop_families_amount)+"\n"]
    lines += [str(instance.plots_amount)+"\n"]

    for crop_index in range(instance.crop_species_amount):
        line = ""
        line += str(instance.crop_species_list[crop_index].family)
        if instance.crop_species_list[crop_index].fertilizer:
            line += " 1 "
        else:
            line += " 0 "
        line += str(instance.crop_species_list[crop_index].planting_season_beginning)
        line += " "
        line += str(instance.crop_species_list[crop_index].planting_season_ending)
        line += " "
        line += str(instance.crop_species_list[crop_index].cycle_duration)
        line += " "
        line += str(instance.crop_species_list[crop_index].productivity)
        line += " "
        line += str(instance.crop_species_list[crop_index].price)
        line += "\n"

        lines += [line]

    for plot_index in range(instance.plots_amount):
        line = ""
        line += str(instance.plots_list[plot_index].area)
        line += " "
        line += str(instance.plots_list[plot_index].neighbors_amount)

        for neighbor_index in range(instance.plots_list[plot_index].neighbors_amount):
            line += " "
            line += str(instance.plots_list[plot_index].neighbors_list[neighbor_index])
        line += "\n"

        lines += [line]

    file.writelines(lines)
    file.close()



def read_instance(instance_name):
    file= open("instances/"+instance_name+".txt","r")

    lines = file.readlines()
    for index in range(len(lines)):
        lines[index] = lines[index].split()

    rest_duration = int(lines[0][0])
    crop_species_amount = int(lines[1][0])
    crop_families_amount = int(lines[2][0])
    plots_amount = int(lines[3][0])

    instance = Instance(instance_name,rest_duration,crop_species_amount,crop_families_amount,[],plots_amount,[])

    for crop_index in range(crop_species_amount):
        family = int(lines[4+crop_index][0])
        if int(lines[4+crop_index][1]) == 1:
            fertilizer = True
        else:
            fertilizer = False
        planting_season_beginning = int(lines[4+crop_index][2])
        planting_season_ending = int(lines[4+crop_index][3])
        cycle_duration = int(lines[4+crop_index][4])
        productivity = int(lines[4+crop_index][5])
        price = int(lines[4+crop_index][6])

        instance.crop_species_list += [Crop_Species(family,fertilizer,planting_season_beginning,planting_season_ending,cycle_duration,productivity,price)]

    for plot_index in range(plots_amount):
        area = int(lines[4+crop_species_amount+plot_index][0])
        neighbors_amount = int(lines[4+crop_species_amount+plot_index][1])

        instance.plots_list += [Plot(area,neighbors_amount,[])]

        for neighbor_index in range(neighbors_amount):
            neighbor = int(lines[4+crop_species_amount+plot_index][2+neighbor_index])
            instance.plots_list[plot_index].neighbors_list += [neighbor]
            
    file.close()
    return instance
