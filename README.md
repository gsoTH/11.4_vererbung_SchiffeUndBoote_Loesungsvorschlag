# 11.4_vererbung_SchiffeUndBoote_Loesungsvorschlag
**Sie finden Lösungsvorschläge in den Branches dieses Repos.**

----
[![](https://mermaid.ink/img/pako:eNqNVE2P2jAQ_SuRT60KCJZ8QLTisO2hh1aqtCtVqiJFQzJJLBKbOhO2C-W_1wmQdRJE8YGgN89v5s3YPrBIxsh8FuVQll84pAqKQMRcYURcCuvpJRCWXk3c-gYiPpyAeo0tAQX6VknKBDcVqj3mBn4MhCnzU_-gSiDTtCo1BB8fLVjrXRCRtVqZmjmgSDHkIiyQUAnf4oJMwlohp1uETGJ2K04ckxREeoPSc9u6esKS0x6VNR6vmh6ZZi_BTt92Ul1tnYAouxqom6KbNsAzqEpRFQWqQWib7weYVDTAcl2wb5Td2vqqIczLMsp4kmhvf1e9yV2nDVvQYdw57m5NZxR5SdVpRJtXYzxtyZ-lIOAClVl0J71ZV4_dmRCIPWR5GF0o17K9gNjcleideOi6jDHFVx5lVFuibo7680PxHdD_JtBjrdozZ9Zgku6awfos4vfk6vXJKpHCC-ODQH3lw-GGjzvJ-6fqWVvO11LSyY9ZllluS-t0rKzRRD8G0eku_y4e-vJbfcbvkL_QDncdsHfPXUrjvMWaDaZnNmL6ZhbAY_3ENpkCRhkWGDBf_40xgSqngAWipkJF8vlNRMwnVeGIVdsYCM-P8gXEmJNU38-vdv0ZsS0I5h_YH-aP7Ym98Gb2fDpfetP53F2O2Bvz3elktpzazoPjOe5i7izt44jtpdSq08nSW8wc23Nd11nMXMdr9H41wTrl8R8nzOwf?type=png)](https://mermaid.live/edit#pako:eNqNVE2P2jAQ_SuRT60KCJZ8QLTisO2hh1aqtCtVqiJFQzJJLBKbOhO2C-W_1wmQdRJE8YGgN89v5s3YPrBIxsh8FuVQll84pAqKQMRcYURcCuvpJRCWXk3c-gYiPpyAeo0tAQX6VknKBDcVqj3mBn4MhCnzU_-gSiDTtCo1BB8fLVjrXRCRtVqZmjmgSDHkIiyQUAnf4oJMwlohp1uETGJ2K04ckxREeoPSc9u6esKS0x6VNR6vmh6ZZi_BTt92Ul1tnYAouxqom6KbNsAzqEpRFQWqQWib7weYVDTAcl2wb5Td2vqqIczLMsp4kmhvf1e9yV2nDVvQYdw57m5NZxR5SdVpRJtXYzxtyZ-lIOAClVl0J71ZV4_dmRCIPWR5GF0o17K9gNjcleideOi6jDHFVx5lVFuibo7680PxHdD_JtBjrdozZ9Zgku6awfos4vfk6vXJKpHCC-ODQH3lw-GGjzvJ-6fqWVvO11LSyY9ZllluS-t0rKzRRD8G0eku_y4e-vJbfcbvkL_QDncdsHfPXUrjvMWaDaZnNmL6ZhbAY_3ENpkCRhkWGDBf_40xgSqngAWipkJF8vlNRMwnVeGIVdsYCM-P8gXEmJNU38-vdv0ZsS0I5h_YH-aP7Ym98Gb2fDpfetP53F2O2Bvz3elktpzazoPjOe5i7izt44jtpdSq08nSW8wc23Nd11nMXMdr9H41wTrl8R8nzOwf)

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

