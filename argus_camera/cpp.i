%module cpp

%include <std_string.i>
%include <std_vector.i>
%include <stdint.i>
%include <carrays.i>

%typemap(in) uint8_t* {
  $1 = (uint8_t*) PyInt_AsLong($input);
}

%typemap(argout) int *info {
  PyObject *o;
  o = PyLong_FromLong(*$1);
  $result = SWIG_Python_AppendOutput($result, o);
}

namespace std {
  %template (UInt32Vector) std::vector<uint32_t>;
  %template (UInt64Vector) std::vector<uint64_t>;
  %template (FloatVector) std::vector<float>;
  %template (FloatVectorVector) std::vector<std::vector<float>>;
}

%{
#include "../src/ArgusCamera.hpp"
%}

%include "../src/ArgusCamera.hpp"
