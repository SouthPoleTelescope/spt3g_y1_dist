from cobaya.likelihoods.base_classes import planck_clik
from cobaya.log import LoggedError, get_logger
from cobaya.tools import are_different_params_lists
import numpy as np


class TTTEEE(planck_clik.PlanckClik): 
    def initialize_with_params(self):
        # Check that the parameters are the right ones
        # the last seven paramters are cosmo parameters, ignore them 
        differences = are_different_params_lists(
            self.input_params, self.expected_params[:37], name_A="given", name_B="expected")
        if differences:
            raise LoggedError(
                self.log, "Configuration error in parameters: %r. "
                          "If this has happened without you fiddling with the defaults, "
                          "please open an issue in GitHub.", differences)

    def log_likelihood(self, cl, **params_values):
        # fill with Cl's
        self.vector[:-len(self.expected_params)] = np.concatenate(
            [(cl[spectrum][:1 + lmax] if spectrum not in ["tb", "eb"]
              else np.zeros(1 + lmax))
             for spectrum, lmax in zip(self.requested_cls, self.l_maxs_cls)])
        # check for nan's: mey produce a segfault in clik
        # dot product is apparently the fastest way in threading-enabled numpy
        if np.isnan(np.dot(self.vector, self.vector)):
            return -np.inf
        # fill with likelihood parameters
        #first the nuisance
        if len(self.expected_params)==37:
            self.vector[-len(self.expected_params):] = (
                [params_values[p] for p in self.expected_params])
        else:    
            self.vector[-len(self.expected_params):-6] = (
                [params_values[p] for p in self.expected_params[:-6]])
            # now to the cosmo parameters

            cpars = np.zeros(7)
            # H0
            #cpars[0] = self.provider.get_param("H0")
            # Omega_b
            #cpars[1] = self.provider.get_param('omegab')
            #sigma_8
            #cpars[2] = self.provider.get_param('sigma8')
            # Omega_m
            #cpars[3] = self.provider.get_param('omegam')
            # ns
            #cpars[4] = self.provider.get_param('ns')
            # tau
            #cpars[5] = self.provider.get_param('tau')

        #self.vector.tofile("gosh.txt",sep="\n")
        loglike = self.clik(self.vector)[0]
        # "zero" of clik, and sometimes nan's returned
        if np.allclose(loglike, -1e30) or np.isnan(loglike):
            loglike = -np.inf
        return loglike
    def get_requirements(self):
        req = planck_clik.PlanckClik.get_requirements(self)
        # State requisites to the theory code
        #req.update({"H0":None,"omegab":None,"sigma8":None})#,"omegam":None})#,"tau":None})#"ns":None})
        return req


_planck_get_data_path = planck_clik.get_data_path

def get_data_path(name):
    log = get_logger(name)
    if "spt" not in name.lower():
        return _planck_get_data_path(name)
    log.info("override default get_data_path from %s"%(_planck_get_data_path.__module__))
    return "spt_data"

planck_clik.get_data_path = get_data_path
