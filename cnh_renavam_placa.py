""" Requisitos:
- CNH = 11 dígitos
- RENAVAM = 11 dígitos
- Placa Mercosul = XXX0X00 """

# Importação dos módulos necessários
import random  # Módulo para geração de números aleatórios
import string  # Módulo para manipulação de strings

# Classe para gerar documentos brasileiros
class GeradorBR:
    # Método estático para gerar um número de CNH
    @staticmethod
    def gerar_cnh():
        # Geração dos dígitos aleatórios (11 dígitos)
        numero_registro = ''.join(random.choices(string.digits, k=11))

        return numero_registro

    # Método estático para gerar um número de RENAVAM
    @staticmethod
    def gerar_renavam():
        # Geração dos dígitos aleatórios (11 dígitos)
        numero_registro = ''.join(random.choices(string.digits, k=11))

        return numero_registro

    # Método estático para gerar uma placa de veículo no padrão Mercosul
    @staticmethod
    def gerar_placa_mercosul():
        # Geração das letras iniciais (3 letras maiúsculas)
        letras = ''.join(random.choices(string.ascii_uppercase, k=3))
        # Geração do primeiro número (1 dígito)
        numero = ''.join(random.choices(string.digits, k=1))
        # Geração da letra do meio (1 letra maiúscula)
        letra = ''.join(random.choices(string.ascii_uppercase, k=1))
        # Geração dos números finais (2 dígitos)
        numeros_finais = ''.join(random.choices(string.digits, k=2))

        # Retorno da placa no formato Mercosul
        return f"{letras}{numero}{letra}{numeros_finais}"

# Função para simular a geração dos documentos
def simular_documentos():
    print("Simulação de Documentos Brasileiros\n")
    print("CNH:", GeradorBR.gerar_cnh())  # Gera e exibe um número de CNH
    print("RENAVAM:", GeradorBR.gerar_renavam())  # Gera e exibe um número de RENAVAM
    print("Placa de Veículo (Mercosul):", GeradorBR.gerar_placa_mercosul())  # Gera e exibe uma placa de veículo no padrão Mercosul

# Executar a simulação
simular_documentos()
