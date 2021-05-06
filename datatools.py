from structures import *



def is_crop_in_family(instance,crop_index,family):
    if instance.crop_species_list[crop_index].family == family:
        return 1
    else:
        return 0


def is_season_for_crop(instance,crop_index,period):
    month = (period*instance.period_duration)%12

    b = instance.crop_species_list[crop_index].planting_season_beginning
    e = instance.crop_species_list[crop_index].planting_season_ending

    if b <= e:
        if (month >= b) or (month <= e):
            return 1
        else:
            return 0
    else:
        if (month >= b) and (month <= e):
            return 1
        else:
            return 0



def are_neighbors(instance,plot_index_1,plot_index_2):
    if plot_index_1 in instance.plots_list[plot_index_2].neighbors_list:
        return 1
    else:
        return 0
