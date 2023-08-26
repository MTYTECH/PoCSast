from codeundertest import is_third_byte_zero  # import function to be tested
from pythonfuzz.main import PythonFuzz        # import fuzz test infrastructure
   
# The fuzz engine calls a function called `fuzz` in the fuzz target and
# passes it random bytes, so we need to define a function with that name,
# and that function must accept 1 parameter.
   
@PythonFuzz                           # Python decorator required by fuzz test infrastructure
	def fuzz(random_bytes):               # Accept random data...
	    is_third_byte_zero(random_bytes)  # ...and pass it on to the code-under-test.
	   
	if __name__ == '__main__':            # required by fuzz test infrastructure
	    fuzz()
