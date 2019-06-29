## lab5 report

### Step1
#### CMakeLists.txt
cmake_minimum_required(VERSION 3.3)
project(Tutorial)
set(Tutorial_VERSION_MAJOR 1)
set(Tutorial_VERSION_MINOR 0)
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)
configure_file(
    "${PROJECT_SOURCE_DIR}/TutorialConfig.h.in"
    "${PROJECT_BINARY_DIR}/TutorialConfig.h"
    )

add_executable(Tutorial tutorial.cxx)
target_include_directories(Tutorial PUBLIC
                             "${PROJECT_BINARY_DIR}"
                             )
#### tutorial.cxx
// A simple program that computes the square root of a number
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <string>
#include "TutorialConfig.h"
int main(int argc, char* argv[])
{
  if (argc < 2) {
    std::cout << "Usage: " << argv[0] << " number" << std::endl;
    return 1;
  }

  double inputValue = std::stod(argv[1]);

  double outputValue = sqrt(inputValue);
  std::cout << "The square root of " << inputValue << " is " << outputValue
            << std::endl;
  return 0;
}
#### screenshot ![step1](step1.PNG)

### step2
#### CMakeLists.txt
cmake_minimum_required(VERSION 3.3)
project(Tutorial)

set(CMAKE_CXX_STANDARD 14)

set(Tutorial_VERSION_MAJOR 1)
set(Tutorial_VERSION_MINOR 0)
configure_file(
  "${PROJECT_SOURCE_DIR}/TutorialConfig.h.in"
  "${PROJECT_BINARY_DIR}/TutorialConfig.h"
  )

option (USE_MYMATH "Use tutorial provided math implementation" ON)


if(USE_MYMATH)
  add_subdirectory(MathFunctions)
  list(APPEND EXTRA_LIBS MathFunctions)
  list(APPEND EXTRA_INCLUDES "${PROJECT_SOURCE_DIR}/MathFunctions")
endif(USE_MYMATH)

add_executable(Tutorial tutorial.cxx)

target_link_libraries(Tutorial ${EXTRA_LIBS})


target_include_directories(Tutorial PUBLIC
                           "${PROJECT_BINARY_DIR}"
                           )

#### tutorial.cxx
'''
// A simple program that computes the square root of a number
#include <cmath>
#include <iostream>
#include <string>

#include "TutorialConfig.h"

int main(int argc, char* argv[])
{
  if (argc < 2) {
    std::cout << argv[0] << " Version " << Tutorial_VERSION_MAJOR << "."
              << Tutorial_VERSION_MINOR << std::endl;
    std::cout << "Usage: " << argv[0] << " number" << std::endl;
    return 1;
  }

  double inputValue = std::stod(argv[1]);
 #ifdef USE_MYMATH
    double outputValue = mysqrt(inputValue);
  #else
    double outputValue = sqrt(inputValue);
  #endif
  std::cout << "The square root of " << inputValue << " is " << outputValue
            << std::endl;
  return 0;
}
'''
#### screenshot ![step2](step2.PNG)

### Step3
#### CMakeLists.txt
cmake_minimum_required(VERSION 3.3)
project(Tutorial)

set(CMAKE_CXX_STANDARD 14)


option(USE_MYMATH "Use tutorial provided math implementation" ON)


set(Tutorial_VERSION_MAJOR 1)
set(Tutorial_VERSION_MINOR 0)


configure_file(
  "${PROJECT_SOURCE_DIR}/TutorialConfig.h.in"
  "${PROJECT_BINARY_DIR}/TutorialConfig.h"
  )


if(USE_MYMATH)
  add_subdirectory(MathFunctions)
  list(APPEND EXTRA_LIBS MathFunctions)
  list(APPEND EXTRA_INCLUDES "${PROJECT_SOURCE_DIR}/MathFunctions")
endif(USE_MYMATH)


add_executable(Tutorial tutorial.cxx)

target_link_libraries(Tutorial ${EXTRA_LIBS})


target_include_directories(Tutorial PUBLIC
                           "${PROJECT_BINARY_DIR}"
                           ${EXTRA_INCLUDES}
                           )
target_include_directories(MathFunctions 
INTERFACE ${CMAKE_CURRENT_SOURCE_DIR})

add_library(MathFunctions mysqrt.cxx)

#### screenshot ![step3](step3.PNG)


### Step4
#### CMakeLists.txt
cmake_minimum_required(VERSION 3.3)
project(Tutorial)

set(CMAKE_CXX_STANDARD 14)
option(USE_MYMATH "Use tutorial provided math implementation" ON)

set(Tutorial_VERSION_MAJOR 1)
set(Tutorial_VERSION_MINOR 0)


configure_file(
  "${PROJECT_SOURCE_DIR}/TutorialConfig.h.in"
  "${PROJECT_BINARY_DIR}/TutorialConfig.h"
  )
if(USE_MYMATH)
  add_subdirectory(MathFunctions)
  list(APPEND EXTRA_LIBS MathFunctions)
endif(USE_MYMATH)
add_executable(Tutorial tutorial.cxx)

target_link_libraries(Tutorial PUBLIC ${EXTRA_LIBS})

target_include_directories(Tutorial PUBLIC
                           "${PROJECT_BINARY_DIR}"
                           )

install(TARGETS Tutorial DESTINATION bin)
install(FILES "${PROJECT_BINARY_DIR}/TutorialConfig.h"
        DESTINATION include
        )


enable_testing()


add_test(NAME Runs COMMAND Tutorial 25)


add_test(NAME Usage COMMAND Tutorial)
set_tests_properties(Usage
  PROPERTIES PASS_REGULAR_EXPRESSION "Usage:.*number"
  )

function(do_test target arg result)
  add_test(NAME Comp${arg} COMMAND ${target} ${arg})
  set_tests_properties(Comp${arg}
    PROPERTIES PASS_REGULAR_EXPRESSION ${result}
  )
endfunction(do_test)
do_test(Tutorial 25 "25 is 5")
do_test(Tutorial -25 "-25 is [-nan|nan|0]")
do_test(Tutorial 0.0001 "0.0001 is 0.01")
#### MathFunctions CMakeLists.txt
add_library(MathFunctions mysqrt.cxx)
target_include_directories(MathFunctions
          INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}
          )

install (TARGETS MathFunctions DESTINATION bin)
install (FILES MathFunctions.h DESTINATION include)

#### screenshot ![step4](step4.PNG) ![step4d](step4d.PNG)

### Step5
#### CMakeLists.txt
cmake_minimum_required(VERSION 3.3)
project(Tutorial)

set(CMAKE_CXX_STANDARD 14)
option(USE_MYMATH "Use tutorial provided math implementation" ON)


set(Tutorial_VERSION_MAJOR 1)
set(Tutorial_VERSION_MINOR 0)


configure_file(
  "${PROJECT_SOURCE_DIR}/TutorialConfig.h.in"
  "${PROJECT_BINARY_DIR}/TutorialConfig.h"
  )

if(USE_MYMATH)
  add_subdirectory(MathFunctions)
  list(APPEND EXTRA_LIBS MathFunctions)
endif()

add_executable(Tutorial tutorial.cxx)
target_link_libraries(Tutorial PUBLIC ${EXTRA_LIBS})
target_include_directories(Tutorial PUBLIC
                           "${PROJECT_BINARY_DIR}"
                           )


install(TARGETS Tutorial DESTINATION bin)
install(FILES "${PROJECT_BINARY_DIR}/TutorialConfig.h"
  DESTINATION include
  )


enable_testing()


add_test(NAME Runs COMMAND Tutorial 25)


add_test(NAME Usage COMMAND Tutorial)
set_tests_properties(Usage
  PROPERTIES PASS_REGULAR_EXPRESSION "Usage:.*number"
  )

function(do_test target arg result)
  add_test(NAME Comp${arg} COMMAND ${target} ${arg})
  set_tests_properties(Comp${arg}
    PROPERTIES PASS_REGULAR_EXPRESSION ${result}
    )
endfunction(do_test)


do_test(Tutorial 4 "4 is 2")
do_test(Tutorial 9 "9 is 3")
do_test(Tutorial 5 "5 is 2.236")
do_test(Tutorial 7 "7 is 2.645")
do_test(Tutorial 25 "25 is 5")
do_test(Tutorial -25 "-25 is [-nan|nan|0]")
do_test(Tutorial 0.0001 "0.0001 is 0.01")

include(CheckSymbolExists)
set(CMAKE_REQUIRED_LIBRARIES "m")
check_symbol_exists(log "math.h" HAVE_LOG)
check_symbol_exists(exp "math.h" HAVE_EXP)
#### MathFunctions CMakeLists.txt
add_library(MathFunctions mysqrt.cxx)

target_include_directories(MathFunctions
        INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}
        PRIVATE ${Tutorial_BINARY_DIR}
        )

install(TARGETS MathFunctions DESTINATION lib)
install(FILES MathFunctions.h DESTINATION include)

#### screenshot ![step5](step5.PNG) 

## The part I wish I learned before the bloody test

#### Makefile:
all: static_mf dynamic_mf
'''
# static library
static_mf: static_mf.o static_lib_thelib.a
	cc static_mf.o static_lib_thelib.a -o static_mf
static_lib_thelib.a: static_src.o
	ar qc static_lib_thelib.a static_src.o
static_mf.o: program.c
	cc -c program.c -o static_mf.o
static_src.o: ./source/block.c
	cc -c ./source/block.c -o static_src.o

# shared library
dynamic_mf: shared_mf.o shared_lib_thelib.so
	cc shared_mf.o shared_lib_thelib.so -o dynamic_mf -Wl,-rpath='$$ORIGIN'
shared_lib_thelib.so: dynamic_src.o
	cc -shared -o shared_lib_thelib.so dynamic_src.o
shared_mf.o: program.c
	cc -c program.c -o shared_mf.o
dynamic_src.o: ./source/block.c
	cc -fPIC -c ./source/block.c -o dynamic_src.o
'''
#### output ![part2make](part2make.png)

#### CMakeLists.txt
cmake_minimum_required(VERSION 1.0)
project(program)

set(program_VERSION_MAJOR 1)
set(program_VERSION_MINOR 0)

add_library(cshared SHARED ./source/block.c ./headers/block.h)
add_library(cstatic STATIC ./source/block.c ./headers/block.h)

add_executable(cmake_dynamic_mf program.c)
target_link_libraries(cmake_dynamic_mf cshared)

add_executable(cmake_static_mf program.c)
target_link_libraries(cmake_static_mf cstatic)

#### CMake's Makefile
'''
# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

# Default target executed when no arguments are given to make.
default_target: all

.PHONY : default_target

# Allow only one "make -f Makefile2" at a time, but pass parallelism.
.NOTPARALLEL:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /mnt/c/Users/yumin/Desktop/cshw/Lab-Example

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /mnt/c/Users/yumin/Desktop/cshw/Lab-Example/ah

#=============================================================================
# Targets provided globally by CMake.

# Special rule for the target rebuild_cache
rebuild_cache:
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --cyan "Running CMake to regenerate build system..."
	/usr/bin/cmake -H$(CMAKE_SOURCE_DIR) -B$(CMAKE_BINARY_DIR)
.PHONY : rebuild_cache

# Special rule for the target rebuild_cache
rebuild_cache/fast: rebuild_cache

.PHONY : rebuild_cache/fast

# Special rule for the target edit_cache
edit_cache:
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --cyan "No interactive CMake dialog available..."
	/usr/bin/cmake -E echo No\ interactive\ CMake\ dialog\ available.
.PHONY : edit_cache

# Special rule for the target edit_cache
edit_cache/fast: edit_cache

.PHONY : edit_cache/fast

# The main all target
all: cmake_check_build_system
	$(CMAKE_COMMAND) -E cmake_progress_start /mnt/c/Users/yumin/Desktop/cshw/Lab-Example/ah/CMakeFiles /mnt/c/Users/yumin/Desktop/cshw/Lab-Example/ah/CMakeFiles/progress.marks
	$(MAKE) -f CMakeFiles/Makefile2 all
	$(CMAKE_COMMAND) -E cmake_progress_start /mnt/c/Users/yumin/Desktop/cshw/Lab-Example/ah/CMakeFiles 0
.PHONY : all

# The main clean target
clean:
	$(MAKE) -f CMakeFiles/Makefile2 clean
.PHONY : clean

# The main clean target
clean/fast: clean

.PHONY : clean/fast

# Prepare targets for installation.
preinstall: all
	$(MAKE) -f CMakeFiles/Makefile2 preinstall
.PHONY : preinstall

# Prepare targets for installation.
preinstall/fast:
	$(MAKE) -f CMakeFiles/Makefile2 preinstall
.PHONY : preinstall/fast

# clear depends
depend:
	$(CMAKE_COMMAND) -H$(CMAKE_SOURCE_DIR) -B$(CMAKE_BINARY_DIR) --check-build-system CMakeFiles/Makefile.cmake 1
.PHONY : depend

#=============================================================================
# Target rules for targets named cshared

# Build rule for target.
cshared: cmake_check_build_system
	$(MAKE) -f CMakeFiles/Makefile2 cshared
.PHONY : cshared

# fast build rule for target.
cshared/fast:
	$(MAKE) -f CMakeFiles/cshared.dir/build.make CMakeFiles/cshared.dir/build
.PHONY : cshared/fast

#=============================================================================
# Target rules for targets named cmake_static_mf

# Build rule for target.
cmake_static_mf: cmake_check_build_system
	$(MAKE) -f CMakeFiles/Makefile2 cmake_static_mf
.PHONY : cmake_static_mf

# fast build rule for target.
cmake_static_mf/fast:
	$(MAKE) -f CMakeFiles/cmake_static_mf.dir/build.make CMakeFiles/cmake_static_mf.dir/build
.PHONY : cmake_static_mf/fast

#=============================================================================
# Target rules for targets named cmake_dynamic_mf

# Build rule for target.
cmake_dynamic_mf: cmake_check_build_system
	$(MAKE) -f CMakeFiles/Makefile2 cmake_dynamic_mf
.PHONY : cmake_dynamic_mf

# fast build rule for target.
cmake_dynamic_mf/fast:
	$(MAKE) -f CMakeFiles/cmake_dynamic_mf.dir/build.make CMakeFiles/cmake_dynamic_mf.dir/build
.PHONY : cmake_dynamic_mf/fast

#=============================================================================
# Target rules for targets named cstatic

# Build rule for target.
cstatic: cmake_check_build_system
	$(MAKE) -f CMakeFiles/Makefile2 cstatic
.PHONY : cstatic

# fast build rule for target.
cstatic/fast:
	$(MAKE) -f CMakeFiles/cstatic.dir/build.make CMakeFiles/cstatic.dir/build
.PHONY : cstatic/fast

# target to build an object file
program.o:
	$(MAKE) -f CMakeFiles/cmake_static_mf.dir/build.make CMakeFiles/cmake_static_mf.dir/program.o
	$(MAKE) -f CMakeFiles/cmake_dynamic_mf.dir/build.make CMakeFiles/cmake_dynamic_mf.dir/program.o
.PHONY : program.o

# target to preprocess a source file
program.i:
	$(MAKE) -f CMakeFiles/cmake_static_mf.dir/build.make CMakeFiles/cmake_static_mf.dir/program.i
	$(MAKE) -f CMakeFiles/cmake_dynamic_mf.dir/build.make CMakeFiles/cmake_dynamic_mf.dir/program.i
.PHONY : program.i

# target to generate assembly for a file
program.s:
	$(MAKE) -f CMakeFiles/cmake_static_mf.dir/build.make CMakeFiles/cmake_static_mf.dir/program.s
	$(MAKE) -f CMakeFiles/cmake_dynamic_mf.dir/build.make CMakeFiles/cmake_dynamic_mf.dir/program.s
.PHONY : program.s

# target to build an object file
source/block.o:
	$(MAKE) -f CMakeFiles/cshared.dir/build.make CMakeFiles/cshared.dir/source/block.o
	$(MAKE) -f CMakeFiles/cstatic.dir/build.make CMakeFiles/cstatic.dir/source/block.o
.PHONY : source/block.o

# target to preprocess a source file
source/block.i:
	$(MAKE) -f CMakeFiles/cshared.dir/build.make CMakeFiles/cshared.dir/source/block.i
	$(MAKE) -f CMakeFiles/cstatic.dir/build.make CMakeFiles/cstatic.dir/source/block.i
.PHONY : source/block.i

# target to generate assembly for a file
source/block.s:
	$(MAKE) -f CMakeFiles/cshared.dir/build.make CMakeFiles/cshared.dir/source/block.s
	$(MAKE) -f CMakeFiles/cstatic.dir/build.make CMakeFiles/cstatic.dir/source/block.s
.PHONY : source/block.s

# Help Target
help:
	@echo "The following are some of the valid targets for this Makefile:"
	@echo "... all (the default if no target is provided)"
	@echo "... clean"
	@echo "... depend"
	@echo "... rebuild_cache"
	@echo "... edit_cache"
	@echo "... cshared"
	@echo "... cmake_static_mf"
	@echo "... cmake_dynamic_mf"
	@echo "... cstatic"
	@echo "... program.o"
	@echo "... program.i"
	@echo "... program.s"
	@echo "... source/block.o"
	@echo "... source/block.i"
	@echo "... source/block.s"
.PHONY : help



#=============================================================================
# Special targets to cleanup operation of make.

# Special rule to run CMake to check the build system integrity.
# No rule that depends on this can have commands that come from listfiles
# because they might be regenerated.
cmake_check_build_system:
	$(CMAKE_COMMAND) -H$(CMAKE_SOURCE_DIR) -B$(CMAKE_BINARY_DIR) --check-build-system CMakeFiles/Makefile.cmake 0
.PHONY : cmake_check_build_system

'''
#### CMakerunning ![part2cmake](partcmake.PNG)

#### comparing ![part2comp](part2comp.PNG)

### The size for both dynamiclib programs are 8600, and for both staticlib programs are 8784