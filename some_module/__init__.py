""" Here is the docstring from the :code:`__init__.py` file. In this file, it is good practise to define
 :code:`__all__` so that anyone running :code:`import *` gets the right content!

 It is also good for removing unnecessary filenames. If you read the :code:`__init__.py` file, you can see that
 someone could now run :code:`from some_module import add_stuff` instead of
 having to run :code:`from some_module.code import integrate_trapz`.

 Also note that members without documentation (such as :code:`untested_subtract` do not appear in the doco).

 """
from .code import integrate_trapz
from .code import extract_sentence_containing_word

__all__ = ['extract_sentence_containing_word', 'integrate_trapz']
