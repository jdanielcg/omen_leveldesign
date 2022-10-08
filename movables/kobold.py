        
        
        
        #velocidade universal dos movables
        velx = 100
        vely = 100

        # -> Kobold Laborer
        #cima
        laborercima = Sprite("assets\movables\Allies\kobold_laborer\cima.png", 9)
        laborercima_idle = Sprite("assets\movables\Allies\kobold_laborer\cima9.png")
        laborercima.set_position(w/2,h/2)
        laborercima_idle.set_position(w/2,h/2)
        laborercima.set_total_duration(1000)

        #baixo
        laborerbaixo = Sprite("assets\movables\Allies\kobold_laborer\Baixo.png", 9)
        laborerbaixo_idle = Sprite("assets\movables\Allies\kobold_laborer\Baixo9.png")
        laborerbaixo.set_position(w/2,h/2)
        laborerbaixo_idle.set_position(w/2,h/2)
        laborerbaixo.set_total_duration(1000)

        #esquerda
        laboreresquerda = Sprite("assets\movables\Allies\kobold_laborer\esquerda.png", 9)
        laboreresquerda_idle = Sprite("assets\movables\Allies\kobold_laborer\esquerda9.png")
        laboreresquerda.set_position(w/2,h/2)
        laboreresquerda_idle.set_position(w/2,h/2)
        laboreresquerda.set_total_duration(1000)

        #direita
        laborerdireita = Sprite("assets\movables\Allies\kobold_laborer\direita.png", 9)
        laborerdireita_idle = Sprite("assets\movables\Allies\kobold_laborer\direita9.png")
        laborerdireita.set_position(w/2,h/2)
        laborerdireita_idle.set_position(w/2,h/2)
        laborerdireita.set_total_duration(1000)

        #começo
        laborer = laborerbaixo_idle
        checkpos = 'S'
        
        
        
        
        
        
        
        
        
        checkpos = allies.move(janelajogo, tecladojogo, checkpos, laborer, velx, vely)
        if checkpos == 'W':
            if tecladojogo.key_pressed("W"):
                laborer = allies.setposition(laborer,laborercima)
                laborer.update()
            else:
                laborer = allies.setposition(laborer,laborercima_idle)
        if checkpos == 'A':
            if tecladojogo.key_pressed("A"):
                laborer = allies.setposition(laborer,laboreresquerda)
                laborer.update()
            else:
                laborer = allies.setposition(laborer,laboreresquerda_idle)
        if checkpos == 'S':
            if tecladojogo.key_pressed("S"):
                laborer = allies.setposition(laborer,laborerbaixo)
                laborer.update()
            else:
                laborer = allies.setposition(laborer,laborerbaixo_idle)
        if checkpos == 'D':
            if tecladojogo.key_pressed("D"):
                laborer = allies.setposition(laborer,laborerdireita)
                laborer.update()
            else:
                laborer = allies.setposition(laborer,laborerdireita_idle)
            #fim

        laborer.draw()