# Smilang: eine esoterische Programmiersprache
***
## Allgemeine Informationen
Besteht nur aus Smileys  
Programmierparadigma Imperativ oder so  
Interpretierte Sprache  
In Python geschrieben  
Smilang ist eine esoterische Programmiersprache, deren Code man einzig und allein mit Smileys bzw. Emoticons schreibt. Es gibt Variablen, Schleifen und If-Anweisungen mit denen man in der Lage ist verschiedene algorithmische Probleme zu lösen.
## Installation
## Syntax
### Allgemein
Zwischen jedem Emoticon muss ein Leerzeichen sein  
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
Die Programmiersprache hat nur die bekannten Datentypen Integer und String
#### Integer
Ganze Zahlen können im Binärsystem dargestellt werden. Dabei steht :) für 1 und :( für 0. Das erste Bit steht für das Vorzeichen.  
_Beispiel für die Zahl 18_:  
`:( :) :( :( :) :(`
#### String
Ein String kann nur ASCII-Buchstaben enthalten.  
Jeder Buchstabe wird mit einem mehreren Emoticons dargestellt:  
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
Sowohl Zahlen als auch Buchstaben können mit dem [Converter](converter.py) konvertiert werden und müssen nicht manuell übersetzt werden.
### Variablen
Der Datentyp muss nicht extra angegeben werden, sondern wird automatisch erkannt.  
Es gibt nur eine begrenzte Anzahl an Variablen, da es nur eine begrenzte Anzahl an möglichen Namen gibt. Diese Namen bestehen aus einer Kombination von maximal 5 Emoticons.  
**Mögliche Emoticons**: `;) ;-) ;D :P :-o`  
Eine Variable weist man einen Wert wie folgend zu:
`[Name] =) [Wert]`  
Der Wert kann hierbei ein String oder ein Integer (oder eine Rechnung) sein.
### If-Anweisungen
Eine If-Anweisung schreibt man wie folgend:
`xD [Bedingung]`  
Danach folgt ein Zeilenumbruch und man kann dann den Code innerhalb der-Anweisung schreiben. Am Ende der If-Anweisung muss `;-]` in einer einzelnen Zeile stehen.


## Beispielskript

Nicht Effizient, weil in Python geschrieben
