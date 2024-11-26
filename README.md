# Gerenciador de Tarefas  

## 📋 Descrição do Projeto  
Este projeto é um sistema de gerenciamento de tarefas desenvolvido em Python, que utiliza estruturas de dados avançadas (pilhas, filas, tabelas hash e heaps) para organizar e priorizar tarefas em um projeto de software.  

### **Funcionalidades Principais**  
- Adicionar tarefas com descrição, prioridade (1 a 10) e responsável.  
- Mover tarefas para o histórico, registrando o tempo de conclusão.  
- Ordenar tarefas por prioridade.  
- Calcular o tempo médio de conclusão das tarefas realizadas.  
- Exibir tarefas pendentes e histórico de tarefas concluídas.  

---

## 🚀 Como Executar o Código  

### **Pré-requisitos**  
- Python 3.8 ou superior instalado no seu computador.  

### **Passo a Passo**  
1. Clone este repositório:  
   ```bash
   git clone https://github.com/seu-usuario/GerenciadorTarefas.git
   ```  
2. Acesse o diretório do projeto:  
   ```bash
   cd GerenciadorTarefas
   ```  
3. Execute o programa:  
   ```bash
   python3 gerenciador_tarefas.py
   ```  

4. Siga as instruções no menu interativo para usar o sistema.  

---

## 📖 Exemplos de Uso  

### **Adicionar uma Tarefa**  
O sistema solicitará a descrição, a prioridade (número entre 1 e 10) e o responsável.  

**Entrada do usuário:**  
```
Descrição da tarefa: Finalizar relatório  
Prioridade (número inteiro entre 1 e 10): 5  
Responsável pela tarefa: João  
```  
**Saída no terminal:**  
```
✅ Tarefa "Finalizar relatório" adicionada com sucesso!
```  

### **Mover Tarefa para o Histórico**  
O sistema listará as tarefas pendentes para o usuário escolher qual deseja mover.  

**Entrada do usuário:**  
```
Digite o número da tarefa que deseja mover para o histórico: 0  
```  
**Saída no terminal:**  
```
✅ Tarefa "Finalizar relatório" movida para o histórico.
```  

### **Calcular Tempo Médio de Conclusão**  
Após concluir algumas tarefas, o tempo médio será calculado automaticamente.  

**Saída no terminal:**  
```
⏱️  Tempo médio de conclusão: 12.34 segundos
```  

---

## 🛠️ Estruturas de Dados Utilizadas  

### **1. Pilha (Histórico de Tarefas Concluídas)**  
- Utilizada para armazenar as tarefas concluídas, permitindo fácil acesso ao histórico.  
- Implementação direta com uma lista (`list`), onde as tarefas são adicionadas e removidas no final (método LIFO).  

### **2. Fila (Tarefas Pendentes)**  
- Responsável por armazenar as tarefas que ainda precisam ser concluídas.  
- Implementada com uma lista simples (`list`).  

### **3. Tabela Hash (Mapeamento de Tarefas a Responsáveis)**  
- Permite associar rapidamente cada tarefa ao seu responsável.  
- Implementada com um dicionário (`dict`) para acesso eficiente por chave.  

### **4. Heap (Ordenação por Prioridade)**  
- Usada para ordenar dinamicamente as tarefas pendentes com base na prioridade.  
- Implementada com a biblioteca padrão `heapq`, que garante eficiência na organização.  

---

## 📌 Observação  
Este projeto foi desenvolvido como parte de uma avaliação acadêmica focada no uso de estruturas de dados avançadas.  
