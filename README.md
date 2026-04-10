
# Jogo Interativo de Segurança IIoT - SENAI

[![Status](https://img.shields.io/badge/status-ativo-brightgreen.svg)]()
[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)]()
[![License](https://img.shields.io/badge/license-MIT-lightgrey.svg)]()

## Sobre o Projeto

O Jogo Interativo de Segurança IIoT é uma ferramenta educacional desenvolvida para o SENAI com o objetivo de treinar profissionais de segurança cibernética em ambientes industriais (IIoT - Industrial Internet of Things).

Através de cenários realistas e desafiadores, o jogador assume o papel de um Analista de Segurança responsável por proteger uma fábrica inteligente contra ameaças cibernéticas.

## Objetivos Educacionais

- Identificar e responder a ataques de phishing em ambientes industriais
- Implementar políticas de senhas fortes e autenticação multifator
- Configurar corretamente firewalls industriais
- Gerenciar crises durante ataques de ransomware
- Aplicar conceitos de segmentação de rede (IT vs OT)

## Funcionalidades

### Cenários de Aprendizado

| Cenário | Descrição | Habilidade Desenvolvida |
|---------|-----------|------------------------|
| Ataque de Phishing | Email suspeito direcionado a operadores | Conscientização de usuários |
| Senhas Fracas | Dispositivos com credenciais padrão | Gerenciamento de acesso |
| Configuração de Firewall | Mini-game de regras de firewall | Segurança de perímetro |
| Ataque Ransomware | Crise em tempo real | Resposta a incidentes |
| Segmentação de Rede | Classificação IT/OT de dispositivos | Arquitetura segura |

### Sistema de Progressão

- Pontuação dinâmica: Suas escolhas afetam diretamente sua pontuação
- Nível de alerta: Indicador visual do estado de segurança da fábrica
- Gerenciamento de tempo: Decisões devem ser rápidas e precisas
- Inventário: Colete evidências e relatórios durante o jogo
- Classificação final: De "Fábrica Comprometida" a "Especialista IIoT"

## Como Executar

### Pré-requisitos

```bash
Python 3.7 ou superior
```

### Instalação

1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/jogo-seguranca-iiot.git
cd jogo-seguranca-iiot
```

2. Execute o jogo
```bash
python jogo_iiot.py
```

## Como Jogar

1. Inicie o jogo e leia as instruções iniciais
2. Enfrente cenários escolhendo entre opções numeradas (1-4)
3. Gerencie seu tempo - decisões atrasadas podem ser custosas
4. Monitore seu status a cada rodada (pontuação, alerta, inventário)
5. Complete todos os cenários para receber seu relatório final

### Comandos Básicos

- Digite 1, 2, 3 ou 4 para escolher ações
- Pressione ENTER para avançar diálogos
- Ao final, digite s para jogar novamente ou n para sair

## Sistema de Pontuação

### Pontuações Positivas
- Bloquear phishing corretamente: +10
- Implementar 2FA em todos dispositivos: +20
- Configurar firewall corretamente: +25
- Isolar rede durante ransomware: +30
- Segmentação correta (7+/9 acertos): +25

### Penalidades
- Ignorar phishing: -15
- Negociar com ransomware: -30
- Desligamento inadequado: -10
- Erro na configuração do firewall: -5 por porta incorreta

## Classificações

| Pontuação | Título | Descrição |
|-----------|--------|-----------|
| >= 80 | ESPECIALISTA EM IIoT | Proteção exemplar da fábrica |
| 50-79 | TÉCNICO SENAI | Bom desempenho, precisa de melhorias |
| 20-49 | EM TREINAMENTO | Conhecimento básico, estudar mais |
| < 20 | FÁBRICA COMPROMETIDA | Falhas críticas de segurança |

## Tecnologias Utilizadas

- Python 3.7+ - Linguagem principal
- Bibliotecas padrão:
  - time - Efeitos de digitação e delays
  - random - Gerador de eventos aleatórios
  - os - Limpeza de tela multi-plataforma
  - datetime - Registro de timestamps

## Estrutura do Projeto

```
jogo-seguranca-iiot/
│
├── jogo_iiot.py           # Arquivo principal do jogo
├── README.md              # Documentação

```

## Público-alvo

- Estudantes de cybersecurity do SENAI e outras instituições
- Profissionais de TI/OT em transição para segurança industrial
- Instrutores que buscam ferramentas interativas de ensino
- Entusiastas de segurança cibernética

## Dicas para Instrutores

### Aplicação em Sala de Aula

1. Pré-aula (30 min): Conceitos básicos de IIoT
2. Atividade prática (45 min): Jogo completo
3. Debriefing (30 min): Discussão das escolhas e consequências
4. Avaliação (20 min): Relatório individual dos alunos

### Métricas de Avaliação

- Capacidade de identificar ameaças
- Tempo de resposta a incidentes
- Conhecimento de portas e protocolos
- Entendimento da segregação IT/OT

## Próximas Atualizações (Roadmap)

- Modo multiplayer com rankings
- Novos cenários (ataque a supply chain, IoT hijacking)
- Interface gráfica (Tkinter/PyGame)
- Exportação de relatórios em PDF
- Sistema de conquistas e badges
- Banco de dados de incidentes reais
- Modo sandbox para treinamento livre

## Contribuições

Contribuições são bem-vindas! Para contribuir:

1. Faça um Fork do projeto
2. Crie uma Branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request


<div align="center">
  Desenvolvido para o futuro da segurança industrial
  
  Iniciar Jogo
</div>

---

# Dashboard de Monitoramento IIoT - Cybersegurança Industrial

## Sobre o Projeto

O Dashboard de Monitoramento IIoT é uma ferramenta web interativa para simulação e visualização de ataques cibernéticos em ambientes industriais. Desenvolvido com HTML, CSS e JavaScript puros, o sistema demonstra em tempo real como invasões podem afetar sensores industriais e como mecanismos de autodefesa respondem a essas ameaças.

## Funcionalidades

### Monitoramento em Tempo Real

- **Três dispositivos industriais simulados:**
  - Termo-Forno Industrial (monitoramento de temperatura)
  - Motor de Indução (monitoramento de vibração)
  - Esteira Logística (monitoramento de corrente elétrica)

### Indicadores Visuais

- Barras de progresso dinâmicas para cada sensor
- Código de cores (verde para normal, vermelho para alerta)
- Badges de status (ESTÁVEL/CRÍTICO)
- Efeito de pulsação no cabeçalho durante ataques

### Simulação de Ataques

- **Ataques manuais:**
  - Injetar Calor (eleva temperatura do forno)
  - Sabotar Eixo (aumenta vibração do motor)
  - Pico de Corrente (eleva corrente da esteira)

- **Ataques automáticos:** O sistema gera ataques aleatórios a cada 25 segundos

### Sistema de Defesa

- **Recuperação automática:** Os sensores retornam gradualmente aos valores normais
- **Purge & Hard Reset:** Botão para restauração imediata de todos os parâmetros
- **Log de eventos:** Console com histórico de todas as ações e alertas

### Métricas

- Contador de ataques detectados
- Contador de auto-recuperações
- Uptime do sistema

## Como Executar

### Pré-requisitos

Nenhum! O projeto roda em qualquer navegador moderno.

### Execução

1. Salve o código HTML em um arquivo com extensão `.html` (ex: `dashboard-iiot.html`)
2. Abra o arquivo em qualquer navegador web
3. O dashboard iniciará automaticamente com o monitoramento ativo

### Ou acesse online

Basta abrir o arquivo HTML diretamente no navegador - não há necessidade de servidor web.

## Como Usar

### Simulação de Ataques

1. **Ataques manuais:** Clique nos botões vermelhos para simular diferentes tipos de invasão
2. **Ataques automáticos:** Aguarde 25 segundos para ver o sistema sendo testado automaticamente

### Monitoramento

- Observe as barras de progresso mudando de cor (verde para vermelho)
- Acompanhe o console de logs para ver todos os eventos registrados
- Verifique os contadores de ataques e recuperações

### Resposta a Incidentes

- O sistema se recupera automaticamente em alguns segundos
- Use o botão "Purge & Hard Reset" para restauração imediata

## Tecnologias Utilizadas

- **HTML5** - Estrutura da página
- **CSS3** - Estilização com Glassmorphism, animações e layout responsivo
- **JavaScript (Vanilla)** - Lógica de simulação, atualizações em tempo real e manipulação do DOM

## Estrutura do Projeto

```
dashboard-iiot/
│
├── index.html             # Arquivo único com todo o código
└── README.md              # Documentação
```

## Arquitetura do Sistema

### Componentes Principais

1. **Estado dos Dispositivos** - Objeto JavaScript que mantém os valores atuais
2. **Detector de Anomalias** - Função que verifica violações de limites de segurança
3. **Sistema de Auto-Recuperação** - Algoritmo que gradualmente normaliza os valores
4. **Interface Visual** - Atualização dinâmica do DOM a cada 100ms
5. **Gerador de Ameaças** - Ataques manuais e automáticos

### Limites de Segurança Configurados

| Dispositivo | Parâmetro | Limite Seguro | Estado Crítico |
|-------------|-----------|---------------|----------------|
| Termo-Forno | Temperatura | até 230°C | acima de 230°C |
| Motor | Vibração | até 1.20 mm/s | acima de 1.20 mm/s |
| Esteira | Corrente | 10-20A | fora da faixa |

## Cenários de Aprendizado

### Para Estudantes de Cybersegurança

- **Impacto de ataques OT:** Visualize como invasões afetam sensores físicos
- **Detecção de anomalias:** Aprenda a identificar padrões anormais
- **Resposta a incidentes:** Observe mecanismos de auto-recuperação

### Para Instrutores

- Demonstre conceitos de segurança industrial
- Simule ataques sem riscos ao ambiente real
- Ensine sobre limites operacionais e zonas de segurança

## Personalização

### Alterando Limites de Segurança

No JavaScript, modifique os valores no objeto `devices`:

```javascript
const devices = {
    forno: { temperature: 200, targetTemp: 200, status: 'normal', limit: 230 },
    motor: { vibration: 0.5, targetVib: 0.5, status: 'normal', limit: 1.2 },
    esteira: { current: 15, targetCurrent: 15, status: 'normal', limitMin: 10, limitMax: 20 }
};
```

### Alterando Cores do Tema

Modifique as variáveis CSS no início do arquivo:

```css
:root {
    --primary: #00ff9d;   /* Verde neon para estado OK */
    --danger: #ff3e3e;    /* Vermelho para alertas */
    --warning: #ffbe0b;   /* Amarelo para avisos */
    --bg-dark: #05070a;   /* Fundo escuro */
}
```

## Próximas Atualizações (Roadmap)

- Adicionar mais dispositivos industriais (bombas, compressores, válvulas)
- Implementar gráficos históricos de tendências
- Adicionar diferentes tipos de ataque (MITM, DoS, replay attack)
- Exportar logs de incidentes
- Modo noturno/configurável
- API para integração com sistemas reais de SCADA

## Contribuições

Contribuições são bem-vindas! Para contribuir com o Dashboard IIoT:

1. Faça um Fork do projeto
2. Crie uma Branch para sua feature
3. Commit suas mudanças
4. Push para a Branch
5. Abra um Pull Request



<div align="center">
  Dashboard interativo para demonstração de conceitos de segurança industrial
  
  [Executar Dashboard] - Basta abrir o arquivo HTML no navegador
</div>
```
