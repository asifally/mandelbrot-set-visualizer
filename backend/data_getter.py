from sympy import symbols, lambdify
import numpy as np
import typing

class MandelbrotSetGetter:
    """
    Returns data in order to depict the Mandelbrot Set
    f(z) = z^2 + c where c is a complex number
    """

    def _compute_iterations(self, complex_number: complex, max_iter: int):
        z = 0
        for n in range(max_iter):
            if abs(z) > 2:
                # diverges
                return n
            z = z**2 + complex_number
        
        return max_iter

    def get_mandelbrot_set(self, xmin, xmax, ymin, ymax, width, height, max_iter) -> typing.List[typing.List[int]]:
        x = np.linspace(xmin, xmax, width)
        y = np.linspace(ymin, ymax, width)

        mandelbrot_set = np.zeros((height, width))

        for i in range(height):
            for j in range(width):
                c = complex(x[j], y[i])
                mandelbrot_set[i, j] = self._compute_iterations(c, max_iter)

        return mandelbrot_set