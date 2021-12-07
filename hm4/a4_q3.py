G = 6.673 * 10 ** (-11)
k_b=1.3806503*10**(-23)
m_h=1.673532499*10**(-27)
pi=3.14
au=1.4959787066*10**11
m_sun = 1.9891 * (10 ** 30)

# (a)
T=10
n=1
mu=2.8

M_J = (5*k_b*T/(G*mu*m_h))**1.5 * (3/(4*pi*mu*n*m_h))**0.5
R_J = (15*k_b*T/(4*pi*G* mu**2 * n * m_h**2))**0.5

print("Jean Mass: {:.3e} kg".format(M_J ))
print("Jean Mass in solar masses: {:.3e} ".format(M_J/m_sun ))
print("Jean Radius: {:.3e} m".format(R_J ))
print("Jean Radius: {:.3e} AU".format(R_J/au ))

#(b)
dp_dr = n*k_b*T/R_J
print("|dp/dr|: {:.3e} N/m^2".format(dp_dr ))

#(c)
dp_dr_2 = 3*G*M_J**2/(4*pi*R_J**5)
print("dp_dr_2: {:.3e} N/m^2".format(dp_dr_2 ))

