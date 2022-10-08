
from buildings.buildingdata import BuildingData
#classe que indexa todas as construções e suas informações


class BuildingCatalog:   
  
    def __init__(self):
        
        self.catalog = {}
        self.build_catalog()
        pass

    def build_catalog(self):
        building = BuildingData("Dinner",(3,4), (1, 3),"dinner.png")



        self.catalog["dinner"] = building

    def get(self, name):
        return self.catalog[name]