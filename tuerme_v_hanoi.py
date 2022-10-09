def bewegeTurm(n, eins, zwei, drei):
    if n == 1:
        print(eins, "-->", zwei)
    else:
        bewegeTurm(n-1, eins, drei, zwei)
        bewegeTurm(1, eins, zwei, drei)
        bewegeTurm(n-1, drei, zwei, eins)
bewegeTurm(7, "A", "C", "B")