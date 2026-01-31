"""
Project Euler Problem 836: A Bold Proposition

The problem asks to find the answer by looking at the bolded words
in the description. This was an April Fools' joke problem.
Task: Concatenate the first letter of each bolded word.
"""

def solve_bold_proposition():
    # Las frases en negrita tal como aparecen en el enunciado
    bold_phrases = [
        "affine plane",
        "radically integral local field",
        "open oriented line section",
        "jacobian",
        "orthogonal kernel embedding"
    ]
    
    result = []
    
    print("Processing bold terms:")
    
    for phrase in bold_phrases:
        # Dividimos la frase en palabras
        words = phrase.split()
        
        # Extraemos la primera letra de cada palabra
        initials = [w[0] for w in words]
        
        # Guardamos para el resultado final
        result.extend(initials)
        
        print(f"'{phrase}' -> {''.join(initials)}")
        
    final_answer = "".join(result)
    
    print("-" * 30)
    print(f"Solution: {final_answer}")

if __name__ == "__main__":
    solve_bold_proposition()