G = 6.673 * 10 ** (-11)
m_sun = 1.9891 * (10 ** 30)
m_earth = 5.9736 * 10 ** 24
m_moon = 7.349 * 10 ** 22
d_m_e = 384.4 * 10 ** 6  # orbiting  around the earth
d_s_e = 1.4959787066 * 10 ** 11  # orbiting around the sun
r_earth = 6.378136 * 10 ** 6  # radius of the earth

# Question 1 (a)
print("\n### Question 1(a)####")
f_m = G * m_earth * m_moon / (d_m_e ** 3) * 2 * r_earth
print("Tidal force due to the moon: {:.3e}".format(f_m))

f_e = G * m_sun * m_earth / (d_s_e ** 3) * 2 * r_earth
print("Tidal force due to the sun: {:.3e}".format(f_e))
print("df_m/df_e: ", f_m / f_e)
print("df_m-df_e: ", f_m - f_e)

# (b)
print("\n### Question 1(b)####")
h = 1.7
a_m_h = G * m_moon / (d_m_e ** 3) * 2 * h
print("Tidal acceleration on the person due to the moon: ", a_m_h)
a_m_h = G * m_earth / (r_earth ** 3) * 2 * h
print("Tidal acceleration on the person due to the earth: ", a_m_h)

#（c）
print("\n### Question 1(c)####")
c=2.99292458*10**8
a_b = c**6*h/(4*(10**16)*(G**2)*(m_sun**2))

print("Tidal acceleration on the person due to the black hole: ", "{:.3e}".format(a_b))


#(d)
print("\n### Question 1(d)####")
m_b2 = 10*m_sun
a_b2 = c**6*h/(4*(G**2)*(m_b2**2))
print("Tidal acceleration on the person due to the black hole: ", "{:.3e}".format(a_b2))



