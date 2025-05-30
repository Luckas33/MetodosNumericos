## 📘 Cálculo do Erro

Este módulo aborda os conceitos e implementações relacionadas ao  **cálculo de erro numérico** , frequentemente utilizado na análise de algoritmos matemáticos e métodos numéricos.

### 📌 Conteúdo

* Diferença entre erro absoluto e erro relativo
* Cálculo do erro verdadeiro e erro aproximado
* Aplicações práticas em algoritmos de aproximação
* Exemplos implementados em Python

### 🧮 Fórmulas Utilizadas

* **Erro Absoluto (EA)** :

    $EA = |x_{\text{verdadeiro}} - x_{\text{aproximado}}|$

* **Erro Relativo (ER)** :

    $	ER = \frac{|x_{\text{verdadeiro}} - x_{\text{aproximado}}|}{|x_{\text{verdadeiro}}|}$

* **Erro Relativo Percentual (ERP)** :

    $ERP=$$(\frac{EA}{|x_{\text{verdadeiro}}|}) \times 100\%$

* **Erro Relativo Percentual Aproximado** (em métodos iterativos):

  $ERP_{aprox} = \left( \frac{|x_{\text{novo}} - x_{\text{antigo}}|}{|x_{\text{novo}}|} \right) \times 100\%$

### 💠 Implementações

As funções disponíveis neste diretório permitem calcular os erros dados valores reais ou aproximados. Exemplos:

* `erroAbsoluto(x_real, x_aproximado)`
* `erroRelativo(x_real, x_aproximado)`
* `erroRelativoPercentual(x_real, x_aproximado)`
* `erroRelativoAproximadoPercentual(x_novo, x_antigo)`

### 📂 Estrutura

```
0-calculoErro/
├── erroAbsoluto.py
├── erroRelativo.py
└── README.md
```
