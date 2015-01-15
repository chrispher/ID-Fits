import os
import time
import argparse
import numpy as np

execfile(os.path.join(os.path.dirname(__file__), "fix_imports.py"))
import config
from datasets import lfw
from learning.pca import *



def compute(filename, dims, samples_nb, output_file=None):
    if filename.find("_not_normalized_") < 0:
        raise Exception("Need to use a non normalized descriptor")
        
    print "Using %s to compute PCA" % filename

    data = np.load(filename)
    pca = computePCA(data, dim=dims, samples_nb=samples_nb)

    if output_file is None:
        output_file = os.path.join(config.models_path, "PCA.txt")
    pca.save(output_file)
    print "Results saved in %s" % output_file




if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Computes PCA")
    parser.add_argument("input_data_file", help="descriptor file on which to compute PCA (e.g. ulbp_not_normalized_lfwa.npy)")
    parser.add_argument("-d", dest="dim_num", type=int, default=200, help="number of dimensions kept by PCA")
    parser.add_argument("-s", dest="samples_number", type=int, default=1000, help="number of samples used to compute the PCA")
    parser.add_argument("-o", dest="output_file", default=None, help="where to save PCA")
    args = parser.parse_args()

    compute(args.input_data_file, args.dim_num, args.samples_number, args.output_file)
