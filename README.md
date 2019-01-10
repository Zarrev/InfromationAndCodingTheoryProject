# InfromationAndCodingTheoryProject
Optional task with sub-tasks for getting advantages to university subject (namely Information and Coding Theory). 
 The sub-task are the following: 
 - Error Correction Coding;
 - Data Compression;
 - Encryption.







## I. Hibajavító kódolás (100 pont)

Írjon szimulációt, mely szimulálja a csatornaátvitelt és valamilyen hibajavító kódolást.
` (Pl.: mint ez: http://users.itk.ppke.hu/~lorma/select_dmin/ ) `
A szimuláció menete, hogy egy véletlenszerűen generált u vektort kódoljon a program,
adjon hozzá egy véletlenszerűen (állítható eloszlással) generált hibavektort, majd
próbálja meg visszaalakítani.
Az egyes lépések láthatóak és elkülöníthetőek legyenek a program futása során!
` (Jelenjen meg u, c, e, v, e’, u’) `
A kész szimulációval teljesítőképesség analízist is kell készíteni (= grafikonok pl.
csatorna P_b hibavalószínűségánek függvényében a helyesen átvitt üzenetek száma), és
azokat szövegesen is ki kell értékelni.

- Pontozás:
  - Használható GUI : 15 pont
  - Ismétléses kód implementálása: 5 pont
  - Hamming kód implementálása (paraméterben kérje be n-t, generáljon hozzá k-t,
    írja is ki őket)
    - Minden 1 hiba javítása: 5 pont
    - Minden 2 hiba javítása: 5 pont
  - Golay kód (ciklikus kód) : 15 pont
    - Ez előadáson és gyakorlaton nem került elő, az utánaolvasás és egy 
          legalább 2 diás összefoglaló írása is része a feladatnak.
  - RS kód GF(q) felett 25 pont
    - A generátort nem kell generálni programból, azok előre
        legenerálhatóak. Ha nem a programból generálódik, legyen legalább
        három beépítve, melyek képesek javítani minden 2, 3 és 4 hibát.
    - A feladat az ETA implementálását is tartalmazza
  - RS kód GF(2^n) felett 30 pont
    - A generátort nem kell generálni programból, azok előre
        legenerálhatóak. Ha nem a programból generálódik, legyen legalább
        három beépítve, melyek képesek javítani minden 2, 3 és 4 hibát.
    - A feladat az ETA implementálását is tartalmazza
            
            
## II. Adattömörítés (100)

A feladat egy tömörítő és kicsomagoló program írása, amely képes tetszőleges bináris
fájlt betömöríteni és kicsomagolni.
A tömörítés kimenete két fájl, egyik a tömörített adatot tartalmazza, a másik a
kicsomagoláshoz szükséges metainformációkat (pl.: szimbólumtábla). Egy valódi
tömörítőprogramnál (pl. WinZip) ezek egy fájlba kerülnek, de most fontos, hogy
látszódjon, mekkora a tömörített adat és mennyi információ kell a visszaállításához.
Mindegyik algoritmus esetén a feladat része a kiosztott 5 fájl tömörítése 
` (véletlen, egyenletes eloszlású bináris fájl; véletlen, nem egyenletes eloszlású bináris fájl;
Karinthy összes verse plain text formátumban, Karinthy összes verse docx
formátumban, Karinthy összes verse plain text formátumban GZ-vel tömörítve) `
és a tapasztalatok rövid leírása. 
` (Melyik fájlt mennyire lehetett tömöríteni, miért?) `

A választható tömörítő algoritmusok:

- [x] 1. SF (15 pont)
- [x] 2. Huffman (15 pont)
- [x] 3. Adaptív Huffman (25 pont)
- [x] 4. SFE (15 pont)
- [x] 5. Lempel-Ziv (15-15 pont)

        
## III. Titkosítás (50)

A tananyag harmadik rész a titkosítás, melyből két algoritmust lehet implementálni:
* OTP : 10 pont
* RSA : 40 pont

Mindkét algoritmus bemenete egy tetszőleges fájl és a (publikus) kulcs, kimenete pedig
a titkosított fájl.
A feladathoz hozzátartozik egy visszafejtő program is, melyek bemenete a (privát)
kulcs, kimenete pedig az eredeti állomány.
