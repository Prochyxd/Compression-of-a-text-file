# Compression-of-a-text-file
A program to compress a text file with a .txt extension that takes any text file with natural language text as input and converts it to another file with a provably smaller size.


# Podmínky
- [x] Vstupem programu je jeden textový soubor.
- [x] Výstupem programu je jeden nebo více souborů.
- [ ] Text po všech úpravách musí být čitelný člověkem a jeho význam musí být zachován i po změně nebo odstranění a nahrazení slov. Tedy text se může změnit, například odstraněním nepotřebných slov a nic neříkajících vět, ale nesmí to ovlivnit to, co je v textu zásadní.
- [ ] Program musí být konfigurovatelný například, jaký soubor má načítat, kam má uložit výsledek a jak ho má pojmenovat.
- [ ] Program musí informaci o každé úpravě textu vytvořit záznam v logu, kde bude informace o tom, v jaké konfiguraci se program nacházel, co kdy zpracoval, a zda-li a jak dobře se povedlo komprimovat nebo dekomprimovat, nebo zda-li nastala chyba.
- [ ] Program musí umět vypsat informace o svých operacích z logu a musí je umožnit filtrovat podle zadaného času a dalších parametrů, které zvolíte.
- [ ] Program musí umět poskytnout uživateli nápovědu o tom, jak se používá.
- [ ] Program nesmí používat žádnou externí knihovnu pro komprese nebo dekomprese.
- [ ] Program se musí umět vypořádat s chybami typu, že soubor nelze číst kvůli oprávnění, že soubor není textový apod. O každé chybě musí být záznam v logu a také se musí uživateli zobrazit vhodná chybová hláška.
- [ ] Program musí obsahovat unit testy s ukázkami jednotlivých funkcí.
- [ ] Program musí být rozdělen do více souborů a složek pro jednotlivé části. Logy by měly být ve složce /log, konfigurace ve složce /config, data a soubory ve složce /data, zdrojový kód pak musí být rozdělen do dalších package/modulů ve složce /src (uživatelské rozhraní zvlášť, algoritmy pro kompresi zvlášť, práce s logem zvlášť). Dokumentace ve složce /doc a unit testy ve složce /test. Pokud použijete cizí zdrojový kód, musí být také ve zvláštní složce, například /lib nebo /vendor.
- [ ] Program může kromě komprimovaného souboru generovat i pomocné soubory, například s kódovací tabulkou, seznam zkratek apod.
