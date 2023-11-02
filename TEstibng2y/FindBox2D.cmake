# Find Box2D library and include directory
# Box2D_FOUND - system has Box2D
# Box2D_INCLUDE_DIRS - Box2D include directories
# Box2D_LIBRARIES - link these to use Box2D

find_path(Box2D_INCLUDE_DIR Box2D/Box2D.h
  HINTS
    ${VCPKG_PATH}/installed/x64-osx/include
)

find_library(Box2D_LIBRARY_RELEASE NAMES Box2D
  HINTS
    ${VCPKG_PATH}/installed/x64-osx/lib
)

find_library(Box2D_LIBRARY_DEBUG NAMES Box2D
  HINTS
    ${VCPKG_PATH}/installed/x64-osx/debug/lib
)

include(FindPackageHandleStandardArgs)
find_package_handle_standard_args(Box2D DEFAULT_MSG
  Box2D_LIBRARY_RELEASE
  Box2D_INCLUDE_DIR
)

if(Box2D_FOUND AND NOT TARGET Box2D)
  add_library(Box2D INTERFACE IMPORTED)
  set_target_properties(Box2D PROPERTIES
    INTERFACE_INCLUDE_DIRECTORIES "${Box2D_INCLUDE_DIR}"
    INTERFACE_LINK_LIBRARIES "$<$<CONFIG:Release>:${Box2D_LIBRARY_RELEASE}>;$<$<CONFIG:Debug>:${Box2D_LIBRARY_DEBUG}>"
  )
endif()

