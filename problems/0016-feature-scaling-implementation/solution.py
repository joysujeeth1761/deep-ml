import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# stamdardization -> z = x - mean / var
	# normalization -> x' = x - x_min /  x_max - x_min
	mean = np.mean(data,axis=0) # axis = 0 means it calulates the rows and columns separatly
	var = np.std(data,axis =0)
	standardized_data = (data-mean)/var
	min_val = np.min(data,axis=0)
	max_val = np.max(data,axis=0)
	normalized_data = (data-min_val) / (max_val - min_val)
	# rounding upto 4 decimal values 
	standardized_data = np.round(standardized_data,4)
	normalized_data = np.round(normalized_data,4)
	return standardized_data, normalized_data