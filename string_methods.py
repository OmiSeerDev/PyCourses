text = "I can program in C, Java, JS, TS, Node, Rust and Kotlin"
print("Go" in text) #False (no contiene Go)

print(f"{len(text)} characters.") #Retorna la longitud

print(text.upper()) #Pasa a mayus
print(text.lower()) #Pasa a minus

print(text.count("a")) #Conteo de caracteres

print(text.swapcase()) #Invierte mayus y minusc
print(text.startswith("I "))

print(text.replace("I", "We all"))

# .capitalize pasa la primera letra a mayus

print(text.title()) #Mayus en cada palabra

print(text.index("Java")) #Buscar índice

print(text[20:24]) #Buscar caracteres  en rangos
print(text[::2]) #Saltar n caracteres 

print(text.split()) #Separa en palabras generando un array

