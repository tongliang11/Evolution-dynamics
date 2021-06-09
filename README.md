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
pandas=1.2.4
```
Optionaly pakcages (jupyter extension configurator and python formatter):
```
jupyter_nbextensions_configurator=0.4.1
autopep8=1.5.6
```
First, clone this repository into your local machine and have [conda](https://docs.conda.io/en/latest/miniconda.html) installed.
Use `conda --version` to check conda version, which should be `4.10.1` or above.
Then create a conda environment named `evolution` and install relavent packages with command:
```
conda create --name evolution --channel conda-forge python=3.9.4 jupyter=1.0.0 matplotlib=3.4.1  numpy=1.20.2 scipy=1.6.2 seaborn=0.11.1 pandas=1.2.4 jupyter_nbextensions_configurator=0.4.1 autopep8=1.5.6 
```
and then you can activate the created conda environment with:
```
conda activate evolution
```
and then run the jupyter notebook with:
```
jupyter notebook
```
then you can open the jupyter notebook in your browser with the provided URL.

## Notebooks
**Agent based stochastic simulation.ipynb:** this notebook contains python scripts for agent-based stochastic simulations with Gillespie algorithm direct method. Both the full agent-based model on a 2D environment and the simplified 5-state model are simulated stochastically. It uses Multiprocessing to run multiple stochastic trajectories in parallel, leading to multiple trials of simulation data for the same set of parameters with no additional runtime. The default number of trials running in parallel is set to 20, but it can be scaled down according to the number of avaible CPU cores on the machine. Empirically, it takes around 35 mins to run the simulation for 20000 iterations on a Linux machine with two Intel&reg; Xeon&reg; Processor E5-2690 v4 CPU (14 cores for each CPU unit)  when all the trials are run in parallel. However, if the number of trials to run is larger than the number of avaible CPU cores, some trials of simulation have to wait until other trials are finihsed, which thus requires longer simulation time. Relavent figures are plotted.
> :warning: For Microsoft Windows user, convert `.ipynb` to `.py` file to use Multiprocessing for running multiple trials of simulation in parallel.

**Mean field model.ipynb:** this notebook numerically solves the 5-state mean-field model of the evolutionary dynamics, which is a set of coupled different equations. It also investigates the low-density limit of the 5-state model and the derived effective objective function from it. Relavent figures are also plotted.

**Figure.ipynb:** this notebook produces all the figures appeared in the article, except the schematic diagram in Figure 1A. All the processed data are stored in the folder `./processed_data`, and it is suffice to recreate all the figures with those processed data. However, if it also possible to recreate the figures with original data when it is available if `LOAD_ORIGINAL_DATA` is set to `True` in the first cell. By default, original data are stored in the folder `./evolve_data`, which is not included in this repository due to its size.

**Animation.ipynb:** this notebook generates animations of the evolutionary dynamics of the full agent-based stochastic model within a single iteration and across 20000 iterations. It is for illustration purpose only and not included in the article.

## Data
Original data generated from the agent-based stochastic simulations and the numerical solutions of the mean-field model are too large to be shared. Thus, we only [link](https://drive.google.com/drive/folders/1MzI-knWeDv4_KMGwptgoQgzGVM8ILfOH?usp=sharing) one set of original data for the standard parameter set in Google drive (198 MB), which is used to create Figure 2A~E. To use this original dataset, create `./evolve_data` folder in the root of this repository if it does not exist, and then download the zip file from the link provided and unzip it into the folder `./evolve_data`. Other original data are availble through inquiry. 

For reproducing the figures in the article, we include the processed data in the folder `./processed_data`.
