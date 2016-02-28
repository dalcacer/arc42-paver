# Verteilungssicht
Deployment: Auf welcher Hardware werden die Bausteine betrieben?

**Inhalt** Diese Sicht beschreibt, in welcher Umgebung das System abläuft. Sie beschreiben die geographische Verteilung Ihres Systems oder die Struktur der Hardwarekomponenten, auf denen die Software abläuft. Sie dokumentiert Rechner, Prozessoren, Netztopologien und Kanäle, sowie sonstige Bestandteile der physischen Systemumgebung. Die Verteilungssicht zeigt das System aus Betreibersicht. Zeigen Sie in dieser Sicht auch, wie die Bausteine des Systems zu Verteilungsartefakten zusammengefasst oder –gebaut werden (engl. deployment artifacts oder deployment units).

**Motivation** Software ohne Hardware tut wenig. Das Minimum, was Sie als Software-Architekt daher brauchen, sind so viele Angaben zu der zugrunde liegenden (Hardware- )Verteilung, dass Sie jeden Software-Baustein, der für den Betrieb interessant ist, irgendwelchen Hardware-Einheiten zuordnen können. (Das gilt auch für Standardsoftware, die Voraussetzung für das Funktionieren des Gesamtsystems ist). Sie sollen mit diesen Modellen die Betreiber in die Lage versetzen, die Software auch komplett und richtig zu installieren.

**Form** Die UML stellt mit Verteilungsdiagrammen (Deployment diagrams) eine Diagrammart zur Verfügung, um diese Sicht auszudrücken. Nutzen Sie diese, evtl. auch geschachtelt, wenn Ihre Verteilungsstruktur es verlangt. (Das oberste Deployment- Diagramm sollte bereits in Ihrer Kontextsicht enthalten sein mit Ihrer Infrastruktur als EINE Black-Box. Jetzt zoomen Sie in diese Infrastruktur mit weiteren Deployment- Diagrammen hinein. Andere Diagramme Ihrer Hardware-Kollegen, die Prozessoren und Kanäle darstellen sind hier ebenfalls einsetzbar. Abstrahieren Sie aber auf die Aspekte, die für die Software-Verteilung relevant sind.

## Infrastruktur Ebene 1

![Infrastruktur Ebene](./images/Infrastruktur_Ebene_1.png) [Quelle](https://github.com/falkoschumann/template-arc42)

### Verteilungsdiagramm 1
- zeigt das Verteilung des Gesamtsystems auf 1 - n Prozessoren (oder Standorte) sowie die physischen Verbindungskanäle zwischen diesen.
- beschreibt wichtige Begründungen, die zu dieser Verteilungsstruktur, d.h. zur Auswahl der Knoten und zhur Auswahl der Kanäle führten
- verweist evtl. auf verworfene Alternativen (mit der Begründung, warum es verworfen wurden
