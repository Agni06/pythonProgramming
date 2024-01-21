def getPay(hours):
  #per hour $15
  amt = hours*15
  #tax 25%
  fin = amt - (amt*(0.25))
  return fin
