# 📘 Métodos Numéricos: Métodos Fechados e Abertos

Este repositório contém a implementação e explicações de **métodos numéricos para encontrar raízes de funções**. São abordados os dois principais grupos: **métodos fechados** e **métodos abertos**.

---

## 📌 Objetivo

Resolver equações do tipo:


usando aproximações sucessivas, já que nem toda equação pode ser resolvida de forma analítica (exata).

---

## 🧩 Conceitos Fundamentais

- **Raiz de uma função**: valor de `x` para o qual `f(x) = 0`.
- **Método numérico**: técnica iterativa para encontrar aproximações da raiz.
- Os métodos são divididos em:
  - **Fechados**: exigem um intervalo inicial onde a raiz esteja garantida.
  - **Abertos**: usam apenas uma ou duas aproximações iniciais, sem garantia de conter a raiz.

---

## 🔒 Métodos Fechados

Utilizam um **intervalo [a, b]** e exigem que **f(a)·f(b) < 0**, ou seja, a função muda de sinal no intervalo ⇒ existe uma raiz.

### ✅ Vantagens:
- Garantem convergência se a função for contínua e as condições forem respeitadas.

### ❌ Desvantagens:
- Convergência geralmente mais lenta.

### Métodos:

#### 1. Método da Bisseção
- Divide o intervalo ao meio a cada iteração.
- Simples e confiável.
- Fórmula:  
  ```xₙ = (a + b) / 2```

#### 2. Método da Falsa Posição (Regula Falsi)
- Usa uma reta secante entre os pontos para estimar a raiz.
- Mais rápido que a bisseção em certos casos.
- Fórmula:  
  ```xₙ = (a·f(b) - b·f(a)) / (f(b) - f(a))```

---

## 🔓 Métodos Abertos

Usam **um ou dois valores iniciais**, sem precisar de um intervalo onde a raiz esteja garantida.

### ✅ Vantagens:
- Convergência mais rápida (quando funciona bem).

### ❌ Desvantagens:
- Pode divergir (não encontrar a raiz).
- Requer boas aproximações iniciais.

### Métodos:

#### 1. Método do Ponto Fixo
- Reescreve `f(x) = 0` na forma `x = g(x)`.
- Iteração:  
  ```xₙ₊₁ = g(xₙ)```

#### 2. Método de Newton-Raphson
- Usa a derivada da função.
- Rápido e eficiente se a função for suave.
- Fórmula:  
  ```xₙ₊₁ = xₙ - f(xₙ)/f'(xₙ)```

#### 3. Método da Secante
- Parecido com Newton, mas sem usar a derivada.
- Usa duas aproximações anteriores:
  ```xₙ = xₙ₋₁ - f(xₙ₋₁)·(xₙ₋₁ - xₙ₋₂)/(f(xₙ₋₁) - f(xₙ₋₂))```

---

## 📈 Comparação entre métodos

| Método              | Usa intervalo? | Requer derivada? | Convergência   | Confiabilidade |
|---------------------|----------------|------------------|----------------|----------------|
| Bisseção            | Sim            | Não              | Lenta          | Alta           |
| Falsa Posição       | Sim            | Não              | Média          | Alta           |
| Ponto Fixo          | Não            | Não              | Lenta/Média    | Média          |
| Newton-Raphson      | Não            | Sim              | Rápida         | Baixa/Média    |
| Secante             | Não            | Não              | Rápida         | Média          |
