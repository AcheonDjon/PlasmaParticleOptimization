import numpy as np

def euler_maruyama(sde_func, y0, t_span, dt):
    """
    Solve SDE where sde_func returns (drift, diffusion)
    
    sde_func: function that returns (f(y,t), g(y,t))
    y0: initial condition
    t_span: (t0, tf)
    dt: time step
    """
    t0, tf = t_span
    t = np.arange(t0, tf + dt, dt)
    y = np.zeros(len(t))
    y[0] = y0
    
    sqrt_dt = np.sqrt(dt)
    
    for i in range(len(t) - 1):
        # Get both drift and diffusion from single function
        drift, diffusion = sde_func(y[i], t[i])
        
        # Random increment
        dW = np.random.normal(0, sqrt_dt)
        
        # Euler-Maruyama step
        y[i+1] = y[i] + drift * dt + diffusion * dW
    
    return t, y