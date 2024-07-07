# Ausbilder- und Azubi-Filter

## Einf�hrung

Dieses Programm wurde entwickelt, um Berufskollegs in Nordrhein-Westfalen (NRW) zu unterst�tzen, indem es erm�glicht, unentschuldigte Fehlstunden von Sch�lern gem�� den rechtlichen Anforderungen der Datenschutz-Grundverordnung (DSGVO) zu verwalten. Das Programm hilft dabei, die Verarbeitung und Verteilung dieser Daten effizienter und sicherer zu gestalten.

## Motivation

In NRW erlaubt die Verordnung �ber die Verarbeitung von Dienst- und Vereinsmitgliederdaten (VO DVI) zur Kommunikation von Abwesenheitsdaten von Berufskollegs an Ausbilder nur die �bermittlung unentschuldigter Fehlstunden. Dies erfolgt auf der rechtlichen Grundlage von DSGVO Artikel 6 Abs. 1 Satz 1 Buchstabe e, Abs. 3 und Artikel 9 Abs. 2 Buchstabe g.

F�r alle anderen Daten, wie entschuldigte Fehlzeiten, ist eine ausdr�ckliche Zustimmung des Sch�lers erforderlich, gem�� Artikel 6 Buchstabe a oder b der DSGVO. (Grunds�tze der Artikel 5, 6, 7, 9 sind in der VO DVI ebenfalls als geltendes Recht erw�hnt.)

Ein Problem entsteht, weil WebUntis zur Anzeige f�r Ausbildungsbeauftragte derzeit nicht zwischen unentschuldigten und entschuldigten Fehlzeiten unterscheiden kann und die Ausbilder �ber die Sch�lerstammdaten importiert werden. Dadurch erhalten Ausbilder zwangsl�ufig Zugriff auf die Abwesenheitsdaten aller Sch�ler im Datensatz, auch wenn nicht alle Sch�ler zugestimmt haben. Dies f�hrt zu einem Datenschutzproblem.

Um dieses Problem zu l�sen, m�sste entweder manuell in SCHILD NRW gefiltert werden, was sehr umst�ndlich ist, oder der Ausbilder m�sste auf alle Daten verzichten, was nicht praktikabel ist.

Das Programm bietet eine L�sung f�r dieses Problem, indem es erm�glicht, Sch�ler, die nicht zugestimmt haben, auf eine Blacklist zu setzen und den Import auf bestimmte Klassen zu beschr�nken (insbesondere n�tzlich f�r Probephasen).

## Grundfunktionen

- **CSV-Import**: Laden Sie eine CSV-Datei hoch, die die Sch�lerdaten enth�lt.
- **Blacklist**: Setzen Sie Sch�ler, die nicht zugestimmt haben, auf eine Blacklist.
- **Klassenfilter**: Begrenzen Sie den Import auf bestimmte Klassen.
- **CSV-Export**: Exportieren Sie die gefilterten Daten in eine neue CSV-Datei mit Datums- und Uhrzeitangaben im Dateinamen.
- **Automatisches �ffnen im Browser**: Die Webanwendung wird nach dem Start automatisch im Browser ge�ffnet.

## Installation und Nutzung

1. **Download und Installation**: Laden Sie die ausf�hrbare Datei (`run.exe`) herunter und speichern Sie sie in einem Verzeichnis Ihrer Wahl.
2. **Starten der Anwendung**: Doppelklicken Sie auf `run.exe`. Die Anwendung erstellt automatisch eine `config.ini`-Datei, falls diese nicht vorhanden ist, und �ffnet die Webanwendung im Standardbrowser.
3. **CSV-Datei hochladen**: Laden Sie �ber die Weboberfl�che eine CSV-Datei hoch, die die Sch�lerdaten enth�lt.
4. **Konfigurieren der Klassen und Blacklist**: Verwenden Sie die Weboberfl�che, um Klassen festzulegen und Sch�ler auf die Blacklist zu setzen.
5. **CSV-Datei filtern**: Klicken Sie auf den Button "CSV-Datei filtern", um die gefilterten Daten zu exportieren.

## Beispielhafte `config.ini`

Eine beispielhafte `config.ini` k�nnte wie folgt aussehen:

```ini
[FILTER]
Classes=Klasse1,Klasse2,Klasse3

[BLACKLIST]
IDs=12345,67890
Diese Datei wird automatisch erstellt, wenn sie nicht vorhanden ist, und kann �ber die Weboberfl�che bearbeitet werden.
```

 ## Rechtliche Hinweise
Dieses Programm wurde entwickelt, um Berufskollegs dabei zu unterst�tzen, die Anforderungen der DSGVO zu erf�llen. Bitte stellen Sie sicher, dass Sie die rechtlichen Anforderungen Ihrer spezifischen Situation kennen und einhalten.
Stellen Sie sicher, dass Sie diese Datei in Visual Studio in Ihrem Projekt als `README.md` speichern. Diese Datei wird dann auf GitHub korrekt formatiert angezeigt.
