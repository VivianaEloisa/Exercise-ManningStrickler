import math as m


def calc_discharge(b, h, m_bank,S,**kwargs):
    A= h*(b+h*m_bank)
    P=b+2*h*m.sqrt(m_bank**2+1)
    RH=A/P

    for key in kwargs.items():
        if "D_90" in key[0]:
             return (26/key[1]**(1/6))*m.sqrt(S)*RH**(2/3)*A
        elif "k_st" in key[0]:
             return key[1]*m.sqrt(S)*RH**(2/3)*A
        elif "m_n" in key[0]:
             return 1/key[1]*m.sqrt(S)*RH**(2/3)*A


def interpolate_h(*args, **kwargs):
    pass


if __name__ == '__main__':
    # input parameters
    Q = 15.5        # discharge in (m3/s)
    b = 5.1         # bottom channel width (m)
    m_bank = 2.5    # bank slope
    k_st = 20       # Strickler value
    n_m = 1 / k_st  # Manning's
    S_0 = 0.005     # channel slope
    h=2
    # call the solver with user-defined channel geometry and discharge
    h_n = interpolate_h(Q, b, n_m=n_m, m_bank=m_bank, S0=0)
    Q=calc_discharge(b,h,m_bank,S_0, k_st=20)
    print("The flow discharge is: %0.3f" %Q)
