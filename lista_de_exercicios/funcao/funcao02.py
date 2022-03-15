retas =[]

for i in range(1,4):
    retas.append(float(input(f"Defina o comprimento da {i}ª reta: ")))

def pode_triangular(retas: list):
    for reta in retas:
        if reta <= 0 or (sum(retas) <= 2 * max(retas)):
            return False
        else:
            return True

print(pode_triangular(retas))
