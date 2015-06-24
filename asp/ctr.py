#script (python)

from gringo import *
from pprint import pprint

def onModel(model):
    atoms = model.atoms(Model.ATOMS)
    events = getFluents(atoms, "ticker")
    states = getFluents(atoms, "holds" )
    attributes = getFluents(atoms, "attribute" , time=False)
    for time in range(len(states)):
        print "{}".format(time)
        if time in events:
            for e in events[time]:
                print "[e]  {}".format(e)
                for att in attributes:
                    if att[0] == e: print "---  {}: {}".format(att[1], att[2])
        print "[s] "
        for s in states[time]:
            print "     {}".format(s)

def getFluents(atoms, name, time=True):
    if time:
        fluents = {}
        for (lit,time) in [atom.args() for atom in atoms if atom.name() == name]:
            if time not in fluents:
                fluents[time] = [lit]
            else:
                fluents[time].append(lit)
        return fluents
    else:
        return [atom.args() for atom in atoms if atom.name() == name]

def main(ctr):
    ctr.ground([("base", [])])
    ret = ctr.solve([], onModel)

#end.
