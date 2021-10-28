# Installation instructions for `montepython`

**Prerequisite**:
Download and install `clik` _(version >= 15.0)_ from [https://github.com/benabed/clik](https://github.com/benabed/clik), or make sure that your cobaya installation already includes a `clik` at version >= 15.0.

You must have a `montepython` installation with version at least 3.0, You also must follow the instruction of the `montepython` installation guide and install the Planck likelihood.

### Installing by hand
Those steps are performed automatically by the install script.

- Create a `spt_data` directory in `/path/to/montepython/data`
- Move the `SPT3G_Y1_v3_EETE.clik` to `/path/to/montepython/data/spt_data`
- Copy the `spt3g_y1` directory to `/path/to/montepython/montepython/likelihoods`
- If your montepython installation does not contains a version>=15.0 of `clik`(this is probably the case if you have followed the instruction from the `montepython` `readme` file regarding the installation of the Planck likelihood), create a link `clik` library installation (downloaded from [https://github.com/benabed/clik](https://github.com/benabed/clik)) to `/path/to/planck/code/plc_3.0/clik`.

		$> ln -s /path/to/clik /path/to/planck/code/plc_3.0/clik
	
- Modify the `path['clik']` parameter in the configuration file `/path/to/montepython/default.conf` to

		path['clik'] = '/path/to/planck/code/plc_3.0/clik'
	
You should now be able to use the spt3g_y1 likelihood. Look at `params_SPT3GY1_class_base.yaml` for example use.

	$> source /path/to/clik/bin/clik_profile.sh
	$> python /path/to/montepython/montepython/MontePython.py run -o base_spt -p input/base_spt3g_y1.param 

----------
15/09/2021
K. Benabed

