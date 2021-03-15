


class Instance():
    def __init__(self,name,rest_duration,crop_species_amount,crop_families_amount,crop_species_list,plots_amount,plots_list):
        self.name = name
        self.rest_duration = rest_duration
        self.crop_species_amount = crop_species_amount
        self.crop_families_amount = crop_families_amount
        self.crop_species_list = crop_species_list
        self.plots_amount = plots_amount
        self.plots_list = plots_list

    def print(self):
        print("///////////// Instance "+self.name+" /////////////")
        print("rest_duration: "+str(self.rest_duration))
        print("crop_species_amount: "+str(self.crop_species_amount))
        print("crop_families_amount: "+str(self.crop_families_amount))
        print("plots_amount: "+str(self.plots_amount))
        print()
        print("crop_species_list:")
        for index in range(self.crop_species_amount):
            print("crop species "+str(index)+":")
            self.crop_species_list[index].print()
        print()
        print("plots_list:")
        for index in range(self.plots_amount):
            print("plot "+str(index)+":")
            self.plots_list[index].print()




class Crop_Species():
    def __init__(self,family,fertilizer,planting_season_beginning,planting_season_ending,cycle_duration,productivity,price):
        self.family = family
        self.fertilizer = fertilizer
        self.planting_season_beginning = planting_season_beginning
        self.planting_season_ending = planting_season_ending
        self.cycle_duration = cycle_duration
        self.productivity = productivity
        self.price = price

    def print(self):
        if self.fertilizer:
            fertilizer_str = ", fertilizer, "
        else:
            fertilizer_str = ", "

        print("family "+str(self.family)+fertilizer_str+"planting season from "+str(self.planting_season_beginning)+" to "+str(self.planting_season_ending)+", cycle duration "+str(self.cycle_duration)+", productivity "+str(self.productivity)+", price "+str(self.price))



class Plot():
    def __init__(self,area,neighbors_amount,neighbors_list):
        self.area = area
        self.neighbors_amount = neighbors_amount
        self.neighbors_list = neighbors_list

    def print(self):
        print("area "+str(self.area)+", neighbors amount "+str(self.neighbors_amount)+", neighbors "+str(self.neighbors_list))
