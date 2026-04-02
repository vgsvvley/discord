
# EXERCICE 1 : Résidu Numérique


def residu1(n):
    """Calcule le résidu numérique de n par récursion (méthode p+q)."""
    if n < 10:
        return n
    p, q = n // 10, n % 10
    return residu1(p + q)

def residu2(n):
    """Calcule le résidu numérique avec la compréhension de liste."""
    if n < 10:
        return n
    chiffres = [int(x) for x in str(n)]
    return residu2(sum(chiffres))

def residu3(n):
    """Calcule le résidu numérique sans récursion (formule directe)."""
    return n - 9 * ((n - 1) // 9)



# EXERCICE 2 : Fonctions et Dictionnaires


def applique(f, L):
    """Fonction génératrice appliquant f à chaque élément de L."""
    for x in L:
        yield f(x)

def list2tuple(L):
    """Convertit récursivement les listes en tuples."""
    resultat = []
    for x in L:
        if type(x) is list:
            resultat.append(list2tuple(x))
        else:
            resultat.append(x)
    return tuple(resultat)

def suivants(s):
    """Retourne le dictionnaire des successeurs de chaque caractère."""
    d = {}
    for c in s:
        if c not in d:
            d[c] = set()
    for i in range(len(s) - 1):
        caractere_actuel = s[i]
        caractere_suivant = s[i+1]
        d[caractere_actuel].add(caractere_suivant)
    return d



# EXERCICE 4 : Suite de Prouhet-Thue-Morse


def morse1(n):
    """Calcule u_n de la suite de Morse par récursion."""
    if n == 0:
        return 0
    if n % 2 == 0:
        return morse1(n // 2)
    else:
        return 1 - morse1(n // 2)

def morse2(n):
    """Génère la liste [u_0, ..., u_n] de manière itérative."""
    u = [0] * (n + 1)
    for i in range(1, n + 1):
        if i % 2 == 0:
            u[i] = u[i // 2]
        else:
            u[i] = 1 - u[i // 2]
    return u

def compte(n):
    """Renvoie le nombre de chiffres 1 dans l'écriture binaire de n."""
    return bin(n).count('1')

def f(E, n):
    """Nombre de couples (a, b) dans E tels que a + b = n et a < b."""
    Compte = 0
    L = sorted(list(E))
    for i in range(len(L)):
        for j in range(i + 1, len(L)):
            if L[i] + L[j] == n:
                Compte += 1
    return Compte

def verifier_question8():
    """Vérifie la propriété f_A(n) == f_B(n) pour n de 0 à 100."""
    L_morse = morse2(100)
    A = {i for i, v in enumerate(L_morse) if v == 0}
    B = {i for i, v in enumerate(L_morse) if v == 1}
    for n in range(101):
        if f(A, n) != f(B, n):
            return False
    return True






# Test Ex 1
n_test = 31415926
print(f"\n[Ex 1] Résidu de {n_test}:")
print(f"  - Méthode 1 (p+q)  : {residu1(n_test)}")
print(f"  - Méthode 2 (somme): {residu2(n_test)}")
print(f"  - Méthode 3 (direct): {residu3(n_test)}")

# Test Ex 2
s_test = "abbaeabbad"
print(f"\n[Ex 2] Dictionnaire suivants pour '{s_test}':")
print(f"  {suivants(s_test)}")

# Test Ex 4
print(f"\n[Ex 4] Suite de Morse (n=0 à 6):")
print(f"  {morse2(6)}")

print(f"\n[Ex 4] Vérification Conjecture Q8 (f_A = f_B):")
resultat_q8 = verifier_question8()
print(f"  Résultat : {resultat_q8}")
