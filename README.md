# Ausbilder- und Azubi-Filter

## Einführung

Dieses Programm wurde entwickelt, um Berufskollegs in Nordrhein-Westfalen (NRW) zu unterstützen, indem es ermöglicht, unentschuldigte Fehlstunden von Schülern gemäß den rechtlichen Anforderungen der Datenschutz-Grundverordnung (DSGVO) zu verwalten. Das Programm hilft dabei, die Verarbeitung und Verteilung dieser Daten effizienter und sicherer zu gestalten.

## Motivation

In NRW erlaubt die Verordnung über die zur Verarbeitung zugelassenen Daten von Schülerinnen, Schülern und Eltern (VO DVI) zur Kommunikation von Abwesenheitsdaten von Berufskollegs an Ausbilder nur [die Übermittlung unentschuldigter Fehlstunden]([https://recht.nrw.de/lmi/owa/br_text_anzeigen?v_id=10000000000000000576#:~:text=4.%20Erreichbarkeit%2C-,5.%20Angaben%20zu%20unentschuldigten%20Schulvers%C3%A4umnissen.,-(5)%20Zur%20Organisation](https://bass.schul-welt.de/101.htm#:~:text=4.%20Erreichbarkeit%2C-,5.%20Angaben%20zu%20unentschuldigten%20Schulvers%C3%A4umnissen.,-(5)%20Zur%20Organisation)).
Dies erfolgt auf der rechtlichen Grundlage von DSGVO Artikel 6 Abs. 1 Satz 1 Buchstabe e, Abs. 3 und Artikel 9 Abs. 2 Buchstabe g.

Für alle anderen Daten, wie entschuldigte Fehlzeiten, ist eine ausdrückliche Zustimmung des Schülers erforderlich, gemäß Artikel 6 Buchstabe a oder b der DSGVO. (Grundsätze der Artikel 5, 6, 7, 9 sind in der VO DVI ebenfalls als geltendes Recht erwähnt.)

Ein Problem entsteht, weil WebUntis zur Anzeige für Ausbildungsbeauftragte derzeit nicht zwischen unentschuldigten und entschuldigten Fehlzeiten unterscheiden kann und die Ausbilder über die Schülerstammdaten importiert werden. Dadurch erhalten Ausbilder zwangsläufig Zugriff auf die Abwesenheitsdaten aller Schüler im Datensatz, auch wenn nicht alle Schüler zugestimmt haben. Dies führt zu einem Datenschutzproblem.

Um dieses Problem zu lösen, müsste entweder manuell in SCHILD NRW gefiltert werden, was sehr umständlich ist, oder der Ausbilder müsste auf alle Daten verzichten, was nicht praktikabel ist.

Das Programm bietet eine Lösung für dieses Problem, indem es ermöglicht, Schüler, die nicht zugestimmt haben, auf eine Blacklist zu setzen und den Import auf bestimmte Klassen zu beschränken (insbesondere nützlich für Probephasen).

## Grundfunktionen

- **CSV-Import**: Laden Sie eine CSV-Datei hoch, die die Schülerdaten enthält.
- **Blacklist**: Setzen Sie Schüler, die nicht zugestimmt haben, auf eine Blacklist.
- **Klassenfilter**: Begrenzen Sie den Import auf bestimmte Klassen.
- **CSV-Export**: Exportieren Sie die gefilterten Daten in eine neue CSV-Datei mit Datums- und Uhrzeitangaben im Dateinamen.
- **Automatisches Öffnen im Browser**: Die Webanwendung wird nach dem Start automatisch im Browser geöffnet.

## Installation und Nutzung

1. **Download und Installation**: Laden Sie die ausführbare Datei (`run.exe`) herunter und speichern Sie sie in einem Verzeichnis Ihrer Wahl.
2. **Starten der Anwendung**: Doppelklicken Sie auf `run.exe`. Die Anwendung erstellt automatisch eine `config.ini`-Datei, falls diese nicht vorhanden ist, und öffnet die Webanwendung im Standardbrowser.
3. **CSV-Datei hochladen**: Laden Sie über die Weboberfläche eine CSV-Datei hoch, die die Schülerdaten enthält.
4. **Konfigurieren der Klassen und Blacklist**: Verwenden Sie die Weboberfläche, um Klassen festzulegen und Schüler auf die Blacklist zu setzen.
5. **CSV-Datei filtern**: Klicken Sie auf den Button "CSV-Datei filtern", um die gefilterten Daten zu exportieren.

## Beispielhafte `config.ini`

Eine beispielhafte `config.ini` könnte wie folgt aussehen:

```ini
[FILTER]
Classes=Klasse1,Klasse2,Klasse3

[BLACKLIST]
IDs=12345,67890
```
Diese Datei wird automatisch erstellt, wenn sie nicht vorhanden ist, und kann über die Weboberfläche bearbeitet werden.

 ## Rechtliche Hinweise
Dieses Programm wurde entwickelt, um Berufskollegs dabei zu unterstützen, die Anforderungen der DSGVO zu erfüllen. Bitte stellen Sie sicher, dass Sie die rechtlichen Anforderungen Ihrer spezifischen Situation kennen und einhalten.
