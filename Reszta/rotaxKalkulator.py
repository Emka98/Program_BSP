# Słownik zawierający szczegółowe dane techniczne i cenowe silników Rotax
# Format: "Nazwa silnika": {
#     "moc_hp": wartość, 
#     "moc_kw": wartość, 
#     "masa_kg": wartość, 
#     "cena_usd": średnia cena netto w USD,
#     "zasilanie": rodzaj wtrysku/gaźnika,
#     "dolot": "Turbodoładowany" lub "Wolnossący"
# }
rotax_engines = {
    "Rotax 912 UL / A / F": {
        "moc_hp": 80.0,
        "moc_kw": 59.6,
        "masa_kg": 55.4,
        "cena_usd": 21400,
        "zasilanie": "2x Gaźnik",
        "dolot": "Wolnossący"
    },
    "Rotax 912 ULS / S": {
        "moc_hp": 100.0,
        "moc_kw": 73.5,
        "masa_kg": 56.6,
        "cena_usd": 24100,
        "zasilanie": "2x Gaźnik",
        "dolot": "Wolnossący"
    },
    "Rotax 912 iS Sport": {
        "moc_hp": 100.0,
        "moc_kw": 73.5,
        "masa_kg": 63.6,
        "cena_usd": 33300,
        "zasilanie": "Wtrysk (iFI)",
        "dolot": "Wolnossący"
    },
    "Rotax 914 UL / F": {
        "moc_hp": 115.0,
        "moc_kw": 84.5,
        "masa_kg": 64.0,
        "cena_usd": 37500,
        "zasilanie": "2x Gaźnik",
        "dolot": "Turbodoładowany"
    },
    "Rotax 915 iS A / iSc A": {
        "moc_hp": 141.0,
        "moc_kw": 105.0,
        "masa_kg": 84.0,
        "cena_usd": 49300,
        "zasilanie": "Wtrysk (iFI)",
        "dolot": "Turbodoładowany"
    },
    "Rotax 916 iS A / iSc A": {
        "moc_hp": 160.0,
        "moc_kw": 117.0,
        "masa_kg": 85.8,
        "cena_usd": 61050,
        "zasilanie": "Wtrysk (iFI)",
        "dolot": "Turbodoładowany"
    }
}

def oblicz_parametry(silniki):
    wyniki = []
    
    for nazwa, dane in silniki.items():
        moc_hp = dane["moc_hp"]
        moc_kw = dane["moc_kw"]
        masa = dane["masa_kg"]
        cena = dane["cena_usd"]
        
        # Obliczenia stosunku mocy do masy oraz ceny do mocy
        hp_na_kg = moc_hp / masa
        kw_na_kg = moc_kw / masa
        usd_na_hp = cena / moc_hp  # Koszt jednego konia mechanicznego
        
        wyniki.append({
            "nazwa": nazwa,
            "moc_hp": moc_hp,
            "moc_kw": moc_kw,
            "masa_kg": masa,
            "cena_usd": cena,
            "zasilanie": dane["zasilanie"],
            "dolot": dane["dolot"],
            "hp_na_kg": hp_na_kg,
            "kw_na_kg": kw_na_kg,
            "usd_na_hp": usd_na_hp
        })
        
    # Sortowanie od najlepszego stosunku mocy do masy (HP/kg)
    return sorted(wyniki, key=lambda x: x["hp_na_kg"], reverse=True)

def wyswietl_analize(wyniki, kurs_usd_pln=4.0):
    szerokosc_linii = 143
    print("=" * szerokosc_linii)
    print(
        f"{'Model silnika':<24} | "
        f"{'Masa':<8} | "
        f"{'Moc (HP)':<8} | "
        f"{'Zasilanie':<13} | "
        f"{'Dolot':<16} | "
        f"{'HP/kg':<8} | "
        f"{'Cena (USD)':<11} | "
        f"{'Cena (PLN)*':<12} | "
        f"{'USD / 1 HP':<10}"
    )
    print("=" * szerokosc_linii)
    
    for s in wyniki:
        cena_pln = s['cena_usd'] * kurs_usd_pln
        print(
            f"{s['nazwa']:<24} | "
            f"{s['masa_kg']:>5.1f} kg | "
            f"{s['moc_hp']:>8.1f} | "
            f"{s['zasilanie']:<13} | "
            f"{s['dolot']:<16} | "
            f"{s['hp_na_kg']:>8.4f} | "
            f"${s['cena_usd']:>9,d} | "
            f"{cena_pln:>9,.0f} zł | "
            f"${s['usd_na_hp']:>8.2f}"
        )
    print("=" * szerokosc_linii)
    print(f"* Szacunkowa cena w PLN obliczona przy założeniu kursu 1 USD = {kurs_usd_pln:.2f} PLN (netto, bez VAT).")
    print("=" * szerokosc_linii)

if __name__ == "__main__":
    print("\nKOMPLEKSOWA ANALIZA PARAMETRÓW I CEN SILNIKÓW ROTAX\n")
    dane_obliczone = oblicz_parametry(rotax_engines)
    # Możesz zmienić domyślny kurs USD/PLN, wpisując np. wyswietl_analize(dane_obliczone, 4.10)
    wyswietl_analize(dane_obliczone)