#ifndef FFI_HPP
#define FFI_HPP

#include <string>
#include <unordered_map>
#include <functional>
#include <stdexcept>
#include <iostream>

extern "C" {
    typedef int(*ffi_func_ptr)(int, int);
}

class FFIRegistry {
public:
    static FFIRegistry& instance() {
        static FFIRegistry registry;
        return registry;
    }

    void register_func(const std::string& name, ffi_func_ptr fn) {
        registry[name] = fn;
    }

    ffi_func_ptr get(const char* name) {
        auto it = registry.find(name);
        if (it == registry.end())
            throw std::runtime_error("Function not found: " + std::string(name));
        return it->second;
    }

private:
    std::unordered_map<std::string, ffi_func_ptr> registry;
};

#define REGISTER_FFI(fn) \
    namespace { \
        struct fn##_registrar { \
            fn##_registrar() { \
                FFIRegistry::instance().register_func(#fn, fn); \
            } \
        }; \
        static fn##_registrar _##fn##_registrar_instance; \
    }

extern "C" {
    ffi_func_ptr ffi_get_function(const char* name);
}

#endif
