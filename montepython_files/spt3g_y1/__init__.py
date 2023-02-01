from montepython.likelihood_class import Likelihood, Likelihood_clik


class spt3g_y1(Likelihood_clik):
    def __init__(self, path, data, command_line):

        Likelihood.__init__(self, path, data, command_line)
        self.need_cosmo_arguments(
            data, {'lensing': 'yes', 'output': 'tCl lCl pCl'})

        try:
            import clik
        except ImportError:
            raise io_mp.MissingLibraryError(
                "You must first activate the binaries from the Clik " +
                "distribution. Please run : \n " +
                "]$ source /path/to/clik/bin/clik_profile.sh \n " +
                "and try again.")
        if int(clik.version().split("_")[1].split(".")[0])<16:
            raise ImportError("Clik must be at version 16+ to use the SPT3G TTTEEE likelihood")
        # for lensing, some routines change. Intializing a flag for easier
        # testing of this condition
        #if self.name == 'Planck_lensing':
        if 'lensing' in self.name and 'Planck' in self.name:
            self.lensing = True
        else:
            self.lensing = False

        try:
            if self.lensing:
                self.clik = clik.clik_lensing(self.path_clik)
                try:
                    self.l_max = max(self.clik.get_lmax())
                # following 2 lines for compatibility with lensing likelihoods of 2013 and before
                # (then, clik.get_lmax() just returns an integer for lensing likelihoods;
                # this behavior was for clik versions < 10)
                except:
                    self.l_max = self.clik.get_lmax()
            else:
                if hasattr(self,"options"):
                    options = self.options
                    self.clik = clik.clik(self.path_clik,**options)
                else:
                    self.clik = clik.clik(self.path_clik)
                self.l_max = max(self.clik.get_lmax())
        except clik.lkl.CError:
            raise io_mp.LikelihoodError(
                "The path to the .clik file for the likelihood "
                "%s was not found where indicated:\n%s\n"
                % (self.name,self.path_clik) +
                " Note that the default path to search for it is"
                " one directory above the path['clik'] field. You"
                " can change this behaviour in all the "
                "Planck_something.data, to reflect your local configuration, "
                "or alternatively, move your .clik files to this place.")
        except KeyError:
            raise io_mp.LikelihoodError(
                "In the %s.data file, the field 'clik' of the " % self.name +
                "path dictionary is expected to be defined. Please make sure"
                " it is the case in you configuration file")

        self.need_cosmo_arguments(
            data, {'l_max_scalars': self.l_max})

        self.nuisance = list(self.clik.extra_parameter_names)

        # line added to deal with a bug in planck likelihood release: A_planck called A_Planck in plik_lite
        if (self.name == 'Planck15_highl_lite') or (self.name == 'Planck15_highl_TTTEEE_lite'):
            for i in range(len(self.nuisance)):
                if (self.nuisance[i] == 'A_Planck'):
                    self.nuisance[i] = 'A_planck'
            print("In %s, MontePython corrected nuisance parameter name A_Planck to A_planck" % self.name)

        # testing if the nuisance parameters are defined. If there is at least
        # one non defined, raise an exception.
        exit_flag = False
        nuisance_parameter_names = data.get_mcmc_parameters(['nuisance'])
        for nuisance in self.nuisance:
            if nuisance not in nuisance_parameter_names:
                exit_flag = True
                print('%20s\tmust be a fixed or varying nuisance parameter' % nuisance)

        if exit_flag:
            raise io_mp.LikelihoodError(
                "The likelihood %s " % self.name +
                "expected some nuisance parameters that were not provided")

        # deal with nuisance parameters
        try:
            self.use_nuisance
        except:
            self.use_nuisance = []

        # Add in use_nuisance all the parameters that have non-flat prior
        for nuisance in self.nuisance:
            if hasattr(self, '%s_prior_center' % nuisance):
                self.use_nuisance.append(nuisance)

