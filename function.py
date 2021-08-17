class decida_por_mim:
    
    def __init__(self):
        self.answer = [
            'Sim! Faça isso',
            'Com toda certeza!',
            'Não sei, decida você mesmo',
            'Não faz isso',
            'Acho melhor não'
        ]
    

    def iniciar(self):
        import random
        str(input('Faça uma pergunta: '))
        print(random.choice(self.answer))
