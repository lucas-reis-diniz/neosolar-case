# Neosolar - Case Geradores

## Descrição
Este projeto foi desenvolvido para o **Case Neosolar**, com o objetivo de gerar combinações automáticas de geradores solares, atendendo aos critérios descritos no documento do case.

A solução utiliza Python para buscar os produtos disponíveis via API e gerar combinações válidas entre painéis solares, inversores e controladores de carga, garantindo que a potência total atenda aos requisitos.

## Tecnologias Utilizadas
- Python
- Pandas
- Requests
- CSV

## Arquitetura
1. **Busca de Produtos:**
   - Os produtos são obtidos via API disponibilizada no case.
   - A lista contém três categorias: Painel Solar, Inversor e Controlador de Carga.

2. **Filtragem de Produtos:**
   - Os produtos são filtrados por categoria para facilitar a geração de combinações.

3. **Geração de Combinações:**
   - O algoritmo combina até 2 painéis solares para alcançar a potência desejada.
   - As combinações são validadas para garantir que a potência dos painéis solares seja igual à potência do inversor e do controlador de carga.

4. **Criação do CSV:**
   - As combinações são armazenadas em um arquivo **geradores_configurados.csv**, contendo:
     - ID do Gerador
     - Potência
     - ID do Produto
     - Nome do Produto
     - Quantidade

## Como Executar
### Pré-requisitos
- Python 3.10+
- Instalar dependências:
```bash
pip install requests pandas
```

### Execução
```bash
python main.py
```

O arquivo **geradores_configurados.csv** será gerado na raiz do projeto.

## Validação
- Todos os geradores possuem exatamente 4 componentes.
- A potência dos painéis solares é **igual** à potência do inversor e do controlador de carga.
- Não há combinações duplicadas.

## Melhorias Futuras
- Suporte para mais de 2 painéis solares.
- Otimização de performance para grandes volumes de produtos.
- Interface gráfica para seleção de parâmetros.

## Desenvolvido Por:
Lucas Reis Diniz

LinkedIn: [https://www.linkedin.com/in/lucas-reis-diniz-13516421b/](https://www.linkedin.com/in/lucas-reis-diniz-13516421b/)

---
Projeto desenvolvido para o processo seletivo da Neosolar. 🌞⚡

