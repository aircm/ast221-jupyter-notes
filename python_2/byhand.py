G = 6.673 * 10 ** (-11)
m_sun=1.9891*10**30
R=6.95508*10**8
mu=0.61
m_h=1.673532499*10**(-27)
k=1.3806503*10**(-23)

T_0=3*G*m_sun*mu*m_h/(k*R)

print("The center temperature of the Sun is  {:.3e}K".format(T_0))
