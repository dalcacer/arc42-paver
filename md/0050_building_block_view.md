# Bausteinsicht
**Inhalt.**

Statische Zerlegung des Systems in Bausteine (Module, Komponenten, Subsysteme, Teilsysteme, Klassen, Interfaces, Pakete, Bibliotheken, Frameworks, Schichten, Partitionen, Tiers, Funktionen, Makros, Operationen, Datenstrukturen...) sowie deren Beziehungen.

**Motivation.**

Dies ist die wichtigste Sicht, die in jeder Architekturdokumentation vorhanden sein muss. In der Analogie zum Hausbau bildet die Bausteinsicht den _Grundrissplan_.

**Form.**

Die Bausteinsicht ist eine hierarchische Sammlung von Blackbox- und Whitebox- Beschreibungen (siehe Abbildung unten):

![Baustein Sichten](./images/arc42_bausteinsicht.png)

**Ebene 1** ist die Whitebox-Beschreibung des Gesamtsystems (System under Development / SUD) mit den Blackbox- Beschreibungen der Bausteine des Gesamtsystems

**Ebene 2** zoomt dann in einige Bausteine der Ebene 1 hinein. Sie enthält somit alle vorhandenen Whitebox-Beschreibungen von Bausteinen der Ebene 1, zusammen mit den Blackbox-Beschreibungen der Bausteine von Ebene 2.

**Ebene 3** zoomt in einige Bausteine der Ebene 2 hinein, usw.

**Whitebox-Template.**

Enthält mehrere Bausteine (== Blackboxes), zu denen Sie jeweils eine Blackbox Beschreibung erstellen können.

**Blackbox-Template (Kurzfassung).**

Für jeden Baustein aus dem White-Box-Template können Sie folgende Angaben machen: (Kopieren Sie diese Punkte in die folgenden Unterkapitel)

(eine ausführlichere Fassung des Blackbox-Templates finden Sie weiter unten.)

## Whitebox Gesamtsystem
An dieser Stelle beschreiben Sie die Whitebox-Sicht der Ebene 1 gemäß dem Whitebox-Template.

Das Überblicksbild zeigt das Innenleben des Gesamtsystems mit den darin enthaltenen Bausteinen 1 .. n, sowie deren Zusammenhänge und Abhängigkeiten.

Begründen Sie die Struktur: Warum gibt es diese Bausteine mit diesen Abhängigkeiten/Schnittstellen.

Erklären Sie ggfs. auch verworfene Alternativen, mitsamt Begründung, warum sie verworfen wurden.

### *Baustein 1* (Blackbox)
Beschreiben Sie diesen Baustein anhand des Blackbox-Templates. Nachfolgend finden Sie eine kompakte und eine ausführliche Fassung davon.

(In den folgenden Abschnitten finden Sie nur noch die Kurzfassung des Blackbox-Template)

### *Baustein 2* (Blackbox)
### *Baustein n* (Blackbox)
## Ebene 2
An dieser Stelle können Sie den inneren Aufbau (einiger) Bausteine aus Ebene 1 als Whitebox beschreiben.

### *Baustein 1* (Whitebox)
- ...zeigt das Innenleben von _Baustein 1_ in Diagrammform mit den

  lokalen Bausteinen 1.1 - 1.n, sowie deren Zusammenhänge und

  Abhängigkeiten.

- begründet diese Struktur

#### *Baustein 1.1* (Blackbox)
#### *Baustein 1.2* (Blackbox)
#### *Baustein 1.n* (Blackbox)
### *Baustein 2* (Whitebox)
- ...zeigt das Innenleben von _Baustein 2_ in Diagrammform mit den

  lokalen Bausteinen 2.1 - 2.n, sowie deren Zusammenhänge und

  Abhängigkeiten.

- begründet diese Struktur

#### *Baustein 2.1* (Blackbox)
#### *Baustein 2.2* (Blackbox)
#### *Baustein 2.n* (Blackbox)
### *Baustein 3* (Whitebox)
- ...zeigt das Innenleben von _Baustein 3_ in Diagrammform mit den

  lokalen Bausteinen 3.1 - 3.n, sowie deren Zusammenhänge und

  Abhängigkeiten.

- begründet diese Struktur

***Hier Whitebox-Erläuterung für Baustein 3 einfügen***

#### *Baustein 3.1* (Blackbox)
#### *Baustein 3.2* (Blackbox)
#### *Baustein 3.n* (Blackbox)
## Ebene 3
An dieser Stelle können Sie den inneren Aufbau (einiger) Bausteine aus Ebene 2 als Whitebox beschreiben.

Welche Bausteine Ihres Systems Sie hier beschreiben, müssen Sie selbst entscheiden. Bitte stellen Sie dabei Relevanz vor Vollständigkeit. Skizzieren Sie wichtige, überraschende, riskante, komplexe oder besonders volatile Bausteine. Normale, einfache oder standardisierte Teile sollten Sie weglassen.

### *Baustein 1.1* (Whitebox)
- ...zeigt das Innenleben von _Baustein 1.1_ in Diagrammform mit den

  lokalen Bausteinen 1.1.1 - 1.1.n, sowie deren Zusammenhänge und

  Abhängigkeiten.

- begründet diese Struktur

#### *Baustein 1.1.1* (Blackbox)
#### *Baustein 1.1.2* (Blackbox)
