# Alex Tran
# Anahid Zandi Haghighi
from logic import *

ATruthoraptor = Symbol("A is a Truthoraptor")
ALieosaurus = Symbol("A is a Lieosaurus")

BTruthoraptor = Symbol("B is a Truthoraptor")
BLieosaurus = Symbol("B is a Lieosaurus")

CTruthoraptor = Symbol("C is a Truthoraptor")
CLieosaurus = Symbol("C is a Lieosaurus")

# Puzzle 0
# A says "I am both a Truthoraptor and a Lieosaurus."
knowledge0 = And( 
    And(Or(ALieosaurus, ATruthoraptor), Not(And(ALieosaurus, ATruthoraptor))), Implication(ALieosaurus, Not(And(ATruthoraptor, ALieosaurus))), Implication(ATruthoraptor, (And(ATruthoraptor, ALieosaurus)))
)

# Puzzle 1
# A says "We are both Lieosauruss."
# B says nothing.
knowledge1 = And(
    And(Or(ALieosaurus, ATruthoraptor), Not(And(ALieosaurus, ATruthoraptor))), And(Or(BLieosaurus, BTruthoraptor), Not(And(BLieosaurus, BTruthoraptor))), Implication(ALieosaurus, Not(And(ALieosaurus, BLieosaurus))), Implication(ATruthoraptor,(And(ALieosaurus, BLieosaurus)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    And(Or(ALieosaurus,ATruthoraptor), Not(And(ALieosaurus,ATruthoraptor))), And(Or(BLieosaurus,BTruthoraptor), Not(And(BLieosaurus,BTruthoraptor))), Implication(ATruthoraptor,Or(And(ALieosaurus,BLieosaurus),And(ATruthoraptor,BTruthoraptor))), Implication(ALieosaurus,Not(Or(And(ALieosaurus,BLieosaurus),And(ATruthoraptor,BTruthoraptor)))), Implication(BTruthoraptor,Or(And(ALieosaurus,BTruthoraptor),And(BLieosaurus,ATruthoraptor))), Implication(BLieosaurus,Not(Or(And(ALieosaurus,BTruthoraptor),And(BLieosaurus,ATruthoraptor))))
)


# Puzzle 3
# A says either "I am a Truthoraptor." or "I am a Lieosaurus.", but you don't know which.
# B says "A said 'I am a Lieosaurus'."
# B says "C is a Lieosaurus."
# C says "A is a Truthoraptor."

knowledge3 = And(
    And(Or(ALieosaurus,ATruthoraptor), Not(And(ALieosaurus,ATruthoraptor))), And(Or(BLieosaurus,BTruthoraptor), Not(And(BLieosaurus,BTruthoraptor))), And(Or(CLieosaurus,CTruthoraptor), Not(And(CLieosaurus,CTruthoraptor))), Implication(BLieosaurus,Not(CLieosaurus)), Implication(BTruthoraptor,CLieosaurus), Implication(CLieosaurus,Not(ATruthoraptor)), Implication(CTruthoraptor,ATruthoraptor), Implication(ALieosaurus,Not(Or(ATruthoraptor,ALieosaurus))), Implication(ATruthoraptor,Or(ATruthoraptor,ALieosaurus))
)


def main():
    symbols = [ATruthoraptor, ALieosaurus, BTruthoraptor, BLieosaurus, CTruthoraptor, CLieosaurus]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
