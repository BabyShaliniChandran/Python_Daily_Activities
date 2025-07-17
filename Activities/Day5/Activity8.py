#remove(),pop(),insert()
input=["Track A","Track B","Track C","Track D"]
#Track C need to removed
input.remove("Track C")
#remove the Track D
input.pop()
#insert track X in position 0
input.insert(0,"Track X")
#insert track D in position 1
input.insert(1,"Track D")
#unpcaking using *
print(*input)
