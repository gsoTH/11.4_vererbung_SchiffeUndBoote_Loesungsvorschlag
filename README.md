# 11.4_vererbung_SchiffeUndBoote_Loesungsvorschlag
**Sie finden Lösungsvorschläge in den Branches dieses Repos.**

----
[![](https://mermaid.ink/img/pako:eNqNVN-PmkAQ_lfIPrWpGkSUg1x8uPaxfbpLmjQkZoUBNsKsXYa7ntb_vQsKt4A17oOS75tf38zsHlkkY2ABi3Jelt8ETxUvQoyFgoiEROvpJURLn4a3vnOMj2egPlMLeQGBVZIywV0F6gC5gZ9CNMP81D-gEp5psyo1Aj4-WnyrvXhE1nptxsw5YAobgZsCCBQGlkAyDbYKBN0yyCRkt3gSkKQc0xsmA7WdqicoBR1AWdPpuumRKbYle317lepq65BH2VWibopu2gjPeFViVRSgRtQ-P4wwqWiE5brgwCi7k_UcZSJJtKi_68HIBvxY9Jm6c7L99BcUREnVeRq7N2MSXXVfJRIXCKo0yjznNSsZmPWmwPHAs3wTtSbX0rxw3N3O8GFx7OuKIYU3EWVUi6B-8GZtpKT_d_fCrrsF6i2VJu_q7vbiHAzC1OeLVQJtWotPCPrebsYOn1-lGK2GlpZvu_rrcnrjb-leR8oaTfRNjs4X8XfhDMPu9YLeCNvSx7tW5UNj36RR2mGNg6mRTZi-TgUXsX4Xm0whowwKCFmgP2NIeJVTyEKsTXlF8vkdIxaQqmDCqn3MCS4vaQtCLEiqH5entv6bsD1HFhzZHxbMvdmDs_QXC3e5ch3bn7D3GlzO5r7ruZ7vuA-2650m7CClDmnPPHu1sH1_7nuOY68crwn2qyHrfKd_Ew_Mdg?type=png)](https://mermaid.live/edit#pako:eNqNVN-PmkAQ_lfIPrWpGkSUg1x8uPaxfbpLmjQkZoUBNsKsXYa7ntb_vQsKt4A17oOS75tf38zsHlkkY2ABi3Jelt8ETxUvQoyFgoiEROvpJURLn4a3vnOMj2egPlMLeQGBVZIywV0F6gC5gZ9CNMP81D-gEp5psyo1Aj4-WnyrvXhE1nptxsw5YAobgZsCCBQGlkAyDbYKBN0yyCRkt3gSkKQc0xsmA7WdqicoBR1AWdPpuumRKbYle317lepq65BH2VWibopu2gjPeFViVRSgRtQ-P4wwqWiE5brgwCi7k_UcZSJJtKi_68HIBvxY9Jm6c7L99BcUREnVeRq7N2MSXXVfJRIXCKo0yjznNSsZmPWmwPHAs3wTtSbX0rxw3N3O8GFx7OuKIYU3EWVUi6B-8GZtpKT_d_fCrrsF6i2VJu_q7vbiHAzC1OeLVQJtWotPCPrebsYOn1-lGK2GlpZvu_rrcnrjb-leR8oaTfRNjs4X8XfhDMPu9YLeCNvSx7tW5UNj36RR2mGNg6mRTZi-TgUXsX4Xm0whowwKCFmgP2NIeJVTyEKsTXlF8vkdIxaQqmDCqn3MCS4vaQtCLEiqH5entv6bsD1HFhzZHxbMvdmDs_QXC3e5ch3bn7D3GlzO5r7ruZ7vuA-2650m7CClDmnPPHu1sH1_7nuOY68crwn2qyHrfKd_Ew_Mdg)

## Arbeitsauftrag
1)  :heavy_check_mark: ~~Refactoring: Wenden Sie das [DRY-Prinzip](https://www.generic.de/blog/dry-vs-kiss-clean-code-prinzipien) an, indem Sie Vererbung einsetzen um Wiederholungen zu minimieren!~~

    - ~~Suchen Sie nach gemeinsamen Attributen in den Klassen um daraus geeignete Eltern-Klassen abzuleiten!~~

    - ~~Ihr Refactoring ist erfolgreich, wenn alle Testfälle weiterhin erfolgreich sind.~~

2)  Erweitern Sie den Code, damit die folgenden Anforderungen erfüllt werden:

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

