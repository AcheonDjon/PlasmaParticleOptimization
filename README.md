# Charge Optimization Project

This project performs symbolic and numerical optimization of particle (charge) arrangements under a given potential. It uses Python and the SymPy library for symbolic mathematics, along with custom modules for potential energy calculations and root finding.

## Project Structure

- `charge_optimization/`
  - `main.py` — Main script for running the optimization.
  - `energy.py` — Contains the `potential` class for energy calculations.
  - `solver.py` — Contains the `find_roots` function for root finding.
  - `2solver.py` — (Purpose unspecified, likely related to solving for 2 particles.)
- `fft/` — Contains data files, scripts, and results related to FFT (Fast Fourier Transform) analysis (not directly used in charge optimization).

## How It Works

1. **Parameter Setup**: The user specifies physical parameters such as wavelength (`lam_da`), distance (`z`), force constant (`k`), and number of particles (`nums`).
2. **Potential Calculation**: The `potential` class computes the interaction and confinement energies for the system.
3. **Symbolic Computation**: The total energy is expressed symbolically as a function of the arrangement variable (`l`).
4. **Optimization**: The derivative of the energy with respect to `l` is computed, and roots are found to locate critical points (minima/maxima).
5. **Output**: The energy expression and optimal arrangement(s) are printed.

## Example Usage

Run the main script:

```powershell
python charge_optimization/main.py
```

## Customization

- To change the number of particles, modify the `nums` variable in `main.py`.
- To implement arrangements for more than 2 particles, extend the logic in `main.py` where indicated.
- Adjust physical parameters (`lam_da`, `z`, `k`) as needed for your scenario.

## Requirements

- Python 3.x
- [SymPy](https://www.sympy.org/)

Install dependencies with:

```powershell
pip install sympy
```

## File Descriptions

- **main.py**: Entry point. Sets up parameters, computes energy, finds optimal arrangements.
- **energy.py**: Defines the `potential` class with methods for interaction and confinement energies.
- **solver.py**: Provides the `find_roots` function for finding roots of symbolic expressions.
- **2solver.py**: (Purpose to be clarified.)

## Domain Background: Energy in Charge Optimization

This project models the energy of a system of charged particles (such as ions or electrons) under the influence of two main effects:

### 1. Interaction Energy
- The interaction energy describes the repulsive force between like charges (e.g., electrons or ions) as a function of their separation distance.
- In this model, the interaction potential is given by:
  
  $U_{\text{interaction}}(l) = \frac{z^2 e^2}{4 \pi \epsilon_0 l} \exp\left(-\frac{l}{\lambda}\right)$
  
  where:
  - $z$ is the charge number,
  - $e$ is the elementary charge,
  - $\epsilon_0$ is the vacuum permittivity,
  - $l$ is the separation between charges,
  - $\lambda$ is a screening length (e.g., Debye length),
  - The exponential term models screening effects (e.g., in a plasma or electrolyte).

### 2. Confinement Energy
- The confinement energy represents the effect of an external potential (such as a harmonic trap) that keeps the charges from dispersing.
- In this model, the confinement potential is:
  
  $U_{\text{confinement}}(r) = k z e r^2$
  
  where:
  - $k$ is a force constant (related to the strength of the confining potential),
  - $r$ is the position variable (distance from the trap center).

### Total Energy
- The total energy is the sum of all pairwise interaction energies and the sum of all confinement energies for the particles.
- The goal is to find the arrangement of particles (values of $l$ and $r$) that minimizes the total energy, representing the most stable configuration.

### Applications
- This type of modeling is relevant in fields such as plasma physics, ion trap experiments, condensed matter physics, and materials science, where understanding the equilibrium positions of charged particles is important.

## Suggestions for Improvement

- Generalize arrangement logic for more than 2 particles.
- Add input validation and error handling.
- Improve documentation and code comments.
- Modularize code for easier extension.

## License

Specify your license here (e.g., MIT, GPL, etc.).

## Contact

For questions or contributions, please contact the project maintainer.
