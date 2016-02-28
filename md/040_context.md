# Kontextabgrenzung

`Kurzinfo` In welchem fachlichen und/oder technischen Umfeld arbeitet das System?

**Inhalt**
Die Kontextsicht grenzt das System, für das Sie die Architektur entwickeln, von allen Nachbarsystemen ab. Sie legt damit die wesentlichen externen Schnittstellen fest.
Stellen Sie sicher, dass die Schnittstellen mit allen relevanten Aspekten (was wird übertragen, in welchem Format wird übertragen, welches Medium wird verwendet, ...) spezifiziert wird, auch wenn einige populäre Diagramme (wie z.B. das UML Use-Case Diagramm) nur ausgewählte Aspekte der Schnittstelle darstellen.

**Motivation**
Die Schnittstellen zu Nachbarsystemen gehören zu den kritischsten Aspekten eines Projektes. Stellen Sie rechtzeitig sicher, dass Sie diese komplett verstanden haben.

**Form**
Diverse Kontextdiagramme (siehe folgende Abschnitte)
Listen von Nachbarsystemen mit deren Schnittstellen.
Die folgenden Unterkapitel zeigen die Einbettung unseres Systems in seine Umgebung.


## Fachlicher Kontext

**Inhalt**
Festlegung aller Nachbarsysteme des betrachteten Systems mit Spezifikation aller fachlichen Daten, die mit diesen ausgetauscht werden. Zusätzlich evtl. Datenformate und Protokolle der Kommunikation mit Nachbarsystemen und der Umwelt (falls diese nicht erst bei den spezifischen Bausteinen präzisiert wird.

**Motivation**
Verstehen, welche (logischen) Informationen mit Nachbarsystemen (in welcher Form) ausgetauscht werden.

**Form**
Logisches Kontextdiagramm, in der UML z.B. simuliert durch Klassendiagramme, Use Case Diagramme, Kommunikations–diagramme - kurz durch alle Diagramme, die das System als Black Box darstellen und die Schnittstellen zu den Nachbarsystemen (mehr oder weniger ausführlich) beschreiben.
Alternativ oder ergänzend können Sie einfach eine Tabelle verwenden. Der Titel gibt den Namen Ihres Systems wieder; die drei Spalten sind: Nachbarsystem, Input, Output. Auch so kommen Sie zu einer kompletten Schnittstellenbeschreibung.


![Fachlicher Kontext](./images/Fachlicher_Kontext.png)
[Quelle](https://github.com/falkoschumann/template-arc42)

## Technischer- oder Verteilungskontext

**Inhalt**
Festlegung der Kanäle zwischen Ihrem System, den Nachbarsystemen und der Umwelt;
Zusätzlich eine Mappingtabelle, welcher logische Input (aus 3.1) über welchen Kanal ein- oder ausgegeben wird.

**Motivation**
Verstehen, über welche Medien Informationen mit Nachbarsystemen bzw. der Umwelt ausgetauscht werden.

**Form**
z.B.: UML Deploymentdiagramm mit den Kanälen zu Nachbarsystemen, begleitet von einer Mappingtabelle Kanal x Input/Output.

![Technischer Kontext](./images/Technischer_Kontext.png)
[Quelle](https://github.com/falkoschumann/template-arc42)
