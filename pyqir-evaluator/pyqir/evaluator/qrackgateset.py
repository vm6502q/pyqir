# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from pyqrack import QrackSimulator, Pauli

class QrackGateSet:
    """
    Defines the quantum circuit operations which may be registered for
    callbacks during evaluation of QIR
    """
    
    def __init__(self):
        self._sim = QrackSimulator()
        self._qubit_dict = dict()
        self._measurement_dict = dict()

    def _checkAlloc(self, qubit: str):
        if not qubit in self._qubit_dict.values():
            self._sim.allocate_qubit(len(self._qubit_dict))
        return self._qubit_dict[qubit]

    def cx(self, control: str, target: str):
        self._sim.mcx([self._checkAlloc(control)], self._checkAlloc(target))

    def cz(self, control: str, target: str):
        self._sim.mcz([self._checkAlloc(control)], self._checkAlloc(target))

    def h(self, target: str):
        self._sim.h(self._checkAlloc(target))

    def m(self, qubit: str, target: str):
        self._measurement_dict[target] = self._sim.m(self._checkAlloc(target))

    def mz(self, qubit: str, target: str):
        self._measurement_dict[target] = self._sim.m(self._checkAlloc(target))

    def reset(self, target: str):
        q = self._checkAlloc(target)
        if self._sim.m(q):
            self._sim.x(q)

    def rx(self, theta: float, qubit: str):
        self._sim.r(Pauli.PauliX, self._checkAlloc(target))

    def ry(self, theta: float, qubit: str):
        self._sim.r(Pauli.PauliY, self._checkAlloc(target))

    def rz(self, theta: float, qubit: str):
        self._sim.r(Pauli.PaulZ, self._checkAlloc(target))

    def s(self, qubit: str):
        self._sim.s(self._checkAlloc(target))

    def s_adj(self, qubit: str):
        self._sim.adjs(self._checkAlloc(target))

    def t(self, qubit: str):
        self._sim.t(self._checkAlloc(target))

    def t_adj(self, qubit: str):
        self._sim.adjt(self._checkAlloc(target))

    def x(self, qubit: str):
        self._sim.x(self._checkAlloc(target))

    def y(self, qubit: str):
        self._sim.y(self._checkAlloc(target))

    def z(self, qubit: str):
        self._sim.z(self._checkAlloc(target))

    def finish(self, metadata: dict):
        """
        Called at the end of QIR evaluation supplying run metadata.
        """
        metadata['classical_registers'] = self._measurement_dict

