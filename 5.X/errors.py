## A useful dict with error codes to text
#
# Author: Bas van der Vlies <bas.vandervlies@surfsara.nl>
#
# SVN Info:
#	$Id: errors.py 429 2005-11-04 13:59:06Z bas $
#

def error():
  """
  Check if there is an error, if so fetch the error message string. 
  It says more then a number!
  """
  e = get_error()
  return (e, pbs_strerror(e))
#     return (e, errors_txt[e])
#  else:
#     return (e, "Could not find a text for this error, uhhh")
