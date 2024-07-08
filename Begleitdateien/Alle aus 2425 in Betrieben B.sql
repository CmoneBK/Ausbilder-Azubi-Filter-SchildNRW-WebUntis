SELECT Schueler.* FROM Schueler,Schueler_AllgAdr
WHERE
Schueler.Status IN (2,9,8) 
AND Schueler.Geloescht='-' 
AND Schueler.AktSchuljahr=2024
AND (Schueler.ID=Schueler_AllgAdr.Schueler_ID AND Schueler_AllgAdr.Vertragsart_ID = 1)