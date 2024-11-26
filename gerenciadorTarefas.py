import heapq
import time


class GerenciadorTarefas:
    def __init__(self):
        self.historico_tarefas = []  # Pilha para histórico de tarefas concluídas
        self.tarefas_pendentes = []  # Lista para tarefas pendentes
        self.heap_prioridade = []  # Heap para ordenação por prioridade
        self.mapeamento_tarefa_responsavel = {}  # Tabela hash tarefa -> responsável
        self.tempos_conclusao = []  # Para calcular o tempo médio de conclusão

    def adicionar_tarefa(self, descricao, prioridade, responsavel):
        if not descricao or not responsavel:
            print("\n⚠️  Erro: A descrição e o responsável não podem estar vazios.")
            return
        if not (1 <= prioridade <= 10):
            print("\n⚠️  Erro: A prioridade deve estar entre 1 e 10.")
            return

        tarefa = {
            "descricao": descricao,
            "prioridade": prioridade,
            "responsavel": responsavel,
            "tempo_criacao": time.time()
        }

        self.tarefas_pendentes.append(tarefa)
        heapq.heappush(self.heap_prioridade, (prioridade, descricao))
        self.mapeamento_tarefa_responsavel[descricao] = responsavel
        print(f'\n✅ Tarefa "{descricao}" adicionada com sucesso!')

    def mover_para_historico(self):
        if not self.tarefas_pendentes:
            print("\n⚠️  Nenhuma tarefa pendente para mover.")
            return

        print("\n📋 Tarefas pendentes:")
        for i, tarefa in enumerate(self.tarefas_pendentes):
            print(f"{i}. {tarefa['descricao']} (Prioridade: {tarefa['prioridade']}, Responsável: {tarefa['responsavel']})")

        try:
            escolha = int(input("\nDigite o número da tarefa que deseja mover para o histórico: "))
            if escolha < 0 or escolha >= len(self.tarefas_pendentes):
                print("\n⚠️  Escolha inválida! Operação cancelada.")
                return

            tarefa = self.tarefas_pendentes.pop(escolha)

            # Remover tarefa da heap
            self.heap_prioridade = [
                item for item in self.heap_prioridade if item[1] != tarefa["descricao"]
            ]
            heapq.heapify(self.heap_prioridade)

            # Calcular tempo de conclusão
            tempo_conclusao = time.time() - tarefa["tempo_criacao"]
            self.tempos_conclusao.append(tempo_conclusao)

            self.historico_tarefas.append(tarefa)
            print(f'\n✅ Tarefa "{tarefa["descricao"]}" movida para o histórico.')

        except ValueError:
            print("\n⚠️  Entrada inválida! Operação cancelada.")

    def listar_tarefas_ordenadas(self):
        if not self.heap_prioridade:
            print("\n⚠️  Nenhuma tarefa pendente.")
            return

        print("\n📋 Tarefas pendentes ordenadas por prioridade:")
        for prioridade, descricao in sorted(self.heap_prioridade):
            print(f"- Prioridade: {prioridade} | Descrição: {descricao}")

    def calcular_tempo_medio_conclusao(self):
        if not self.tempos_conclusao:
            print("\n⚠️  Nenhuma tarefa foi concluída ainda.")
            return 0

        tempo_medio = sum(self.tempos_conclusao) / len(self.tempos_conclusao)
        print(f"\n⏱️  Tempo médio de conclusão: {tempo_medio:.2f} segundos")
        return tempo_medio

    def exibir_tarefas(self):
        print("\n📌 Tarefas Pendentes:")
        if not self.tarefas_pendentes:
            print("⚠️  Nenhuma tarefa pendente.")
        else:
            for tarefa in self.tarefas_pendentes:
                print(f'- {tarefa["descricao"]} (Prioridade: {tarefa["prioridade"]}, Responsável: {tarefa["responsavel"]})')

        print("\n📜 Histórico de Tarefas Concluídas:")
        if not self.historico_tarefas:
            print("⚠️  Nenhuma tarefa concluída.")
        else:
            for tarefa in reversed(self.historico_tarefas):
                print(f'- {tarefa["descricao"]} (Responsável: {tarefa["responsavel"]})')


# Menu interativo
def menu_interativo():
    gerenciador = GerenciadorTarefas()

    while True:
        print("\n🛠️   MENU DE GERENCIAMENTO DE TAREFAS 🛠️")
        print("1. Adicionar Tarefa")
        print("2. Mover Tarefa para o Histórico")
        print("3. Listar Tarefas Ordenadas por Prioridade")
        print("4. Calcular Tempo Médio de Conclusão")
        print("5. Exibir Tarefas (Pendentes e Histórico)")
        print("6. Sair")
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            descricao = input("\nDescrição da tarefa: ")

            while True:
                try:
                    prioridade = int(input("Prioridade (número inteiro entre 1 e 10): "))
                    if 1 <= prioridade <= 10:
                        break
                    else:
                        print("⚠️  Erro: A prioridade deve estar entre 1 e 10.")
                except ValueError:
                    print("⚠️  Erro: A prioridade deve ser um número inteiro.")

            responsavel = input("Responsável pela tarefa: ")
            gerenciador.adicionar_tarefa(descricao, prioridade, responsavel)

        elif opcao == "2":
            gerenciador.mover_para_historico()

        elif opcao == "3":
            gerenciador.listar_tarefas_ordenadas()

        elif opcao == "4":
            gerenciador.calcular_tempo_medio_conclusao()

        elif opcao == "5":
            gerenciador.exibir_tarefas()

        elif opcao == "6":
            print("\n👋 Saindo do sistema...")
            break

        else:
            print("\n⚠️  Opção inválida! Tente novamente.")


if __name__ == "__main__":
    menu_interativo()
