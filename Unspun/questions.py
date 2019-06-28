"""
Using Python 2.7, or 3.3-3.5 syntax/semantics, please fill out the bodies of
the included functions to include implementations of what is described in the
docstrings.

You can test your answers against the __basic__ included unittests by running:
`python -m doctest questions.py`
"""

import re
def list_of_integers():
    L= []
    i=0
    for x in range(17, 100):
        if(x % 11 == 0):
            L.insert(i,x);
            i = i+1
    return L

def dict_mapping():
    L= {}
    for x in range(2, 100):
        L[x]=x**(1/2.75)
    return L

def generate_cubes_until(modulus):
    list1 = []
    list1.append(1)
    i=2
    while(1):
        if(modulus%i != 0):
            list1.append(i**3)
            i = i+1
        else:
            break;
    return list1


def check_type(typ):
    assert len(types) == typ.func_code.co_argcount
    def new_f(*args, **kwds):
        for (a, t) in zip(args, types):
            assert isinstance(a, t), \
                   "arg %r does not match %s" % (a,t)
        return typ(*args, **kwds)
    new_f.func_name = typ.func_name
    return new_f


def left_turn(one, two, three):
    n1 = two[1]-one[1]
    n2 = three[1]-two[1]
    d1 = two[0]-one[0]
    d2 = three[0]-two[0]
    s1 = 0
    s2 = 0
    if(d1 == 0):
        if(n1>0):
            s1 = 10000
        if(n1<0):
            s1 = -10000
        if(n1 == 0):
            s1 = 0
    if(d1 != 0):
        s1 = n1/d1
    if(d2 == 0):
        if(n2>0):
            s2 = 10000
        if(n2<0):
            s2 = -10000
        if(n2 == 0):
            s2 = 0
    if(d2 != 0):
        s2 = n2/d2
    result = s1 * s2
    if(result > 0):
        return "true"
    if(result <= 0):
        return "false"



def nearest_point(candidate_points, points):
    dist = 10000
    p1 = []
    for c in candidate_points:
        curr_dist = 0
        for p in points:
            curr_dist = (p[0]-c[0])*(p[0]-c[0]) + (p[1]-c[1])*(p[1]-c[1])
            if(curr_dist<=dist):
                dist = curr_dist
                p1 = c
    print(p1)
    return p1

nearest_point([(0.1, 0.1), (2, 2), (2, 3)], [(0, 0), (5, 5), (2, 1), (2, 4)])

def is_a_square(one, two, three, four, threshold=0.0):
    a = [0 for x in range(6)]
    a[0] = (one[0]-two[0])*(one[0]-two[0]) + (one[1]-two[1])*(one[1]-two[1])
    a[1] = (one[0]-three[0])*(one[0]-three[0]) + (one[1]-three[1])*(one[1]-three[1])
    a[2] = (one[0]-four[0])*(one[0]-four[0]) + (one[1]-four[1])*(one[1]-four[1])
    a[3] = (three[0]-two[0])*(three[0]-two[0]) + (three[1]-two[1])*(three[1]-two[1])
    a[4] = (four[0]-two[0])*(four[0]-two[0]) + (four[1]-two[1])*(four[1]-two[1])
    a[5] = (four[0]-three[0])*(four[0]-three[0]) + (four[1]-three[1])*(four[1]-three[1])
    for x in a:
        count=0
        for y in a:
            if(x==y):
                count = count + 1
        if(count==4):
            return "true"
    return "false"