import numpy as np


class Relations():
    def __init__(self, s, R):
        self.s = s
        self.R = R
        self.M = np.zeros((len(s), len(s)))
        for i in R:
            self.M[i[0]-1][i[1]-1] = 1

    def returnMatrix(self):
        return self.M

    def isReflexive(self):
        for i in range(len(self.M)):
            if self.M[i][i] == 0:
                return False
        return True

    def isIrreflexive(self):
        for i in range(len(self.M)):
            if self.M[i][i] == 1:
                return False
        return True

    def isSymmetric(self):
        T = self.M.transpose()
        if np.array_equal(T, self.M):
            return True
        return False

    def isAntisymmetric(self):
        if self.isSymmetric():
            return False
        return True

    def isTransitive(self):
        M = self.M
        Msquare = np.dot(M, M)
        # A relation R ⊆ A × A is transitive iff R has the property that for all x, y, z ∈ A, whenever (x, y) ∈ R and (y, z) ∈ R, then (x, z) ∈ R.
        for i in range(len(M)):
            for j in range(len(M)):
                if Msquare[i][j] == 1:
                    if M[i][j] == 0:
                        return False
        return True

    def isTrichotomy(self):
        # A relation R on A satisfies the requirement for trichotomy iff, for every x and y
        # chosen from A such that x ≠ y, we have that x and y are comparable,
        # i.e. for all x, y ∈ A such that x ≠ y, x R y or y R x (i.e. (x, y) ∈ R or (y, x) ∈ R).
        for i in range(len(self.M)):
            for j in range(len(self.M)):
                if i != j:
                    if self.M[i][j] == 0 and self.M[j][i] == 0:
                        return False
        return True

    def EquivalenceRelation(self):
        if self.isReflexive() and self.isSymmetric() and self.isTransitive():
            return True
        return False

    def WeakPartialOrder(self):
        if self.isReflexive() and self.isTransitive() and self.isAntisymmetric():
            return True
        return False

    def StrictPartialOrder(self):
        if self.isTransitive() and self.isAntisymmetric() and self.isIrreflexive():
            return True
        return False

    def WeakTotalOrder(self):
        if self.isReflexive() and self.isTransitive() and self.isTrichotomy():
            return True
        return False

    def StrictTotalOrder(self):
        if self.isTransitive() and self.isTrichotomy() and self.isIrreflexive():
            return True
        return False

    def StrictEquivalenceRelation(self):
        if self.EquivalenceRelation() and self.isIrreflexive():
            return True
        return False

    def printPropertiesOfRelation(self):
        # print only the properties that are true
        if self.isReflexive():
            print("Reflexive")
        if self.isIrreflexive():
            print("Irreflexive")
        if self.isSymmetric():
            print("Symmetric")
        if self.isAntisymmetric():
            print("Antisymmetric")
        if self.isTransitive():
            print("Transitive")
        if self.isTrichotomy():
            print("Trichotomy")
        if self.EquivalenceRelation():
            print("Equivalence Relation")
        if self.StrictEquivalenceRelation():
            print("Strict Equivalence Relation")
        if self.WeakPartialOrder():
            print("Weak Partial Order")
        if self.StrictPartialOrder():
            print("Strict Partial Order")
        if self.WeakTotalOrder():
            print("Weak Total Order")
        if self.StrictTotalOrder():
            print("Strict Total Order")

# Using set
#s = {0,a,b,ab}
#R = {(0,{a}),(0,{b}),(0,{a,b}),({a},{b}),({a},{a,b}),({b},{a,b})}


# since our class uses numerical values, we need to convert the set to a list of numbers and tuples of ordered pairs
s = [1, 2, 3,4]
#    0  a  b  ab

R = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
r1 = Relations(s, R)
r1.printPropertiesOfRelation()

# Output
# Irreflexive
# Antisymmetric
# Transitive
# Trichotomy
# Strict Partial Order
# Strict Total Order
