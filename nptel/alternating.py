def updown(l):
  if len(l) < 2:
    return(True)
  return(l[0] < l[1] and downup(l[1:]))

def downup(l):
  if len(l) < 2:
    return(True)
  return(l[0] > l[1] and updown(l[1:]))
    
def alternating(l):
  return(updown(l) or downup(l))