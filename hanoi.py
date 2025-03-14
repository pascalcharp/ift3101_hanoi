from copy import copy


def move_disks(n, src, tgt, aux):
    arg = copy(src)
    print(f"Entrée dans move_disks({n}) avec source = {arg}")
    if n != 0:
        move_disks(n - 1, src, aux, tgt)
        tgt.append(src.pop())
        move_disks(n - 1, aux, tgt, src)
    print(f"Sortie de move_disks({n})avec source = {arg}")

if __name__ == '__main__':
    src = [i for i in range(2, 0, -1)]
    tgt = []
    aux = []

    print(f"Source avant: {src}")
    print(f"Target avant: {tgt}")

    move_disks(len(src), src, tgt, aux)

    print(f"Source après: {src}")
    print(f"Target après: {tgt}")