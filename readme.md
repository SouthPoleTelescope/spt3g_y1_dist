# SPT3G Y1 release in `clik` format

This package contains the SPT3G Y1 likelihood code and data encapsulated in `clik` format `spt3g_Y1_v1_TTTEEE.clik` allowing it to be called from any sampled that is already linked with the `clik` library in order to run the Planck likelihoods.

The package contains instruction for usage in `cobaya` and `montepython`.
Please use the F90 version from [https://pole.uchicago.edu/public/data/balkenhol22/](https://pole.uchicago.edu/public/data/balkenhol22/) for cosmomc.

**Prerequisite**:
Download and install `clik` _(version >= 16.0)_ from [https://github.com/benabed/clik](https://github.com/benabed/clik)  or make sure that your cosmo sampler installation already includes a `clik` at version >= 16.0 

_Nota:_ running `clik_print` or `clik_example_C` with a clikfile will display the library version. From version 15 running either without clikfile will also display the version and version can also be accessed from python with 

	import clik
	print(clik.version())


**Production notes**

The `spt3g_Y1_v1_TTTEEE.clik` was produced from the cosmomc specific SPT3G code and data v1.1 at [https://pole.uchicago.edu/public/data/balkenhol22/](https://pole.uchicago.edu/public/data/balkenhol22/), and using the `prepare_spt3g_ttteee` tool in the `clik` package with the following parameters 

	res_object = spt3g_Y1_v1_TTTEEE.clik

	data_path = SPT3G_2018_TTTEEE_public_likelihood/data/SPT3G_2018_TTTEEE/
	dataset_path = SPT3G_2018_TTTEEE_public_likelihood/data/SPT3G_2018_TTTEEE/SPT3G_2018_TTTEEE.dataset

	SPT3G_2018_TTTEEE_N_freq_0 = 3

	SPT3G_2018_TTTEEE_N_b_0_TT = 44
	SPT3G_2018_TTTEEE_N_b_0_TE = 44
	SPT3G_2018_TTTEEE_N_b_0_EE = 44
	SPT3G_2018_TTTEEE_N_b_0_total = 792
	SPT3G_2018_TTTEEE_N_s_0 = 18

	SPT3G_2018_TTTEEE_aberration_coefficient = -0.0004826

As usual, the file also contains a test case that is run at each initialization.

**TEEE likelhood**

The previous `spt3g_Y1_v3_EETE.clik` file has been removed from this package. The analysis of the SPT3G data have improved and it is strongly recommanded to use the new likelihood version. Please look into the `readme` files for cobaya and montepython to learn how to use only the TEEE data using the new package.
Note that when changing the initialization parameters, the automatic test run at initialization of the likelihood will fail.

**Changes**
*25/05/2023*

 - previous recipes to restrict likelihood to TT only (resp TE, EE) were still using a single bins of TEEE (resp. TTEE, TTTE). This has been corrected. That requires modification to the parameter files that are described in the cobaya and montepython readmes.
 
*31/01/2023*

- add montepython version and installation script
- allow for modification of the likelihood from the parameter files in cobaya and montepython
- tidy up...

*16/12/2022*

- Updated to v1.0 version of TTTEEE

*28/10/2021*
	
- Updated to v3.0 version of the data. Former clik file named `SPT3G_Y1_EETE.clik` replaced by `SPT3G_Y1_v3_EETE.clik`. Installation instruction updated accordingly. 
- Inclusion of `montepython` instructions.
  
*26/04/2021*

- initial release

----------
28/10/2021
K. Benabed, L. Balkenhol, S. Galli, with help from J. Lesgourgues for the montepython version.
