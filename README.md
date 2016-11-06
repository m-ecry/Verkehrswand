# Verkehrswand
Einfache Anzeige für Ankunft und Abfahrt von einer Haltestelle mit Siebensegmentanzeigen und ein paar kleinen Extras.

- 2 Haltestellen
- 5 Linien
  - jeweils zwei Richtungen
  - Abfahrt in.., Nächste Abfahrt in..

Bauteilliste:
40x 7-Segmentanzeigen SC56-11GWA (Grün, 0,56") Common Cathode
40x Schieberegister SN74HC595
- pro Richtung 2x2 für Abfahrt in und nächste Abfahrt

1x Raspberry Pi (für Internetzugang, evtl. Austauschen durch Stromsparende Alternative)
X Knöpfe

Das ganze auf einer Holzplatte mit Abmaßen 75 x 55 cm, 5 cm hoch für Raum zum bestücken.
Jeden Tag ein wenig..
Und noch ein wenig..

SCHema und BoRDdateien, erstellt mit Eagle 7.7.0.
Enthalten Boardentwurf für 7-Segment Anzeige, angesteuert durch 2 74-595 Shift-Register. Nötige Anschlusskontaktierung: 
- Supply (1x GND, 1x VCC)
- SER
- CLK
- (optional) OE
Version A (doppelshift2): Standartversion mit Lötanschlüssen für Kontaktierung
Version B (doppelshift2Bus): Kontaktierung über Flachbandkabel (6-adrig) dank Wannenstecker.


Idee für anderes Projekt: Pilzmonitor, Zeitschloss mit DC-Motor (Schrittmotor geeigneter?)
