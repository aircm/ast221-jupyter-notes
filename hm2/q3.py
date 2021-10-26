G = 6.673 * 10 ** (-11)
m_jupiter = 317.83*5.9736*10**24
luminosity_sun = 3.839*10**26
r_jupiter = 11.209*6.378136*10**6

# 3(a)
print("\n### Question 3(a)####")
t_hk = 3/10*(G*m_jupiter**2)/(8.7*10**(-10)*luminosity_sun*r_jupiter)
print("t_hk: {:.7} s".format(t_hk))
print("t_hk: {:.7} year".format(t_hk/31536000))

# 3(b)
print("\n### Question 3(b)####")
d_r = 2/3*(-8.7*10**(-10)*luminosity_sun)*r_jupiter**2/(G*m_jupiter**2)
print("d_r: {:.4} m/s".format(d_r))
print("d_r: {:.4} cm/year".format(d_r*100*31536000))
print("d_r: {:.4} km/Gyr".format(d_r/1000*31536000*10**9))
