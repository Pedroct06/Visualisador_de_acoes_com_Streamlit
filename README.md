# 📈 Visualização de Ações

Aplicação web desenvolvida com Streamlit para visualizar o desempenho histórico de ações da bolsa de valores.

## 🚀 Funcionalidades

- Busca de ações por ticker (código)
- Visualização do preço atual
- Cálculo da variação total no período
- Cálculo da variação percentual
- Gráfico de linha com o histórico de preços

## 📋 Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes do Python)

## 🔧 Instalação

1. Clone este repositório:
```bash
git clone https://github.com/Pedroct06/Visualisador_de_acoes_com_Streamlit.git
cd Visualisador_de_acoes_com_Streamlit
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

Ou instale manualmente:
```bash
pip install streamlit pandas yfinance
```

## 💻 Como usar

1. Execute a aplicação:
```bash
streamlit run acoes.py
```

2. O navegador abrirá automaticamente com a aplicação

3. Selecione o período de tempo a ser observado

4. Digite o código da ação desejada no campo de texto. Exemplos:
   - **Ações brasileiras**: PETR4.SA, VALE3.SA, ITUB4.SA, BBDC4.SA
   - **Ações americanas**: AAPL, GOOGL, MSFT, TSLA

5. Clique em "Buscar ação" ou pressione Enter

6. Visualize os resultados:
   - Preço atual da ação
   - Variação total em reais
   - Variação percentual
   - Gráfico histórico de preços

## 📦 Dependências

- **streamlit**: Framework para criação da interface web
- **pandas**: Manipulação e análise de dados
- **yfinance**: Download de dados financeiros do Yahoo Finance

## 📝 Estrutura do projeto

```
.
├── acoes.py           # Código principal da aplicação
├── requirements.txt   # Dependências do projeto
└── README.md         # Este arquivo
```

## ⚠️ Observações

- Para ações brasileiras, adicione `.SA` ao final do ticker (ex: PETR4.SA)
- Os dados são obtidos do Yahoo Finance através da biblioteca yfinance
- A aplicação utiliza cache para otimizar o carregamento dos dados
- Certifique-se de ter conexão com a internet para buscar os dados

## 🐛 Problemas comuns

**Erro ao carregar dados**: Verifique se o código da ação está correto e no formato adequado (com .SA para ações brasileiras)

**Nenhuma ação encontrada**: O ticker pode estar incorreto ou a ação pode não estar disponível no Yahoo Finance

## 📄 Licença

Este projeto está sob a licença MIT.

## 👤 Autor

Pedro Henrique Coelho Torres - [Pedroct06](https://github.com/Pedroct06)

---

⭐ Se este projeto foi útil para você, considere dar uma estrela no repositório!