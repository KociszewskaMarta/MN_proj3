# Badanie interpolacji funkcji
### Marta Kociszewska 198143

---
# Wstęp

W niniejszym raporcie przedstawiono analizę metod interpolacji funkcji, ze szczególnym uwzględnieniem wielomianu interpolacyjnego Lagrange’a oraz funkcji sklejanych trzeciego stopnia.
Celem analizy jest zbadanie przydatności obu metod w kontekście aproksymacji funkcji na podstawie danych rzeczywistych, a także ocena wpływu różnych parametrów na wyniki interpolacji.

Interpolacja jest procesem szacowania wartości funkcji w punktach, które nie są bezpośrednio znane, na podstawie wartości funkcji w innych punktach (węzłach interpolacyjnych).
W kontekście analizy danych rzeczywistych interpolacja jest szczególnie przydatna do wygładzania danych, uzupełniania brakujących wartości oraz analizy trendów.

## Interpolacja
Zadaniem interpolacji jest wyznaczenie przybliżonych wartości funkcji w punktach niebędących węzłami interpolacyjnymi 
oraz oszacowanie błędu tych przybliżonych wartości funkcji. W tym celu należy znaleźć funkcję interpolującą $F(x)$, 
która w węzłach interpolacyjnych przyjmuje takie same wartości co funkcja f(x).

## Interpolacja wielomianowa
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

# Analiza

## Dane wejściowe

Analiza interpolacji funkcji została przeprowadzona na podstawie danych, dla różnych rodzajów tras, takich jak:
- **Trasa 1 - spacerniak w Gdańsku**: Trasa prawie płaska, z niewielkimi wzniesieniami i spadkami.

![Trasa 1](plots/plot_elevation/SpacerniakGdansk.csv.png)

- **Trasa 2 - Mount Everest**: Trasa o jednym wyraźnym wzniesieniu.
![Trasa 2](plots/plot_elevation/MountEverest.csv.png)

- **Trasa 3 - Genoa Rapallo**: Trasa różnorodna, z wieloma wzniesieniami i spadkami.
![Trasa 3](plots/plot_elevation/genoa_rapallo.txt.png)

## Interpolacja wielomianowa Lagrange’a

Dla każdego zbioru danych przeprowadzono interpolację wielomianową Lagrange’a, analizując wpływ liczby węzłów interpolacyjnych na dokładność interpolacji oraz ich rozmieszczenie.

Wyniki interpolacji przedstawiono na wykresach, gdzie porównano wartości funkcji interpolowanej z rzeczywistymi wartościami funkcji w punktach węzłów interpolacyjnych.

### Analiza wpływu dystrybucji węzłów interpolacyjnych
Analiza została przeprowadzona dla dwóch rodzajów rozmieszczenia węzłów interpolacyjnych: **równomiernego**, **Chebysheva** oraz **losowego**.
Celem było zbadanie, jak rozmieszczenie węzłów wpływa na dokładność interpolacji.

Wyniki interpolacji dla różnych rozmieszczeń węzłów interpolacyjnych przedstawiono na wykresach, gdzie porównano wartości funkcji interpolowanej z rzeczywistymi wartościami funkcji w punktach węzłów interpolacyjnych.

![Wykresy interpolacji Lagrange’a - spacerniak Gdańsk, rozmieszczenie równomierne](plots/plot_lagrange/SpacerniakGdansk.csv_nodes=15_uniform.png)
![Wykresy interpolacji Lagrange’a - spacerniak Gdańsk, rozmieszczenie Chebysheva](plots/plot_lagrange/SpacerniakGdansk.csv_nodes=15_chebyshev.png)

![Wykresy interpolacji Lagrange’a - Mount Everest, rozmieszczenie równomierne](plots/plot_lagrange/MountEverest.csv_nodes=15_uniform.png)
![Wykresy interpolacji Lagrange’a - Mount Everest, rozmieszczenie Chebysheva](plots/plot_lagrange/MountEverest.csv_nodes=15_chebyshev.png)

![Wykresy interpolacji Lagrange’a - Genoa Rapallo, rozmieszczenie równomierne](plots/plot_lagrange/genoa_rapallo.txt_nodes=15_uniform.png)
![Wykresy interpolacji Lagrange’a - Genoa Rapallo, rozmieszczenie Chebysheva](plots/plot_lagrange/genoa_rapallo.txt_nodes=15_chebyshev.png)

#### Wnioski z analizy rozmieszczenia węzłów interpolacyjnych

Analiza wykazała, że rozmieszczenie węzłów interpolacyjnych ma istotny wpływ na dokładność interpolacji.
W przypadku rozmieszczenia równomiernego, interpolacja może prowadzić do dużych błędów, zwłaszcza w obszarach o dużych wartościach pochodnych funkcji.
Z kolei rozmieszczenie Chebysheva pozwala na uzyskanie znacznie lepszych wyników, minimalizując błąd interpolacji.

Występuje _efekt Rungego_, który polega na tym, że w przypadku rozmieszczenia równomiernego, błąd interpolacji rośnie wraz ze wzrostem liczby węzłów interpolacyjnych. 
Na krańcach przedziału występują duże oscylacje, co prowadzi do znacznych błędów. 
Rozmieszczenie Chebysheva pozwala na zminimalizowanie tego efektu, co jest szczególnie widoczne w przypadku funkcji o dużych wartościach pochodnych.

Poniższy wykres ilustruje _efekt Rungego_, gdzie widać duże oscylacje na krańcach przedziału przy równomiernym rozmieszczeniu węzłów interpolacyjnych.
![Wykresy interpolacji Lagrange’a - spacerniak Gdańsk, rozmieszczenie równomierne](plots/plot_lagrange/SpacerniakGdansk.csv_nodes=30_uniform.png)

Dla porównania, poniżej przedstawiono wykresy interpolacji z rozmieszczeniem Chebysheva, które nie wykazuje tego efektu:
![Wykresy interpolacji Lagrange’a - spacerniak Gdańsk, rozmieszczenie Chebysheva](plots/plot_lagrange/SpacerniakGdansk.csv_nodes=30_chebyshev.png)


### Analiza wpływu liczby węzłów interpolacyjnych

Analiza została przeprowadzona dla różnych liczby węzłów interpolacyjnych - **10, 15, 20, 30, 40**, w celu oceny wpływu liczby węzłów na dokładność interpolacji.
Aby uzyskać lepsze wyniki, węzły interpolacyjne zostały rozmieszczone zgodnie z rozkładem Chebysheva. Dzięki temu możliwe było zminimalizowanie błędu interpolacji, 
zwłaszcza w obszarach o dużych wartościach pochodnych funkcji oraz uniknięcie _efektu Rungego_.

Wyniki interpolacji dla różnych liczby węzłów interpolacyjnych przedstawiono na wykresach, gdzie porównano wartości funkcji 
interpolowanej z rzeczywistymi wartościami funkcji w punktach węzłów interpolacyjnych.

![Wykresy interpolacji Lagrange’a dla 10 węzłów - trasa 1](plots/plot_lagrange/SpacerniakGdansk.csv_nodes=10_chebyshev.png)
![Wykresy interpolacji Lagrange’a dla 15 węzłów - trasa 1](plots/plot_lagrange/SpacerniakGdansk.csv_nodes=15_chebyshev.png)
![Wykresy interpolacji Lagrange’a dla 20 węzłów - trasa 1](plots/plot_lagrange/SpacerniakGdansk.csv_nodes=20_chebyshev.png)
![Wykresy interpolacji Lagrange’a dla 30 węzłów - trasa 1](plots/plot_lagrange/SpacerniakGdansk.csv_nodes=30_chebyshev.png)
![Wykresy interpolacji Lagrange’a dla 40 węzłów - trasa 1](plots/plot_lagrange/SpacerniakGdansk.csv_nodes=40_chebyshev.png)

![Wykresy interpolacji Lagrange’a dla 10 węzłów - trasa 2](plots/plot_lagrange/MountEverest.csv_nodes=10_chebyshev.png)
![Wykresy interpolacji Lagrange’a dla 15 węzłów - trasa 2](plots/plot_lagrange/MountEverest.csv_nodes=15_chebyshev.png)
![Wykresy interpolacji Lagrange’a dla 20 węzłów - trasa 2](plots/plot_lagrange/MountEverest.csv_nodes=20_chebyshev.png)
![Wykresy interpolacji Lagrange’a dla 30 węzłów - trasa 2](plots/plot_lagrange/MountEverest.csv_nodes=30_chebyshev.png)
![Wykresy interpolacji Lagrange’a dla 40 węzłów - trasa 2](plots/plot_lagrange/MountEverest.csv_nodes=40_chebyshev.png)

![Wykresy interpolacji Lagrange’a dla 10 węzłów - trasa 3](plots/plot_lagrange/genoa_rapallo.txt_nodes=10_chebyshev.png)
![Wykresy interpolacji Lagrange’a dla 15 węzłów - trasa 3](plots/plot_lagrange/genoa_rapallo.txt_nodes=15_chebyshev.png)
![Wykresy interpolacji Lagrange’a dla 20 węzłów - trasa 3](plots/plot_lagrange/genoa_rapallo.txt_nodes=20_chebyshev.png)
![Wykresy interpolacji Lagrange’a dla 30 węzłów - trasa 3](plots/plot_lagrange/genoa_rapallo.txt_nodes=30_chebyshev.png)
![Wykresy interpolacji Lagrange’a dla 40 węzłów - trasa 3](plots/plot_lagrange/genoa_rapallo.txt_nodes=40_chebyshev.png)

TODO: dopisz wnioski z analizy liczby węzłów interpolacyjnych



