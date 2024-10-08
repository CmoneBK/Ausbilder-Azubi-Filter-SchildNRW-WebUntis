# Ausbilder- und Azubi-Filter (SchildNRW -> WebUntis)

## Einführung

Dieses Programm wurde entwickelt, um Berufskollegs in Nordrhein-Westfalen (NRW) zu unterstützen, indem es ermöglicht, Fehlstunden von Auszubildenden gemäß den rechtlichen Anforderungen `der Verordnung über die zur Verarbeitung zugelassenen Daten von Schülerinnen, Schülern und Eltern (VO DVI) und Datenschutz-Grundverordnung (DSGVO)` den Ausbildungsbeauftragten/Ausbildern in WebUntis zur Verfügung zu stellen. 
Das Programm hilft dabei, die Verarbeitung und Verteilung dieser Daten mittels Filterung und Blacklisting aufwandtechnisch effizienter und rechtlich sicherer zu gestalten.

## Disclaimer
Ich bin kein Anwalt, sondern Lehrkraft und alle hier getätigten rechtlichen Aussagen und Interpretationen sind die vorherrschende Meinung und Interpretation an unserem Berufskolleg. Prüfe Sie dies im Zweifelsfall selbst. Im Folgenden Teil sind dazu hilfreiche Quellen verlinkt.

## Motivation und ursprüngliches Problem

In NRW erlaubt die Verordnung über die zur Verarbeitung zugelassenen Daten von Schülerinnen, Schülern und Eltern (VO DVI) zur Kommunikation von Abwesenheitsdaten von Berufskollegs an Ausbilder nur [die Übermittlung unentschuldigter Fehlstunden](https://bass.schul-welt.de/101.htm#:~:text=4.%20Erreichbarkeit%2C-,5.%20Angaben%20zu%20unentschuldigten%20Schulvers%C3%A4umnissen.,-(5)%20Zur%20Organisation).

[Dies erfolgt auf der rechtlichen Grundlage von DSGVO Artikel 6 Abs. 1 Satz 1 Buchstabe e, Abs. 3 und Artikel 9 Abs. 2 Buchstabe g.](https://bass.schul-welt.de/101.htm#:~:text=Nach%20Artikel%206%20Abs.%201%20Satz%201%20Buchstabe%20e%2C%20Abs.%203%20und%20Artikel%209%20Abs.%202%20Buchstabe%20g)

Für alle anderen Daten, wie entschuldigte Fehlzeiten, ist eine ausdrückliche Zustimmung des Schülers bzw. der Schülerin bzw. des/der Auszubildenden erforderlich, [gemäß Artikel 6 Buchstabe a oder b der DSGVO](https://dsgvo-gesetz.de/art-6-dsgvo/#:~:text=Die%20betroffene%20Person,betroffenen%20Person%20erfolgen%3B). [Grundsätze der Artikel 5, 6, 7, 9 sind in der BASS zur VO DVI ebenfalls als geltendes Recht erwähnt](https://bass.schul-welt.de/101.htm#:~:text=insbesondere,6%2C%207%2C%209).

Probleme entstehen, weil 
- WebUntis (Stand 08.07.2024) zur Anzeige von Fehlzeiten für Ausbildungsbeauftragte derzeit nicht zwischen unentschuldigten und entschuldigten Fehlzeiten unterscheidet und
- die Ausbilder über die Schülerstammdaten mittels Abgleich der Ausbilderdaten importiert und zugeordnet werden.

Dadurch erhalten Ausbilder zwangsläufig permanenten Zugriff auf die Abwesenheitsdaten aller ihnen so zuogeordneten Schülerinnnen und Schüler im Datensatz, auch wenn nicht alle Schüler zugestimmt haben. 
Dies führt zu einem Datenschutzproblem.

Um dieses Problem zu lösen, müsste entweder manuell in SCHILD NRW gefiltert werden, was sehr umständlich sein kann*, oder der Ausbilder müsste auf alle Daten verzichten, was nicht praktikabel ist.

Das Programm bietet eine Lösung für dieses Problem, indem es ermöglicht, Schüler, die nicht zugestimmt haben, auf eine Blacklist zu setzen und den Import auf bestimmte Klassen zu beschränken (insbesondere nützlich für Probephasen).

Übrigens: Selbst wenn ausschließlich unentschuldigte Daten sichtbar wären oder wiederholt übertragen würden könnte man durch den dauerhaften bzw. wiederholten Zugriff im Nachhinein Entschuldigte identifizieren, was nach VO DVI ebenfalls nicht zulässig wäre.

*In SchildNRW gibt es die Checkbox "```DV-Einwilligung vorh.```". Wenn Sie diese auch in der Vergangenheit nie genutzt haben (Datenkonsistenz), nutzen Sie diese gerne hierfür. Sie brauchen hier dann nicht mehr weiterlesen. Wenn Sie oder Ihr Sekretariat diese Checkbox jedoch jemals für etwas anderes genutzt haben sind Sie in der selben Situation wie der Ersteller dieses Programms :). 

## Vorraussetzungen zur Verwendung des Programms
- Sie Nutzen die Interne-ID zur Schülerdidentifikation in SchildNRW
- Sie Nutzen den Schlüssel (extern) Zur Schüleridentifikation in WebUntis
  
## Grundfunktionen

- **CSV-Import**: Laden einer CSV-Datei im Verzeichnis der App oder als Upload über das WebEnd, welche die Schülerdaten enthält.
- **Blacklist**: Setzen der Schüler, die nicht zugestimmt haben, auf eine Blacklist.
- **Klassenfilter**: Begrenzen des Imports auf bestimmte Klassen.
- **CSV-Export**: Exportieren der gefilterten Daten in eine neue CSV-Datei mit Datums- und Uhrzeitangaben im Dateinamen.

## Vor der Installation 

1. Sorgen Sie dafür, dass in SchildNRW im Datensatz für Betreuer bei allen im aktuellen Schuljahr Aktiven, Abgägern und Abschlüssen ordentlich gepflegt ist (Vorraussetzungen für den sicheren AusbilderImport in WebUntis):
   - Betreuer dürfen bei allen exportierten Auszubildenen nur
     - in einer Schreibweise (Vorname, Nachname, E-Mail Adrese,...) und
     - mit allen Namensfeldern vorhanden und korrekt ausgefüllt 
     - und dem E-Mail Feld vorkommen. Die E-Mail Adresse sollte dabei keine allgemeine Firmenadresse sondern spezifisch die des Betreuers sein.
     - Auch die Anrede wird benötigt (s.u.).
   
   Wenn Sie die Daten überarbeiten füllen Sie am Besten ALLE Felder.

   Tipp: Ordnen Sie dabei in SchildNRW einen fertig aufbereitetenen Betreuer immer allen betreuten Auszubildenden zu.
     
2. Erstellen Sie in SchildNRW einen Filter, der zuverlässig ALLE im Schuljahr Auszubildenden (Aktiv, Abgang & Abschluss) erfasst.

    Dabei ist es besonders wichtig Abgägner und Abschlüsse und idealerweise auch ausgetragene Adressen zu erfassen, damit bei diesen beim späteren Import die Zuweisung zum Ausbilder auch wieder entfernt wird.
  
    - Beispiel 1 (Filter Typ I) (sofern letzter Punkt gepflegt):
  
    Laufbahn-Schuljahr: Aktuelles; Status: Aktiv, Abgang, Abschluss; (Unter Weitere Daten:) Weitere Adressen-Beschäftigungsart: Auszubildener 
  
    - Beispiel 2 (Filter Typ II (SQL)):
      
        [Variante A](Begleitdateien/Alle_aus_2425_in_Betrieben_A.sql) (Prüft, ob eine Adresse im Reiter Adressen/Betriebe vorhanden ist) 
        <pre>
        SELECT Schueler.* FROM Schueler,K_AllgAdresse,Schueler_AllgAdr
        WHERE
        Schueler.Geloescht='-'
        AND (Schueler_AllgAdr.Adresse_ID=K_AllgAdresse.ID AND Schueler.ID=Schueler_AllgAdr.Schueler_ID AND K_AllgAdresse.AllgAdrAdressArt IS NOT NULL)
        AND Schueler.Status IN (2,9,8) 
        AND Schueler.AktSchuljahr = 2024
        </pre> 
        [Variante B:](Begleitdateien/Alle_aus_2425_in_Betrieben_B.sql) (Prüft ob die Beschäftigungsart im Reiter Adressen/Betriebe Auszubildener ist)
        <pre>
        SELECT Schueler.* FROM Schueler,Schueler_AllgAdr
        WHERE
        Schueler.Status IN (2,9,8) 
        AND Schueler.Geloescht='-' 
        AND Schueler.AktSchuljahr=2024
        AND (Schueler.ID=Schueler_AllgAdr.Schueler_ID AND Schueler_AllgAdr.Vertragsart_ID = 1)
        </pre>
        [Variante A und B als ODER kombiniert](Begleitdateien/Alle_aus_2425_in_Betrieben_A-B.sql):
        <pre>
        SELECT Schueler.*
        FROM Schueler
        JOIN Schueler_AllgAdr ON Schueler.ID = Schueler_AllgAdr.Schueler_ID
        LEFT JOIN K_AllgAdresse ON Schueler_AllgAdr.Adresse_ID = K_AllgAdresse.ID
        WHERE
        Schueler.Geloescht = '-'
        AND ((K_AllgAdresse.AllgAdrAdressArt = 'Betrieb') OR(Schueler_AllgAdr.Vertragsart_ID = 1))
        AND Schueler.Status IN (2, 9, 8)
        AND Schueler.AktSchuljahr = 2024
        </pre>
3. Erstellen Sie in SchildNRW eine Dateiexportvorlage, die folgende Daten umfasst:
    - Allg. Adresse: Betreuer Anrede ```(Wird von WebUntis zur ordentlichen Darstellung benötigt)```
    - Allg. Adresse: Betreuer Vorname ```(Wird von WebUntis zur Identifikation benötigt)```
    - Allg. Adresse: Betreuer Name ```(Wird von WebUntis zur Identifikation benötigt)```
    - Allg. Adresse: Betreuer E-Mail ```(Wird von WebUntis für den Betreueraccount benötigt)```
    - Allg. Adresse: Betreuer Titel ```(sofern Feld als Anrede verwendet)```
    - Allg. Adresse: Betreuer Telefon ```(Kann von WebUntis zur Identifikation genutzt werden)```
    - Allg. Adresse: Betreuer Abteilung ```(Kann von WebUntis zur Identifikation genutzt werden)```  
    - Allg. Adresse: Fax-Nr. ```(Kann von WebUntis zur Identifikation genutzt werden)```
    - Allg. Adresse: Name1 ```(nutzen wir als Betriebname, welcher bei der Übersicht der Daten helfen kann)```
    - Interne ID-Nummer    ```(Wird von der APP und WebUntis zur Identifikation benötigt)```
    - Nachname             ```(Wird von der APP Benötigt)```
    - Vorname              ```(Wird von der APP Benötigt)```
    - Klasse               ```(Wird von der APP Benötigt)```

     Die Vorlage muss so konfiguriert sein, dass sie als Dateityp eine .csv Datei ausgibt (manuell als Dateityp "Alle Dateien (*.*)" auswählen und die Endung .csv anfügen)
   
4. Exportieren Sie eine Datei zum Testen.
   
5. Erstellen Sie in WebUntis eine Import Vorlage für Ausbildungsbeauftragte mit folgenden Einstellungen:
   - Erste Zeile ignorieren: Ja
   - Schülerverbindung additiv importieren: Nein (ein Ja würde dazu führen, dass neue Einträge auf der Blacklist nicht entfernt werden bzw. leere Einträge vorhandene nicht überschreiben)
   - Identifikation des Ausbildungsbeauftragten: automatisch
   
   Ordnen Sie die Felder sinvoll zu und lassen Sie die leer, die Sie nicht brauchen (zusätzliche Betreuerdaten helfen bei der automatischen Identifikation des Ausbildungsbeauftragten).
   Wesentlich sind dabei:
   - Allg. Adresse: Betreuer Anrede --> Titel ```(Darstellung des Namens in WebUntis in machen Bereichen sonst unvorteilhaft)```
   - Allg. Adresse: Betreuer Vorname --> Vorname ```(Grunddaten)```
   - Allg. Adresse: Betreuer Name --> Nachname ```(Grunddaten)```
   - Allg. Adresse: Betreuer E-Mail --> E-Mail Adresse ```(Grunddaten)```
   - Allg. Adresse: Betreuer Telefon --> Mobiltelefon ```(Optional aber nützlich)```
   - Allg. Adresse: Fax-Nr. --> Telefonnummer ```(Optional aber nützlich)```
   - Interne ID-Nummer --> Schlüssel (extern, Schüler) ```(Zentral zur Identifikation)```
  
## Installation und Nutzung

1. **Download und Installation**: Laden Sie die ausführbare Datei (`Ausbilder-Azubi-Filter-SchildNRW-WebUntis.exe`) herunter und speichern Sie sie in einem Verzeichnis Ihrer Wahl.  [Ausbilder-Azubi-Filter-SchildNRW-WebUntis.exe herunterladen (Downloadbutton dann oben rechts)](AusbilderImporterFlask/dist/Ausbilder-Azubi-Filter-SchildNRW-WebUntis.exe)
2. **Starten der Anwendung**: Doppelklicken Sie auf `AusbilderImporter.exe`. Die Anwendung erstellt automatisch eine `config.ini`-Datei, falls diese nicht vorhanden ist, und öffnet die Webanwendung im Standardbrowser. Löschen oder Verschieben Sie diese config.ini nicht. Sie enthält und behält den Filter, den Sie aufsetzen.
3. **CSV-Datei hochladen**: Laden Sie über die Weboberfläche eine CSV-Datei hoch, die die Schüler- und Ausbilderdaten enthält.
4. **Konfigurieren der Klassen und Blacklist**: Verwenden Sie die Weboberfläche, um Klassen festzulegen und Schüler auf die Blacklist zu setzen. (Keine Klassen = Kein Klassenfilter)
5. **CSV-Datei filtern**: Klicken Sie auf den Button "CSV-Datei filtern und ausgeben", um die gefilterten Daten zu exportieren. Sie werden im Unterverzeichnis AusbilderImportDateien gespeichert.
6. **Optional: CSV-Verzeichnis**: Geben Sie in der config.ini ein Verzeichnis an, in welchem das Programm zukünftig nach einer Importdatei suchen soll. Es darf dabei immer nur die zu importierende .csv Datei in diesem Verzeichnis sein.

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
Dieses Programm wurde entwickelt, um Berufskollegs dabei zu unterstützen, die Anforderungen der VO DVI und DSGVO zu erfüllen. Bitte stellen Sie sicher, dass Sie die rechtlichen Anforderungen Ihrer spezifischen Situation kennen und einhalten.
Ich übernehme keinerlei Haftung für das, was Sie mit diesem Tool tun.
