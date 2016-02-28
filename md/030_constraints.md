# Randbedingungen

`(engl.: Architecture Constraints)`

**Inhalt**
Fesseln, die Software-Architekten in ihren Freiheiten bezüglich des Entwurfs oder des Entwicklungsprozesses einschränken.

**Motivation**
Architekten sollten klar wissen, wo Ihre Freiheitsgrade bezüglich Entwurfsentscheidungen liegen und wo sie Randbedingungen beachten müssen.
Randbedingungen können vielleicht noch verhandelt werden, zunächst sind sie aber da.

**Form**
Informelle Listen, gegliedert nach den Unterpunkten dieses Kapitels.

**Beispiele**
siehe Unterkapitel
Hintergründe
Im Idealfall sind Randbedingungen durch die Anforderungen vorgegeben, spätestens die Architekten müssen sich dieser Randbedingungen bewusst sein.
Den Einfluss von Randbedingungen auf Software- und Systemarchitekturen beschreibt  [Hofmeister+1999] (Softwware-Architecture, A Practical Guide, Addison-Wesley 1999) unter dem Stichwort „Global Analysis“.


## Technische Randbedingungen

**Inhalt**
Tragen Sie hier alle technischen Randbedingungen ein. Zu dieser Kategorie gehören Hard- und Software-Infrastruktur, eingesetzte Technologien (Betriebssysteme, Middleware, Datenbanken, Programmiersprachen, ...).

| Hardwarevorgaben |
|---|---|
| **Name** | **Randbedingung** |
| ... | ... |


| Softwarevorgaben |
|---|---|
| **Name** | **Randbedingung** |
| ... | ... |


| Programmiervorgaben |
|---|---|
| **Name** | **Randbedingung** |
| ... | ... |

**Beispiele**

| Randbedingung | Erläuterung |
|---|---|
| Hardware-Infrastruktur | Prozessoren, Speicher, Netzwerke, Firewalls und andere relevante Elemente der Hardware- Infrastruktur |
| Software-Infrastruktur | Betriebssysteme, Datenbanksysteme, Middleware, Kommunikationssysteme, Transaktionsmonitor, Webserver, Verzeichnisdienste |
| Systembetrieb | Batch- oder Onlinebetrieb des Systems oder notwendiger externer Systeme? |
| Verfügbarkeit der Laufzeitumgebung | Rechenzentrum mit 7x24h Betriebszeit? Gibt es Wartungs- oder Backupzeiten mit eingeschränkter Verfügbarkeit des Systems oder wichtiger Systemteile? |
| Grafische Oberfläche | Existieren Vorgaben hinsichtlich grafischer Oberfläche (Style Guide)? |
| Bibliotheken, Frameworks und Komponenten | Sollen bestimmte „Software-Fertigteile“ eingesetzt werden? |
| Programmiersprachen | Objektorientierte, strukturierte, deklarative oder Regelsprachen, kompilierte oder interpretierte
Sprachen? |
| Referenzarchitekturen | Gibt es in der Organisation vergleichbare oder übertragbare Referenzprojekte? |
| Analyse und Entwurfsmethoden | Objektorientierte oder strukturierte Methoden? |
| Datenstrukturen | Vorgaben für bestimmte Datenstrukturen, Schnittstellen zu bestehenden Datenbanken oder Dateien
 |
 | Programmierschnittstellen | Schnittstellen zu bestehenden Programmen |
 | Programmiervorgaben | Programmierkonventionen, fester Programmaufbau |
 | Technische Kommunikation | Synchron oder asynchron, Protokolle |
 | Betriebssysteme und Middleware | Vorgegebene Betriebssysteme oder Middleware |


## Organisatorische Randbedingungen

**Inhalt**
Tragen Sie hier alle organisatorischen, strukturellen und ressourcenbezogenen Randbedingungen ein. Zu dieser Kategorie gehören auch Standards, die Sie einhalten müssen und juristische Randbedingungen.

| Organisation und Struktur |
|---|---|
| **Name** | **Randbedingung** |
| ... | ... |

| Ressourcen (Budget, Zeit, Personal) |
|---|---|
| **Name** | **Randbedingung** |
| ... | ... |

| Organisatorische Standards |
|---|---|
| **Name** | **Randbedingung** |
| ... | ... |

| Juristische Faktoren |
|---|---|
| **Name** | **Randbedingung** |
| ... | ... |

**Beispiel**

| Randbedingung | Erläuterung |
|---|---|
|**Organisation und Struktur**|
| Organisationsstruktur beim Auftraggeber| Droht Änderung von Verantwortlichkeiten? Änderung von Ansprechpartnern |
| Organisationsstruktur des Projektteams| mit/ohne Unterauftragnehmer Entscheidungsbefugnis der Projektleiterin |
| Entscheidungsträger|Erfahrung mit ähnlichen Projekten Risiko-/Innovationsfreude |
| Bestehende Partnerschaften oder Kooperationen | Hat die Organisation bestehende Kooperationen mit bestimmten Softwareherstellern? Solche Partnerschaften geben oftmals Produktentscheidungen (unabhängig von Systemanforderungen) vor. |
| Eigenentwicklung oder externe Vergabe | Selbst entwickeln oder an externe Dienstleister vergeben? |
| Entwicklung als Produkt oder zur eigenen Nutzung? | Bedingt andere Prozesse bei Anforderungsanalyse und Entscheidungen. Im Fall der Produktentwicklung: Neues Produkt für neuen Markt? Verbessertes Produkt für bestehenden Markt? Vermarktung eines bestehenden (eigenen) Systems. Entwicklung ausschließlich zur eingenen Nutzung? |





## Konventionen
