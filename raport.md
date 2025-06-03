# Badanie interpolacji funkcji
#### Marta Kociszewska 198143

---
## Wstęp

W niniejszym raporcie przedstawiono analizę metod interpolacji funkcji, ze szczególnym uwzględnieniem wielomianu interpolacyjnego Lagrange’a oraz funkcji sklejanych trzeciego stopnia.
Celem analizy jest zbadanie przydatności obu metod w kontekście aproksymacji funkcji na podstawie danych rzeczywistych, a także ocena wpływu różnych parametrów na wyniki interpolacji.

Interpolacja jest procesem szacowania wartości funkcji w punktach, które nie są bezpośrednio znane, na podstawie wartości funkcji w innych punktach (węzłach interpolacyjnych).
W kontekście analizy danych rzeczywistych interpolacja jest szczególnie przydatna do wygładzania danych, uzupełniania brakujących wartości oraz analizy trendów.

### Interpolacja
Zadaniem interpolacji jest wyznaczenie przybliżonych wartości funkcji w punktach niebędących węzłami interpolacyjnymi 
oraz oszacowanie błędu tych przybliżonych wartości funkcji. W tym celu należy znaleźć funkcję interpolującą $F(x)$, 
która w węzłach interpolacyjnych przyjmuje takie same wartości co funkcja f(x).

### Interpolacja wielomianowa
Interpolacja wielomianowa polega na znalezieniu wielomianu $W_n(x)$, który przechodzi przez zadane punkty (węzły interpolacyjne).

## Wielomian interpolacyjny Lagrange’a:

Wielomian interpolacyjny Lagrange’a jest jedną z metod interpolacji, która pozwala na znalezienie wielomianu przechodzącego przez zadane punkty (węzły interpolacyjne). 
Jest to metoda szczególnie przydatna, gdy mamy do czynienia z małą liczbą punktów i chcemy uzyskać dokładne odwzorowanie funkcji w tych punktach.


Interpolacja z wykorzystaniem wzoru Lagrange’a zakłada dowolne rozmieszczenie węzłów interpolacyjnych. 
Wartość wielomianu interpolacyjnego można uzyskać bez czasochłonnego rozwiązywania układu równań dla współczynników.
W tym celu stosuje się wzór interpolacyjny Lagrange’a: 
$$
W_n(x) = \sum_{i=0}^{n} y_i \frac{\omega_n(x)}{(x-x_j)*\omega'_n(x)}
$$
gdzie:
 - $\omega_n(x) = (x-x_0)(x-x_1)...(x-x_n)$
 - $\omega'_n(x)$ to wartość pochodnej w punkcie $x_j$.

Wzór ten pozwala na obliczenie wartości wielomianu interpolacyjnego w dowolnym punkcie $x$ na podstawie wartości funkcji w węzłach interpolacyjnych $y_i$.

Wartość **błędu bezwzględnego** interpolacji funkcji $f(x)$ w punktach z przedziału $[a,b]$ nie będących węzłami interpolacyjnymi można oszacować za pomocą wzoru:
$$
R_n(x) = |f(x) - W_n(x)| \leq \frac{M_{n+1}}{(n+1)!} |\omega_n(x)|
$$

gdzie:
 - $M_{n+1}$ to największa wartość $|f^{(n+1)}(x)|$ w przedziale $[a,b]$,
 - $\omega_n(x)$ to iloczyn $(x-x_0)(x-x_1)...(x-x_n)$.

## Funkcje sklejane trzeciego stopnia
Funkcje sklejane trzeciego stopnia to metoda interpolacji, która polega na łączeniu kilku funkcji wielomianowych trzeciego stopnia w taki sposób, aby zapewnić ciągłość i gładkość w punktach węzłów interpolacyjnych.
Funkcje sklejane trzeciego stopnia są szczególnie przydatne w przypadku, gdy mamy do czynienia z dużą liczbą punktów i chcemy uzyskać gładkie odwzorowanie funkcji w tych punktach.

Funkcja sklejona trzeciego stopnia jest zdefiniowana jako:
$$
S(x) = \begin{cases}
S_0(x) & \text{dla } x \in [x_0, x_1] \\
S_1(x) & \text{dla } x \in [x_1, x_2] \\
S_2(x) & \text{dla } x \in [x_2, x_3] \\
\vdots & \vdots \\
S_{n-1}(x) & \text{dla } x \in [x_{n-1}, x_n]
\end{cases}
$$
gdzie $S_i(x)$ to funkcja wielomianowa trzeciego stopnia zdefiniowana na przedziale $[x_i, x_{i+1}]$.

W i-tym podprzedziale funkcja sklejona trzeciego stopnia jest zdefiniowana jako:
$$
S_i(x) = a_i + b_i (x - x_i) + c_i (x - x_i)^2 + d_i (x - x_i)^3
$$
gdzie:
- $a_i$, $b_i$, $c_i$, $d_i$ to współczynniki wielomianu trzeciego stopnia,
- $x_i$ to punkt węzła interpolacyjnego.

## Wybór węzłów interpolacyjnych
Wybór węzłów interpolacyjnych jest kluczowym elementem procesu interpolacji. Węzły powinny być rozmieszczone w taki sposób, aby zapewnić jak najlepsze odwzorowanie funkcji w danym przedziale.
Przeanalizowano różne metody wyboru węzłów interpolacyjnych, takie jak:
- **Równomierne rozmieszczenie**: Węzły są rozmieszczone równomiernie w przedziale, co jest najprostszą metodą, 
ale może prowadzić do problemów z błędem interpolacji, zwłaszcza w przypadku funkcji o dużych wartościach pochodnych.

- **Rozmieszczenie Chebysheva**: Węzły są rozmieszczone w taki sposób, aby zminimalizować błąd interpolacji. Jest to 
szczególnie przydatne w przypadku funkcji o dużych wartościach pochodnych.

- **Losowe rozmieszczenie**: Węzły są rozmieszczone losowo w przedziale. Ta metoda jest mniej przewidywalna, 
ale może być użyteczna w przypadku funkcji o nieregularnych kształtach.
