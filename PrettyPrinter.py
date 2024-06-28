import numpy as np
import math

def ppm(M, name="",**kwargs):

    # Main keyword argument is "sigfigs".

    if not isinstance(M,np.ndarray):
        print(f"ppm works on objects with class numpy.ndarray, ")
        print(f"but the given object has class {M.__class__.__name__}. No output.")
        return(None)

    if len(M.shape)!=2:
        # If the numpy array is just 1D, try to make it a 1-column matrix
        rowcount = math.prod(M.shape)
        MMM = M.reshape(rowcount,1)
        print(f"Warning: Input ndarray has shape {M.shape}. Printing it as a column.")
    else:
        MMM = M
    (rowcount,colcount) = MMM.shape

    if len(name)==0:
        padname=" "
    else:
        padname=" "+name+" "

    s = int(kwargs.get('sigfigs',4))   # Default number of sig figs is hard-coded here
    s = max([1,s])                     # Silently repair bogus request

    # Preferred format has "r" digits before dot and "d" digits after,
    # using the largest absolute value of the numbers in the given matrix.
    # Of course, the sig figs "s" should nominally equal r+d.
    reference = np.max(np.abs(M))
    if reference > 0.0:
        r = 1 + int(np.floor(np.log10(reference)))
    else:
        r = 1
    d = s - r

    relax = False  # Decide whether to allow an extra char for simple decimals

    if r>0 and d>0:
        # Nominal case worked. Formulate format code and print
        print(f"Matrix{padname}has size {rowcount}x{colcount}:")
        fmt = "{"+f":{s+2:d}.{d:d}f"+"}"
        for r in range(rowcount):
            print(" "+" ".join([fmt.format(q) for q in MMM[r,:]]))
    elif r==0 and relax:
        # Stretch case. All sig figs follow "0.".
        # Just allow an extra character column for cosmetic reasons.
        print(f"Matrix{padname}has size {rowcount}x{colcount}:")
        fmt = "{"+f":{s+3:d}.{d:d}f"+"}"
        for r in range(rowcount):
            print(" "+" ".join([fmt.format(q) for q in MMM[r,:]]))
    else:
        # Scale the whole matrix so at least one entry shows all sig figs
        p = r - 1
        print(f"Matrix{padname}has size {rowcount}x{colcount};")
        print(f" ... multiply each value below by 1E{p}:")
        fmt = "{"+f":{s+2:d}.{s-1:d}f"+"}"
        for r in range(rowcount):
            print(" "+" ".join([fmt.format(q) for q in MMM[r,:]/10**p]))

    return(None)
