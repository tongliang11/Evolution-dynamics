# Evolution-dynamics
This repository is associated with the research article **"Evolution of innate behavioral strategies through competitive population dynamics"** by Tong Liang and Braden A. W. Brinkman.

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
ffmpeg=4.3.1
```
Optional pakcages (jupyter extension configurator and python formatter):
```
jupyter_nbextensions_configurator=0.4.1
autopep8=1.5.6
```
First, clone this repository into your local machine and have [conda](https://docs.conda.io/en/latest/miniconda.html) installed.
Use `conda --version` to check conda version, which should be `4.10.1` or above. For Linux systems, the conda environment named `evolution` can be created from the file `environment.yml` with the following command (**only works for Linux systems**):
```
conda env create --file environment.yml
```
Alternatively, **for Windows and MacOS systems** or Linux systems that above commond failed, create the conda environment named `evolution` (or your own choice) and install relavent packages with command:
```
conda create --name evolution --channel conda-forge python=3.9.4 jupyter=1.0.0 matplotlib=3.4.1  numpy=1.20.2 scipy=1.6.2 seaborn=0.11.1 pandas=1.2.4 ffmpeg=4.3.1 jupyter_nbextensions_configurator=0.4.1 autopep8=1.5.6 
```
After the conda environment named `evolution` is created, [activate the environment](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#activating-an-environment) with:
```
conda activate evolution
```
and then run the jupyter notebook with:
```
jupyter notebook
```
then you can open the jupyter notebook in your browser with the provided URL.


## Notebooks
**Agent based stochastic simulation.ipynb** contains python scripts for running the agent-based stochastic simulations with Gillespie algorithm direct method. Both the full agent-based model on a 2D environment and the simplified 5-state model are simulated stochastically. It uses Multiprocessing to run multiple stochastic trajectories in parallel, leading to multiple trials of simulation data for the same set of parameters with no additional runtime. The default number of trials running in parallel is set to 20, but it can be scaled down according to the number of avaible CPU cores on the machine. Empirically, it takes around 35 mins to run the simulation for 20000 iterations on a Linux machine with two Intel&reg; Xeon&reg; Processor E5-2690 v4 CPU (14 cores for each CPU unit) when all the trials are run in parallel. However, if the number of trials to run is larger than the number of avaible CPU cores, some trials of simulation have to wait until other trials are finished, which thus requires longer simulation time. Relevant figures are plotted.
> :warning: For Microsoft Windows user, convert `.ipynb` to `.py` file to use Multiprocessing for running multiple trials of simulation in parallel.

**Mean field model.ipynb** numerically solves the 5-state mean-field model of the evolutionary dynamics, which is a set of coupled different equations. It also investigates the low-density limit of the 5-state model and the derived effective objective function from it. Relevant figures are also plotted.

**Figure.ipynb** produces all the figures that appear in the article, except for the schematic diagram in Figure 1A, which is created with [Inkscape](https://inkscape.org/). All processed data are stored in the folder `./processed_data`, and it is sufficient to regenerate all the figures with those processed data. However, it also possible to regenerate the figures with original data when it is available and `LOAD_ORIGINAL_DATA` is set to `True`. By default, original data are stored in the folder `./evolve_data`, but this data is not included in this repository due to its size.

**Animation.ipynb** generates animations of the evolutionary dynamics of the full agent-based stochastic model. The same set of the [original data](#data-avaibility) used to create `Fig. 2A~D` are required to create an animated version of the violin plots showing how the violions evolve throughout 20000 iterations' evolution. The same data are also used to generate an animation of the spatial distribution of the agents after catastrophes. Meanwhile, data of agents giving birth and relocating within one iteration are simulated and made as an animation to show the stochastic birth-hopping dynamics of the population. The animations are saved in the folder `./Animations`.

## Data
The full set of original data generated from the agent-based stochastic simulations and the numerical solutions of the mean-field model is too large to be shared online. Thus, we only upload one set of original data for the standard parameter set in Google Drive (198 MB), which is used to create Figure 2A-E. To use this original dataset, download the zip file from this [link](https://drive.google.com/drive/folders/1MzI-knWeDv4_KMGwptgoQgzGVM8ILfOH?usp=sharing) and unzip it into the `./evolve_data` folder. Other original data are availble through inquiry. 

For reproducing the figures in the article, we include processed data in the folder `./processed_data` and all the figures in `Figure.ipynb` can be reproduced with the those processed data. If desidered, change `LOAD_ORIGINAL_DATA=True` in the first cell of `Figure.ipynb` and the scripts will try to load the original data first and use the processed data only when the original data is not available.
