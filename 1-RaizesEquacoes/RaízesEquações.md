
Claro! Aqui está a versão atualizada da seção, agora com as fórmulas importantes incluídas:

---

## 🔄 Raiz das Equações

Este módulo apresenta os principais métodos numéricos para encontrar raízes de equações não lineares, divididos entre **métodos fechados** (que requerem intervalo inicial) e **métodos abertos** (que utilizam apenas uma ou poucas aproximações iniciais). Também estão incluídos utilitários como o **método de Horner** e  **busca intervalar** .

---

### 📌 Conteúdo

* **Métodos Fechados** :
* Bisseção
* Posição Falsa (Regula Falsi)
* **Métodos Abertos** :
* Newton-Raphson
* Ponto Fixo (Iteração de Função)
* Secante
* **Utilitários** :
* Avaliação eficiente de polinômios (Horner)
* Busca de intervalo com mudança de sinal

---

### 🧮 Fórmulas Importantes

**🔹 Método de Bisseção**

Atualização do ponto médio do intervalo:

$xmédia=a+b2x_{\text{médio}} = \frac{a + b}{2}$
**🔹 Método da Posição Falsa (Regula Falsi)**

Ponto de interseção da reta secante com o eixo xx:

$xr=\frac{a*f(b)-b*f(a)}{f(a) - f(b)}$
**🔹 Método de Newton-Raphson**

Atualização da raiz:

$xn+1=$ $x_n - \frac{f(x_n)}{f'(x_n)}$
**🔹 Método do Ponto Fixo**

Iteração simples de uma função reescrita x=g(x)x = g(x):

$xn+1=g(xn)x_{n+1} $
**🔹 Método da Secante**

Aproximação da derivada com dois pontos:

$xn+1= \frac{x0*f(x1) - x1*f(x0)}{f(x1) - f(x0)}$
**🔹 Método de Horner (Avaliação de Polinômios)**

Para um polinômio $P(x)=anxn+an−1xn−1+⋯+a1x+a0P(x) = a_nx^n + a_{n-1}x^{n-1} + \dots + a_1x + a_0:$

$P(x)=(...((anx+an−1)x+an−2)x+⋯+a1)x+a0P(x) = (...((a_nx + a_{n-1})x + a_{n-2})x + \dots + a_1)x + a_0$

### 💠 Implementações

* `bisseccao(f, a, b, tol, max_iter)`
* `posicao_falsa(f, a, b, tol, max_iter)`
* `newton(f, df, x0, tol, max_iter)`
* `ponto_fixo(g, x0, tol, max_iter)`
* `secante(f, x0, x1, tol, max_iter)`
* `horner(x, coeficientes)`
* `busca_intervalo(f, a, b, passos)`

---

### 📅 Observações

* Todos os métodos usam tolerância como critério de parada baseado no erro relativo percentual.
* A função `busca_intervalar` é útil para encontrar intervalos com mudança de sinal, facilitando o uso de métodos fechados.
* `horner` é recomendada para avaliação rápida de polinômios em algoritmos como Newton-Raphson.

Se quiser, posso incluir exemplos de uso ou gráficos para ilustrar algum dos métodos!
