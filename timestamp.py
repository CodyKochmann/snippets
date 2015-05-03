def timestamp(human_readable=False):
  # Generates a unix timestamp and a human readable timestamp if passed True
  # by: Cody Kochmann
  from calendar import timegm
  from datetime import datetime
  if human_readable:
    return(datetime.now())
  else:
    return(str(timegm(datetime.now().utctimetuple())))
