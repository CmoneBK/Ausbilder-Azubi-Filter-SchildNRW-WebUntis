SELECT Schueler.*
FROM Schueler
JOIN Schueler_AllgAdr ON Schueler.ID = Schueler_AllgAdr.Schueler_ID
LEFT JOIN K_AllgAdresse ON Schueler_AllgAdr.Adresse_ID = K_AllgAdresse.ID
WHERE
Schueler.Geloescht = '-'
AND ((K_AllgAdresse.AllgAdrAdressArt = 'Betrieb') OR(Schueler_AllgAdr.Vertragsart_ID = 1))
AND Schueler.Status IN (2, 9, 8)
AND Schueler.AktSchuljahr = 2024
