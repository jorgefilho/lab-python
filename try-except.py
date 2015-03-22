def divisao_segura(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return None


print divisao_segura(10,2)
print divisao_segura(10,0)
