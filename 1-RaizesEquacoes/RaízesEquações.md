## 🔄 Raiz das Equações

Este módulo apresenta os principais métodos numéricos para encontrar raízes de equações não lineares, divididos entre **métodos fechados** (que requerem intervalo inicial) e **métodos abertos** (que utilizam apenas uma ou poucas aproximações iniciais). Também estão incluídos utilitários como o **método de Horner** e **busca intervalar**.

### 📌 Conteúdo

* Métodos Fechados:
  * Bisseção
  * Posição Falsa (Regula Falsi)
* Métodos Abertos:
  * Newton-Raphson
  * Ponto Fixo (Iteração de Função)
  * Secante
* Utilitários:
  * Avaliação eficiente de polinômios (Horner)
  * Busca de intervalo com mudança de sinal

### 🧮 Fórmulas Importantes

* **Horner**:
* **Critério de parada** (erro aproximado percentual):

### 💠 Implementações

* `bisseccao(f, a, b, tol, max_iter)`
* `posicao_falsa(f, a, b, tol, max_iter)`
* `newton(f, df, x0, tol, max_iter)`
* `ponto_fixo(g, x0, tol, max_iter)`
* `secante(f, x0, x1, tol, max_iter)`
* `horner(x, coeficientes)`
* `busca_intervalo(f, a, b, passos)`

### 📅 Observações

* Todos os métodos usam tolerância como critério de parada baseado no erro relativo percentual.
* A função `busca_intervalar` é útil para encontrar intervalos com mudança de sinal, facilitando o uso de métodos fechados.
* `horner` é recomendada para avaliação rápida de polinômios em algoritmos como Newton.
