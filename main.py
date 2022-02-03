from tkinter import *
from PIL import ImageTk, Image
import numpy as np
#unbounded_gen
from tkinter import messagebox

v = []
w = []
n = 0



def add():
   e = int(weight.get())
   w.append(e)
   e = int(value.get())
   v.append(e)


def addN():
    n = num.get()
    return n


def Wmax():
    maxWx = Mweight.get()
    return maxWx


def code():
    col= addN()
    col=int(col)
    n=col
    maxW=Wmax()
    maxW=int(maxW)
    row=500
    r = 500
    rm = row * r
    mi = min(w)

    # generate the population matrix
    bestG = np.random.randint(0, 1, (rm, col + 2))

    def population(r, cl):
        rand = np.random.randint(0, int(maxW / mi), (r, cl))
        ze = np.zeros((r, 4))
        rand = np.append(rand, ze, axis=1)
        return rand

    def validate_genome(g):
        summm = 0
        for m in range(col):

            summm += ((g[m]) * w[m])

            if summm > maxW:
                return 0
        return summm

    rand_pop = population(row, col)
    rand_popTemp = population(row, col)

    maxVal = 0
    bestChrom = []
    cr = int(np.floor(0.80 * row))
    cm = int(np.ceil(0.20 * row))

    def sum_fun(u) -> int:
        sum2 = 0
        for i in range(col):
            sum2 += (v[i] * rand_pop[u, i])
            # print(sum,"\n")

        return sum2

    q = 0

    for itr in range(r):
        #print("b",rand_pop)

        for i in range(row):

            b = validate_genome(rand_pop[i, 0:col])
            Value = 0
            rand_pop[i, col] = b
            if b != 0:
                Value = int(sum_fun(i))
                rand_pop[i, col + 1] = Value
                if Value > maxVal:
                    maxVal = Value
                    bestChrom = rand_pop[i, 0:col]
                    bestG[q] = rand_pop[i, 0:col + 2]
                    bestG[q, col] = maxVal
                    q += 1

            else:
                Value = 0
                rand_pop[i, col + 1] = Value

            # Fitness i

            # print("\nBest Genome up:", bestChrom, "\nMaximum Value: ", maxVal)
        x = np.average(rand_pop[:, col + 1])
        # print(x)
        # print(rand_pop)
        if x == 0.0 or x == 0:
            rand_pop = population(row, col)
            rand_popTemp = population(row, col)
            continue
        matrix = np.random.randint(0, 1, (row, 2))
        for i in range(row):
            rand_pop[i, col + 2] = rand_pop[i, col + 1] / x
            rand_pop[i, col + 3] = int(np.round(abs(rand_pop[i, col + 2])))
            matrix[i, 0] = i
            matrix[i, 1] = int(np.round(abs(rand_pop[i, col + 2])))
            m = matrix[np.argsort(matrix[:, 1])]
            # sorted(matrix, key=itemgetter(1),reverse=True)
        len = row / 2
        g = 1
        while len:
            r = m[row - g, 0]
            cc = m[row - g, 1]
            t = 2
            while t:
                rand_popTemp[g] = rand_pop[r, :col + 4]
                t = t - 1
            len = len - 1
            g = g + 1
            # Next generation formation

        rand_pop[:, 0:col + 4] = rand_popTemp

        # print("\nThe next generation: \n", rand_pop[:, 0:col])
        # Crossover
        # print("before", rand_pop)
        for i in range(cr):
            # print("crrr")
            k = np.random.randint(0, n)
            r1 = np.random.randint(0, row)
            r2 = np.random.randint(0, row)
            while r1 == r2:
                r2 = np.random.randint(0, row)

            a = rand_pop[r1, :col].tolist()
            b = rand_pop[r2, :col].tolist()
            # print(a, " ", b, " ", k)

            cr1 = a[0:k] + b[k:col]
            cr2 = b[0:k] + a[k:col]
            # print(cr1, " ", cr2)

            rand_pop[r1, :col] = np.reshape(cr1, (1, n))
            rand_pop[r2, :col] = np.reshape(cr2, (1, n))
        # print("cr", rand_pop)
        # Mutation
        # np.reshape(x, (3, 2))

        for i in range(cm):
            rrow = np.random.randint(0, row)
            rcol = np.random.randint(0, n)
            bl = np.random.randint(0, maxW / mi)
            rand_pop[rrow, rcol] = bl

        for i in range(row):
            b = validate_genome(rand_pop[i, 0:col])
            Value = 0
            rand_pop[i, col] = b
            if b != 0:

                Value = int(sum_fun(i))
                rand_pop[i, col + 1] = Value
                if Value > maxVal:
                    maxVal = Value
                    bestChrom = rand_pop[i, 0:col]
                    print("best", bestChrom)
                    bestG[q] = rand_pop[i, 0:col + 2]
                    bestG[q, col] = maxVal
                    q += 1
            else:
                Value = 0
                rand_pop[i, col + 1] = Value

            # print("\nBest Genome last:", bestChrom, "\nMaximum Value: ", maxVal)

    # sorted(bestG, key=lambda x: x[col])
    m2 = bestG[np.argsort(bestG[:, col])]
    # m=np.flip(sorted_array)
    # y=np.flip(m)

    # sorted(bestG, key=itemgetter(col))
    # np.linalg.inv(sorted_array)
    # print(m2)

    print(m2[rm - 1, :col], " ", m2[rm - 1, col])
    s1 = str(m2[rm - 1, col])
    s2 = str(m2[rm - 1, :col])
    s = str("Max Value: " + s1 + "  Best Chromosome:  " + s2 + " ")
    messagebox.showinfo("Solution", s)


def get_result():
    # not ready
    code()


screen = Tk()
screen.title('knapsack')
screen.geometry('800x500')
screen.config(bg='#D3D3D3')

screen.iconbitmap(r'knapsack.png')  # path of icon like D:/photos/Thief.ico
my_img = ImageTk.PhotoImage(Image.open(r'knapsack.png'))  # path of photo

my_label = Label(image=my_img)
my_label.pack()
addButton = Button(screen, text='Add Item', command=add)  # command is function that button will call
addButton.place(x=350, y=375)
bestkanp = Button(screen, text='best chromosome', command=get_result)
bestkanp.place(x=450, y=375)
addButton = Button(screen, text='enter number of items', command=addN)  # command is function that button will call
addButton.place(x=200, y=375)
# addButton.pack()
addButton = Button(screen, text='enter the max weight', command=Wmax)  # command is function that button will call
addButton.place(x=60, y=375)

#######################################################
l = Label(screen, text="weight", bg='#FFFFF0')
l.config(font=("Impact", 10))
l.place(x=450, y=320)
weight = Entry(screen, width=15)
weight.place(x=450, y=350)
###########################################################
l = Label(screen, text="value", bg='#FFFFF0')
l.config(font=("Impact", 10))
l.place(x=350, y=320)
value = Entry(screen, width=10)
value.place(x=350, y=350)
################################################

l = Label(screen, text="number of items", bg='#FFFFF0')
l.config(font=("Impact", 10))
l.place(x=200, y=320)
num = Entry(screen, width=10)
num.place(x=200, y=350)
#######################################################

#######################################################
l = Label(screen, text="Max weight", bg='#FFFFF0')
l.config(font=("Impact", 10))
l.place(x=70, y=320)
Mweight = Entry(screen, width=15)
Mweight.place(x=70, y=350)
screen.mainloop()

# Bounded_Genetic
