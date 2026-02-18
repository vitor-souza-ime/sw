
# Análise de Normalidade de Dados com Python

Este repositório contém um script em Python (`main.py`) para demonstrar **testes de normalidade estatística** e visualizações gráficas de dados sintéticos. O projeto é ideal para estudo e compreensão de distribuições estatísticas, testes de hipóteses e análise exploratória de dados.

## 🎯 Objetivo

O objetivo do script é:

* Gerar conjuntos de dados com diferentes distribuições (normal e não normal).
* Aplicar o **teste de Shapiro-Wilk** para verificar se os dados seguem uma distribuição normal.
* Visualizar os dados através de **histogramas** e **Q-Q plots**, permitindo análise visual da normalidade.

## ⚙️ Metodologia

1. **Geração de dados sintéticos**
   Dois conjuntos de 100 valores são gerados com `numpy`:

   * **Gaussianos**: dados com distribuição normal (`loc=0, scale=1`).
   * **Não Gaussianos**: dados com distribuição exponencial (`scale=1`).

2. **Teste estatístico de normalidade**
   O **teste de Shapiro-Wilk** é aplicado a cada conjunto de dados.

   * Valor-p > 0.05 → dados **provavelmente normais**
   * Valor-p ≤ 0.05 → dados **não normais**

3. **Visualização dos dados**
   Para cada conjunto:

   * **Histograma**: mostra a distribuição dos dados.
   * **Q-Q Plot (quantile-quantile plot)**: compara os quantis dos dados com os quantis teóricos de uma distribuição normal.

   Isso permite confirmar visualmente se os dados seguem uma distribuição normal.

## 🧪 Pré-requisitos

Instale as bibliotecas necessárias:

pip install numpy matplotlib scipy

## ▶️ Como executar

No terminal, execute:

python main.py

O script exibirá no terminal os resultados do **teste de Shapiro-Wilk** e abrirá os gráficos correspondentes para cada conjunto de dados.

## 📈 Resultados Esperados

* Para os dados gaussianos: o teste de Shapiro-Wilk deve indicar normalidade, e os gráficos mostrarão uma forma aproximadamente simétrica no histograma e pontos próximos da linha no Q-Q plot.
* Para os dados não gaussianos: o teste indicará que os dados não seguem distribuição normal, e os gráficos evidenciarão assimetria no histograma e desvio da linha no Q-Q plot.

## 📝 Observações

Este projeto é útil para:

* Compreender conceitos básicos de estatística descritiva e testes de normalidade.
* Visualizar diferenças entre distribuições normais e não normais.
* Servir como base para análises exploratórias em projetos maiores de ciência de dados.


