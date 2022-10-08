



class Building:   
    #são criadas com referencia ao canto superior esquerdo
    def __init__(self, data, u, v):
        self.data = data
        self.u = u
        self.v = v

        self.x = u*32
        self.y = v*32

    def draw(self, surface):
        surf = self.data.surf                          
        surface.blit(surf, (self.x, self.y))

    


