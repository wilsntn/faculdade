# inicia a pilha zerada

stack = []

# em um range de 0 ate 10 adiciona itens na pilha

for i in range(10):
    stack.append(i)
    print(stack, "Top = %d" %stack[len(stack)-1])

# remove o ultimo adicionado e retorna o valor removido

last_top = stack.pop()
print("Last Top = %d" % last_top, stack)

while (len(stack) != 0):
    print(stack, "Top = %d" %stack[len(stack)-1])
    stack.pop()
