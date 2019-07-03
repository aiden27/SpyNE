import numpy as np

from autodiff.operations.base import UniTensorOperation
from autodiff.operations.utils import nest_func


class TensorSum(UniTensorOperation):
    name = 'Tensor Sum'

    def execute(self):
        return self._a.sum()

    def vector_jacobian_product(self, func=lambda g: g):
        internal_shape = self._a.shape

        @nest_func(func)
        def a_vjp(g):
            if g.shape == ():
                return g * np.ones(internal_shape)
            else:
                raise NotImplementedError('''the VJP builder for TensorSum can only handle 
                                          scalar arguments for now.''')
        return a_vjp


class TensorSquared(UniTensorOperation):
    name = 'Tensor Square'

    def execute(self):
        return np.square(self._a)

    def vector_jacobian_product(self, func=lambda g: g):
        a = self._a

        @nest_func(func)
        def a_vjp(g):
            return g * 2 * a

        return a_vjp
