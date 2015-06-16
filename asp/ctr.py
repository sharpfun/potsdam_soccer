#script (python)

from gringo import *
from pprint import pprint

def onModel(model):
    atoms = model.atoms(Model.ATOMS)
    events = getEvents(atoms)
    states = getStates(atoms)
    for time in range(len(states)):
        print "{}".format(time)
        if time in events:
            for e in events[time]:
                print "[e]  {}".format(e)
        print "[s] "
        for s in states[time]:
            print "     {}".format(s)

def getEvents(atoms):
    events = {}
    for (lit,time) in [atom.args() for atom in atoms if atom.name() == "ticker"]:
        if time not in events:
            events[time] = [lit]
        else:
            events[time].append(lit)
    return events

def getStates(atoms):
    states = {}
    for (lit,time) in [atom.args() for atom in atoms if atom.name() == "holds"]:
        if time not in states:
            states[time] = [lit]
        else:
            states[time].append(lit)
    return states

def main(ctr):
    ctr.ground([("base", [])])
    ret = ctr.solve([], onModel)

#end.
