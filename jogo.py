import time
import random
import os
from datetime import datetime

# ============================================
# JOGO INTERATIVO DE SEGURANÇA IIoT - SENAI
# ============================================

class JogoSegurancaIIoT:
    def __init__(self):
        self.pontuacao = 0
        self.nivel_alerta = 0
        self.medidas_implementadas = []
        self.sensores_protegidos = 0
        self.inventario = []
        self.tempo_restante = 10  # minutos para agir

    def limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def digitar_lento(self, texto, velocidade=0.03):
        """Efeito de digitação para dar mais imersão"""
        for char in texto:
            print(char, end='', flush=True)
            time.sleep(velocidade)
        print()

    def mostrar_status(self):
        """Mostra status atual do jogo"""
        print("\n" + "="*60)
        print(f"🛡️ STATUS DO ANALISTA SENAI")
        print("="*60)
        print(f"🎯 Pontuação: {self.pontuacao}")
        print(f"⚠️ Nível de Alerta: {'🔴' * self.nivel_alerta}{'⚪' * (5-self.nivel_alerta)}")
        print(f"⏰ Tempo restante: {self.tempo_restante} minutos")
        print(f"🛡️ Medidas implementadas: {len(self.medidas_implementadas)}")
        print(f"📦 Inventário: {', '.join(self.inventario) if self.inventario else 'Vazio'}")
        print("="*60)

    def cenario_ataque_phishing(self):
        """Cenário 1: Email suspeito para operador"""
        self.limpar_tela()
        self.digitar_lento("📧 ALERTA: Operador da fábrica recebeu um email suspeito!")
        print("\n'URGENTE: Atualização crítica de firmware - Clique aqui'")
        print("\nO que você faz?")
        print("1️⃣ Bloquear imediatamente o email no servidor")
        print("2️⃣ Deixar o operador decidir (testar conscientização)")
        print("3️⃣ Ignorar - parece ser só spam")
        print("4️⃣ Investigar o link em ambiente isolado primeiro")

        escolha = input("\nSua escolha (1-4): ")

        if escolha == "1":
            self.digitar_lento("\n✅ Bloqueio realizado! O link era malicioso.")
            self.pontuacao += 10
            self.medidas_implementadas.append("Filtro Anti-Phishing")
        elif escolha == "2":
            self.digitar_lento("\n❌ O operador clicou e abriu a rede para o atacante!")
            self.pontuacao -= 5
            self.nivel_alerta += 2
        elif escolha == "3":
            self.digitar_lento("\n💥 30 funcionários clicaram no link! Ataque espalhado!")
            self.pontuacao -= 15
            self.nivel_alerta += 3
        else:
            self.digitar_lento("\n🔍 Descobrimos que era um ataque direcionado (spear phishing)!")
            self.pontuacao += 15
            self.inventario.append("Relatório do Ataque")

        input("\nPressione ENTER para continuar...")

    def cenario_senhas_fracas(self):
        """Cenário 2: Descoberta de senhas padrão"""
        self.limpar_tela()
        self.digitar_lento("🔑 AUDITORIA: Dispositivos com senhas padrão encontrados!")
        print("\nSensores com 'admin/admin' detectados na rede:")
        print("• Controlador de Temperatura - Setor A")
        print("• Válvula de Pressão - Setor B")
        print("• Medidor de Vazão - Setor C")

        print("\nQual sua estratégia?")
        print("1️⃣ Trocar todas as senhas imediatamente")
        print("2️⃣ Priorizar apenas os sensores críticos")
        print("3️⃣ Implementar autenticação de dois fatores")
        print("4️⃣ Criar política de senhas fortes e agendar troca")

        escolha = input("\nSua escolha (1-4): ")

        if escolha == "1":
            if self.tempo_restante >= 3:
                self.digitar_lento("\n✅ Troca realizada! Rede mais segura.")
                self.pontuacao += 10
                self.sensores_protegidos += 3
                self.tempo_restante -= 2
            else:
                self.digitar_lento("\n⚠️ Tempo insuficiente! Ataque ocorreu durante a troca.")
                self.pontuacao -= 5
        elif escolha == "2":
            self.digitar_lento("\n⚠️ Os sensores não prioritários foram invadidos!")
            self.pontuacao -= 10
            self.nivel_alerta += 2
        elif escolha == "3":
            self.digitar_lento("\n🚀 Ótimo! 2FA implementado em todos dispositivos.")
            self.pontuacao += 20
            self.medidas_implementadas.append("2FA")
        else:
            self.digitar_lento("\n📋 Boa! Política criada, mas ataque ocorreu antes da execução.")
            self.pontuacao += 5
            self.nivel_alerta += 1

        input("\nPressione ENTER para continuar...")

    def mini_game_firewall(self):
        """Mini-game de configuração de firewall"""
        self.limpar_tela()
        print("🔥 CONFIGURANDO FIREWALL INDUSTRIAL")
        print("Regras de firewall precisam ser configuradas!")
        print("\nPortas comuns em redes IIoT:")
        print("• 502/TCP - Modbus (Controle industrial)")
        print("• 161/UDP - SNMP (Monitoramento)")
        print("• 80/TCP - HTTP (Interfaces web)")
        print("• 22/TCP - SSH (Acesso remoto)")

        acertos = 0
        print("\n📝 DESAFIO: Quais portas BLOQUEAR?")
        print("(Digite os números separados por vírgula - ex: 502,80)")

        resposta = input("Sua resposta: ")
        portas_escolhidas = [int(p.strip()) for p in resposta.split(",") if p.strip().isdigit()]

        # Portas que deveriam ser bloqueadas em uma rede industrial segura
        portas_corretas = [80, 23]  # HTTP e Telnet são inseguros

        for porta in portas_escolhidas:
            if porta in portas_corretas:
                acertos += 1
                self.digitar_lento(f"✅ Porta {porta} bloqueada corretamente!")
            else:
                self.digitar_lento(f"❌ Porta {porta} é necessária para operação!")
                self.pontuacao -= 5

        if acertos >= 2:
            self.pontuacao += 25
            self.medidas_implementadas.append("Firewall Configurado")
            self.digitar_lento("\n🏆 Excelente! Firewall configurado com sucesso!")
        else:
            self.nivel_alerta += 2
            self.digitar_lento("\n⚠️ Firewall mal configurado! Rede vulnerável.")

        input("\nPressione ENTER para continuar...")

    def cenario_ataque_ransomware(self):
        """Cenário de ataque em andamento"""
        self.limpar_tela()
        self.digitar_lento("🚨 URGENTE! ATAQUE RANSOMWARE DETECTADO!")
        print("\n" + "█"*50)
        print("""
        ⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️
        SENSORES CRÍTICOS SENDO CRIPTOGRAFADOS!
        ⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️
        """)

        # Barra de progresso do ataque
        for i in range(0, 101, 20):
            print(f"🔴 Ataque em progresso: [{'█' * (i//10)}{'░' * (10-(i//10))}] {i}%")
            time.sleep(0.3)

        print("\n🔥 AÇÕES DE EMERGÊNCIA:")
        print("1️⃣ Isolar rede industrial imediatamente")
        print("2️⃣ Desligar todos os equipamentos")
        print("3️⃣ Tentar negociar com atacantes")
        print("4️⃣ Ativar backups e restaurar sistemas")

        escolha = input("\nQual ação de emergência? (1-4): ")

        if escolha == "1":
            self.digitar_lento("\n✅ Isolamento bem sucedido! Ataque contido!")
            self.pontuacao += 30
            self.medidas_implementadas.append("Isolamento de Rede")
        elif escolha == "2":
            self.digitar_lento("\n⚡ Desligamento causou danos aos equipamentos!")
            self.pontuacao -= 10
            self.nivel_alerta += 1
        elif escolha == "3":
            self.digitar_lento("\n💰 Atacantes sumiram com o dinheiro! Dispositivos perdidos!")
            self.pontuacao -= 30
            self.nivel_alerta += 3
        else:
            self.digitar_lento("\n💾 Backups restaurados! Produção volta em 2h!")
            self.pontuacao += 20
            self.inventario.append("Backup Validado")

        input("\nPressione ENTER para continuar...")

    def desafio_segmentacao_rede(self):
        """Desafio de segmentação de rede"""
        self.limpar_tela()
        print("🌐 DESAFIO: SEGMENTAÇÃO DE REDE IIoT")
        print("\nVocê precisa separar a rede em VLANs:")
        print("Rede IT (Escritório) x Rede OT (Chão de fábrica)")

        dispositivos = [
            "Computador RH", "Sensor Temperatura", "Notebook Diretor",
            "Controlador Robô", "Impressora", "Válvula Automática",
            "Servidor Email", "CLP Esteira", "Access Point Visitantes"
        ]

        print("\nDispositivos a classificar:")
        for i, dispositivo in enumerate(dispositivos, 1):
            print(f"{i}. {dispositivo}")

        print("\nClassifique cada dispositivo:")
        print("I = Rede IT (Escritório)")
        print("O = Rede OT (Industrial)")

        acertos = 0
        respostas = {}

        for dispositivo in dispositivos:
            resp = input(f"\n{dispositivo}: (I/O): ").upper()
            respostas[dispositivo] = resp

        # Correção
        classificacao_correta = {
            "Computador RH": "I",
            "Sensor Temperatura": "O",
            "Notebook Diretor": "I",
            "Controlador Robô": "O",
            "Impressora": "I",
            "Válvula Automática": "O",
            "Servidor Email": "I",
            "CLP Esteira": "O",
            "Access Point Visitantes": "I"
        }

        for disp, resp in respostas.items():
            if resp == classificacao_correta[disp]:
                acertos += 1
                self.digitar_lento(f"✅ {disp} correto!")
            else:
                self.digitar_lento(f"❌ {disp} - Deveria ser {classificacao_correta[disp]}")

        if acertos >= 7:
            self.pontuacao += 25
            self.medidas_implementadas.append("Segmentação Correta")
            self.digitar_lento(f"\n🏆 Excelente! {acertos}/9 acertos!")
        else:
            self.nivel_alerta += 2
            self.digitar_lento(f"\n⚠️ Segmentação inadequada! {acertos}/9 acertos.")

        input("\nPressione ENTER para continuar...")

    def mostrar_relatorio_final(self):
        """Mostra relatório final do jogo"""
        self.limpar_tela()
        print("\n" + "="*60)
        print("📊 RELATÓRIO FINAL - ANALISTA SENAI")
        print("="*60)

        print(f"\n🎯 Pontuação Total: {self.pontuacao}")
        print(f"⚠️ Nível Máximo de Alerta: {self.nivel_alerta}/5")
        print(f"🛡️ Medidas Implementadas: {len(self.medidas_implementadas)}")

        print("\n📋 MEDIDAS DE SEGURANÇA ADOTADAS:")
        for medida in self.medidas_implementadas:
            print(f"   • {medida}")

        print("\n📦 ITENS NO INVENTÁRIO:")
        for item in self.inventario:
            print(f"   • {item}")

        # Avaliação de desempenho
        print("\n" + "="*60)
        if self.pontuacao >= 80:
            print("🏆 CLASSIFICAÇÃO: ESPECIALISTA EM IIoT!")
            print("   Parabéns! Você protegeu a fábrica com excelência!")
        elif self.pontuacao >= 50:
            print("🔰 CLASSIFICAÇÃO: TÉCNICO SENAI")
            print("   Bom trabalho! Algumas melhorias são necessárias.")
        elif self.pontuacao >= 20:
            print("📚 CLASSIFICAÇÃO: EM TREINAMENTO")
            print("   Precisa estudar mais sobre segurança IIoT.")
        else:
            print("💀 CLASSIFICAÇÃO: FÁBRICA COMPROMETIDA")
            print("   Ataque bem sucedido! Reavaliar toda a segurança.")

        print("\n" + "="*60)
        print("LIÇÕES APRENDIDAS:")
        print("• Segurança em IIoT é multilayer")
        print("• Prevenir é melhor que remediar")
        print("• Treinamento contínuo é essencial")
        print("• Backups salvam vidas (digitais)")
        print("="*60)

    def jogar(self):
        """Método principal do jogo"""
        self.limpar_tela()
        self.digitar_lento("🎮 BEM-VINDO AO JOGO INTERATIVO DE SEGURANÇA IIoT - SENAI")
        self.digitar_lento("Você é o Analista de Segurança responsável por proteger uma fábrica inteligente!")
        time.sleep(1)

        # Tutorial
        print("\n📌 COMO JOGAR:")
        print("• Você enfrentará diversos cenários de segurança")
        print("• Suas escolhas afetam pontuação e nível de alerta")
        print("• Gerencie bem seu tempo!")
        print("• Objetivo: Manter a fábrica segura")

        input("\nPressione ENTER para começar sua missão...")

        # Sequência de cenários
        cenarios = [
            self.cenario_ataque_phishing,
            self.cenario_senhas_fracas,
            self.mini_game_firewall,
            self.cenario_ataque_ransomware,
            self.desafio_segmentacao_rede
        ]

        for cenario in cenarios:
            if self.tempo_restante <= 0:
                self.digitar_lento("\n⏰ TEMPO ESGOTADO! Ataque em massa ocorreu!")
                break

            self.mostrar_status()
            cenario()
            self.tempo_restante -= random.randint(1, 3)

        self.mostrar_relatorio_final()

        # Opção de jogar novamente
        print("\n🔄 Deseja jogar novamente? (s/n)")
        if input().lower() == 's':
            self.__init__()
            self.jogar()

# ============================================
# INICIAR JOGO
# ============================================

if __name__ == "__main__":
    jogo = JogoSegurancaIIoT()
    jogo.jogar()    