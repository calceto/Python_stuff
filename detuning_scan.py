import time
import numpy
# #Physical constants
# hbar=1.05457182*1e-34;
# epsilon= 8.8541878128*1e-12;
# a0=5.29*1e-11;
# elec=1.60217663*1e-19;    
# c = 
pi = numpy.pi
# #Definitions
eta = numpy.sqrt(0.13)/3
# wavelength = 
omega = 2*pi* 1.87
gamma = 2*pi* 6
# Areapixel = 69 *1e-12;
# lambda = 560.7 *1e-9;
# Nmolecule = 500;
# d = 1.3 * elec*a0;

#Saving data
filename="gamma" + str(gamma/(2*pi)) + "omega" + str(omega/(2*pi)) + "eta" + str(eta) + ".txt"
file = open(filename,"w")

# Iteration
t0= time.time()
dt = 1e-9 #us
duration = 10#us
n = int(duration/dt)
n_delta = 30
delta_max = 10000/n_delta
delta_list = numpy.empty((n_delta,1))
rho_gg_last_list = numpy.empty((n_delta,1))
for delta_index in range (0,n_delta):
    delta = delta_index * 2*pi*delta_max
    rho_gg = 1
    rho_ee = 0
    rho_ge = 0
    rho_eg = 0
    for j in range(1,n):
        rho_gg_next = rho_gg + dt * (eta * gamma * rho_ee + 1j/2 * omega * (rho_eg - rho_ge))
        rho_ee_next = rho_ee + dt * (-gamma * rho_ee + 1j/2 * omega * (rho_ge - rho_eg))
        rho_ge_next = rho_ge + dt * (-(gamma/2 + 1j*delta) * rho_ge + 1j/2 * omega * (rho_ee-rho_gg))
        rho_eg_next = numpy.conjugate(rho_ge_next)
        
        rho_gg = rho_gg_next
        rho_ee = rho_ee_next
        rho_ge = rho_ge_next
        rho_eg = rho_eg_next
    file.write('{}\t {}\n'.format(delta,rho_gg))



tf = round(time.time() - t0)
print('Elpased time: {:}'.format(tf))
file.close()