# Smilang: eine esoterische Programmiersprache
## Allgemeine Informationen
Smilang ist eine esoterische Programmiersprache, deren Code man ausschließlich mit Smileys bzw. Emoticons schreibt. Es gibt Variablen, Schleifen und If-Anweisungen, mit denen man in der Lage ist, verschiedene algorithmische Probleme zu lösen.
## Installation (nur Windows)
Zum Installieren der Programmiersprache musst du nur den [Installer](installer/InnoSetup/mysetup.exe) herunterladen und ausführen. Danach erstellst du eine Datei mit der Endung ".smiley", in der du deinen Code schreiben und ihn dann ausführen kannst.
## Syntax
### Allgemein
Zwischen jedem Emoticon muss ein Leerzeichen sein.  
In jeder Zeile muss eine Wertzuweisung, eine If-Anweisung, eine Schleife oder die Ausgabe eines Wertes stehen, gefolgt von einem Zeilenumbruch.  
### Operatoren
#### Arithmetische Operatoren
Addition: `:-)`  
Subtraktion: `:-(`  
Multiplikation: `:-*`  
Division: `:-/`  
#### Vergleichsoperatoren
Kleiner als: `:<`  
Größer als: `:>`  
Gleich: `:=)`  
Ungleich: `:=(`  
### Datentypen
Die Programmiersprache hat nur die bekannten Datentypen Integer und String.
#### Integer
Ganze Zahlen können im Binärsystem dargestellt werden. Dabei steht `:)` für 1 und `:(` für 0. Das erste Bit steht für das Vorzeichen.  
_**Beispiel für die Zahl 18**_:  
`:( :) :( :( :) :(`  
_Hinweis_: Wenn der Quotient einer Division keine ganze Zahl ist, wird er abgerundet.
#### String
Ein String kann nur ASCII-Buchstaben enthalten.  
Jeder Buchstabe wird mit einem oder mehreren Emoticons dargestellt:  
_**Optionales Emoticon**_: Um einen Buchstaben groß zu schreiben, schreibt man `:))` davor.  
_**Einteilung des Alphabets**_: Das Alphabet wird in 5 gleich große Gruppen (und den Buchstaben Z) eingeteilt, sodass es nur 6 Emoticons gibt, die man zur Bestimmung eines Buchstabens braucht und nicht 26.  
_**Erstes Emoticon**_: Dieses Emoticon gibt die Gruppe an, in der sich der Buchstabe befindet. Wenn dieser Buchstabe "z" ist, dann wird das sechste Emoticon verwendet und das zweite Emoticon wird nicht gebraucht.  
_**Zweites Emoticon**_: Dieses Emoticon gibt die Position des Buchstabens innerhalb der vorher bestimmten Gruppe an.  
_**Die Gruppen**_: `"a", "b", "c", "d", "e" | "f", "g", "h", "i", "j" | "k", "l", "m", "n", "o" | "p", "q", "r", "s", "t" | "u", "v", "w", x", "y" | "z"`  
_**Die Emoticons**_: `:^) :-] =] :] :D :-))`  
_**Beispiel für das Wort "Hi"**_:  
&emsp;"H": Groß, Zweite Gruppe, Dritter Buchstabe &rarr; `:)) :-] =]`  
&emsp;"i": Klein, Zweite Gruppe, Vierter Buchstabe &rarr; `:-] :]`  
&emsp;"Hi": `:)) :-] =] :-] :]`
#### Hinweis
Sowohl Zahlen als auch Buchstaben können mit dem [Converter](converter.py) umgewandelt werden und müssen nicht manuell übersetzt werden.
### Variablen
Der Datentyp muss nicht extra angegeben werden, sondern wird automatisch erkannt.  
Es gibt nur eine begrenzte Anzahl an Variablen, da es nur eine begrenzte Anzahl an möglichen Namen gibt. Diese Namen bestehen aus einer Kombination von maximal 5 Emoticons.  
**Mögliche Emoticons**: `;) ;-) ;D :P :-o`  
Einer Variable weist man einen Wert wie folgt zu:
`[Name] =) [Wert]`  
Der Wert kann hierbei ein String oder ein Integer (oder eine Rechnung) sein.  
**Beispiel**:
`;) =) :)) :-] =] :-] :]`
### If-Anweisungen
Eine If-Anweisung schreibt man wie folgt:
`xD [Bedingung]`  
Danach folgt ein Zeilenumbruch und man kann dann den Code innerhalb der If-Anweisung schreiben. Am Ende der If-Anweisung muss `;-]` in einer einzelnen Zeile stehen.  
In der Bedingung können Strings (nur mit Strings) und Integer (nur mit Integer) mithilfe der Vergleichsoperatoren verglichen werden.  
**Beispiel**:  
```
xD :( :) :( :> :( :)
[Code]
;-]
```
### Else-Anweisung
Um eine Else-Anweisung an eine If-Anweisung anzuhängen, schreibt man `XD`, aber ohne Bedingung. Wenn die Bedingung der If-Anweisung falsch ist, wird der Code in der Else-Anweisung ausgeführt. Am Ende muss wieder `;-]` stehen.  
**Beispiel**:
```
[If-Anweisung]
XD
[Code]
;-]
```
### Schleife
Eine Schleife schreibt man wie folgt:
`8-) [Anzahl an Iterationen]`, gefolgt vom Code und am Ende wieder das Schlusszeichen `;-]`.  
**Beispiel**:
```
8-) :( :) :) :)
[Code]
;-]
```
### Ausgabe
Um Werte in der Konsole auszugeben, schreibt man `:p [Wert]`.  
**Beispiel**:  
`:p :)) :-] =] :-] :]`

### Kommentare
Auch wenn das vielleicht die Ästhetik der Emoticons stört, ist es trotzdem möglich `://` zu schreiben, woraufhin der Rest der Zeile ignoriert wird.

## Errors
Die Programmiersprache erkennt selber Fehler, beispielsweise in der Syntax. Beim Auftreten eines Fehlers wird man auf diesen hingewiesen und erhält außerdem die Code-Zeile, in der er auftrat.

## Beispielskript
### Berechnung der ersten zehn Fibonacci-Zahlen:
```
;) =) :( :)
;-) =) :( :)
;D =) :( :(
8-) :( :) :( :( :(
;D =) ;) :-) ;-)
;) =) ;-)
;-) =) ;D
;-]
:p ;-)
```
