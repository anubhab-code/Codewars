def pattern(n):
    return '\n'.join(str(a) * a for a in range(1, n + 1))