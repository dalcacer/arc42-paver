# Lösungsstrategie
**Inhalt.**

Kurzer Überblick über Ihre grundlegenden Entscheidungen und Lösungsansätze, die jeder, der mit der Architektur zu tun hat, verstanden haben sollte.

**Motivation.**

Dieses Kapitel motiviert übergreifend die zentralen Gestaltungskriterien für Ihre Architektur. Beschränken Sie sich hier auf das Wesentliche. Detailentscheidungen können immer noch bei den einzelnen Bausteinen oder im Kapitel 10 festgehalten werden. Das Kapitel soll Ihren Lesern die gewählte Strategie verdeutlichen.

**Form.**

Fassen Sie auf wenigen Seiten die Beweggründe für zentrale Entwurfsentscheidungen zusammen. Motivieren Sie ausgehend von Aufgabenstellung, Qualitätszielen und Randbedingungen, was Sie entschieden haben und warum Sie so entschieden haben. Verweisen Sie – wo nötig – auf weitere Ausführungen in Folgekapiteln.

## Einstiegshilfe

In diesem Kapitel beschreiben wir Stellen im Code anhand von Klassen oder Methode, an denen wichtige fachliche Funktionalität implementiert ist und/oder die im weiteren Lebenszyklus der Anwendung potenziell geändert werden.

Fall                               | Konsequenz                        | Stelle                          | Hinweise
---------------------------------- | --------------------------------- | ------------------------------- | ------------------------------
(Beispiel:) Neue Entität einführen | Ggf. neue UseCases implementieren | de.arc42.sample.ManagerCRUDImpl | ggf Factory Methoden erweitern
