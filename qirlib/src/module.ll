%Qubit = type opaque
%Result = type opaque

define void @QuantumApplication__Run__body() #0 {
entry:
  ret void
}

declare void @__quantum__qis__cnot__body(%Qubit*, %Qubit*)
declare void @__quantum__qis__cz__body(%Qubit*, %Qubit*)
declare void @__quantum__qis__h__body(%Qubit*)
declare void @__quantum__qis__s__body(%Qubit*)
declare void @__quantum__qis__s__adj(%Qubit*)
declare void @__quantum__qis__t__body(%Qubit*)
declare void @__quantum__qis__t__adj(%Qubit*)
declare void @__quantum__qis__x__body(%Qubit*)
declare void @__quantum__qis__y__body(%Qubit*)
declare void @__quantum__qis__z__body(%Qubit*)
declare void @__quantum__qis__rx__body(double, %Qubit*)
declare void @__quantum__qis__ry__body(double, %Qubit*)
declare void @__quantum__qis__rz__body(double, %Qubit*)
declare void @__quantum__qis__reset__body(%Qubit*)
declare %Result* @__quantum__qis__m__body(%Qubit*)
declare %Result* @__quantum__rt__result_get_one()
declare %Result* @__quantum__rt__result_get_zero()
declare i1 @__quantum__rt__result_equal(%Result*, %Result*)
declare %Qubit* @__quantum__rt__qubit_allocate()
declare void @__quantum__rt__qubit_release(%Qubit*)

attributes #0 = { "EntryPoint" }
