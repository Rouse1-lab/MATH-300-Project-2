import numpy as np
import constants as c

def main():
    # Set the truncation depth N
    M = 50 
    
    # 1. Define true reference values using NumPy
    refs = {
        "Golden Ratio": (1 + np.sqrt(5)) / 2,
        "Square Root of 2": np.sqrt(2),
        "Euler's Number (e)": np.e,
        "Pi (pi)": np.pi,
        "Natural Log of 2": np.log(2)
    }

    # 2. Call continued fraction functions
    approxs = {
        "Golden Ratio": c.const_phi(M),
        "Square Root of 2": c.const_sqrt2(M),
        "Euler's Number (e)": c.const_e(M),
        "Pi (pi)": c.const_pi(M),
        "Natural Log of 2": c.const_ln2(M)
    }

    # 3. Print table headers
    print(f"{'Constant':<20} | {'Approximation':<20} | {'Reference':<20} | {'Abs Error':<20} | {'Rel Error'}")
    print("-" * 105)

    # 4. Compute and print absolute and relative errors for each constant
    for name in refs:
        ref = refs[name]
        approx = approxs[name]

        # Failsafe in case c_f function returns none
        if approx is None:
            print(f"{name:<20} | {'Failed':<20} | {ref:<20.15f} | {'N/A':<20} | N/A")
            continue

        # Calculate metrics
        abs_err = abs(approx - ref)
        rel_err = abs_err / abs(ref)

        # Print rows. Used scientific notation for errors since they get pretty small.
        print(f"{name:<20} | {approx:<20.15f} | {ref:<20.15f} | {abs_err:<20.15e} | {rel_err:.15e}")

if __name__ == "__main__":
    main()