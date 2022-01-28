import number_theory as utils

p = 2**255 - 19
#q = 2**252 + 27742317777372353535851937790883648493
# eqn => y^2 = x^3 + Ax^2 + x
A = 486662

a = 3413124334234343
assert (utils.inv(a,p) == utils.fermat_inv(a,p))

def onCurve(P):
    x = P[0]
    y = P[1]
    assert (y**2)%p == (x**3 + A*x**2 + x)%p

def add (P,Q):
    x1 = P[0]
    y1 = P[1]
    x2 = Q[0]
    y2 = Q[1]
    assert utils.fermat_inv(x2-x1,p) == utils.inv(x2-x1,p)
    lamda = ((y2-y1)%p * utils.fermat_inv(x2-x1,p)) %p
    x3 = ((lamda**2)%p - (A + x1 + x2 )%p )%p
    y3 = (y1%p + (lamda*(x3-x1))%p)%p
    onCurve((x3,y3))
    return (x3,y3)

def nG(G,n): #returns 2G, n is not used
    x1 = G[0]
    y1 = G[1]
    x2 = G[0]
    y2 = G[1]
    lamda = (((3*x1**2 + 2*A*x1 + 1)%p)*(utils.inv((2*y1)%p,p)))%p
    print ("a : " + str(2*y1%p))
    print ("inverse : " + str(utils.inv((2*y1)%p,p)%p))
    x3 = ((lamda**2)%p - (A + x1 + x2 )%p )%p
    y3 = (y1%p + (lamda*(x3-x1))%p)%p
    print(x3)
    print(y3)
    onCurve((x3,y3))
    return (x3,y3)


G = [9 , 14781619447589544791020593568409986887264606134616475288964881837755586237401]

P=( 12697861248284385512127539163427099897745340918349830473877503196793995869202 , 18782504731206017997790968374142055202547214238579664877619644464800823583275 )
Q=( 14847277145635483483963372537557091634710985132825781088887140890597596352251 , 48981431527428949880507557032295310859754924433568441600873610210018059225738 )

onCurve(P)
onCurve(Q)

nG(G,2)

