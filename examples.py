from WNS import sim_str_str,sim_str_str_multiling

print("EXAMPLES")
# print(sim_str_str_multiling("Mon pare anirà a comprar pernil i formatge a la tenda de l'esquina.","Аав маань булангийн дэлгүүрээс сонирхогчид, бяслаг худалдаж авах гэж байна.",stat="mean"))
# print(sim_str_str("I am testing this new application on my laptop connected to the Internet.","My son studied computer science and he's working at Google",stat="max"))

print(sim_str_str_multiling("Estoy probando esta nueva aplicación en mi portátil conectado a internet.","My son studied computer science and he's working at Google",stat="mean"))
print(sim_str_str_multiling("Estoy probando esta nueva aplicación en mi portátil conectado a internet.","My son studied boat mechanics and he's working at Balearia",stat="mean"))
# print(sim_str_str_multiling("Mi padre irá a comprar jamón y queso a la tienda de la esquina.","My son studied computer science and he's working at Google",stat="max"))
# print(sim_str_str_multiling("Mi padre irá a comprar jamón y queso a la tienda de la esquina.","Аав маань булангийн дэлгүүрээс сонирхогчид, бяслаг худалдаж авах гэж байна.",stat="mean"))
# print(sim_str_str_multiling("Mi padre irá a comprar jamón y queso a la tienda de la esquina.","Mi padre irá a comprar chorizo y queso al supermercado de la esquina.",stat="mean"))
# print(sim_str_str_multiling("tienda","supermercado"))
# print(sim_str_str_multiling("futbol","baloncesto"))
# print(sim_str_str_multiling("Mi gato","perro"))
# print(sim_str_str_multiling("Gato","araña"))
# print(sim_str_str_multiling("My cat is losing its hair","Mascota:Gato",stat="mean"))
# print(sim_str_str_multiling("My horse is losing its hair","Mascota:Gato",stat="mean"))
# print(sim_str_str_multiling("My cat is losing its hair","Mascota:Gato",stat="q90"))
# print(sim_str_str_multiling("My horse is losing its hair","Mascota:Gato",stat="q90"))
