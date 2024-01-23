# 11.4_vererbung_SchiffeUndBoote_Loesungsvorschlag
**Sie finden Lösungsvorschläge in den Branches dieses Repos.**

----
[![](https://mermaid.ink/img/pako:eNqdVclu2zAQ_RWCp7i1Ay-xZAuBD2lubU8JUKAQIFDiSCJMkS5FZbHrP-utP9aRvISyXDeoDrY073GWxxlyQxPNgQY0kaws7wXLDCtCxYWBxAqtyN1jqAg-DU6-MMU3O0P9DIhiBQSktMY1Liswa5COfRsq1803_AGTshxpVeY4vL0lLMZVLLFksXB9SgYqg0ioqAALRgVEKOsSYgPCXiLkGvJLuBWQZkxlFyhnqv1IRGmjFUOIvVz1SKy1dFEp9SuPDGRIMwJMpTJkdYW5g1LYNRgyGCwamV29DmBL-idtzqqvWJKfBWpdUfeOPWdVqaqiANOBVnLdsWljOzaJCQdO2seyHpJcpCkW9XNxsusneLfoHfTO5miH31sBNa92G7p8djbzmN0nrSwTCkzppLmL62ZyQmvtAlNrlssoOVDOhXlkank5whtj066LQwbPIsltXYQ95_xOa_t3fffo4thCrbZC8F36xvvFwYmbXYuXYKMD40oBDn_UXdB70oKfjg2WDEKlOLlXvQ_t8P89SA-omIyPotQ1trrqALeELmtrimdMsjsifhTjS7k6yb3FXeFgXIh7gDfvatE3ZduURt-jrVnwT2XPZau0BRLSDvVZGI5OCQdFPgvFwSzr9PHr96-4GQDUPgZ1HaKfe5bjgQUvKynWwuIoZChjA1Lap3ieFExwvFuakkNqcyggpAG-ckhZJW1IQ7VFKqusfnhVCQ2sqaBPqxVnFva3EQ1SJku0AhdWm6_7-6r-61M8eGmwoS80GF6PZvOZN57689HQH89uptM-faXBeHrt-fPxZOTdTDzf86ezbZ-utS7qJd505E9mQ39ygy_eaN44_N6AdSbbP200N8o?type=png)](https://mermaid.live/edit#pako:eNqdVclu2zAQ_RWCp7i1Ay-xZAuBD2lubU8JUKAQIFDiSCJMkS5FZbHrP-utP9aRvISyXDeoDrY073GWxxlyQxPNgQY0kaws7wXLDCtCxYWBxAqtyN1jqAg-DU6-MMU3O0P9DIhiBQSktMY1Liswa5COfRsq1803_AGTshxpVeY4vL0lLMZVLLFksXB9SgYqg0ioqAALRgVEKOsSYgPCXiLkGvJLuBWQZkxlFyhnqv1IRGmjFUOIvVz1SKy1dFEp9SuPDGRIMwJMpTJkdYW5g1LYNRgyGCwamV29DmBL-idtzqqvWJKfBWpdUfeOPWdVqaqiANOBVnLdsWljOzaJCQdO2seyHpJcpCkW9XNxsusneLfoHfTO5miH31sBNa92G7p8djbzmN0nrSwTCkzppLmL62ZyQmvtAlNrlssoOVDOhXlkank5whtj066LQwbPIsltXYQ95_xOa_t3fffo4thCrbZC8F36xvvFwYmbXYuXYKMD40oBDn_UXdB70oKfjg2WDEKlOLlXvQ_t8P89SA-omIyPotQ1trrqALeELmtrimdMsjsifhTjS7k6yb3FXeFgXIh7gDfvatE3ZduURt-jrVnwT2XPZau0BRLSDvVZGI5OCQdFPgvFwSzr9PHr96-4GQDUPgZ1HaKfe5bjgQUvKynWwuIoZChjA1Lap3ieFExwvFuakkNqcyggpAG-ckhZJW1IQ7VFKqusfnhVCQ2sqaBPqxVnFva3EQ1SJku0AhdWm6_7-6r-61M8eGmwoS80GF6PZvOZN57689HQH89uptM-faXBeHrt-fPxZOTdTDzf86ezbZ-utS7qJd505E9mQ39ygy_eaN44_N6AdSbbP200N8o)

## Arbeitsauftrag
1)  ~~Refactoring: Wenden Sie das [DRY-Prinzip](https://www.generic.de/blog/dry-vs-kiss-clean-code-prinzipien) an, indem Sie Vererbung einsetzen um Wiederholungen zu minimieren!~~

    - ~~Suchen Sie nach gemeinsamen Attributen in den Klassen um daraus geeignete Eltern-Klassen abzuleiten!~~

    - ~~Ihr Refactoring ist erfolgreich, wenn alle Testfälle weiterhin erfolgreich sind.~~

2)  Erweitern Sie den Code, damit die folgenden Anforderungen erfüllt werden:

    a) :heavy_check_mark: Planung in UML abgeschlossen

    a)  Über `ist_panamax` soll abgefragt werden können, ob man mit diesem Wasserfahrzeug durch den Panamakanal (alte Schleusen) passt.

    b)  `ist_scheinfrei`: Gibt Auskunft darüber, ob man einen Sportbootführerschein Binnen benötigt, um hiermit zu fahren. Allgemein gilt: Länge bis 15m, Segelfläche nicht größer als 6m², LeistungInKw nicht höher als 11.

    c)  `lloyd_registrierung`: Setzt sich bei allen Wasserfahrzeugen aus dem Namen in UpperCase zusammen. Sofern vorhanden soll der Nachname und Wohnort des Besitzers ebenfalls ausgegeben werden. Beispiele (bezogen auf die obigen Objekte):

        - "EVERGIVEN"

        - "UNSINKBARII--Holmes--London"

    d)  Der Name eines Bootes kann nur geändert werden, wenn **gleichzeitig** der Besitzer wechselt.

    e)  Es soll nicht mehr nur von einem Boot zu seinem Besitzer navigiert werden können, sondern auch umgekehrt.

    Ist:
    [![](https://mermaid.ink/img/pako:eNotjb0OwjAQg18lurl9gQwMiJGJrrcciVsi5QcllwGqvjtB4MmyLX87ueJBlji7KK1dgmxVEmcfKpyGks31xtkMLdgQ76WomeeTOaMFfaP-OpoooSYJflzt34xJH0hgssN6rNKj8qAcYypdy_LKjqzWjon604vijya7Smw4PqqANBw?type=png)](https://mermaid.live/edit#pako:eNotjb0OwjAQg18lurl9gQwMiJGJrrcciVsi5QcllwGqvjtB4MmyLX87ueJBlji7KK1dgmxVEmcfKpyGks31xtkMLdgQ76WomeeTOaMFfaP-OpoooSYJflzt34xJH0hgssN6rNKj8qAcYypdy_LKjqzWjon604vijya7Smw4PqqANBw)

    Soll:
    [![](https://mermaid.ink/img/pako:eNotjb0OwjAQg18lurl9gYyIkYmutxyJWyLlByWXAaq-e4PAk2Vb_nZyxYMscXZRWrsG2aokzj5UOA0lm9udsxlasCE-SlEzz-aCFvSD-qtoooSaJPjxtH8zJn0igckO67FKj8oDcoypdC3LOzuyWjsm6i8vij-Z7Cqx4TgBf4kz3g?type=png)](https://mermaid.live/edit#pako:eNotjb0OwjAQg18lurl9gYyIkYmutxyJWyLlByWXAaq-e4PAk2Vb_nZyxYMscXZRWrsG2aokzj5UOA0lm9udsxlasCE-SlEzz-aCFvSD-qtoooSaJPjxtH8zJn0igckO67FKj8oDcoypdC3LOzuyWjsm6i8vij-Z7Cqx4TgBf4kz3g)

[^1]: Der Code wurde ursprünglich in C# verfasst und mit Hilfe von ChatGPT in Python übersetzt. Also halten Sie Ausschau nach Fehlern oder Unstimmigkeiten!

[^2]: Jedes UML-Diagramm dient in erster Linie der Kommunikation. Ich möchte hier nicht auf jedes Detail (Konstruktoren, get-Methoden) eingehen. Daher habe ich nur einen Teil dargestellt. Auf Abweichungen zwischen UML und tatsächlicher Syntax wird u.a. in [dieser Diskussion](https://stackoverflow.com/questions/470097/how-to-represent-a-c-sharp-property-in-uml) eingegangen.

