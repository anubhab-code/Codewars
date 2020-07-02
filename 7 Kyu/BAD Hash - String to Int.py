def string_hash(s):
    a = sum(map(ord, s))
    b = sum(ord(y) - ord(x) for x, y in zip(s, s[1:]))
    c = (a | b) & (~a << 2)
    d = c ^ (32 * (s.count(' ') + 1))
    return d