from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # AKnight or AKnave but not both
    And(Or(AKnight, AKnave), 
        Not(And(AKnight, AKnave))
    ),
    # Biconditional AKnight and ASaid
    Biconditional(
        AKnight, 
        And(AKnight, AKnave)
    ),
    # Biconditional Not(AKnave) and ASaid
    Biconditional(
        Not(AKnave), 
        And(AKnight, AKnave)
    ) 
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # One can be a Knight or a Knave but not both
    And(
        Or(AKnight, AKnave), 
        Not(And(AKnight, AKnave))
    ),
    And(
        Or(BKnight, BKnave), 
        Not(And(BKnight, BKnave))
    ),
    # Biconditional AKnight and ASaid
    Biconditional(
        AKnight, 
        And(AKnave, BKnave)
    ),
    # Biconditional Not(AKnave) and ASaid
    Biconditional(
        Not(AKnave), 
        And(AKnave, BKnave)
    )
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
# ASaid = Or(And(AKnight, BKnight), And(AKnave, BKnave))
# BSaid = Or(And(AKnight, BKnave), And(AKnave, BKnight))
knowledge2 = And(
    # One can be a Knight or a Knave but not both
    And(
        Or(AKnight, AKnave), 
        Not(And(AKnight, AKnave))
    ),
    And(
        Or(BKnight, BKnave), 
        Not(And(BKnight, BKnave))
    ),
    # Biconditional AKnight and ASaid
    Biconditional(
        AKnight, 
        Or(
            And(AKnight, BKnight), 
            And(AKnave, BKnave)
        )
    ),
    # Biconditional Not(AKnave) and ASaid
    Biconditional(
        Not(AKnave), 
        Or(
            And(AKnave, BKnave), 
            And(AKnight, BKnight)
        )
    ),
    # Biconditional BKnight and BSaid
    Biconditional(
        BKnight, 
        Or(
            And(AKnight, BKnave), 
            And(AKnave, BKnight)
        )
    ),
    # Biconditional Not(BKnave) and BSaid
    Biconditional(
        Not(BKnave), 
        Or(
            And(AKnight, BKnave), 
            And(AKnave, BKnight)
        )
    )
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
# ASaid = AKnight OR ASaid = AKnave
# Or(And(Biconditional(AKnight, AKnight), Biconditional(Not(AKnave), AKnight), And(Biconditional(AKnight, AKnave), Biconditional(Not(AKnave), AKnave)))
# BSaid1 = And(Biconditional(AKnight, AKnave), Biconditional(Not(AKnave), AKnave))
# BSaid2 = CKnave
# Biconditional(BSaid1, BSaid2) 
# CSaid = AKnight
knowledge3 = And(
    # One can either be a Knight or a Knave but not both
    And(
        Or(AKnight, AKnave), 
        Not(And(AKnight, AKnave))
    ),
    And(
        Or(BKnight, BKnave), 
        Not(And(BKnight, BKnave))
    ),
    And(
        Or(CKnight, CKnave), 
        Not(And(CKnight, CKnave))
    ),
    # ASaid = AKnight OR ASaid = AKnave
    Or(
        And(
            Biconditional(AKnight, AKnight), 
            Biconditional(Not(AKnave), AKnight)
        ), 
        And(
            Biconditional(AKnight, AKnave), 
            Biconditional(Not(AKnave), AKnave)
        )
    ),
    # Biconditional BKnight and BSaid1
    Biconditional(
        BKnight, 
        And(
            Biconditional(AKnight, AKnave), 
            Biconditional(Not(AKnave), AKnave)
        )
    ),
    # Biconditional BKnight and Bsaid2
    Biconditional(BKnight, CKnave),
    # Biconditional Not(BKnave) and BSaid1
    Biconditional(
        Not(BKnave), 
        And(
            Biconditional(AKnight, AKnave), 
            Biconditional(Not(AKnave), AKnave)
        )
    ),
    # Biconditional Not(BKnave) and BSaid2
    Biconditional(Not(BKnave), CKnave),
    # Biconditional BSaid1 and BSaid2
    Biconditional(
        And(
            Biconditional(AKnight, AKnave), 
            Biconditional(Not(AKnave), AKnave)
        ), 
        CKnave
    ),
    # Biconditional(CKnight, CSaid)
    Biconditional(CKnight, AKnight),
    # Biconditional(Not(CKnave), CSaid)
    Biconditional(Not(CKnave), AKnight)
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
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
