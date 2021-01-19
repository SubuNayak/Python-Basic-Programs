def simpleinterest(pr,ra,ti):
    simp = (pr * ra * ti)/100
    return simp
p = int ( input( 'P = '))
r = int ( input( 'r = '))
t = int ( input('t = '))
s = simpleinterest(p,r,t)
print('Output :',s)