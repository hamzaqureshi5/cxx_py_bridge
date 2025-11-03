#include "ffi.hpp"

extern "C" {

int llmx_add(int a, int b) { return a + b; }
REGISTER_FFI(llmx_add)

int llmx_mul(int a, int b) { return a * b; }
REGISTER_FFI(llmx_mul)

int llmx_sub(int a, int b) { return a - b; }
REGISTER_FFI(llmx_sub)

int llmx_divide(int a, int b) { return a / b; }
REGISTER_FFI(llmx_divide)

}
