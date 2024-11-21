# **Manual do Sistema de Gerenciamento de Treinos de Corrida**

## **1. Introdução**
O **Sistema de Gerenciamento de Treinos de Corrida** foi desenvolvido para ajudar Pedro a organizar e acompanhar seus treinos, competições e progresso ao longo do tempo. Com este sistema, você pode:
- Registrar informações sobre **treinos** e **competições**.
- Monitorar seu desempenho com base em **tempo** e **distância**.
- Filtrar dados para analisar seu progresso.
- Receber sugestões de treinos aleatórios para variar a rotina.

Esse manual detalha todas as funcionalidades e como utilizá-las.



## **2. Requisitos do Sistema**
Antes de utilizar o programa, verifique os requisitos mínimos:
- **Sistema Operacional:** Windows, macOS ou Linux.
- **Python:** Versão 3.8 ou superior.
- **Bibliotecas Python:** Apenas as bibliotecas padrão.



## **3. Funcionalidades**

### **3.1 Registro e visualização de Treinos e Competições**
Registre informações detalhadas sobre suas atividades:
- **Tipo:** Indique se foi um treino ou uma competição.
- **Data:** Informe a data da atividade.
- **Distância:** Informe a distância percorrida (em km).
- **Tempo:** Informe o tempo gasto (em minutos).
- **Local** Informe o local onde foi realizado o treino ou competicão.
- **Clima** Informe o clima de onde você realizou.
  

### **3.2 Filtros de Dados**
Analise seu progresso utilizando filtros:
- **Por Tempo:** Veja todas as atividades realizadas em um tempo específico.
- **Por Distância:** Veja todas as atividades realizadas para uma distância específica.

### **3.3 Sugestões de Treinos Aleatórios**
O sistema sugere treinos aleatórios baseados no histórico registrado, incentivando a variação na rotina e melhora do desempenho.

---
# **Manual do Sistema de Gerenciamento de Treinos de Corrida**

## **Descrição do Problema**
Pedro, um atleta dedicado, enfrenta desafios para acompanhar seus treinos, tempos em provas e progresso ao longo do tempo. Para ajudá-lo a resolver esse problema, criamos um **Sistema de Gerenciamento de Treinos de Corrida**, que permite a Pedro registrar seus treinos e competições, monitorando sua evolução e ajudando a planejar novos desafios.

![Menu do Programa]([https://github.com/Artur-Antunes-1/Projeto-FP/blob/main/image.png](https://github.com/Artur-Antunes-1/Projeto-FP/blob/main/Menu.png))  

---

## **Funcionalidades**

### **Funcionalidade 1 - Adicionar**
Ao entrar no sistema, Pedro pode escolher se deseja salvar a atividade como **competição** ou **treino**. Após isso, ele deve inserir os seguintes dados:

- **Data da Atividade**
- **Distância**
- **Tempo em minutos**
- **Localização**
- **Condições Climáticas durante a atividade**

Essas informações são salvas em um arquivo `.txt`.

### **Funcionalidade 2 - Visualizar**
Ao acessar esta funcionalidade, Pedro verá o número total de **treinos** e **competições** registrados. Em seguida, o sistema exibe um menu de opções de visualização dos treinos:

- **[1]** Ver todos os treinos e competições.
- **[2]** Ver treinos ou competições específicas pelo ID.
- **[3]** Voltar ao menu principal.

### **Funcionalidade 3 - Atualizar um Treino**
Ao acessar essa opção, Pedro será solicitado a inserir o **ID** do treino ou competição que deseja atualizar. Em seguida, ele escolherá uma das seguintes opções de atualização:

- **[1]** Atualizar data
- **[2]** Atualizar distância
- **[3]** Atualizar tempo
- **[4]** Atualizar localização
- **[5]** Atualizar clima
- **[6]** Voltar ao menu principal

### **Funcionalidade 4 - Excluir**
Pedro pode excluir um treino ou competição ao fornecer o **ID** da atividade que deseja remover do sistema.

### **Funcionalidade 5 - Metas**
Pedro pode definir, visualizar e excluir metas no sistema. O menu de metas tem as seguintes opções:

- **[1]** Adicionar meta
  - **[1]** Adicionar meta de tempo
  - **[2]** Adicionar meta de distância
  - **[3]** Adicionar meta de tempo e distância
  - **[4]** Voltar

- **[2]** Visualizar metas
- **[3]** Excluir meta (informe o ID da meta a ser excluída)

### **Funcionalidade 6 - Sugestão**
O sistema sugere um treino aleatório com base nos treinos realizados de Pedro.

### **Funcionalidade 7 - Filtragem de Treinos**
Um menu de filtragem de treinos com base no tempo ou distância. As opções são:

- **[1]** Filtrar treinos por tempo.
- **[2]** Filtrar treinos por distância.
- **[3]** Voltar ao menu principal.

### **Funcionalidade 8 - Pace**
Essa funcionalidade exibe todos os paces registrados nos treinos de Pedro.

### **Funcionalidade 0 - Sair**
Esta opção permite que Pedro saia do programa.

---


