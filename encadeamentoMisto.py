def encadeamentoMisto(new_data):
    for x in range(10):

        if new_data["mulher_com_outra"] and new_data["relacionamento_aberto"]:
            new_data["corno"] = False

        if new_data["mulher_com_outro"] and new_data["relacionamento_semi_aberto"]:
            new_data["corno"] = True

        if new_data["mulher_com_outra"] and new_data["relacionamento_semi_aberto"]:
            new_data["corno"] = False

        if new_data["corno"]:
            print("Parabéns você é um chifrudo!")
            break

        if new_data["tem_relacionamento"] == False:
            new_data["corno"] = False

        if new_data["tem_relacionamento"] and new_data["mulher_com_outro"]:
            new_data["corno"] = True

        if new_data["mulher_com_outro"] and new_data["relacionamento_aberto"]:
            new_data["corno"] = False

    else:
        print("Não é corno, fique tranquilo")
