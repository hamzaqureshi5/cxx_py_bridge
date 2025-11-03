#include "ffi.hpp"

extern "C" ffi_func_ptr ffi_get_function(const char *name) {
  return FFIRegistry::instance().get(name);
}
