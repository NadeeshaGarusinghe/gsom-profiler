**_GSOM Interactive Profile Visualizer_**

This GSOM Interactive profiler is able to generate a latent representation 
of input space and create cluster profiles. The generated cluster profiles 
are visualized using a GSOM map in an interactive manner

This visualization tool can be used in;
1. Generation mode 
2. Visualization mode (You must have previously generated a latent 
representation to use this mode.) 

**Procedure**
  
If Generation mode:
1. Update the configuration file (`app/config.py`)
2. Run `app/main.py`

If visualization only mode:
1. Enable only_visualization parameter in config file (`app/config.py`)
2. Provide the results directory location (e.g., `output/Exp-2019-05-09-18-35-48/Survey_data_0.5_T_1_mage_80itr`)
3. Run `app/main.py`
