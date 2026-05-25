# 🚀 Roboline – Suorituskyvyn & Core Web Vitals -optimointisuunnitelma

Tämä asiakirja toimii valmiina muistiona ja teknisenä toteutussuunnitelmana seuraavaa kehitysvaihetta varten. Tavoitteena on saavuttaa täydelliset **100/100 mobiilipisteet Lighthouse-testissä** poistamalla renderöintiä estävät pyynnöt ja optimoimalla kuvien toimitus.

---

## 📋 Suorituskykyvelka (Performance Backlog)

| Prioriteetti | Tehtävä | Vaikutus (Lighthouse) | Tavoite |
| :--- | :--- | :--- | :--- |
| **KORKEA** | Korvaa Tailwind Play CDN staattisella build-prosessilla | **+ 2 480 ms säästö** (LCP / FCP) | Poistaa `cdn.tailwindcss.com` -skriptin |
| **KESKITALO** | Optimoikuvaformaatit ja lisäresoluutiot (WebP/AVIF) | **+ 864 KiB tiedostokoon säästö** | Parantaa kaistan käyttöä ja CLS-arvoja |
| **KORKEA/KESKI** | Optimoi Google Fonts -lataukset (`font-display: swap`) | **+ 780 ms säästö** (FCP) | Poistaa fonttien estovaikutuksen |

---

## 🛠️ Vaiheittainen toteutussuunnitelma

### Vaihe 1: Tailwind CSS:n asennus ja integrointi Viteen
Poistetaan selaimessa tapahtuva dynaaminen kääntäminen ja korvataan se staattisella build-prosessilla.

1. **Asenna Tailwind ja PostCSS riippuvuudet:**
   ```bash
   npm install -D tailwindcss postcss autoprefixer
   ```
2. **Luo Tailwind-konfiguraatio (`tailwind.config.js`):**
   ```javascript
   /** @type {import('tailwindcss').Config} */
   export default {
     content: [
       "./index.html",
       "./innovaatiot.html",
       "./ymmarryksentie.html",
       "./src/**/*.{js,ts,jsx,tsx}",
     ],
     theme: {
       extend: {
         colors: {
           brand: {
             dark: '#0f0a29',
             primary: '#1d4ed8', // robosaw-korostukset ja linkit
           }
         }
       },
     },
     plugins: [],
   }
   ```
3. **Luo `postcss.config.js`:**
   ```javascript
   export default {
     plugins: {
       tailwindcss: {},
       autoprefixer: {},
     },
   }
   ```
4. **Luo CSS-sisääntulotiedosto (`style.css`):**
   ```css
   @tailwind base;
   @tailwind components;
   @tailwind utilities;
   
   /* Mahdolliset mukautetut tyylit tähän */
   ```
5. **Päivitä HTML-sivut (`index.html`, `innovaatiot.html`, `ymmarryksentie.html`):**
   * Poista: `<script src="https://cdn.tailwindcss.com"></script>`
   * Varmista, että linkitys osoittaa paikalliseen css-tiedostoon: `<link rel="stylesheet" href="./style.css">`

---

### Vaihe 2: Google Fonts -latauksen optimointi
Vähennetään fonttien latauksen viivettä.

1. **Lisää `preconnect`-vihjeet HTML-tiedostojen `<head>`-osaan:**
   ```html
   <link rel="preconnect" href="https://fonts.googleapis.com">
   <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
   ```
2. **Käytä `font-display: swap` -parametria linkissä:**
   ```html
   <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;900&display=swap" rel="stylesheet">
   ```

---

### Vaihe 3: Kuvien modernisointi (AVIF/WebP) ja CLS-hallinta
Varmistetaan, että selain tietää kuvien koot etukäteen ja tiedostokoot ovat mahdollisimman pieniä.

1. **Muunnetaan PNG/JPG-kuvat AVIF/WebP-muotoon:**
   * Käytetään komentorivin työkaluja tai projektin `process_images.sh`-skriptiä.
2. **Lisätään kuville selkeät mitat:**
   * Määritetään `width` ja `height` -attribuutit kaikille kuville, jotta layout ei siirry (Cumulative Layout Shift, CLS = 0).
