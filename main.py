import numpy as np
import matplotlib.pyplot as plt

def f(x):
    ans = 0;
    i = a;
    while (i>=0):
        ans = ans*x+koef[i];
        i = i-1;
    return ans;

def PRINT():
    i=a;
    s = "";
    while (i>1):
        s = s + str(abs(koef[i])) + "x^" + str(i);
        i = i-1;
        while (koef[i] == 0):
            i = i-1;
        if (koef[i] > 0):
            s = s + " + ";
        else:
            s = s + " - ";
    if (i == 1):
        s = s + str(koef[1]) + "x";
        if (koef[0] > 0):
            s = s + " + " + str(koef[0]);
        else:
            if(koef[0] < 0):
                s = s + " - " + str(abs(koef[0]));
    else:
        s = s + str(koef[0]);
    return s;

a = int(input("Derajat fungsi : "));
koef = np.zeros(a+1);
for i in range(a+1):
    if (i == 0):
        koef[0] = input("Konstanta fungsi : ");
    else:
        koef[i] = int(input('Koefisien x^' + str(i) + ': '));
print("f(x) = ", str(PRINT()));
l = float(input("Batas kiri akar: "));
r = float(input("Batas kanan akar: "));
xlist = np.arange(l,r,.1);
ylist = f(xlist);
l0 = l;
r0 = r;

m = (l+r)/2.0;
print();
while ((abs(f(m)) > 0.000000001) and (abs(l-r) > 0.000000001)):
    if (f(m)*f(l) > 0):
        l = m;
    else:
        r = m;
    m = (l+r)/2.0;
if (abs(f(m)) <= 0.000000001):
    print("Akar persamaan : %.5f" % m);
    plt.plot(xlist, ylist, c='c');
    plt.vlines(x=m,ymin=min(ylist),ymax=0,colors='red');
    plt.hlines(y=0,xmin=l0,xmax=m,colors='yellow');

else:
    print("Persamaan tidak memiliki akar diantara ", l0, " dan ", r0);
    print("atau nilai f(", l0, ") dan f(", r0, ") keduanya positif / keduanya negatif");
    plt.hlines(y=0,xmin=l0,xmax=r0,colors='yellow');

plt.plot(xlist, ylist, c='c',label="f(x)");
plt.title("Function Graph");
plt.legend();
plt.show();