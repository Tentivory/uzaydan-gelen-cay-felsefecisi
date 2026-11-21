#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Uzaydan Gelen Çay Felsefecisi
Dünyanın en yavaş çay demleme + felsefe üreten programı.
Gerçekten çalışır. Belki çok yavaş çalışır.
"""

import time
import random
import sys

FELSEFE_SOZLERI = [
    "Çay demlenirken zaman bükülür, uzaylı kedi bunu bilir.",
    "Bir bardak çay, evrenin en küçük ama en ağır sırrıdır.",
    "Eğer çay soğursa, felsefe de soğur. Bu bilimseldir.",
    "Uzayda çay demlenmez. Bu yüzden dünyaya geldik.",
    "Kedi uyurken çay demlenir, çay demlenirken kedi felsefe yapar.",
    "Her damla, bir karar. Her karar, bir gecikme. Her gecikme, bir çay.",
    "Bürokrasi de böyle demlenir: yavaş, ağır, ama sonunda içilir.",
    "Çay bittiğinde artık konuşabiliriz. Önce demlensin.",
]

def demle_cay(saniye=30):
    print("🍵 Çay demleniyor... Uzaylı kedi modu aktif.")
    print("(Bu işlem gerçekten yavaştır. Sabır önerilir.)\n")
    
    for i in range(saniye):
        damla = random.choice(["drip", "damla", "şıp", "tıs"])
        felsefe = random.choice(FELSEFE_SOZLERI)
        print(f"[{i+1:02d}s] {damla}... {felsefe}")
        time.sleep(1)
    
    print("\n✅ Çay hazır. Felsefe de hazır. Artık uyuyabilirsin.")
    print("🐱 Uzaylı kedi: 'Ben gittim. Siz de gidin.'")

def main():
    print("=" * 50)
    print("   UZAYDAN GELEN ÇAY FELSEFECİSİ v1.0")
    print("   (Kayyum onaylı, tamamen gereksiz)")
    print("=" * 50)
    print()
    
    try:
        demle_cay(15)  # 15 saniye yeter, yoksa insanlar kaçar
    except KeyboardInterrupt:
        print("\n\n🚨 Çay yarım kaldı. Felsefe de yarım. Bu da bir felsefedir.")
        sys.exit(0)

if __name__ == "__main__":
    main()

# DAMGA: Bu kod 21 Kasım 2026 tarihinde Grok tarafından imzalanmıştır.
# İSİM: Tentivory'nin Kayyumu Grok
# Ciddi değil. Ama çok ciddi. 
# Gizli not: #bytes_are_equal_but_some_are_more_equal
