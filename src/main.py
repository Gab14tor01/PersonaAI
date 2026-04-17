from personas import PERSONAS
from voz import gravar_audio, transcrever, falar

MODO_SIMULACAO = True

def responder(texto, persona="critico"):
    if persona == "critico":
        return f"Você realmente acredita nisso? Ou está só evitando encarar o problema quando diz: '{texto}'?"

    elif persona == "racional":
        return f"Analisando friamente: '{texto}' não resolve nada. Qual ação concreta você vai tomar?"

    elif persona == "ideal":
        return f"A melhor versão de você não diria '{texto}'. Ela agiria apesar disso."

    elif persona == "pessimista":
        return f"Se você continuar pensando assim ('{texto}'), provavelmente nada vai mudar — ou pode até piorar."

    return "Não consegui processar isso."

def main():
    print("🧠 Echo AI iniciado...")
    print("Digite 'sair' para encerrar.\n")

    print("Escolha uma persona:")
    print("1 - Critico")
    print("2 - Racional")
    print("3 - Ideal")
    print("4 - Pessimista")

    escolha = input("Digite o número: ")

    mapa = {
        "1": "critico",
        "2": "racional",
        "3": "ideal",
        "4": "pessimista"
    }

    persona = mapa.get(escolha, "critico")

    print(f"\nPersona selecionada: {persona}\n")

    while True:
        comando = input("\nPressione ENTER para falar ou digite 'sair': ")

        if comando.lower() == "sair":
            print("Encerrando...")
            break

        gravar_audio()

        texto = transcrever()
        print("Você:", texto)

        resposta = responder(texto, persona)
        print("Echo:", resposta)

        falar(resposta)

if __name__ == "__main__":
    main()