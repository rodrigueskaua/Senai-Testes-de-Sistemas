coord_x = int(input("Digite a coordenada X: "))
coord_y = int(input("Digite a coordenada Y: "))

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
    print(quadrante)
