# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from pyqir.evaluator.qrackgateset import QrackGateSet
from pyqir.evaluator._native import PyNonadaptiveJit # type: ignore
from typing import List, Optional


class QrackEvaluator:
    """
    The non-adaptive JIT evaluates QIR programs without simulating the quantum
    state. Measurement results are pre-determined before the program starts.
    """

    def __init__(self):
        self._jit = PyNonadaptiveJit()

    def eval(self,
             file_path: str,
             gateset: QrackGateSet,
             entry_point: Optional[str] = None):
        """
        JIT compiles and evaluates the QIR program, delegating quantum
        operations to the supplied gate set.

        The result stream will be read in order by the measurement instruction.
        Each measurement will pop a result from the beginning of the stream. If
        the stream runs out of results, measurement returns zero.

        Right now the evaluator does not have a full runtime environment and can
        JIT QIR produced by the pyqir-generator, but cannot use any external function
        calls.

        :param file_path: file path of existing QIR in a ll or bc file
        :param gateset: python GateSet based object defining the operations
        :param entry_point: entry point name; required if QIR contains multiple entry points
        :param result_stream: list of boolean result values representing the QIS measure results
        """
        self._jit.eval(file_path, gateset, entry_point, result_stream)
