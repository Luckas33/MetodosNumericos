## 📊 Sistemas Lineares

Este módulo trata da resolução de sistemas lineares de equações, abordando desde o cálculo de determinantes até os principais métodos de eliminação e escalonamento: **método de Gauss** e **método de Gauss-Jordan**.

### 📌 Conteúdo

* Cálculo de determinantes
* Verificação de singularidade
* Escalonamento de matrizes
* Solução de sistemas por:
  * Eliminação de Gauss
  * Eliminação de Gauss-Jordan

### 🧮 Conceitos Importantes

* Um sistema linear  possui solução única se o determinante é diferente de zero.
* O método de **Gauss** transforma a matriz em forma triangular superior para aplicar substituição regressiva.
* O **Gauss-Jordan** vai além e transforma a matriz em forma reduzida por linhas (diagonal principal com 1 e zeros fora dela).

### 💠 Implementações

* `calcular_determinante(matriz)`
* `eh_singular(matriz)`
* `gauss(A, b)` — retorna vetor solução via eliminação de Gauss
* `gauss_jordan(A, b)` — retorna vetor solução via Gauss-Jordan
* `print_matriz_escalonada(A)` — utilitário para exibir a matriz durante o processo

### 📂 Estrutura

```
3-sistemas-lineares/
├── determinantes.py
├── gauss.py
├── gauss_jordan.py
└── README.md
```

### 📅 Observações

* As funções aceitam matrizes como listas de listas (representação nativa do Python).
* O cálculo de determinantes é utilizado como pré-condição para verificar se o sistema admite solução única.
* Para matrizes grandes ou com ponto flutuante, considere o uso do `<span>numpy.linalg</span>` para maior estabilidade numérica.
