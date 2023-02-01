# Installation instructions for `montepython`

**Prerequisite**:
Download and install `clik` _(version >= 16.0)_ from [https://github.com/benabed/clik](https://github.com/benabed/clik), or make sure that your cobaya installation already includes a `clik` at version >= 16.0.

You must have a `montepython` installation with version at least 3.0, You also must follow the instruction of the `montepython` installation guide and install the Planck likelihood.

### Using the install script
Run the `spt3g_montepython_install` script 
	
	$> spt3g_montepython_install /path/to/montepython [/path/to/clik]

`/path/to/montepython/` is the path to your montepython install.
	
`/path/to/clik` optionnaly point toward an install of clik with version at least >16.0. You can download and install the clik library from
[https://github.com/benabed/clik](https://github.com/benabed/clik)

You should now be able to use the spt3g_y1 likelihood. Look at `base_spt3g_y1.param` for example use.

	$> source /path/to/clik/bin/clik_profile.sh
	$> python /path/to/montepython/montepython/MontePython.py run -o base_spt -p base_spt3g_y1.param 


### Installing by hand
Those steps are performed automatically by the install script.

- Create a `spt_data` directory in `/path/to/montepython/data`
- Move the `SPT3G_Y1_v1_TTTEEE.clik` to `/path/to/montepython/data/spt_data`
- Copy the `spt3g_y1` directory to `/path/to/montepython/montepython/likelihoods`
- Download and install clik version 16+ from [https://github.com/benabed/clik](https://github.com/benabed/clik)
- In the `/path/to/montepython/default.conf` file of your montepython install make sure to change the definition of the clik path to your new clik library

		path['clik'] = /path/to/clik_16+/
	
You should now be able to use the spt3g_y1 likelihood. Look at `base_spt3g_y1.param` for example use.

	$> source /path/to/clik/bin/clik_profile.sh
	$> python /path/to/montepython/montepython/MontePython.py run -o base_spt -p base_spt3g_y1.param 

### modifying the SPT3G likelihood

After installation, you can modify the likelihood to use only a subset of th2 data. Look into `/path/to/montepython/data/spt3g_y1/spt3g_y1.data for examples.

----------
31/01/2023
K. Benabed

