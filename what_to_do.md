 Lista TODO dla projektu 3 z Metod Numerycznych

1. [x] Pobierz dane rzeczywiste (geocontext.org, Google Maps Api) dla kilku tras (maksymalnie 5) o zróżnicowanym charakterze:
   Trasy:
   - Prawie płaska trasa:
   ```
   SpacerniakGdansk.csv  
   ```
    
   - Trasa z jednym wyraźnym wzniesieniem:
   ```
   MountEverest.csv
   ```

   - Trasa z jednym wyraźnym spadkiem:
   ```
   WielkiKAnionKolorado.csv
   ```
     
  - Trasa z wieloma stromymi wzniesieniami:
   ```
   genoa_rapallo.txt
   ```
    
  - Trasa o zróżnicowanym charakterze:
   ```
   ulm_lugano.txt
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


