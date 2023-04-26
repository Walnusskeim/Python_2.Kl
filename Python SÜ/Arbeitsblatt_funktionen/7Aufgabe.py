def teilbarzahl(z):
    z = int(z)
    if z %3 == 0:
        return "teilbar"
    else:
        return "nicht teilbar"

print(teilbarzahl(74875938))