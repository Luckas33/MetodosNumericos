# 📐 Interpolação Polinomial

Este repositório contém implementações de diferentes métodos de **interpolação polinomial** em Python. A interpolação polinomial é uma técnica de análise numérica para construir um novo polinômio que passa exatamente por um conjunto de pontos de dados conhecidos.

---

## 🧮 O Problema Fundamental

Dado um conjunto de $n+1$ pontos distintos $(x_0, y_0), (x_1, y_1), \dots, (x_n, y_n)$, o objetivo é encontrar um polinômio $P_n(x)$ de grau no máximo $n$ que satisfaça a condição de interpolação:

$$
P_n(x_i) = y_i, \quad \text{para todo } i = 0, 1, \dots, n
$$

Este polinômio é único e é chamado de polinômio interpolador.

---

## 📏 Métodos de Interpolação

Existem várias formas de se calcular e representar o polinômio interpolador. Este repositório aborda as seguintes:

### 1. Forma de Lagrange

A interpolação de Lagrange constrói o polinômio como uma combinação linear de polinômios base de Lagrange $L_i(x)$. A fórmula é:

$$
P_n(x) = \sum_{i=0}^{n} y_i L_i(x)
$$

Onde cada polinômio da base de Lagrange $L_i(x)$ é definido por:

$$
L_i(x) = \prod_{\substack{j=0 \\ j \neq i}}^{n} \frac{x - x_j}{x_i - x_j}
$$

Cada $L_i(x)$ tem a propriedade de ser igual a $1$ em $x=x_i$ e $0$ em $x=x_j$ para $j \neq i$.

### 2. Forma de Newton

A interpolação de Newton utiliza o método das **diferenças divididas** para construir o polinômio de forma incremental. Sua forma é:

$$
P_n(x) = a_0 + a_1(x - x_0) + a_2(x - x_0)(x - x_1) + \dots + a_n(x - x_0) \cdots (x - x_{n-1})
$$

Onde os coeficientes $a_k$ são as diferenças divididas, calculadas como:

$$
a_k = f[x_0, x_1, \dots, x_k]
$$

As diferenças divididas são definidas recursivamente:

* **Ordem 0:**
  $$
  [x_i] = y_i
  $$
* **Ordem k:**
  $$
  [x_i, x_{i+1}, \dots, x_{i+k}] = \frac{f[x_{i+1}, \dots, x_{i+k}] - f[x_i, \dots, x_{i+k-1}]}{x_{i+k} - x_i}
  $$

---

## 📈 Vantagens da Interpolação de Newton

A forma de Newton é frequentemente preferida na prática por suas vantagens computacionais:

* **Adição de Novos Pontos:** Se um novo ponto $(x_{n+1}, y_{n+1})$ for adicionado, os coeficientes $a_0, \dots, a_n$ já calculados permanecem os mesmos. Apenas o novo coeficiente $a_{n+1}$ precisa ser calculado, tornando o processo mais eficiente.
* **Estrutura Incremental:** A natureza aninhada do polinômio permite uma avaliação eficiente do valor de $P_n(x)$ em um ponto específico usando o **algoritmo de Horner**.

---

## 🧑‍💻 Estrutura do Repositório

Os arquivos neste repositório demonstram a implementação dos métodos de interpolação:

* `1-SistemaLinear/InterpolaLinear.py`: Demonstra a interpolação polinomial através da resolução de um sistema de equações lineares (Método de Vandermonde).
* `2-Quadratica/InterpolaQuadratica.py`: Exemplo específico de interpolação para um polinômio de grau 2 (quadrático).
* `3-Lagrange/Lagrange.py`: Implementação do método de interpolação usando os polinômios de base de Lagrange.
* `4-Newton/Newton.py`: Implementação do método de interpolação de Newton utilizando diferenças divididas.
