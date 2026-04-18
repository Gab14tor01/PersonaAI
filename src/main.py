from personas import PERSONAS
from voz import gravar_audio, transcrever, falar

historico = []

def responder(texto, persona="critico"):
    contexto = " | ".join(historico[-2:]) if historico else "nenhum histórico relevante"

    if persona == "critico":
        return f"Você disse antes: {contexto}. Agora você fala '{texto}'. Percebe algum padrão?"

    elif persona == "racional":
        return f"Histórico recente: {contexto}. Analise logicamente o que você acabou de dizer: '{texto}'."

    elif persona == "ideal":
        return f"Comparando com o que você disse antes ({contexto}), você pode fazer melhor do que '{texto}'."

    elif persona == "pessimista":
        return f"Você já vem repetindo isso: {contexto}. E agora diz '{texto}'. Isso não parece bom."

    return "Não consegui processar."

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
        comando = input("\nPressione ENTER para falar, 'reset' para limpar memória ou 'sair': ")

        if comando.lower() == "sair":
            print("Encerrando...")
            break

        if comando.lower() == "reset":
            historico.clear()
            print("🧠 Memória apagada!")
            continue

        gravar_audio()

        texto = transcrever()
        print("Você:", texto)

        historico.append(texto)
        if len(historico) > 10:
            historico.pop(0)


        if not texto.strip():
            print("Não entendi o áudio, tenta novamente.")
            continue

        resposta = responder(texto, persona)
        

        print("Echo:", resposta)

        falar(resposta)


if __name__ == "__main__":
    main()