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

**Reference**  
  
[1] D. Alahakoon, S. K. Halgamuge, and B. Srinivasan, “Dynamic self-organizing maps with controlled growth for knowledge discovery,” IEEE Transactions on Neural Networks, vol. 11, no. 3, pp. 601–614, May 2000.  
[2] R. Nawaratne, D. Alahakoon, D. De Silva, P. Chhetri, and N. Chilamkurti, “Self-evolving intelligent algorithms for facilitating data interoperability in IoT environments,” Future Generation Computer Systems, vol. 86, pp. 421–432, Sep. 2018.  
