from budget import Category, create_spend_chart


comida = Category('comida')
comida.ledger.append({"amount": 150})
comida.ledger.append({"amount": -25})
comida.ledger.append({"amount": -50})

ropa = Category('ropa')
ropa.ledger.append({"amount": 200})
ropa.ledger.append({"amount": -10})
ropa.ledger.append({"amount": -20})

entretenimiento = Category('entretenimiento')
entretenimiento.ledger.append({"amount": 350})
entretenimiento.ledger.append({"amount": -15})
entretenimiento.ledger.append({"amount": -30})

viaje = Category('viaje')
viaje.ledger.append({"amount": 1500})
viaje.ledger.append({"amount": -280})
viaje.ledger.append({"amount": -500})
viaje.ledger.append({"amount": -320})

lista = [comida, ropa, entretenimiento, viaje]

create_spend_chart(lista)