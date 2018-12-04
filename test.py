import turtle as tu
def floc(l) :
  if l<3 :
    tu.fd(l)
    return
  floc(l/3)
  tu.lt(60)
  floc(l/3)
  tu.rt(120)
  floc(l/3)
  tu.lt(60)
  floc(l/3)
 
def flocon(l)  :
  tu.speed(0)
  tu.color('#0000ff', '#55ffff')
  tu.begin_fill()
  for i in range(3) :
    floc(l)
    tu.rt(120)
  tu.end_fill()
 
flocon(100)