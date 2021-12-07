T_sun = 5777
R_sun = 6.95508* 10**8
Mag_sun = 4.74
Mag_bol=-19.5
T_bol=10000
au=1.4959787066*10**11

#(a)
R = T_sun**2 * R_sun/ T_bol**2 * 10**(0.2*(Mag_sun-Mag_bol))
print("Radius[m]: {:.3e}".format(R))
print("Radius[AU]: {:.3e}".format(R/au))


#(c)
E=2.8*10**44
m_sun = 1.9891 * (10 ** 30)
v=(10*E/7/m_sun)**0.5
print("Speed[m/s]: {:.3e}".format(v))
