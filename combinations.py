"""Υπολογίζω το πλήθος των συνδυασμών των ν ανά κ, όπου οι αριθμοί ν και κ δίνονται από τον χρήστη."""
from math import factorial

def count_permutations(n,k):
    perm_num = int((factorial(n)) // (factorial(n-k)))
    return perm_num

def count_combinations(n, k):
    """Μετρώ τους συνδυασμούς των ν ανά κ"""
    n_fact = factorial(n)
    k_fact = factorial(k)
    diff_fact = factorial(n-k)
    comb_num = int(n_fact // (k_fact * diff_fact))
    return comb_num

def main():
    while True:
        n = input("n = ")

        try:
            n = int(n)
        except:
            print("Παρακαλώ εισάγετε μόνο θετικούς ακέραιους αριθμούς.")
            continue
        else:
            if n <= 0:
                print("Παρακαλώ εισάγετε μόνο θετικούς ακέραιους αριθμούς.")
                continue
            else:
                while True:
                    k = input("k = ")
                    try:
                        k = int(k)
                    except:
                        print("Παρακαλώ εισάγετε μόνο θετικούς ακέραιους αριθμούς.")
                        continue
                    else:
                        if k <= 0:
                            print("Παρακαλώ εισάγετε μόνο θετικούς ακέραιους αριθμούς.")
                            continue
                        elif k > n:
                            print("Πρέπει το k να είναι μικρότερο ή ίσο του n.")
                        else:
                            print(count_combinations(n, k))
                            exit()

if __name__ == '__main__':
    main()