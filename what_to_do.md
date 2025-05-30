 Lista TODO dla projektu 3 z Metod Numerycznych

1. [ ] Pobierz dane rzeczywiste (geocontext.org, Google Maps Api) dla kilku tras (maksymalnie 5) o zróżnicowanym charakterze:
   - Trasa prawie płaska bez różnic wysokości.
   - Trasa z jednym wyraźnym wzniesieniem.
   - Trasa z wieloma stromymi wzniesieniami.

   Trasy:
   - Prawie płaska trasa:
     - Biebrzański Park Narodowy
     ```
      (53.2000, 22.5000)
      (53.2100, 22.5100)
      (53.2200, 22.5200)
      (53.2300, 22.5300)
      (53.2400, 22.5400)
      (53.2500, 22.5500
     ```
   - Trasa z jednym wyraźnym wzniesieniem:
     - Góra Świętej Anny 
     ```
      (50.4500, 18.2000)
      (50.4600, 18.2100)
      (50.4700, 18.2200)
      (50.4800, 18.2300)
      (50.4900, 18.2400)
      (50.5000, 18.2500)
     ```
   - Trasa z wieloma stromymi wzniesieniami:
     - Tatry – Dolina Kościeliska 
     ```
      (49.2700, 19.8500)
      (49.2800, 19.8600)
      (49.2900, 19.8700)
      (49.3000, 19.8800)
      (49.3100, 19.8900)
      (49.3200, 19.9000)
     ```
   - Trasa o zróżnicowanym charakterze:
     - Kaszuby – Wzgórza Szymbarskie 
      ```
      (54.2000, 18.0000)
      (54.2100, 18.0100)
      (54.2200, 18.0200)
      (54.2300, 18.0300)
      (54.2400, 18.0400)
      (54.2500, 18.0500)
     ```
   - Trasa miejska:
     - Warszawa – Trasa wzdłuż Wisły 
     ```
      (52.2300, 21.0100)
      (52.2400, 21.0200)
      (52.2500, 21.0300)
      (52.2600, 21.0400)
      (52.2700, 21.0500)
      (52.2800, 21.0600)
     ```
     
2. Zastosuj metody aproksymacji interpolacyjnej:
   - [ ] Wielomian interpolacyjny Lagrange’a.
   - [ ] Funkcje sklejane trzeciego stopnia.

3. [ ] Zastosuj transformację dziedziny funkcji interpolowanej do przedziału [-1,1] lub [0,1] w celu poprawy stabilności numerycznej obliczeń.

4. Zweryfikuj przydatność obu metod:
   - [ ] Zbadaj wpływ liczby punktów węzłowych na wyniki.
   - [ ] Zbadaj wpływ rozmieszczenia punktów węzłowych na wyniki.
   - [ ] Zbadaj wpływ dokładności pomiaru punktów węzłowych na wyniki.
   - [ ] Zbadaj wpływ charakteru trasy na wyniki.
   - [ ] Dodaj inne analizy według własnej inwencji.

5. Przygotuj sprawozdanie:
   - [ ] Wstęp z krótkim opisem analizowanych algorytmów.
   - [ ] Analiza podstawowa interpolacji wielomianowej dla każdej trasy (minimum 2 trasy).
   - [ ] Analiza podstawowa interpolacji funkcjami sklejanymi dla każdej trasy (minimum 2 trasy).
   - [ ] Analiza dodatkowa interpolacji (wpływ innych parametrów niż liczba węzłów).
   - [ ] Podsumowanie zawierające wnioski z przeprowadzonej analizy.

6. [ ] Wykonaj wykresy:
   - Minimum 20 wykresów (4 wykresy na każdą analizę).
   - Każdy wykres powinien zawierać:
     - Dane oryginalne.
     - Wartość danych w węzłach interpolacji.
     - Interpolację.
   - Wykresy powinny posiadać legendę, opis osi oraz tytuł informujący o rodzaju interpolacji oraz liczbie węzłów interpolacji.


