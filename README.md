# Evolution-dynamics
This repository is associated with the research article "Evolution of innate behavioral strategies through competitive population dynamics" by Tong Liang and Braden A. W. Brinkman.

## Python environment setup
Required packages:
```
python=3.9.4
jupyter=1.0.0
numpy=1.20.2
scipy=1.6.2
matplotlib=3.4.1
seaborn=0.11.1
```
Optionaly pakcages (jupyter extension configurator and python formatter):
```
jupyter_nbextensions_configurator=0.4.1
autopep8=1.5.6
```
First, clone this repository into your local machine and have [conda](https://docs.conda.io/en/latest/miniconda.html) installed.
Use `conda --version` to check conda version, which should be `4.10.1` or above.
Then create a conda environment named `evolution` with the relavent packages installed with command:
```
conda create --name evolution --channel conda-forge python=3.9.4 jupyter=1.0.0 matplotlib=3.4.1  numpy=1.20.2 scipy=1.6.2 seaborn=0.11.1 jupyter_nbextensions_configurator=0.4.1 autopep8=1.5.6 
```
and then you can activate the created environment with:
```
conda activate evolution
```
and then run the jupyter notebook server with:
```
jupyter notebook
```
then you can open the jupyter notebook in your browser with the provided URL.

## Notebooks
**Agent based stochastic simulation.ipynb:** this notebook contains python scripts for agent-based stochastic simulations with Gillespie algorithm direct method. It uses Multiprocessing to run multiple Gillespie trajectories in parallel, leading to multiple trials of simulation data for the same set of parameters. The default number of trials running in parallel is set to 20, but it can be scaled down according to the number of avaible CPU cores on the machine. Empirically, it takes around 35 mins to run the simulation for 20000 iterations when all the trials are run in parallel. However, if the number of trials to run is larger than the number of avaible CPU cores, some trials of simulation have to wait until other trials are finihsed, which thus requires longer simulation time.
> :warning: For Microsoft Windows user, convert `.ipynb` to `.py` file to use Multiprocessing to run multiple trials of simulation in parallel.

**Mean field model.ipynb:** this notebook numerically solves the 5-state mean-field model of the evolutionary dynamics, which is a set of coupled different equations. 

**Figure.ipynb:** this notebook produces all the figures appeared in the article, except the schematic diagram in Figure 1A.

**Animation.ipynb:** this notebook generates animations of the evolutionary dynamics of our agent-based stochastic model within a single iteration and across 20000 iterations.

## Data
Original data generated from the agent-based stochastic simulations and the numerical solutions of the mean-field model are too large to be shared (over 20 GB). Thus, we only link one set of original data for the standard parameter set, which is used to create Figure 2A~E. Other original data are availble through inquiry. For reproducing the figures in the article, we include the processed data for each figure in `Figure.ipynb` notebook.
