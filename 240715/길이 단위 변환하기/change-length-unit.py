def ft_to_cm(ft):
    return ft * 30.48

def mi_to_cm(mi):
    return mi * 160934

a, b = 9.2, 1.3
print(f'{a}ft = {ft_to_cm(a):.1f}cm')
print(f'{b}mi = {mi_to_cm(b):.1f}cm')