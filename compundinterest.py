def compound_interest(pr,ra,ti):
    amount =float(pr * (pow((1+ra/100),ti)))
    compi =float(amount - pr)
    print('Compound Interest : ', compi)

p =float( input( 'P = '))
r = float ( input( 'r = '))
t = float(input('t : '))
compound_interest(p,r,t)
