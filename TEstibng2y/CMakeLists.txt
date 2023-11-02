cmake_minimum_required(VERSION 3.0)
project(Stickman)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Reemplaza <your_vcpkg_install_path> con la ruta de instalación de vcpkg en tu sistema
set(VCPKG_PATH "/Users/vigowalker/code/vcpkg")

include_directories(${VCPKG_PATH}/installed/x64-osx/include)
link_directories(${VCPKG_PATH}/installed/x64-osx/lib)

find_package(SDL2 REQUIRED)

# Encuentra las bibliotecas Box2D
find_library(BOX2D_LIBRARY_RELEASE NAMES Box2D PATHS ${VCPKG_PATH}/installed/x64-osx/lib)
find_library(BOX2D_LIBRARY_DEBUG NAMES Box2D PATHS ${VCPKG_PATH}/installed/x64-osx/debug/lib)

# Configura la biblioteca Box2D para enlazar con el proyecto
add_library(Box2D STATIC IMPORTED)
set_target_properties(Box2D PROPERTIES
  IMPORTED_LOCATION_RELEASE ${BOX2D_LIBRARY_RELEASE}
  IMPORTED_LOCATION_DEBUG ${BOX2D_LIBRARY_DEBUG}
)

add_executable(Stickman main.cpp)

target_link_libraries(Stickman PRIVATE SDL2::SDL2 SDL2::SDL2main Box2D)
