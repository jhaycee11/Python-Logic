import pdb


li = [
    "Luffy",
    "nami",
    "chopper",
]


def make_upper(l):
    pdb.set_trace()
    for i in l: 
        i.upper()
    return list(map(make_upper, l))

make_upper(li)