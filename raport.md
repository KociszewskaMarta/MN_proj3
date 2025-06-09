# Badanie interpolacji funkcji
### Marta Kociszewska 198143

---
# 1. Wstęp

W niniejszym raporcie przedstawiono analizę metod interpolacji funkcji, ze szczególnym uwzględnieniem wielomianu interpolacyjnego Lagrange’a oraz funkcji sklejanych trzeciego stopnia.
Celem analizy jest zbadanie przydatności obu metod w kontekście aproksymacji funkcji na podstawie danych rzeczywistych, a także ocena wpływu różnych parametrów na wyniki interpolacji.

Interpolacja jest procesem szacowania wartości funkcji w punktach, które nie są bezpośrednio znane, na podstawie wartości funkcji w innych punktach (węzłach interpolacyjnych).
W kontekście analizy danych rzeczywistych interpolacja jest szczególnie przydatna do wygładzania danych, uzupełniania brakujących wartości oraz analizy trendów.

## 1.1 Interpolacja
Zadaniem interpolacji jest wyznaczenie przybliżonych wartości funkcji w punktach niebędących węzłami interpolacyjnymi 
oraz oszacowanie błędu tych przybliżonych wartości funkcji. W tym celu należy znaleźć funkcję interpolującą $F(x)$, 
która w węzłach interpolacyjnych przyjmuje takie same wartości co funkcja f(x).

## 1.2 Interpolacja wielomianowa
Interpolacja wielomianowa polega na znalezieniu wielomianu $W_n(x)$, który przechodzi przez zadane punkty (węzły interpolacyjne).

## 1.3 Wielomian interpolacyjny Lagrange’a:

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

## 1.4 Wybór węzłów interpolacyjnych
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

## 1.5 Zapewnienie stabilności numerycznej

W celu zapewnienia stabilności numerycznej podczas interpolacji, szczególnie w przypadku wielomianu Lagrange’a,
przekształcono dziedzinę funkcji interpolowanej do przedziału:
$$[-1, 1]$$

# 2. Analiza

## 2.1 Dane wejściowe

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

# 3. Interpolacja wielomianowa Lagrange’a

Dla każdego zbioru danych przeprowadzono interpolację wielomianową Lagrange’a, analizując wpływ liczby węzłów interpolacyjnych oraz ich rozmieszczenie na dokładność interpolacji.

Wyniki interpolacji przedstawiono na wykresach, gdzie porównano wartości funkcji interpolowanej z rzeczywistymi wartościami funkcji w punktach węzłów interpolacyjnych.

## 3.1 Analiza wpływu dystrybucji węzłów interpolacyjnych
Analiza została przeprowadzona dla dwóch rodzajów rozmieszczenia węzłów interpolacyjnych: **równomiernego**, **Chebysheva**.
Celem było zbadanie, jak rozmieszczenie węzłów wpływa na dokładność interpolacji.

Wyniki interpolacji dla różnych rozmieszczeń węzłów interpolacyjnych przedstawiono na wykresach, gdzie porównano wartości funkcji interpolowanej z rzeczywistymi wartościami funkcji w punktach węzłów interpolacyjnych.

\newpage

### Trasa 1

| Rozmieszczenie równomierne                                                                                                                        | Rozmieszczenie Chebysheva                                                                                                                          |
|---------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| ![Wykresy interpolacji Lagrange’a - spacerniak Gdańsk, rozmieszczenie równomierne](plots/plot_lagrange/SpacerniakGdansk.csv_nodes=15_uniform.png) | ![Wykresy interpolacji Lagrange’a - spacerniak Gdańsk, rozmieszczenie Chebysheva](plots/plot_lagrange/SpacerniakGdansk.csv_nodes=15_chebyshev.png) | |   
| ![Wykresy interpolacji Lagrange’a - spacerniak Gdańsk, rozmieszczenie równomierne](plots/plot_lagrange/SpacerniakGdansk.csv_nodes=30_uniform.png) | ![Wykresy interpolacji Lagrange’a - spacerniak Gdańsk, rozmieszczenie Chebysheva](plots/plot_lagrange/SpacerniakGdansk.csv_nodes=30_chebyshev.png) |

Węzły rozmieszczone równomiernie:

Krzywa interpolacyjna wykazuje bardzo silne oscylacje na krańcach przedziału (początek i koniec), z wartościami znacznie odbiegającymi od rzeczywistych.
Dodatkowo, silne oscylacje pojawiają się również w innych miejscach trasy, zwłaszcza tam, gdzie występują gwałtowne zmiany wysokości.

Węzły Chebysheva:

Krzywa interpolacyjna dość dobrze podąża za ogólnym kształtem trasy. Początkowy stromy spadek jest uchwycony poprawnie.
Mimo że interpolacja nie oddaje wszystkich drobnych detali, zwłaszcza na płaskim odcinku, nie występują ekstremalne oscylacje, a krzywa jest stabilna.

### Trasa 2

| Rozmieszczenie równomierne                                                                                                                | Rozmieszczenie Chebysheva                                                                                                                  |
|-------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| ![Wykresy interpolacji Lagrange’a - Mount Everest, rozmieszczenie równomierne](plots/plot_lagrange/MountEverest.csv_nodes=15_uniform.png) | ![Wykresy interpolacji Lagrange’a - Mount Everest, rozmieszczenie Chebysheva](plots/plot_lagrange/MountEverest.csv_nodes=15_chebyshev.png) |
| ![Wykresy interpolacji Lagrange’a - Mount Everest, rozmieszczenie równomierne](plots/plot_lagrange/MountEverest.csv_nodes=30_uniform.png) | ![Wykresy interpolacji Lagrange’a - Mount Everest, rozmieszczenie Chebysheva](plots/plot_lagrange/MountEverest.csv_nodes=30_chebyshev.png) |

Węzły rozmieszczone równomiernie:

Mimo że profil jest gładki, nadal widoczne są znaczące oscylacje na krańcach przedziału (początek i koniec trasy). Krzywa interpolacyjna przyjmuje wartości znacznie odbiegające od prawdziwych danych w tych obszarach.
W środkowej części trasy, gdzie funkcja jest bardziej liniowa, dopasowanie jest dobre, ale problem oscylacji na brzegach jest wyraźny.

Węzły Chebysheva:

Krzywa interpolacyjna bardzo dokładnie odwzorowuje profil wysokości. Jest gładka i niemal idealnie pokrywa się z prawdziwymi danymi na całej długości trasy.

### Trasa 3

| Rozmieszczenie równomierne                                                                                                                 | Rozmieszczenie Chebysheva                                                                                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| ![Wykresy interpolacji Lagrange’a - Genoa Rapallo, rozmieszczenie równomierne](plots/plot_lagrange/genoa_rapallo.txt_nodes=15_uniform.png) | ![Wykresy interpolacji Lagrange’a - Genoa Rapallo, rozmieszczenie Chebysheva](plots/plot_lagrange/genoa_rapallo.txt_nodes=15_chebyshev.png) |
| ![Wykresy interpolacji Lagrange’a - Genoa Rapallo, rozmieszczenie równomierne](plots/plot_lagrange/genoa_rapallo.txt_nodes=30_uniform.png) | ![Wykresy interpolacji Lagrange’a - Genoa Rapallo, rozmieszczenie Chebysheva](plots/plot_lagrange/genoa_rapallo.txt_nodes=30_chebyshev.png) |

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

## 3.2 Analiza wpływu liczby węzłów interpolacyjnych

Analiza została przeprowadzona dla różnych liczby węzłów interpolacyjnych - **10, 20, 40, 60, 80, 100**, w celu oceny wpływu liczby węzłów na dokładność interpolacji.
Aby uzyskać lepsze wyniki, węzły interpolacyjne zostały rozmieszczone zgodnie z rozkładem Chebysheva. Dzięki temu możliwe było zminimalizowanie błędu interpolacji, 
zwłaszcza w obszarach o dużych wartościach pochodnych funkcji oraz uniknięcie _efektu Rungego_.

Wyniki interpolacji dla różnych liczby węzłów interpolacyjnych przedstawiono na wykresach, gdzie porównano wartości funkcji 
interpolowanej z rzeczywistymi wartościami funkcji w punktach węzłów interpolacyjnych.

### Trasa 1 - spacerniak w Gdańsku

|                                                                               |                                                                                 |
|-------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| ![10 węzłów](plots/plot_lagrange/SpacerniakGdansk.csv_nodes=10_chebyshev.png) | ![20 węzłów](plots/plot_lagrange/SpacerniakGdansk.csv_nodes=20_chebyshev.png)   |
| ![40 węzłów](plots/plot_lagrange/SpacerniakGdansk.csv_nodes=40_chebyshev.png) | ![60 węzłów](plots/plot_lagrange/SpacerniakGdansk.csv_nodes=60_chebyshev.png)   |
| ![80 węzłów](plots/plot_lagrange/SpacerniakGdansk.csv_nodes=80_chebyshev.png) | ![100 węzłów](plots/plot_lagrange/SpacerniakGdansk.csv_nodes=100_chebyshev.png) |

**Wpływ liczby węzłów interpolacyjnych:**

- Mała liczba węzłów (np. 10 węzłów):

Interpolacja jest znacznie wygładzona i słabo odwzorowuje szczegóły oraz lokalne wahania danych rzeczywistych.
Występuje znaczne odchylenie między krzywą interpolowaną a danymi rzeczywistymi, szczególnie w obszarach o większej zmienności (np. początek i okolice 2500 jednostek odległości).
Generalny kształt danych jest uchwycony, ale brakuje precyzji.

- Zwiększenie liczby węzłów (np. 20, 40, 60 węzłów):

Wraz ze wzrostem liczby węzłów, krzywa interpolacji Lagrange'a staje się coraz dokładniejsza i lepiej dopasowuje się do danych rzeczywistych.
Lokalne szczyty i doliny są lepiej odwzorowywane, a ogólne odchylenie od danych rzeczywistych maleje.
Interpolacja jest bardziej elastyczna i potrafi uchwycić więcej szczegółów w przebiegu danych.

- Duża liczba węzłów (np. 80, 100 węzłów):

Dopasowanie w środkowej części zakresu danych staje się bardzo dobre, a krzywa interpolacji niemal pokrywa się z danymi rzeczywistymi.
Jednakże, pojawia się zjawisko Rungego na krańcach przedziału interpolacji. Widać to wyraźnie na wykresach dla 80 i 100 węzłów, gdzie na początku (okolice 0) i na końcu (okolice 8000-8500 jednostek odległości) krzywa interpolacji zaczyna gwałtownie oscylować i znacznie odbiegać od danych rzeczywistych, przyjmując wartości znacznie większe lub mniejsze niż rzeczywiste. Jest to typowy problem interpolacji wielomianowej wysokiego stopnia, szczególnie gdy węzły są równoodległe (choć tutaj użyto węzłów Chebysheva, które zazwyczaj redukują to zjawisko, przy bardzo dużej liczbie węzłów nadal może być widoczne).
W praktyce oznacza to, że zbyt duża liczba węzłów może prowadzić do overfittingu i niestabilności interpolacji na granicach zakresu danych, co sprawia, że interpolacja staje się niewiarygodna w tych obszarach.

Podsumowując:

Istnieje optymalna liczba węzłów dla interpolacji Lagrange'a. Zbyt mała liczba węzłów prowadzi do niedostatecznego dopasowania (underfitting), podczas gdy zbyt duża liczba węzłów może prowadzić do niestabilności i dużych błędów na krańcach przedziału (zjawisko Rungego, overfitting). W przypadku tych danych, wydaje się, że około 40-60 węzłów Chebysheva zapewnia dobrą równowagę między dokładnością dopasowania a unikaniem problemów na granicach.

### Trasa 2 - Mount Everest

|                                                                           |                                                                             |
|---------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| ![10 węzłów](plots/plot_lagrange/MountEverest.csv_nodes=10_chebyshev.png) | ![20 węzłów](plots/plot_lagrange/MountEverest.csv_nodes=20_chebyshev.png)   |
| ![40 węzłów](plots/plot_lagrange/MountEverest.csv_nodes=40_chebyshev.png) | ![60 węzłów](plots/plot_lagrange/MountEverest.csv_nodes=60_chebyshev.png)   |
| ![80 węzłów](plots/plot_lagrange/MountEverest.csv_nodes=80_chebyshev.png) | ![100 węzłów](plots/plot_lagrange/MountEverest.csv_nodes=100_chebyshev.png) |


**Wpływ liczby węzłów interpolacyjnych:**

- Mała liczba węzłów (np. 10 węzłów):

Krzywa interpolacji (czerwona, przerywana linia) dobrze oddaje ogólny trend danych rzeczywistych (niebieska, ciągła linia).
Jednakże, pomimo że węzły są rozmieszczone strategicznie (Chebyshev), interpolacja jest zbyt "gładka" i nie uchwytuje mniejszych, lokalnych fluktuacji i szczegółów danych rzeczywistych. Widać to szczególnie w okolicach szczytu (ok. 2500-3000 jednostek odległości) oraz na bardziej płaskich odcinkach.
Odchylenia od danych rzeczywistych są zauważalne, ale nie ma tu jeszcze drastycznych oscylacji.

- Zwiększenie liczby węzłów (np. 20, 40, 60 węzłów):

Wraz ze wzrostem liczby węzłów, interpolacja staje się coraz dokładniejsza. Krzywa interpolacji zaczyna coraz wierniej odwzorowywać dane rzeczywiste, przylegając do nich coraz bliżej.
Lokalne wahania i drobne nieregularności danych rzeczywistych są coraz lepiej odwzorowywane przez interpolowaną krzywą.
Węzły interpolacyjne (zielone kropki) są gęściej rozmieszczone, co pozwala na lepsze "uchwycenie" kształtu funkcji.
Dla 40 i 60 węzłów, dopasowanie wydaje się być bardzo dobre na większości przebiegu trasy, bez widocznych oznak niestabilności.

- Duża liczba węzłów (np. 80, 100 węzłów):

W przypadku 80 węzłów, widać wyraźne zjawisko Rungego na krańcach przedziału interpolacji. Na początku (okolice 0) i na końcu (okolice 7500-8000 jednostek odległości) interpolowana krzywa zaczyna gwałtownie oscylować, wykazując duże, nierealistyczne wartości, znacznie odbiegające od danych rzeczywistych. Mimo że w środkowej części zakresu dopasowanie jest nadal bardzo dobre, te ekstremalne oscylacje sprawiają, że interpolacja jest niewiarygodna w obszarach brzegowych.
Dla 100 węzłów, zjawisko Rungego jest jeszcze bardziej intensywne na krańcach, z jeszcze większymi amplitudami oscylacji. Pomimo doskonałego dopasowania w środku, problem na brzegach staje się dominujący.

Podsumowując:

Podobnie jak w poprzednim przypadku, wybór odpowiedniej liczby węzłów jest kluczowy.
Zbyt mała liczba węzłów prowadzi do zbytniego wygładzenia i utraty detali.
Optymalna liczba węzłów (prawdopodobnie w zakresie 40-60 dla tych danych) pozwala na wierne odwzorowanie kształtu danych bez nadmiernych oscylacji.
Zbyt duża liczba węzłów, mimo że teoretycznie zwiększa stopień dopasowania, w praktyce prowadzi do problemu stabilności na granicach (zjawisko Rungego), co czyni interpolację nieużyteczną w tych obszarach. Węzły Chebysheva minimalizują to zjawisko w porównaniu do równoodległych węzłów, ale przy wystarczająco dużej liczbie węzłów problem nadal się pojawia.

### Trasa 3 - Genoa Rapallo

|                                                                            |                                                                              |
|----------------------------------------------------------------------------|------------------------------------------------------------------------------|
| ![10 węzłów](plots/plot_lagrange/genoa_rapallo.txt_nodes=10_chebyshev.png) | ![20 węzłów](plots/plot_lagrange/genoa_rapallo.txt_nodes=20_chebyshev.png)   |
| ![40 węzłów](plots/plot_lagrange/genoa_rapallo.txt_nodes=40_chebyshev.png) | ![60 węzłów](plots/plot_lagrange/genoa_rapallo.txt_nodes=60_chebyshev.png)   |
| ![80 węzłów](plots/plot_lagrange/genoa_rapallo.txt_nodes=80_chebyshev.png) | ![100 węzłów](plots/plot_lagrange/genoa_rapallo.txt_nodes=100_chebyshev.png) |


**Wpływ liczby węzłów interpolacyjnych:**

- Mała liczba węzłów (np. 10 węzłów):

Interpolowana krzywa (czerwona, przerywana linia) jest bardzo wygładzona i stanowi jedynie bardzo ogólne przybliżenie danych rzeczywistych (niebieska, ciągła linia).
Lokalne, szybkie wahania wysokości w danych rzeczywistych (liczne "szczyty" i "doliny") są całkowicie pominięte lub znacznie złagodzone przez interpolację.
Odchylenia od danych rzeczywistych są znaczne. Interpolacja nie jest w stanie uchwycić złożoności terenu.

- Zwiększenie liczby węzłów (np. 20, 30, 40, 60 węzłów):

Wraz ze wzrostem liczby węzłów, interpolacja stopniowo staje się dokładniejsza. Krzywa interpolacji zaczyna coraz lepiej odwzorowywać lokalne szczyty i doliny danych rzeczywistych.
Dla 20 węzłów poprawa jest widoczna, ale nadal wiele detali jest pomijanych.
Przy 30 i 40 węzłach, interpolacja znacząco lepiej dopasowuje się do danych, odzwierciedlając coraz więcej nieregularności terenu.
Dla 60 węzłów, dopasowanie jest już bardzo dobre w większości przedziału. Krzywa interpolacji podąża bardzo blisko za danymi rzeczywistymi, uchwytując wiele z ich zmienności. Węzły interpolacji (zielone kropki) są rozmieszczone coraz gęściej, co naturalnie poprawia lokalne dopasowanie.

- Duża liczba węzłów (np. 80, 100 węzłów):

W przypadku 80 węzłów, pomimo bardzo dobrego dopasowania w środkowej części zakresu, na krańcach przedziału interpolacji (początek i koniec trasy) obserwujemy bardzo silne zjawisko Rungego. Krzywa interpolacji zaczyna gwałtownie oscylować z dużymi amplitudami, wykraczając daleko poza zakres wartości danych rzeczywistych.
Dla 100 węzłów, zjawisko Rungego jest jeszcze bardziej dramatyczne i rozciąga się na większą część przedziału, szczególnie na obu końcach. Oscylacje są ekstremalne, co sprawia, że interpolacja jest całkowicie bezużyteczna do reprezentowania danych w tych obszarach.

Podsumowując:

Dane dla trasy "genoa_rapallo.txt" charakteryzują się dużą zmiennością i licznymi lokalnymi szczytami i dolinami, co czyni je wymagającymi dla interpolacji wielomianowej.
Niewystarczająca liczba węzłów (np. 10): Prowadzi do zbyt dużego wygładzenia i utraty kluczowych informacji o profilu terenu.
Optymalna liczba węzłów (ok. 60): Pozwala na bardzo dobre dopasowanie do danych rzeczywistych, efektywnie uchwytując ich złożoność, bez widocznych oznak niestabilności. Dla tego typu danych, gdzie przebieg jest bardzo nieregularny, większa liczba węzłów jest potrzebna do osiągnięcia akceptowalnej dokładności.
Zbyt duża liczba węzłów (np. 80, 100): Powoduje poważne problemy ze stabilnością interpolacji na krańcach przedziału (zjawisko Rungego). Mimo że węzły Chebysheva pomagają w rozłożeniu błędu, przy tak nieregularnych danych i dużej liczbie węzłów, problem ten staje się dominujący, uniemożliwiając wiarygodne prognozowanie lub reprezentowanie danych w tych obszarach.
Podsumowując, dla danych o wysokiej zmienności, znalezienie idealnej liczby węzłów jest kluczowe. Interpolacja Lagrange'a z węzłami Chebysheva jest skuteczna, ale ma swoje ograniczenia, zwłaszcza gdy dąży się do zbyt dużej dokładności poprzez zwiększanie stopnia wielomianu, co skutkuje niestabilnością na brzegach.

### Wnioski z analizy ilości węzłów interpolacyjnych

**Wpływ liczby węzłów:**

- Zwiększanie liczby węzłów interpolacyjnych zazwyczaj prowadzi do zwiększenia dokładności aproksymacji danych. Im więcej punktów jest użytych do konstrukcji wielomianu interpolacyjnego, tym lepiej jest on w stanie uchwycić szczegóły i fluktuacje oryginalnej funkcji.

- Istnieje punkt nasycenia. Powyżej pewnej liczby węzłów, dalsze ich dodawanie może nie przynosić już widocznej poprawy dokładności, szczególnie jeśli funkcja jest gładka. W niektórych przypadkach (niezaobserwowanych tutaj, ale teoretycznie możliwych przy bardzo dużej liczbie węzłów i niewłaściwym ich rozmieszczeniu, np. równoodległych), może nawet prowadzić do zjawiska Rungego, czyli oscylacji na brzegach przedziału. Użycie węzłów Czebyszewa minimalizuje to ryzyko.

**Wpływ rodzaju trasy (charakterystyki danych):**

- Trasy o wysokiej nieregularności i dużej liczbie ostrych zmian (np. "genoa_rapallo.txt") wymagają znacznie większej liczby węzłów interpolacyjnych, aby uzyskać akceptowalną dokładność. W przypadku takich danych, nawet duża liczba węzłów może nie oddać idealnie wszystkich detali, ale znacznie poprawia ogólne dopasowanie. Wygładzanie jest znaczące przy małej liczbie węzłów.

- Trasy o gładkim i regularnym profilu (np. "MountEverest.csv") mogą być bardzo dobrze aproksymowane za pomocą stosunkowo niewielkiej liczby węzłów. Charakterystyka danych, a konkretnie ich "gładkość" i stopień złożoności, ma fundamentalne znaczenie dla efektywności interpolacji. Im bardziej "gładka" funkcja, tym mniej węzłów potrzeba do jej dokładnego odwzorowania.

Podsumowując, optymalna liczba węzłów interpolacyjnych jest silnie zależna od charakterystyki danych, które mają być interpolowane. Dla bardzo nieregularnych danych, konieczne jest użycie większej liczby węzłów, podczas gdy dla gładkich danych mniejsza liczba węzłów jest często wystarczająca. Węzły Czebyszewa są dobrym wyborem, ponieważ minimalizują oscylacje, co jest szczególnie ważne przy interpolacji danych o dużej zmienności.

# 4. Wnioski
Na podstawie przeprowadzonej analizy interpolacji funkcji można sformułować następujące wnioski:

- **Rozmieszczenie węzłów interpolacyjnych ma kluczowe znaczenie dla jakości interpolacji.** 
  - Węzły rozmieszczone według rozkładu Czebyszewa pozwalają na znaczne ograniczenie błędów interpolacji i eliminację efektu Rungego, który pojawia się przy równomiernym rozmieszczeniu węzłów, zwłaszcza na krańcach przedziału.

- **Liczba węzłów interpolacyjnych wpływa na dokładność aproksymacji.** 
  - Zwiększanie liczby węzłów pozwala lepiej odwzorować szczegóły funkcji, jednak powyżej pewnego poziomu dalsze zwiększanie liczby węzłów nie przynosi już istotnej poprawy, szczególnie dla funkcji gładkich.

- **Charakterystyka danych (profil trasy) determinuje optymalną liczbę węzłów.** 
  - Dla tras o gładkim przebiegu (np. Mount Everest) już niewielka liczba węzłów zapewnia wysoką dokładność. Dla tras o dużej nieregularności (np. Genoa Rapallo) konieczne jest użycie większej liczby węzłów, aby uzyskać satysfakcjonujące dopasowanie.

- **Interpolacja wielomianowa Lagrange’a** jest skuteczna dla niewielkiej liczby węzłów i funkcji gładkich, jednak dla bardziej złożonych danych lub dużej liczby węzłów może prowadzić do oscylacji i błędów na krańcach przedziału.

Podsumowując, dobór odpowiedniej liczby i rozmieszczenia węzłów interpolacyjnych jest kluczowy dla uzyskania dokładnej i stabilnej interpolacji. W praktyce zaleca się stosowanie węzłów Czebyszewa oraz dostosowanie liczby węzłów do charakterystyki interpolowanych danych.
