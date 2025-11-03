cmake_minimum_required(VERSION 3.14)
project(llmx-ffi VERSION 1.0 LANGUAGES CXX)

# ===========================
# Build Configuration
# ===========================
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED YES)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

# Allow Release builds by default
if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Release)
endif()

# ===========================
# Library Target
# ===========================
add_library(llmx SHARED
    src/ffi.cpp
    src/functions.cpp
)

target_include_directories(llmx
    PUBLIC
        ${PROJECT_SOURCE_DIR}/include
)

# For Clang/GCC warnings (optional but recommended)
target_compile_options(llmx PRIVATE
    -Wall -Wextra -Werror
)

# ===========================
# Installation
# ===========================
include(GNUInstallDirs)

install(TARGETS llmx
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)

install(FILES include/ffi.hpp
    DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
)

# ===========================
# Summary Output
# ===========================
message(STATUS "Build type:        ${CMAKE_BUILD_TYPE}")
message(STATUS "Install prefix:    ${CMAKE_INSTALL_PREFIX}")
message(STATUS "C++ Standard:      ${CMAKE_CXX_STANDARD}")
