from LinkedQFile import LinkedQ
import sys


def inlasning_kort():
    kort = sys.stdin.readline()
    kort_lista = kort.split()
    return kort_lista


def sortera_kort(kort_lista):
    kortlek = LinkedQ()
    sorterad_lek = []

    for item in kort_lista:
        kortlek.enqueue(item)
    i = 1
    while not kortlek.isEmpty():
        if i % 2 == 0:
            kort = kortlek.dequeue()
            sorterad_lek.append(kort)

        else:
            kort = kortlek.dequeue()
            kortlek.enqueue(kort)
        i = i+1
    return sorterad_lek


def main():
    kort_lista = inlasning_kort()
    sorterad_lek = sortera_kort(kort_lista)
    kort_sträng = ''
    for item in sorterad_lek:
        kort_sträng = kort_sträng + str(item) + ' ' 
    print(kort_sträng)
#Whaddaup dude

if __name__ == "__main__":
    main()
