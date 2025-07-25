
# 📈 Integração Numérica

Este repositório contém implementações em Python de métodos clássicos de **integração numérica**, também conhecida como **quadratura numérica**. O objetivo desses métodos é encontrar um valor aproximado para uma integral definida.

---

## 🎯 O Problema Fundamental

A integração numérica é essencial quando a integral de uma função não pode ser resolvida analiticamente (ou seja, não possui uma primitiva expressa em termos de funções elementares) ou quando a função é conhecida apenas a partir de um conjunto de pontos de dados discretos.

O problema consiste em calcular o valor de uma integral definida:

$$
I = \int_{a}^{b} f(x) \,dx
$$

A ideia central por trás dos métodos aqui apresentados é aproximar a área sob a curva de $f(x)$ dividindo o intervalo $[a, b]$ em $n$ subintervalos menores e somando as áreas de formas geométricas simples (trapézios, parábolas, etc.) que aproximam a função em cada subintervalo.

---

## 🛠️ Métodos Implementados

As técnicas a seguir, conhecidas como fórmulas de Newton-Cotes, são abordadas neste repositório.

### 1. Regra do Trapézio

Esta regra aproxima a área sob a curva de $f(x)$ em um intervalo usando um único trapézio.

* **Fórmula Simples:**

  $$
  \approx \frac{h}{2} [f(a) + f(b)], \quad \text{onde } h = b - a
  $$
* **Fórmula Repetida (Composta):** Para maior precisão, o intervalo $[a, b]$ é dividido em $n$ subintervalos.

  $$
  \approx \frac{h}{2} \left[ f(x_0) + 2 \sum_{i=1}^{n-1} f(x_i) + f(x_n) \right], \quad \text{onde } h = \frac{b-a}{n}
  $$

### 2. Regra de 1/3 de Simpson

Este método aproxima a função $f(x)$ usando um polinômio de grau 2 (uma parábola), o que geralmente resulta em uma aproximação mais precisa que a regra do trapézio.

* **Fórmula Simples:** Requer 3 pontos ($x_0, x_1, x_2$), ou seja, 2 subintervalos.

  $$
  \approx \frac{h}{3} [f(x_0) + 4f(x_1) + f(x_2)]
  $$
* **Fórmula Repetida (Composta):**

  $$
  \approx \frac{h}{3} \left[ f(x_0) + 4 \sum_{i=1,3,5,\dots}^{n-1} f(x_i) + 2 \sum_{i=2,4,6,\dots}^{n-2} f(x_i) + f(x_n) \right]
  $$

  > **Nota:** A regra de 1/3 de Simpson repetida exige que o número de subintervalos $n$ seja **par**.
  >

### 3. Regra de 3/8 de Simpson

Esta regra utiliza um polinômio de grau 3 para aproximar a função, oferecendo ainda mais precisão para funções suaves.

* **Fórmula Simples:** Requer 4 pontos ($x_0, x_1, x_2, x_3$), ou seja, 3 subintervalos.

  $$
  \approx \frac{3h}{8} [f(x_0) + 3f(x_1) + 3f(x_2) + f(x_3)]
  $$
* **Fórmula Repetida (Composta):**

  $$
  \approx \frac{3h}{8} \left[ f(x_0) + 3\sum_{i=1,2,4,5,\dots}^{n-1} f(x_i) + 2\sum_{i=3,6,9,\dots}^{n-3} f(x_i) + f(x_n) \right]
  $$

  > **Nota:** A regra de 3/8 de Simpson repetida exige que o número de subintervalos $n$ seja um **múltiplo de 3**.
  >

---

## 🧑‍💻 Estrutura do Código

O arquivo `integracao_numerica.py` contém as seguintes funções:

* `f(x)`: Uma função de exemplo para ser integrada.
* `integral_analitica_f(a, b)`: A solução exata da integral para fins de comparação.
* `regra_trapezio(f, a, b)`: Implementação da regra do trapézio simples.
* `regra_trapezio_repetida(f, a, b, n)`: Implementação da regra do trapézio composta.
* `regra_um_terco_simpson(f, a, b)`: Implementação da regra de 1/3 de Simpson simples.
* `regra_um_terco_simpson_repetida(f, a, b, n)`: Implementação da regra de 1/3 de Simpson composta.
* `regra_tres_oitavos_simpson(f, a, b)`: Implementação da regra de 3/8 de Simpson simples.
* `regra_tres_oitavos_simpson_repetida(f, a, b, n)`: Implementação da regra de 3/8 de Simpson composta.
