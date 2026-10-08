campo = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']

temp = []
intervalosM = [0,2,4,5,7,9,11]
intervalosmm = [0,2,3,5,7,9,11]
intervalosmn = [0,2,3,5,7,8,10]
intervalosmh = [0,2,3,5,7,8,11]
concluido = []
def maior(tom = 'C'):
    if concluido:
        concluido.clear()
    if tom not in campo[0]:
        n = campo.index(tom)
        cont = 1
        temp.append(campo[n])
        while True:
            n += 1
            temp.append(campo[n])
            if campo[n] == "B":
                n = 0
                temp.append(campo[n])
            if campo[n] == campo[campo.index(tom) - 1]:
                break
        for i in intervalosM:
            concluido.append(temp[i])
        return concluido
    else:
        for i in intervalosM:
            concluido.append(campo[i])
        return concluido

def menornatu(tom = 'C'):
    if concluido:
            concluido.clear()
    if tom not in campo[0]:
        n = campo.index(tom)
        cont = 1
        temp.append(campo[n])
        while True:
            n += 1
            temp.append(campo[n])
            if campo[n] == "B":
                n = 0
                temp.append(campo[n])
            if campo[n] == campo[campo.index(tom) - 2]:
                break
        for i in intervalosmn:
            concluido.append(temp[i])
        return concluido
    else:
        for i in intervalosmn:
            concluido.append(campo[i])
        return concluido
            
def menorharm(tom = 'C'):
    if concluido:
            concluido.clear()
    if tom not in campo[0]:
        n = campo.index(tom)
        cont = 1
        temp.append(campo[n])
        while True:
            n += 1
            temp.append(campo[n])
            if campo[n] == "B":
                n = 0
                temp.append(campo[n])
            if campo[n] == campo[campo.index(tom) - 1]:
                break
        for i in intervalosmh:
            concluido.append(temp[i])
        return concluido
    else:
        for i in intervalosmh:
            concluido.append(campo[i])
        return concluido
        
def menormelod(tom = 'C'):
    if concluido:
            concluido.clear()
    if tom not in campo[0]:
        n = campo.index(tom)
        cont = 1
        temp.append(campo[n])
        while True:
            n += 1
            temp.append(campo[n])
            if campo[n] == "B":
                n = 0
                temp.append(campo[n])
            if campo[n] == campo[campo.index(tom) - 1]:
                break
        for i in intervalosmm:
            concluido.append(temp[i])
        return concluido
    else:
        for i in intervalosmm:
            concluido.append(campo[i])
        return concluido

def acordeMaior():
    cont = 1
    for c in maior():
        if cont == 1 or cont == 4 or cont == 5:
            print(c)
        if cont == 2 or cont == 3 or cont == 6:
            print(f'{c}m')
        if cont == 7:
            print(f'{c}m75b')
        cont += 1

def acordeMenorNatu():        
    cont = 1
    for c in menornatu():
        if cont == 3 or cont == 6 or cont == 7:
            print(c)
        if cont == 1 or cont == 4 or cont == 5:
            print(f'{c}m')
        if cont == 2:
            print(f'{c}m75b')
        cont += 1
        
def acordeMenorHarm():
    cont = 1
    for c in menorharm():
        if cont == 6 or cont == 5:
            print(c)
        if cont == 1 or cont == 4:
            print(f'{c}m')
        if cont == 2:
            print(f'{c}m75b') 
        if cont == 7:
            print(f'{c}°')
        if cont == 3:
            print(f'{c}5b')
        cont += 1        
             
def acordeMenorMelod():
    cont = 1
    for c in menormelod():
        if cont == 4 or cont == 5:
            print(c)
        if cont == 1 or cont == 2:
            print(f'{c}m')
        if cont == 6 or cont == 7:
            print(f'{c}m75b')
        if cont == 3:
            print(f'{c}5b')
        cont += 1

nota = input('Nota do acorde: ')
maioroumenor = input('M/m: ')
complemento = input('Complementos: ')
triateacorde = []

def montagem_acorde():
    acorde = [nota, maioroumenor, complemento]
    for c in acorde:
        if c == nota:
            triateacorde.append(c)
        if c == 'm':
            cont=1
            n = campo.index(acorde[0])
            while True:
                cont += 1
                n += 1
                if cont == 4 and campo[n] == 'B':
                    triateacorde.append(campo[n])
                    break
                if cont < 4 and campo[n] == 'B':
                    n = -1
                if cont == 4 and campo[n] != "B":
                    triateacorde.append(campo[n])
                    break
        if c == 'M':
            cont=1
            n = campo.index(acorde[0])
            while True:
                cont += 1
                n += 1
                if cont == 5 and campo[n] == 'B':
                    triateacorde.append(campo[n])
                    break
                if cont < 5 and campo[n] == 'B':
                    n = -1
                if cont == 5 and campo[n] != "B":
                    triateacorde.append(campo[n])
                    break
        if c == "7M":
            cont=1
            n = campo.index(acorde[0])
            while True:
                cont += 1
                n += 1
                if cont == 12 and campo[n] == 'B':
                    triateacorde.append(campo[n])
                    break
                if cont < 12 and campo[n] == 'B':
                    n = -1
                if cont == 12 and campo[n] != "B":
                    triateacorde.append(campo[n])
                    break
        if c == "7":
            cont=1
            n = campo.index(acorde[0])
            while True:
                cont += 1
                n += 1
                if cont == 11 and campo[n] == 'B':
                    triateacorde.append(campo[n])
                    break
                if cont < 11 and campo[n] == 'B':
                    n = -1
                if cont == 11 and campo[n] != "B":
                    triateacorde.append(campo[n])
                    break
        if c == "6":
            cont=1
            n = campo.index(acorde[0])
            while True:
                cont += 1
                n += 1
                if cont == 10 and campo[n] == 'B':
                    triateacorde.append(campo[n])
                    break
                if cont < 10 and campo[n] == 'B':
                    n = -1
                if cont == 10 and campo[n] != "B":
                    triateacorde.append(campo[n])
                    break
        if c == "5aum" or c == "6m":
            cont=1
            n = campo.index(acorde[0])
            while True:
                cont += 1
                n += 1
                if cont == 9 and campo[n] == 'B':
                    triateacorde.append(campo[n])
                    break
                if cont < 9 and campo[n] == 'B':
                    n = -1
                if cont == 9 and campo[n] != "B":
                    triateacorde.append(campo[n])
                    break
        if c == "5":
            cont=1
            n = campo.index(acorde[0])
            while True:
                cont += 1
                n += 1
                if cont == 8 and campo[n] == 'B':
                    triateacorde.append(campo[n])
                    break
                if cont < 8 and campo[n] == 'B':
                    n = -1
                if cont == 8 and campo[n] != "B":
                    triateacorde.append(campo[n])
                    break        
        if c == "5dim" or c == '4aum':
            cont=1
            n = campo.index(acorde[0])
            while True:
                cont += 1
                n += 1
                if cont == 7 and campo[n] == 'B':
                    triateacorde.append(campo[n])
                    break
                if cont < 7 and campo[n] == 'B':
                    n = -1
                if cont == 7 and campo[n] != "B":
                    triateacorde.append(campo[n])
                    break
        if c == '4':
            cont=1
            n = campo.index(acorde[0])
            while True:
                cont += 1
                n += 1
                if cont == 6 and campo[n] == 'B':
                    triateacorde.append(campo[n])
                    break
                if cont < 6 and campo[n] == 'B':
                    n = -1
                if cont == 6 and campo[n] != "B":
                    triateacorde.append(campo[n])
                    break
    if acorde[2] != '5dim' or acorde[2] != '5aum':
        cont=1
        n = campo.index(acorde[0])
        while True:
            cont += 1
            n += 1
            if cont == 8 and campo[n] == 'B':
                triateacorde.append(campo[n])
                break
            if cont < 8 and campo[n] == 'B':
                n = -1
            if cont == 8 and campo[n] != "B":
                triateacorde.append(campo[n])
                break           
montagem_acorde()
print(triateacorde)
