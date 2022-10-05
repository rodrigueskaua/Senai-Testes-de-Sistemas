def quadrante(coord_x,coord_y):
    quadrante = False
    while (coord_x != 0 or coord_y != 0):
        if(coord_x > 0 and coord_y > 0):
            quadrante = 'primeiro'
            break
        elif(coord_x < 0 and coord_y > 0):
            quadrante = 'segundo'
            break   
            
        elif(coord_x < 0 and coord_y < 0):
            quadrante = 'terceiro'
            break
        elif(coord_x > 0 and coord_y < 0):
            quadrante = 'quarto'   
            break
        else:
            break    

    if(quadrante):
        return quadrante
    else:
        return ''
        
print(quadrante(2,2))
print(quadrante(3,-2))
print(quadrante(-8,-1))
print(quadrante(-7,1))
print(quadrante(0,2))

