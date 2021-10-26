c=2.99292458*10**8
L_sun = 3.839*10**26
t = 3.154*10**17
m_sun = 1.9891 * (10 ** 30)
m_earth = 5.9736 * 10 ** 24
m_earth_to_sun_ratio = m_earth/m_sun
m_total_to_sun_ration = m_earth_to_sun_ratio + 1

#（b）
print("\n### Question 2(b)####")
print("Mass of Earth to Sun ratio: {:.3e} M_sun".format(m_earth_to_sun_ratio))
print("Total mass to Sun ratio: {:.7} M_sun".format(m_total_to_sun_ration))
delta_m = L_sun * t / (c**2)
delta_m_to_sun_ratio = delta_m/m_sun
print("Mass loss due to the light is: {:.3e} M_sun".format(delta_m_to_sun_ratio))
print("Semimajor axis change is: {:.3e} au".format(delta_m_to_sun_ratio/m_total_to_sun_ration))




