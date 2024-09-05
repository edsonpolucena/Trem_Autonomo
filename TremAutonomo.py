class TremAutonomo:
    def __init__(self):
        self.posicao = 0
        self.movimentos_consecutivos = 0
        self.ultima_direcao = None
        self.movimentos_totais = 0

    def mover(self, comandos):
        for comando in comandos:
            if self.movimentos_totais >= 50:
                print("O trem parou após 50 movimentos.")
                break

            if comando not in ["ESQUERDA", "DIREITA"]:
                raise ValueError(f"Comando inválido: {comando}")

            if comando == self.ultima_direcao:
                self.movimentos_consecutivos += 1
            else:
                self.movimentos_consecutivos = 1

            if self.movimentos_consecutivos > 20:
                raise ValueError("O trem não pode fazer mais de 20 movimentos consecutivos na mesma direção.")

            if comando == "DIREITA":
                self.posicao += 1
            elif comando == "ESQUERDA":
                self.posicao -= 1

            self.ultima_direcao = comando
            self.movimentos_totais += 1

        return self.posicao