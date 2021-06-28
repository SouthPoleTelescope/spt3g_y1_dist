# Installation instructions for `cobaya`

**Prerequisite**:
Download and install `clik` _(version >= 15.0)_ from [https://github.com/benabed/clik](https://github.com/benabed/clik), or make sure that your cobaya installation already includes a `clik` at version >= 15.0.

### Using the install script
Run the `spt3g_cobaya_install` script 
	
	$> spt3g_cobaya_install /path/to/cobaya/packages [/path/to/clik]

`/path/to/cobaya/packages/` is the path where the external code and packages for cobaya are installed. It's the path you gave when first installing the cobaya default cosmology files (using the command `cobaya-install cosmo -m /path/to/cobaya/packages`.
	
`/path/to/clik` must point toward your install of the `clik` library from [https://github.com/benabed/clik](https://github.com/benabed/clik) and must be at least at version>=15.0. If not given, assumes that that cobaya already includes `clik` at version>=15.0.


You should now be able to use the spt3g_y1 likelihood. Look at `params_SPT3GY1_class_base.yaml` for example use.

	$> cobaya-run params_SPT3GY1_class_base.yaml

### Installing by hand
Those steps are performed automatically by the install script.

- Create a `spt_data` directory in `/path/to/cobaya/packages/data`
- Move the `SPT3G_Y1_EETE.clik` to 
- Create a `spt_data` directory in `/path/to/cobaya/packages/data/spt_data`
- Copy the `SPT3G_Y1` directory to `/path/to/cobaya/packages/code`
- If your cobaya installation does not contains a version>=15.0 of `clik`(this is the case if you have installed the cobaya external default cosmology files with a `cobaya-install cosmo -m /path/to/cobaya/packages` for cobaya 3.1), change the name of the directory `path/to/cobaya/packages/code/planck/` to  `path/to/cobaya/packages/code/planck_old/` 
- Create a link to your `clik` library installation (downloaded from [https://github.com/benabed/clik](https://github.com/benabed/clik)) to `path/to/cobaya/packages/code/planck`.

		$> ln -s /path/to/clik path/to/cobaya/packages/code/planck
	
- Check whether astropy or pyfits is installed and accessible to cobaya, if not install astropy (`pip3 install astropy`)

- Edit `params_SPT3GY1_class_base.yaml.tmpl` and  change line 14 to point to the correct path. Save it as `params_SPT3GY1_class_base.yaml`

You should now be able to use the spt3g_y1 likelihood. Look at `params_SPT3GY1_class_base.yaml` for example use.

	$> cobaya-run params_SPT3GY1_class_base.yaml

----------
24/06/2021
S. Galli & K. Benabed 

