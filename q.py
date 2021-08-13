import math
import numpy as np 
import random

# Multiply matrix with vector
def mulMat(vec, mat):
	vec0 = (vec[0] * mat[0][0]) + (vec[1] * mat[1][0])
	vec1 = (vec[0] * mat[0][1]) + (vec[1] * mat[1][1])

	newVec = np.array([vec0, vec1])
	return newVec

# Pick random logic gate and mulitply with vector
def randPickLoop(seq, logicList):

	# Starting Vector
	vec = np.array([1.0, 0.0])

	# Final Vector
	finalVec = np.array([-1.0, 0.0])	

	while str(finalVec) != str(vec):
		gate = random.choice(logicList) 
		seq.append(gate[2])				
		vec = mulMat(vec,gate)

	return seq


# Logic Gates X, Z and H as matrices 
Hnum =  1/math.sqrt(2)
X = [[0,1],[1,0],'X']
Z = [[1,0],[0,-1],'Z']
H = [[1*Hnum, 1*Hnum],[1*Hnum, -1*Hnum],'H']

q2LogicList = [X,H]
q2Seq = []

randPickLoop(q2Seq, q2LogicList)	

q3LogicList = [X,Z,H]
q3Seq = []

# Assume smallest number of gates and change accordingly
while len(q3Seq) > 3 or len(q3Seq) == 0:
	q3Seq = []
	q3Seq = randPickLoop(q3Seq, q3LogicList)

q2Seq = ''.join(q2Seq)
q3Seq = ''.join(q3Seq)

print(f"Sequences of X & H gates: {q2Seq}")	
print(f"Smallest number of sequences of X & Z gates: {q3Seq}")	