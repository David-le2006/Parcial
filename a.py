cantidad_pedidos = int(input("¿Cuántos pedidos vas a ingresar?: "))
pedidos = []

for i in range(cantidad_pedidos):
    print(f"\nPedido {i+1}:")
    nombre = input("Nombre del cliente: ")
    valor = float(input("Valor total del pedido: "))
    estado = input("Estado del pedido (pendiente, enviado, cancelado): ").strip().lower()
    pedidos.append({"nombre": nombre, "valor": valor, "estado": estado})

total_pedidos = len(pedidos)
enviados = [p for p in pedidos if p["estado"] == "enviado"]
pendientes = [p for p in pedidos if p["estado"] == "pendiente"]
monto_total_enviado = sum(p["valor"] for p in enviados)

valor_maximo = max(p["valor"] for p in pedidos)
clientes_maximo_valor = [p["nombre"] for p in pedidos if p["valor"] == valor_maximo]

print("\n--- Resumen ---")
print(f"Total de pedidos procesados: {total_pedidos}")
print(f"Total de pedidos enviados: {len(enviados)}")
print(f"Monto total en ventas (enviados): ${monto_total_enviado:.2f}")
print(f"Cliente(s) con el pedido de mayor valor: {', '.join(clientes_maximo_valor)}")

if len(pendientes) / total_pedidos > 0.7:
    print("Alerta: muchos pedidos sin procesar.")