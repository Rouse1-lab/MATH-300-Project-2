import os
import numpy as np
import matplotlib.pyplot as plt
import functions as f  # Imports Isaac's code

def main():
    # Ensures the figures folder exists for saving plots
    os.makedirs('figures', exist_ok=True)
    
    # Sets truncation depth that shows where the approximation diverges
    M = 5 

    # 1. Exponential Function: exp(x)
    print("Plotting exp(x)...")
    x_exp = np.linspace(-3, 3, 100)
    y_exp_true = np.exp(x_exp)
    y_exp_approx = [f.func_exp(val, M) for val in x_exp]

    plt.figure(figsize=(8, 5))
    plt.plot(x_exp, y_exp_true, label='NumPy exp(x)', color='black', linewidth=2)
    plt.plot(x_exp, y_exp_approx, label=f'Continued Fraction (N={M})', color='red', linestyle='dashed', linewidth=2)
    
    plt.title('Exponential Function Comparison')
    plt.xlabel('x (Input)')
    plt.ylabel('y (Output)')
    plt.legend(fontsize=10)
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.tight_layout()
    
    plt.savefig('figures/01_exp_plot.pdf') # Saves as PDF
    plt.close()

    # 2. Tangent Function: tan(x)
    print("Plotting tan(x)...")
    # Stays inside (-pi/2, pi/2) to avoid asymptote distortion
    x_tan = np.linspace(-1.4, 1.4, 100) 
    y_tan_true = np.tan(x_tan)
    y_tan_approx = [f.func_tan(val, M) for val in x_tan]

    plt.figure(figsize=(8, 5))
    plt.plot(x_tan, y_tan_true, label='NumPy tan(x)', color='black', linewidth=2)
    plt.plot(x_tan, y_tan_approx, label=f'Continued Fraction (N={M})', color='red', linestyle='dashed', linewidth=2)
    
    plt.title('Tangent Function Comparison')
    plt.xlabel('x (Input)')
    plt.ylabel('y (Output)')
    plt.legend(fontsize=10)
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.tight_layout()
    
    plt.savefig('figures/02_tan_plot.pdf')
    plt.close()

    # 3. Hyperbolic Tangent Function: tanh(x)
    print("Plotting tanh(x)...")
    x_tanh = np.linspace(-5, 5, 100)
    y_tanh_true = np.tanh(x_tanh)
    y_tanh_approx = [f.func_tanh(val, M) for val in x_tanh]

    plt.figure(figsize=(8, 5))
    plt.plot(x_tanh, y_tanh_true, label='NumPy tanh(x)', color='black', linewidth=2)
    plt.plot(x_tanh, y_tanh_approx, label=f'Continued Fraction (N={M})', color='red', linestyle='dashed', linewidth=2)
    
    plt.title('Hyperbolic Tangent Function Comparison')
    plt.xlabel('x (Input)')
    plt.ylabel('y (Output)')
    plt.legend(fontsize=10)
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.tight_layout()
    
    plt.savefig('figures/03_tanh_plot.pdf')
    plt.close()

    # 4. Arctangent Function: arctan(x)
    print("Plotting arctan(x)...")
    x_arctan = np.linspace(-5, 5, 100)
    y_arctan_true = np.arctan(x_arctan)
    y_arctan_approx = [f.func_arctan(val, M) for val in x_arctan]

    plt.figure(figsize=(8, 5))
    plt.plot(x_arctan, y_arctan_true, label='NumPy arctan(x)', color='black', linewidth=2)
    plt.plot(x_arctan, y_arctan_approx, label=f'Continued Fraction (N={M})', color='red', linestyle='dashed', linewidth=2)
    
    plt.title('Arctangent Function Comparison')
    plt.xlabel('x (Input)')
    plt.ylabel('y (Output)')
    plt.legend(fontsize=10)
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.tight_layout()
    
    plt.savefig('figures/04_arctan_plot.pdf')
    plt.close()

    # 5. Square Root Function: sqrt(1+x)
    print("Plotting sqrt(1+x)...")
    # Stays above x = -1 to avoid domain errors
    x_sqrt = np.linspace(-0.9, 5, 100)
    y_sqrt_true = np.sqrt(1 + x_sqrt)
    y_sqrt_approx = [f.func_sqrt1p(val, M) for val in x_sqrt]

    plt.figure(figsize=(8, 5))
    plt.plot(x_sqrt, y_sqrt_true, label='NumPy sqrt(1+x)', color='black', linewidth=2)
    plt.plot(x_sqrt, y_sqrt_approx, label=f'Continued Fraction (N={M})', color='red', linestyle='dashed', linewidth=2)
    
    plt.title('Square Root Function Comparison')
    plt.xlabel('x (Input)')
    plt.ylabel('y (Output)')
    plt.legend(fontsize=10)
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.tight_layout()
    
    plt.savefig('figures/05_sqrt_plot.pdf')
    plt.close()
   
if __name__ == "__main__":
    main()