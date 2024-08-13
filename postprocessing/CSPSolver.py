from constraint import *

problem = Problem()
problem.addVariable("x38", [0, 1])
problem.addVariable("x88", [0, 1])
problem.addVariable("x98", [0, 1])
problem.addVariable("x104", [0, 1])

problem.addConstraint(lambda x38: x38 == 1, ["x38"])
problem.addConstraint(lambda x88: x88 == 1, ["x88"])
problem.addConstraint(lambda x38, x98: x38 ^ x98, ["x38", "x98"])
problem.addConstraint(lambda x88, x104: x88 ^ x104, ["x88", "x104"])

print(problem.getSolutions())
