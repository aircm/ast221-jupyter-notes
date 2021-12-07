m_sun = 1.9891 * (10 ** 30)
m_n=1.67492716*10**(-27)
R=10**6 #[cm]
sigma_vn=10**(-42)

n=21*m_sun/(20*3.14* R**3 *m_n)
l_mfp=1/(n*sigma_vn)

c=2.99792458*10**8

#（a）
print("n[particle / cm^3]: {:.3e}".format(n))
print("Mean Free Path: {:.3e}".format(l_mfp))

#(b)
R_in_m =  10**4
l_mfp_in_m = l_mfp/100
t = R_in_m**2/(l_mfp_in_m * c)
print("t[s]: {:.3e}".format(t))


#(c)
n_seen=5*10**9*((1/3*10**(-8))**(2/3))*12
print("Number of people seen: {:.3e}".format(n_seen))

print("{:.3e}".format((1/3*10**(-8))**(1/3)))
