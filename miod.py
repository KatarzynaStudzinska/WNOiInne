import math


def miodStatek(cX, cY, obiekt, stan):               # cX, cY to wspolrzedne srodka kazdego z miodow
    ramie = 1
    kat = math.pi/6

    Ax = cX                                         # Wierzcholek szesciokata
    Ay = cY + ramie

    Bx = cX + ramie*math.cos(kat)                   # Na prawo od wierzcholka
    By = cY + ramie*math.sin(kat)

    Cx = cX + ramie*math.cos(kat)                   # W dol
    Cy = cY - ramie*math.sin(kat)

    Dx = cX                                         # Dolny wierzcholek miodu
    Dy = cY - ramie

    Ex = cX - ramie*math.cos(kat)                   # Do gory
    Ey = cY + ramie*math.sin(kat)

    Fx = cX - ramie*math.cos(kat)                   # Do gory
    Fy = cY - ramie*math.sin(kat)

    Raz = [Ax, Bx, Cx, Dx, Fx, Ex, Ax]
    Dwa = [Ay, By, Cy, Dy, Fy, Ey, Ay]

    if stan == 1:
        obiekt.fill(Raz, Dwa, 'g')
    if stan == 2:
        obiekt.fill(Raz, Dwa, 'r')


def komorkaMiodu(cX, cY, obiekt):
    ramie = 1
    kat = math.pi/6

    Ax = cX
    Ay = cY + ramie

    Bx = cX + ramie*math.cos(kat)
    By = cY + ramie*math.sin(kat)

    Cx = cX + ramie*math.cos(kat)
    Cy = cY - ramie*math.sin(kat)

    Dx = cX
    Dy = cY - ramie

    Ex = cX - ramie*math.cos(kat)
    Ey = cY + ramie*math.sin(kat)

    Fx = cX - ramie*math.cos(kat)
    Fy = cY - ramie*math.sin(kat)

    Raz = [Ax, Bx, Cx, Dx, Fx, Ex, Ax]
    Dwa = [Ay, By, Cy, Dy, Fy, Ey, Ay]
    obiekt.plot(Raz, Dwa, 'k')


def rysujMiod(obiekt):
    srodki = []
    ramie = 1
    kat = math.pi/6
    for i in range(10):
        for j in range(10):
            if j % 2 == 0:
                komorkaMiodu(1+i*2*ramie*math.cos(kat), 1+j*3*ramie*math.sin(kat), obiekt)
                srodki.append([1+i*2*ramie*math.cos(kat), 1+j*3*ramie*math.sin(kat)])
            else:
                komorkaMiodu(1+i*2*ramie*math.cos(kat) + ramie*math.cos(kat), 1 + j*3*ramie*math.sin(kat), obiekt)
                srodki.append([1+i*2*ramie*math.cos(kat) + ramie*math.cos(kat), 1 + j*3*ramie*math.sin(kat)])
    return srodki


def grid(obiekt):
    r = 15
    for i in range(r):
            obiekt.plot([i, i], [0, r], 'g')
            obiekt.plot([0, r], [i, i], 'g')

