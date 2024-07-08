SELECT Schueler.* FROM Schueler,K_AllgAdresse,Schueler_AllgAdr
WHERE
Schueler.Geloescht='-'
AND (Schueler_AllgAdr.Adresse_ID=K_AllgAdresse.ID AND Schueler.ID=Schueler_AllgAdr.Schueler_ID AND K_AllgAdresse.AllgAdrAdressArt IS NOT NULL)
AND Schueler.Status IN (2,9,8) 
AND Schueler.AktSchuljahr = 2024