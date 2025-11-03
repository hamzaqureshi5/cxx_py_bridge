# FFI

### *A Modern, Lightweight C++ → Python Foreign Function Interface with Automatic Registration*

FFI is a minimal, fast, and extensible **Foreign Function Interface
(FFI)** designed to make calling **C++ functions from Python** extremely
simple.\
It provides a **macro-based automatic function registry** in C++ and a
**clean Python loader** that resolves and exposes native functions with
zero boilerplate.

This framework is ideal for anyone building **AI modules**, **CPython
extensions**, **native compute kernels**, or embedding **C++
high-performance functions** into Python.

------------------------------------------------------------------------

## ✅ Features

-   **Automatic C++ function registration** using a single macro:

    ``` cpp
    REGISTER_FFI(fn_name);
    ```

-   **Shared registry** storing all exported functions\

-   **Python-side dynamic loading** via simple dictionary access\

-   Zero code generation\

-   Clean & minimal design\

-   Fully cross-platform (Linux, macOS, Windows)\

-   Supports Clang, GCC, and MSVC\

-   Easy to extend to floats, doubles, buffers, structs, and classes\

-   Works standalone or alongside **pybind11**

------------------------------------------------------------------------

## 📁 Project Structure

    ffi/
     ├── include/
     │    └── ffi.hpp
     ├── src/
     │    ├── ffi.cpp
     │    └── functions.cpp
     ├── python/
     │    └── ffi.py
     ├── CMakeLists.txt
     └── README.md

------------------------------------------------------------------------

## 🛠️ C++ Example

### **Define a function and register it**

``` cpp
#include "ffi.hpp"

extern "C" {

int llmx_add(int a, int b) { return a + b; }
REGISTER_FFI(llmx_add);

int llmx_mul(int a, int b) { return a * b; }
REGISTER_FFI(llmx_mul);

}
```

That's it.\
The functions are now discoverable and callable from Python.

------------------------------------------------------------------------

## ⚙️ Build Instructions (CMake)

### **Build**

``` bash
mkdir build
cd build
cmake ..
make -j8
```

Output:

    libllmx.so      (Linux)
    libllmx.dylib   (macOS)
    llmx.dll        (Windows)

------------------------------------------------------------------------

## 🐍 Python Usage

### **Load the FFI**

``` python
from ffi import ffi
```

### **Call C++ functions**

``` python
result = ffi.cpp_functions["llmx_add"](2, 5)
print(result)  # 7
```

Minimal and clean.

------------------------------------------------------------------------

## 📦 Installing the Library

### Optional (system-wide installation):

``` bash
sudo make install
```

Then Python can load:

``` python
ffi = CPPFFI("libllmx.so")
```

------------------------------------------------------------------------

## 🧠 Use Cases

-   High-performance ML/AI ops\
-   Embedding C++ kernels in Python projects\
-   Rapid prototyping of native accelerators\
-   Game engines and simulation tools\
-   Plugin-based architectures\
-   Replacing slow Python loops with optimized C++

------------------------------------------------------------------------

## 📌 Roadmap

-   [ ] Support for `float` / `double`\
-   [ ] String interop\
-   [ ] Struct marshalling\
-   [ ] Automatic discovery of all registered functions in Python\
-   [ ] Python type hints & stub generation\
-   [ ] PyPI package (`pip install ffi`)\
-   [ ] Add class and object binding

------------------------------------------------------------------------

## 🤝 Contributing

Contributions are welcome.\
Open an issue or PR with a clear description and code samples.

------------------------------------------------------------------------

## 📜 License

MIT License -- free for commercial and personal use.
