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

## Wybór węzłów interpolacyjnych
Wybór węzłów interpolacyjnych jest kluczowym elementem procesu interpolacji. Węzły powinny być rozmieszczone w taki sposób, aby zapewnić jak najlepsze odwzorowanie funkcji w danym przedziale.
Przeanalizowano różne metody wyboru węzłów interpolacyjnych, takie jak:

- **Równomierne rozmieszczenie**: Węzły są rozmieszczone równomiernie w przedziale, co jest najprostszą metodą, 
ale może prowadzić do problemów z błędem interpolacji, zwłaszcza w przypadku funkcji o dużych wartościach pochodnych.

- **Rozmieszczenie Chebysheva**: Węzły są rozmieszczone w taki sposób, aby zminimalizować błąd interpolacji. Jest to 
szczególnie przydatne w przypadku funkcji o dużych wartościach pochodnych.
    Zaimplementowano węzły Chebysheva pierwszego rodzaju, które są rozmieszczone w przedziale $[-1, 1]$ i mają postać:
    $$
    x_k = \cos\left(\frac{(2k + 1) \pi}{2n}\right), \quad k = 0, 1, \ldots, n-1
    $$

## Zapewnienie stabilności numerycznej

W celu zapewnienia stabilności numerycznej podczas interpolacji, szczególnie w przypadku wielomianu Lagrange’a,
przekształcono dziedzinę funkcji interpolowanej do przedziału:
$$[-1, 1]$$

# Analiza

## Dane wejściowe

Analiza interpolacji funkcji została przeprowadzona na podstawie danych, dla różnych rodzajów tras, takich jak:

**Trasa 1 - spacerniak w Gdańsku**: 

![Trasa 1](plots/plot_elevation/SpacerniakGdansk.csv.png)
Trasa prawie płaska, z niewielkimi wzniesieniami i spadkami.

**Trasa 2 - Mount Everest**: 

![Trasa 2](plots/plot_elevation/MountEverest.csv.png)
Trasa o jednym wyraźnym wzniesieniu.

\newpage

**Trasa 3 - Genoa Rapallo**: 

![Trasa 3](plots/plot_elevation/genoa_rapallo.txt.png)
Trasa różnorodna, z wieloma wzniesieniami i spadkami.

## Interpolacja wielomianowa Lagrange’a

Dla każdego zbioru danych przeprowadzono interpolację wielomianową Lagrange’a, analizując wpływ liczby węzłów interpolacyjnych oraz ich rozmieszczenie na dokładność interpolacji.

Wyniki interpolacji przedstawiono na wykresach, gdzie porównano wartości funkcji interpolowanej z rzeczywistymi wartościami funkcji w punktach węzłów interpolacyjnych.

### Analiza wpływu dystrybucji węzłów interpolacyjnych
Analiza została przeprowadzona dla dwóch rodzajów rozmieszczenia węzłów interpolacyjnych: **równomiernego**, **Chebysheva**.
Celem było zbadanie, jak rozmieszczenie węzłów wpływa na dokładność interpolacji.

Wyniki interpolacji dla różnych rozmieszczeń węzłów interpolacyjnych przedstawiono na wykresach, gdzie porównano wartości funkcji interpolowanej z rzeczywistymi wartościami funkcji w punktach węzłów interpolacyjnych.

\newpage

#### Trasa 1

| Rozmieszczenie równomierne                                                                                                                        | Rozmieszczenie Chebysheva                                                                                                                          |
|---------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| ![Wykresy interpolacji Lagrange’a - spacerniak Gdańsk, rozmieszczenie równomierne](plots/plot_lagrange/SpacerniakGdansk.csv_nodes=15_uniform.png) | ![Wykresy interpolacji Lagrange’a - spacerniak Gdańsk, rozmieszczenie Chebysheva](plots/plot_lagrange/SpacerniakGdansk.csv_nodes=15_chebyshev.png) | |                                                                                                                                                    |

Węzły rozmieszczone równomiernie:

Krzywa interpolacyjna wykazuje bardzo silne oscylacje na krańcach przedziału (początek i koniec), z wartościami znacznie odbiegającymi od rzeczywistych.
Dodatkowo, silne oscylacje pojawiają się również w innych miejscach trasy, zwłaszcza tam, gdzie występują gwałtowne zmiany wysokości.

Węzły Chebysheva:

Krzywa interpolacyjna dość dobrze podąża za ogólnym kształtem trasy. Początkowy stromy spadek jest uchwycony poprawnie.
Mimo że interpolacja nie oddaje wszystkich drobnych detali, zwłaszcza na płaskim odcinku, nie występują ekstremalne oscylacje, a krzywa jest stabilna.

#### Trasa 2

| Rozmieszczenie równomierne                                                                                                                | Rozmieszczenie Chebysheva                                                                                                                  |
|-------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| ![Wykresy interpolacji Lagrange’a - Mount Everest, rozmieszczenie równomierne](plots/plot_lagrange/MountEverest.csv_nodes=15_uniform.png) | ![Wykresy interpolacji Lagrange’a - Mount Everest, rozmieszczenie Chebysheva](plots/plot_lagrange/MountEverest.csv_nodes=15_chebyshev.png) |

Węzły rozmieszczone równomiernie:

Mimo że profil jest gładki, nadal widoczne są znaczące oscylacje na krańcach przedziału (początek i koniec trasy). Krzywa interpolacyjna przyjmuje wartości znacznie odbiegające od prawdziwych danych w tych obszarach.
W środkowej części trasy, gdzie funkcja jest bardziej liniowa, dopasowanie jest dobre, ale problem oscylacji na brzegach jest wyraźny.

Węzły Chebysheva:

Krzywa interpolacyjna bardzo dokładnie odwzorowuje profil wysokości. Jest gładka i niemal idealnie pokrywa się z prawdziwymi danymi na całej długości trasy.

#### Trasa 3

| Rozmieszczenie równomierne                                                                                                                 | Rozmieszczenie Chebysheva                                                                                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| ![Wykresy interpolacji Lagrange’a - Genoa Rapallo, rozmieszczenie równomierne](plots/plot_lagrange/genoa_rapallo.txt_nodes=15_uniform.png) | ![Wykresy interpolacji Lagrange’a - Genoa Rapallo, rozmieszczenie Chebysheva](plots/plot_lagrange/genoa_rapallo.txt_nodes=15_chebyshev.png) |

Węzły rozmieszczone równomiernie:

Krzywa interpolacyjna wykazuje ekstremalne oscylacje (zjawisko Rungego), zwłaszcza na krańcach przedziału (początek i koniec trasy) 
oraz w obszarach o dużej zmienności (np. około 30000 jednostek odległości). Wartości interpolacji znacznie wykraczają poza 
zakres wartości prawdziwych danych (np. spadki do -400 i wzrosty powyżej 1000).
Mimo że w niektórych miejscach interpolacja jest bliska prawdziwym danym, ogólna jakość jest bardzo niska z powodu silnych oscylacji.


Węzły Chebysheva:

Krzywa interpolacyjna (czerwona przerywana linia) jest stosunkowo gładka i podąża za ogólnym trendem prawdziwych danych.
Odchylenia od prawdziwych danych są zauważalne, zwłaszcza w obszarach gwałtownych zmian wysokości, ale interpolacja pozostaje 
w rozsądnych granicach wartości prawdziwych danych. Nie widać ekstremalnych oscylacji.

\newpage

### Wnioski z analizy rozmieszczenia węzłów interpolacyjnych

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

\newpage

### Analiza wpływu liczby węzłów interpolacyjnych

Analiza została przeprowadzona dla różnych liczby węzłów interpolacyjnych - **10, 20, 30, 40**, w celu oceny wpływu liczby węzłów na dokładność interpolacji.
Aby uzyskać lepsze wyniki, węzły interpolacyjne zostały rozmieszczone zgodnie z rozkładem Chebysheva. Dzięki temu możliwe było zminimalizowanie błędu interpolacji, 
zwłaszcza w obszarach o dużych wartościach pochodnych funkcji oraz uniknięcie _efektu Rungego_.

Wyniki interpolacji dla różnych liczby węzłów interpolacyjnych przedstawiono na wykresach, gdzie porównano wartości funkcji 
interpolowanej z rzeczywistymi wartościami funkcji w punktach węzłów interpolacyjnych.

#### Trasa 1 - spacerniak w Gdańsku

| Liczba węzłów  | Wykresy interpolacji Lagrange’a |
|:--------------:|----------------------------------|
|       10       | ![Wykresy interpolacji Lagrange’a dla 10 węzłów - trasa 1](plots/plot_lagrange/SpacerniakGdansk.csv_nodes=10_chebyshev.png) |
|       15       | ![Wykresy interpolacji Lagrange’a dla 15 węzłów - trasa 1](plots/plot_lagrange/SpacerniakGdansk.csv_nodes=15_chebyshev.png) |
|       20       | ![Wykresy interpolacji Lagrange’a dla 20 węzłów - trasa 1](plots/plot_lagrange/SpacerniakGdansk.csv_nodes=20_chebyshev.png) |
|       30       | ![Wykresy interpolacji Lagrange’a dla 30 węzłów - trasa 1](plots/plot_lagrange/SpacerniakGdansk.csv_nodes=30_chebyshev.png) |
|       40       | ![Wykresy interpolacji Lagrange’a dla 40 węzłów - trasa 1](plots/plot_lagrange/SpacerniakGdansk.csv_nodes=40_chebyshev.png) |


**Wpływ liczby węzłów interpolacyjnych:**

- 10 węzłów: Interpolacja jest bardzo ogólna. Początkowy, stromy wzrost wysokości jest tylko częściowo uchwycony, a interpolacja wygładza ostry spadek. Dalsza, bardziej płaska część trasy jest również mocno wygładzona, pomijając wiele drobnych wzniesień i zagłębień. Widać wyraźne odstępstwa od prawdziwych danych, zwłaszcza w początkowym, bardziej dynamicznym fragmencie.

- 15 węzłów: Następuje zauważalna poprawa, zwłaszcza na początku trasy, gdzie interpolacja lepiej oddaje stromy początkowy odcinek. W dalszej części, interpolacja zaczyna lepiej śledzić większe wzniesienia, ale nadal pomija wiele drobnych fluktuacji.

- 20 węzłów: Dopasowanie jest wyraźnie lepsze. Krzywa interpolacyjna dość dobrze odwzorowuje początkowy ostry zjazd i początek spłaszczenia. W dalszej części, krzywa interpolacyjna jest bliżej prawdziwych danych, oddając więcej szczegółów, ale nadal nie wszystkie.

- 30 węzłów: Interpolacja jest znacznie dokładniejsza. Krzywa interpolacyjna bardzo dobrze odzwierciedla zarówno początkową, dynamiczną część, jak i dalsze, mniejsze fluktuacje na płaskim terenie. Odstępstwa od prawdziwych danych są niewielkie.

- 40 węzłów: Przy 40 węzłach dopasowanie jest bardzo dobre, prawie idealne na większości odcinków. Krzywa interpolacyjna niemal idealnie pokrywa się z "prawdziwymi danymi", oddając nawet drobne detale profilu wysokości.

Dla trasy "SpacerniakGdansk.csv", która ma mieszaną charakterystykę (bardzo dynamiczny początek i stosunkowo bardziej płaska, ale z drobnymi nieregularnościami, dalsza część), potrzeba jest stosunkowo dużej liczby węzłów (około 30-40) aby uzyskać wysoką dokładność na całej długości. Mniejsza liczba węzłów (10-20) dobrze oddaje ogólny trend, ale pomija wiele lokalnych szczegółów, zwłaszcza tam, gdzie profil jest najbardziej dynamiczny.

##### Trasa 2 - Mount Everest

| Liczba węzłów  | Wykresy interpolacji Lagrange’a |
|:--------------:|----------------------------------|
|       10       | ![Wykresy interpolacji Lagrange’a dla 10 węzłów - trasa 2](plots/plot_lagrange/MountEverest.csv_nodes=10_chebyshev.png) |
|       15       | ![Wykresy interpolacji Lagrange’a dla 15 węzłów - trasa 2](plots/plot_lagrange/MountEverest.csv_nodes=15_chebyshev.png) |
|       20       | ![Wykresy interpolacji Lagrange’a dla 20 węzłów - trasa 2](plots/plot_lagrange/MountEverest.csv_nodes=20_chebyshev.png) |
|       30       | ![Wykresy interpolacji Lagrange’a dla 30 węzłów - trasa 2](plots/plot_lagrange/MountEverest.csv_nodes=30_chebyshev.png) |
|       40       | ![Wykresy interpolacji Lagrange’a dla 40 węzłów - trasa 2](plots/plot_lagrange/MountEverest.csv_nodes=40_chebyshev.png) |


**Wpływ liczby węzłów interpolacyjnych:**

- 10 węzłów: Interpolacja jest już na tym etapie bardzo dobra. Krzywa interpolacyjna z dużą precyzją oddaje ogólny kształt góry. Odchylenia od prawdziwych danych są minimalne, głównie w obszarach o większej krzywiźnie.

- 15 węzłów: Dopasowanie jest niemal idealne. Krzywa interpolacyjna bardzo dokładnie śledzi profil wysokości, a różnice między danymi prawdziwymi a interpolacją są praktycznie niezauważalne wizualnie.

- 20 węzłów: Brak widocznej dalszej znaczącej poprawy w stosunku do 15 węzłów. Interpolacja jest w zasadzie doskonała.

- 30 węzłów: Brak widocznej dalszej znaczącej poprawy.

- 40 węzłów: Brak widocznej dalszej znaczącej poprawy.

Dla trasy o gładkim i regularnym profilu, takiej jak "MountEverest.csv", już niewielka liczba węzłów interpolacyjnych (np. 10-15) jest wystarczająca do uzyskania bardzo wysokiej dokładności. Zwiększanie liczby węzłów powyżej pewnego poziomu (około 15-20) nie przynosi już znaczącej poprawy w dopasowaniu, ponieważ krzywizna funkcji jest niska.

##### Trasa 3 - Genoa Rapallo

| Liczba węzłów  | Wykresy interpolacji Lagrange’a |
|:--------------:|----------------------------------|
|       10       | ![Wykresy interpolacji Lagrange’a dla 10 węzłów - trasa 3](plots/plot_lagrange/genoa_rapallo.txt_nodes=10_chebyshev.png) |
|       15       | ![Wykresy interpolacji Lagrange’a dla 15 węzłów - trasa 3](plots/plot_lagrange/genoa_rapallo.txt_nodes=15_chebyshev.png) |
|       20       | ![Wykresy interpolacji Lagrange’a dla 20 węzłów - trasa 3](plots/plot_lagrange/genoa_rapallo.txt_nodes=20_chebyshev.png) |
|       30       | ![Wykresy interpolacji Lagrange’a dla 30 węzłów - trasa 3](plots/plot_lagrange/genoa_rapallo.txt_nodes=30_chebyshev.png) |
|       40       | ![Wykresy interpolacji Lagrange’a dla 40 węzłów - trasa 3](plots/plot_lagrange/genoa_rapallo.txt_nodes=40_chebyshev.png) |


**Wpływ liczby węzłów interpolacyjnych:**

- 10 węzłów: Interpolacja jest bardzo ogólna. Wiele szczegółów "prawdziwych danych" jest pominiętych. Krzywa interpolacyjna wygładza drastycznie profil, nie oddając ostrych zmian wysokości. Występuje znaczne odchylenie od prawdziwych danych, szczególnie w obszarach o dużym zróżnicowaniu.

- 15 węzłów: Następuje poprawa dopasowania, ale nadal jest to dość ogólna aproksymacja. Widać, że interpolacja próbuje uchwycić niektóre większe wzniesienia i spadki, ale nadal brakuje wielu detali.

- 20 węzłów: Dopasowanie jest wyraźnie lepsze. Krzywa interpolacyjna zaczyna śledzić więcej wzniesień i spadków prawdziwych danych, choć wciąż są miejsca, gdzie różnice są znaczne, szczególnie w przypadku ostrych szczytów.

- 30 węzłów: Interpolacja jest znacznie dokładniejsza. Krzywa interpolacyjna bardzo dobrze odzwierciedla ogólny kształt trasy, a nawet niektóre z mniejszych fluktuacji. Odstępstwa od prawdziwych danych są mniejsze i bardziej lokalne.

- 40 węzłów: Przy 40 węzłach dopasowanie jest bardzo dobre. Krzywa interpolacyjna praktycznie pokrywa się z "prawdziwymi danymi" na większości odcinków, oddając nawet drobne szczegóły profilu wysokości. Widać, że zwiększenie liczby węzłów do tego poziomu znacząco poprawiło dokładność.

Dla trasy o tak dużej nieregularności, jak "genoa_rapallo.txt", do uzyskania satysfakcjonującej dokładności interpolacji Lagrange'a z węzłami Czebyszewa wymagana jest stosunkowo duża liczba węzłów (np. 30-40). Mniejsza liczba węzłów prowadzi do znacznego wygładzenia i utraty kluczowych informacji o profilu wysokości.

### Wnioski z analizy ilości węzłów interpolacyjnych

**Wpływ liczby węzłów:**

- Zwiększanie liczby węzłów interpolacyjnych zazwyczaj prowadzi do zwiększenia dokładności aproksymacji danych. Im więcej punktów jest użytych do konstrukcji wielomianu interpolacyjnego, tym lepiej jest on w stanie uchwycić szczegóły i fluktuacje oryginalnej funkcji.

- Istnieje punkt nasycenia. Powyżej pewnej liczby węzłów, dalsze ich dodawanie może nie przynosić już widocznej poprawy dokładności, szczególnie jeśli funkcja jest gładka. W niektórych przypadkach (niezaobserwowanych tutaj, ale teoretycznie możliwych przy bardzo dużej liczbie węzłów i niewłaściwym ich rozmieszczeniu, np. równoodległych), może nawet prowadzić do zjawiska Rungego, czyli oscylacji na brzegach przedziału. Użycie węzłów Czebyszewa minimalizuje to ryzyko.

**Wpływ rodzaju trasy (charakterystyki danych):**

- Trasy o wysokiej nieregularności i dużej liczbie ostrych zmian (np. "genoa_rapallo.txt") wymagają znacznie większej liczby węzłów interpolacyjnych, aby uzyskać akceptowalną dokładność. W przypadku takich danych, nawet duża liczba węzłów może nie oddać idealnie wszystkich detali, ale znacznie poprawia ogólne dopasowanie. Wygładzanie jest znaczące przy małej liczbie węzłów.

- Trasy o gładkim i regularnym profilu (np. "MountEverest.csv") mogą być bardzo dobrze aproksymowane za pomocą stosunkowo niewielkiej liczby węzłów. Charakterystyka danych, a konkretnie ich "gładkość" i stopień złożoności, ma fundamentalne znaczenie dla efektywności interpolacji. Im bardziej "gładka" funkcja, tym mniej węzłów potrzeba do jej dokładnego odwzorowania.

Podsumowując, optymalna liczba węzłów interpolacyjnych jest silnie zależna od charakterystyki danych, które mają być interpolowane. Dla bardzo nieregularnych danych, konieczne jest użycie większej liczby węzłów, podczas gdy dla gładkich danych mniejsza liczba węzłów jest często wystarczająca. Węzły Czebyszewa są dobrym wyborem, ponieważ minimalizują oscylacje, co jest szczególnie ważne przy interpolacji danych o dużej zmienności.