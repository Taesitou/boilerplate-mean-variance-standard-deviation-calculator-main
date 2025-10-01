import numpy as np

# Create a function named calculate() in mean_var_std.py that
# uses Numpy to output the mean, variance, standard deviation, max, min, and sum 
# of the rows, columns, and elements in a 3 x 3 matrix.


# axis 0 = column
# axis 1 = row

def calculate(list):
    calculations = {}
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")

    npArray = np.array(list).reshape(3,3)
    calculations['mean'] = [npArray.mean(axis=0).tolist(), npArray.mean(axis=1).tolist(), npArray.mean()] 
    calculations['variance'] = [npArray.var(axis=0).tolist(), npArray.var(axis=1).tolist(), npArray.var()]
    calculations['standard deviation'] = [npArray.std(axis=0).tolist(), npArray.std(axis=1).tolist(), npArray.std()]
    calculations['max'] = [npArray.max(axis=0).tolist(), npArray.max(axis=1).tolist(), npArray.max()]
    calculations['min'] = [npArray.min(axis=0).tolist(), npArray.min(axis=1).tolist(), npArray.min()]
    calculations['sum'] = [npArray.sum(axis=0).tolist(), npArray.sum(axis=1).tolist(), npArray.sum()]

    return calculations