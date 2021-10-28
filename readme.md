# SPT3G Y1 release in `clik` format

This package contains the SPT3G Y1 likelihood code and data encapsulated in `clik` format `SPT3G_Y1_v3_EETE.clik` allowing it to be called from any sampled that is already linked with the `clik` library in order to run the Planck likelihoods.

The package contains instruction for usage in `cosmomc`, `cobaya` and `montepython`.

**Prerequisite**:
Download and install `clik` _(version >= 15.0)_ from [https://github.com/benabed/clik](https://github.com/benabed/clik)  or make sure that your cosmo sampler installation already includes a `clik` at version >= 15.0. 

_Nota:_ running `clik_print` or `clik_example_C` with a clikfile will display the library version. From version 15.0 running either without clikfile will also display the version and version can also be accessed from python with 

	import clik
	print clik.version()


**Production notes**

The `SPT3G_Y1_v3_EETE.clik` was produced from the cosmomc specific SPT3G code and data v3.0 at [https://pole.uchicago.edu/public/data/dutcher21](https://pole.uchicago.edu/public/data/dutcher21/), and using the `prepare_spt3g` tool in the `clik` package with the following parameters 

	res_object = spt3g_Y1_v3_EETE.clik
	data_path = /path/to/spt3g_package/data/SPT3G_Y1_EETE/
	dataset_path = /path/to/spt3g_package/data/	SPT3G_Y1_EETE/SPT3G_Y1_EETE.dataset
	ini_path = /path/to/spt3g_package/batch3/SPT3G_Y1_EETE.ini 
 
**Changes**

*28/10/2021*
	
- Updated to v3.0 version of the data. Former clik file named `SPT3G_Y1_EETE.clik` replaced by `SPT3G_Y1_v3_EETE.clik`. Installation instruction updated accordingly. 
- Inclusion of `montepython` instructions.
  
*26/04/2021*

- initial release

----------
28/10/2021
K. Benabed & S. Galli
