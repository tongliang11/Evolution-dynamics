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
Optionaly pakcages (jupyter extension configurator and python formatter):
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
After the conda environment named `evolution` is created, activate the environment with:
```
conda activate evolution
```
and then run the jupyter notebook with:
```
jupyter notebook
```
then you can open the jupyter notebook in your browser with the provided URL.

## Notebooks
**Agent based stochastic simulation.ipynb** contains python scripts for agent-based stochastic simulations with Gillespie algorithm direct method. Both the full agent-based model on a 2D environment and the simplified 5-state model are simulated stochastically. It uses Multiprocessing to run multiple stochastic trajectories in parallel, leading to multiple trials of simulation data for the same set of parameters with no additional runtime. The default number of trials running in parallel is set to 20, but it can be scaled down according to the number of avaible CPU cores on the machine. Empirically, it takes around 35 mins to run the simulation for 20000 iterations on a Linux machine with two Intel&reg; Xeon&reg; Processor E5-2690 v4 CPU (14 cores for each CPU unit)  when all the trials are run in parallel. However, if the number of trials to run is larger than the number of avaible CPU cores, some trials of simulation have to wait until other trials are finihsed, which thus requires longer simulation time. Relavent figures are plotted.
> :warning: For Microsoft Windows user, convert `.ipynb` to `.py` file to use Multiprocessing for running multiple trials of simulation in parallel.

**Mean field model.ipynb** numerically solves the 5-state mean-field model of the evolutionary dynamics, which is a set of coupled different equations. It also investigates the low-density limit of the 5-state model and the derived effective objective function from it. Relavent figures are also plotted.

**Figure.ipynb** produces all the figures appeared in the article, except the schematic diagram in Figure 1A, which is created with [Inkscape](https://inkscape.org/). All the processed data are stored in the folder `./processed_data`, and it is suffice to regenerate all the figures with those processed data. However, it also possible to regenerate the figures with original data when it is available and `LOAD_ORIGINAL_DATA` is set to `True`. By default, original datasets are stored in the folder `./evolve_data`, which are not uploaded in this repository due to its size.

**Animation.ipynb** generates animations of the evolutionary dynamics of the full agent-based stochastic model. The same set of the [original data](https://drive.google.com/drive/folders/1MzI-knWeDv4_KMGwptgoQgzGVM8ILfOH?usp=sharing) used to create `Fig. 2A~D` are required to be present in the folder `./evolve_data` to create an animated version of the violin plots showing how the violions are shaped throughout 20000 iterations' evolution. The same data are also used to generate an animation of the spatial distribution of the agents after catastrophes. Meanwhile, data of agents giving birth and relocating within one iteration are simulated and made as an animation too. The animations are saved in the folder `./Animations`.

## Data
Original data generated from the agent-based stochastic simulations and the numerical solutions of the mean-field model are too large to be shared online. Thus, we only upload one set of original data for the standard parameter set in Google drive (198 MB), which is used to create Figure 2A~E. To use this original dataset, create `./evolve_data` folder in the root of this repository if it does not exist, and then download the zip file from this [link](https://drive.google.com/drive/folders/1MzI-knWeDv4_KMGwptgoQgzGVM8ILfOH?usp=sharing) and unzip it into `./evolve_data` folder. Other original data are availble through inquiry. 

For reproducing the figures in the article, we include the processed data in the folder `./processed_data` and all the figures in `Figure.ipynb` can be reproduced with the those processed data. If desidered, change `LOAD_ORIGINAL_DATA=True` in the first cell of `Figure.ipynb` thus the scripts will try to load the original data first and use the processed data only when the original data are not available.
