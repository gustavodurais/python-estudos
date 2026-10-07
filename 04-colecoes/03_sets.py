"""Sets (conjuntos): itens únicos e sem ordem."""

# Set é uma coleção de itens únicos e desordenados. Isso significa que um set não pode ter itens duplicados e os itens não têm uma ordem específica.


cursos_a = {"python", "sql", "git"}
cursos_b = {"python", "docker", "git", "linux"}

# sorted() é usado só para a saída aparecer sempre na mesma ordem
print("união:", sorted(cursos_a | cursos_b))
print("interseção:", sorted(cursos_a & cursos_b))
print("só em A:", sorted(cursos_a - cursos_b))
print("em um ou outro, não ambos:", sorted(cursos_a ^ cursos_b))

# Uso clássico: remover duplicados
repetidos = [1, 2, 2, 3, 3, 3]
unicos = sorted(set(repetidos))
print(unicos)

cursos_a.add("pandas")
cursos_a.discard("sql")  # não dá erro se o item não existir
print("pandas" in cursos_a)
print(sorted(cursos_a))
