import ctypes
from ctypes import c_int, c_char_p
import os
import ctypes
from ctypes import c_int, c_char_p


class CPPFFI:
    def __init__(self, lib_path=None):
        if lib_path is None:
            # automatic search
            search_paths = ["./libllmx.so", "../build/libllmx.so", "../libllmx.so"]
            for p in search_paths:
                if os.path.exists(p):
                    lib_path = p
                    break

        if lib_path is None:
            raise FileNotFoundError("libllmx.so not found.")

        self.lib = ctypes.CDLL(lib_path)

        self.lib.ffi_get_function.argtypes = [c_char_p]
        self.lib.ffi_get_function.restype = ctypes.c_void_p

        self.cpp_functions = {}

    def load(self, name):
        fn_ptr = self.lib.ffi_get_function(name.encode())
        func = ctypes.CFUNCTYPE(c_int, c_int, c_int)(fn_ptr)
        self.cpp_functions[name] = func
        return func


# class CPPFFI:
#     def __init__(self, lib_path: str):
#         self.lib = ctypes.CDLL(lib_path)

#         self.lib.ffi_get_function.argtypes = [c_char_p]
#         self.lib.ffi_get_function.restype = ctypes.c_void_p

#         self.cpp_functions = {}

#     def load(self, name: str):
#         fn_ptr = self.lib.ffi_get_function(name.encode())
#         if not fn_ptr:
#             raise ValueError(f"Function not found: {name}")

#         func = ctypes.CFUNCTYPE(c_int, c_int, c_int)(fn_ptr)
#         self.cpp_functions[name] = func
#         return func


# Global FFI instance
# ffi = CPPFFI("./libllmx.so")
ffi_ = CPPFFI("../build/libllmx.so")

# Auto load your functions
for fname in ["llmx_add", "llmx_mul", "llmx_sub", "llmx_divide"]:
    ffi_.load(fname)
