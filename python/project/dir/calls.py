# from ffi import ffi

from ..ffi import ffi_

# from ffi import ffi

print(ffi_.cpp_functions["llmx_add"](3, 4))  # 7
print(ffi_.cpp_functions["llmx_mul"](6, 7))  # 42
print(ffi_.cpp_functions["llmx_sub"](10, 3))  # 7
print(ffi_.cpp_functions["llmx_divide"](20, 5))  # 4
