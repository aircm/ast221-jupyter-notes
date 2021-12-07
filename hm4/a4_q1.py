m_sun = 1.9891 * (10 ** 30)
au=1.4959787066*10**11
G = 6.673 * 10 ** (-11)
pi=3.14
m_h=1.673532499*10**(-27)
k_b=1.3806503*10**(-23)
R_e = 6.378136*10**6
R_m=1.7371*10**6

rho=920
R_c = 4000
d_c_i = 40 * au
d_c_f = 1 * au

# (a)
m_c=4/3*pi* R_c**3 * rho
E_k=G * m_sun*m_c*(d_c_f**(-1)-d_c_i**(-1))
print("Kinetic Energy of the coment{:.3e} J".format(E_k))

#(b)
l=10**4
T=3500
rho_s=2000
R = (20*E_k*m_h/(rho_s*k_b*T*pi*l))**0.5
print("Radius of the Cylindrical Crater {:.3e} m".format(R))

#(c)
N_e = 10 * R_e**2/R_m**2
print("Number of Object have struck the Earth {:.3e} ".format(N_e))
