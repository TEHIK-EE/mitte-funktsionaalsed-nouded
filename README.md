# TEHIK Mittefunktsionaalsed nõuded

## Dokumendid
Tervise ja Heaolu Infosüsteemide Keskuse (TEHIK) mittefunktsionaalsed nõuded (edaspidi MFN) on kirjeldatud järgmises dokumendis:

**[TEHIK mittefunktsionaalsed nõuded](mittefunktsionaalsed-nouded.md)**


Non-functional requirements (NFR) of the Health and Welfare Information Systems Centre (TEHIK) are described in the following document:

**[TEHIK non-functional requirements](mittefunktsionaalsed-nouded.en.md)**

## Versioonihaldus
- Hetkel kehtiv MFN versioon on alati "main" harus
  - Iga versiooni kohta tehakse git tag, millega on seotud ka TEHIKu poolt kinnitatud ning allkirjastatud MFN versioon
  - Tag versioonidest tehakse PDF ja Markdown formaadis failid, mis on kättesaavad TEHIKu [arendusjuhiste veebilehelt](https://www.tehik.ee/arendusjuhendid)
- Järgmise versiooni mustand on leitav "draft" prefiksiga harus

### Uue versiooni loomine ja kinnitamine
1. Kui mustand on valmis ja TEHIKu arhitektide poolt kinnitatud, merge'itakse see "main" harusse
2. Pärast merge'i luuakse git tag, mis sisaldab versiooninumbrit
3. Tagi versiooniga commit'ist tehakse PDF ja Markdown formaadis väljundid (väljund peab sisaldama ka git commiti SHA-d)
4. PDF ja Markdown formaadis väljundid allkirjastatakse TEHIKu poolt
5. Allkirjastatud versioonid avalikustatakse TEHIKu arendusjuhiste veebilehele
