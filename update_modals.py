import os
import re

html_files = [
    '/Users/eskomaki/Antigravity/VerkkoSivut/Roboline/index.html',
    '/Users/eskomaki/Antigravity/VerkkoSivut/Roboline/innovaatiot.html',
    '/Users/eskomaki/Antigravity/VerkkoSivut/Roboline/ymmarryksentie.html'
]

modal_html = """
  <!-- Privacy Policy Modal -->
  <div id="privacy-modal" class="fixed inset-0 z-[100] flex items-center justify-center hidden opacity-0 transition-opacity duration-300 p-4">
    <div class="absolute inset-0 bg-brand-dark/60 backdrop-blur-sm" onclick="closeLegalModal('privacy-modal')"></div>
    <div class="bg-white rounded-[2rem] p-6 sm:p-10 max-w-3xl w-full max-h-[85vh] relative z-10 shadow-[0_20px_60px_-15px_rgba(0,0,0,0.5)] border border-gray-100 transform scale-95 transition-transform duration-300 flex flex-col" id="privacy-modal-content">
      <div class="flex justify-between items-center mb-6 shrink-0">
        <h3 class="text-2xl sm:text-3xl font-black text-brand-dark uppercase tracking-tight font-display">Tietosuojaseloste</h3>
        <button onclick="closeLegalModal('privacy-modal')" class="w-10 h-10 bg-gray-100 hover:bg-brand-primary text-gray-600 hover:text-white rounded-full flex items-center justify-center transition-all shrink-0">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M6 18L18 6M6 6l12 12"></path></svg>
        </button>
      </div>
      <div class="overflow-y-auto pr-4 text-gray-600 text-[0.95rem] space-y-6 leading-relaxed">
        <p class="font-medium">Tämä tietosuojaseloste kuvaa, miten keräämme, käsittelemme ja suojaamme asiakkaidemme sekä verkkosivustomme käyttäjien henkilötietoja EU:n yleisen tietosuoja-asetuksen (GDPR) mukaisesti.</p>
        
        <div>
          <h4 class="text-lg font-bold text-gray-800 mb-2">1. REKISTERINPITÄJÄ</h4>
          <ul class="list-disc pl-5 space-y-1">
            <li><strong>Nimi:</strong> Roboline Group Oy</li>
            <li><strong>Y-tunnus:</strong> [Y-tunnus]</li>
            <li><strong>Osoite:</strong> [Osoite]</li>
            <li><strong>Verkkosivusto:</strong> www.roboline.fi</li>
          </ul>
        </div>

        <div>
          <h4 class="text-lg font-bold text-gray-800 mb-2">2. YHTEYSHENKILÖ TIETOSUOJA-ASIOISSA</h4>
          <ul class="list-disc pl-5 space-y-1">
            <li><strong>Sähköposti:</strong> [sähköposti]</li>
            <li><strong>Puhelin:</strong> [numero]</li>
          </ul>
        </div>

        <div>
          <h4 class="text-lg font-bold text-gray-800 mb-2">3. REKISTERIN NIMI</h4>
          <p>Yrityksen asiakas-, sopimus- ja markkinointirekisteri.</p>
        </div>

        <div>
          <h4 class="text-lg font-bold text-gray-800 mb-2">4. HENKILÖTIETOJEN KÄSITTELYN TARKOITUS JA OIKEUSPERUSTE</h4>
          <p class="mb-2">Käsittelemme henkilötietoja seuraaviin tarkoituksiin:</p>
          <ul class="list-disc pl-5 space-y-1 mb-2">
            <li><strong>Asiakassuhteen hoitaminen:</strong> Yhteydenottopyyntöihin vastaaminen, tarjousten tekeminen, tilausten toimitus ja asiakaspalvelu.</li>
            <li><strong>Taloushallinto:</strong> Laskutus, maksujen valvonta ja perintä.</li>
            <li><strong>Liiketoiminnan kehittäminen ja markkinointi:</strong> Palveluidemme laadun parantaminen sekä uutisryhmä- ja markkinointiviestintä (suoramyynti).</li>
          </ul>
          <p class="mb-2 font-medium">Käsittelyn oikeusperusteet:</p>
          <ul class="list-disc pl-5 space-y-1">
            <li><strong>Sopimus:</strong> Käsittely on tarpeen sopimuksen täytäntöönpanemiseksi tai tarjouksen tekemiseksi.</li>
            <li><strong>Lakisääteinen velvoite:</strong> Esimerkiksi kirjanpitolainsäädännön vaatimukset.</li>
            <li><strong>Oikeutettu etu:</strong> Asiakassuhteen hoitaminen, analysointi ja suoramarkkinointi.</li>
            <li><strong>Suostumus:</strong> Mikäli asiakas on erikseen antanut suostumuksensa (esim. uutiskirje).</li>
          </ul>
        </div>

        <div>
          <h4 class="text-lg font-bold text-gray-800 mb-2">5. REKISTERIN TIETOSISÄLTÖ</h4>
          <p class="mb-2">Rekisteriin voidaan tallentaa seuraavia tarpeellisia tietoja:</p>
          <ul class="list-disc pl-5 space-y-1">
            <li><strong>Perustiedot:</strong> Esimerkiksi nimi, puhelinnumero, sähköpostiosoite ja postiosoite.</li>
            <li><strong>Yritysasiakkaat:</strong> Yrityksen nimi, Y-tunnus ja yhteyshenkilön tiedot.</li>
            <li><strong>Asiakkuuteen liittyvät tiedot:</strong> Tilaus- ja laskutustiedot, sopimukset, asiakaspalveluhistoria sekä annetut suostumukset ja kiellot.</li>
            <li><strong>Huomautus:</strong> Mikäli kuluttaja-asiakkaan kanssa tehdään laajempi työtilaus, voidaan tarvittaessa kerätä henkilötunnus laskutusta tai viranomaisilmoituksia (kuten kotitalousvähennystä) varten.</li>
          </ul>
        </div>

        <div>
          <h4 class="text-lg font-bold text-gray-800 mb-2">6. SÄÄNNÖNMUKAISET TIETOLÄHTEET</h4>
          <p>Tietoja kerätään ensisijaisesti suoraan rekisteröidyltä itseltään verkkosivuston lomakkeiden, sähköpostin, puhelimen, sopimusten tai muiden asiakaskohtaamisten kautta. Tarvittaessa luottotiedot voidaan tarkistaa virallisista rekistereistä (esim. Suomen Asiakastieto) ennen sopimuksen solmimista.</p>
        </div>

        <div>
          <h4 class="text-lg font-bold text-gray-800 mb-2">7. TIETOJEN LUOVUTUKSET JA SIIRROT</h4>
          <p class="mb-2">Tietoja käsitellään luottamuksellisesti. Tietoja voidaan luovuttaa luotettaville yhteistyökumppaneillemme (kuten kirjanpitäjälle, IT-tuelle tai alihankkijoille) vain siinä määrin, kuin se on palvelun toteuttamiseksi tai lakisääteisten velvoitteiden täyttämiseksi välttämätöntä.</p>
          <p>Tietoja ei pääsääntöisesti siirretä EU:n tai ETA-alueen ulkopuolelle. Jos järjestelmätoimittaja (esim. sähköpostipalvelu) siirtää tietoja alueen ulkopuolelle, huolehditaan tietoturvasta EU-komission hyväksymillä vakiolausekkeilla.</p>
        </div>

        <div>
          <h4 class="text-lg font-bold text-gray-800 mb-2">8. REKISTERIN SUOJAUKSEN PERIAATTEET</h4>
          <p class="mb-2">Henkilötietoja suojataan huolellisesti:</p>
          <ul class="list-disc pl-5 space-y-1">
            <li><strong>Sähköinen aineisto:</strong> Tiedot on suojattu palomuureilla, salasanapoliitikoilla ja henkilökohtaisilla käyttäjätunnuksilla. Verkkosivustomme käyttää suojattua HTTPS-yhteyttä.</li>
            <li><strong>Manuaalinen aineisto:</strong> Mahdolliset paperiset tulosteet säilytetään lukituissa tiloissa ja ne tuhotaan tietoturvallisesti käytön jälkeen.</li>
            <li><strong>Käyttöoikeudet:</strong> Pääsy tietoihin on vain niillä työntekijöillä tai kumppaneilla, jotka tarvitsevat niitä työtehtäviensä hoitamiseen. Kaikkia käsittelijöitä sitoo vaitiolovelvollisuus.</li>
          </ul>
        </div>

        <div>
          <h4 class="text-lg font-bold text-gray-800 mb-2">9. TIETOJEN SÄILYTYSAIKA</h4>
          <p class="mb-2">Henkilötietoja säilytetään vain niin kauan kuin se on tarpeen tässä selosteessa määriteltyjen käyttötarkoitusten toteuttamiseksi.</p>
          <ul class="list-disc pl-5 space-y-1">
            <li>Potentiaalisten asiakkaiden tietoja (esim. pelkät yhteydenottopyynnöt) säilytetään enintään 2 vuotta viimeisestä yhteydenotosta.</li>
            <li>Sopimus- ja laskutustietoja säilytetään kirjanpitolain vaatiman ajan (6 vuotta tilikauden päättymisestä).</li>
          </ul>
        </div>

        <div>
          <h4 class="text-lg font-bold text-gray-800 mb-2">10. REKISTERÖIDYN OIKEUDET</h4>
          <p class="mb-2">Sinulla on oikeus:</p>
          <ul class="list-disc pl-5 space-y-1 mb-2">
            <li>Tarkastaa itseäsi koskevat tiedot.</li>
            <li>Pyytää virheellisten tai puutteellisten tietojen korjaamista.</li>
            <li>Pyytää tietojesi poistamista ("oikeus tulla unohdetuksi"), ellei meillä ole lakisääteistä velvoitetta säilyttää niitä.</li>
            <li>Rajoittaa tai vastustaa tietojesi käsittelyä (esimerkiksi kieltää suoramarkkinointi).</li>
            <li>Peruuttaa antamasi suostumus milloin tahansa.</li>
          </ul>
          <p>Voit käyttää oikeuksiasi ottamalla yhteyttä kirjallisesti kohdassa 2 mainittuun yhteyshenkilöön. Mikäli koet, että tietojasi käsitellään lainvastaisesti, sinulla on oikeus tehdä valitus Tietosuojavaltuutetun toimistoon (www.tietosuoja.fi).</p>
        </div>

        <div>
          <h4 class="text-lg font-bold text-gray-800 mb-2">11. MUUTOKSET TIETOSUOJASELOSTEESEEN</h4>
          <p>Pidätämme oikeuden päivittää tätä selostetta toimintamme tai lainsäädännön muuttuessa. Suosittelemme tutustumaan selosteen sisältöön säännöllisesti.</p>
        </div>
      </div>
    </div>
  </div>

  <!-- Terms and Cookie Policy Modal -->
  <div id="terms-modal" class="fixed inset-0 z-[100] flex items-center justify-center hidden opacity-0 transition-opacity duration-300 p-4">
    <div class="absolute inset-0 bg-brand-dark/60 backdrop-blur-sm" onclick="closeLegalModal('terms-modal')"></div>
    <div class="bg-white rounded-[2rem] p-6 sm:p-10 max-w-3xl w-full max-h-[85vh] relative z-10 shadow-[0_20px_60px_-15px_rgba(0,0,0,0.5)] border border-gray-100 transform scale-95 transition-transform duration-300 flex flex-col" id="terms-modal-content">
      <div class="flex justify-between items-center mb-6 shrink-0">
        <h3 class="text-2xl sm:text-3xl font-black text-brand-dark uppercase tracking-tight font-display">Eväste- ja käyttöehdot</h3>
        <button onclick="closeLegalModal('terms-modal')" class="w-10 h-10 bg-gray-100 hover:bg-brand-primary text-gray-600 hover:text-white rounded-full flex items-center justify-center transition-all shrink-0">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M6 18L18 6M6 6l12 12"></path></svg>
        </button>
      </div>
      <div class="overflow-y-auto pr-4 text-gray-600 text-[0.95rem] space-y-6 leading-relaxed">
        <p class="font-medium">Verkkosivustollamme käytetään evästeitä (cookies) ja vastaavia tekniikoita käyttökokemuksen parantamiseksi, sivuston toimivuuden varmistamiseksi sekä kävijäliikenteen analysointiin ja markkinointiin.</p>
        
        <div>
          <h4 class="text-lg font-bold text-gray-800 mb-2">Mitä evästeet ovat?</h4>
          <p>Eväste on pieni tekstitiedosto, jonka verkkosivusto tallentaa tietokoneellesi tai mobiililaitteellesi, kun vierailet sivustolla. Evästeet auttavat sivustoa muistamaan asetuksesi ja toimintasi (kuten kielivalinnan tai ostoskorin sisällön) tietyn ajan, jotta sinun ei tarvitse syöttää niitä uudelleen. Evästeet eivät vahingoita laitettasi eivätkä ne pysty lukemaan muita tietoja laitteesi kiintolevyltä.</p>
        </div>

        <div>
          <h4 class="text-lg font-bold text-gray-800 mb-2">Mitä evästeitä käytämme ja miksi?</h4>
          <p class="mb-2">Käytämme sivustollamme seuraaviin ryhmiin kuuluvia evästeitä:</p>
          <ul class="list-decimal pl-5 space-y-3">
            <li><strong>Välttämättömät evästeet:</strong> Nämä evästeet ovat sivuston teknisen toiminnan kannalta pakollisia. Ne mahdollistavat perustoiminnot, kuten sivulla siirtymisen ja suojattujen osioiden käytön. Sivusto ei toimi kunnolla ilman näitä evästeitä. Traficomin linjauksen mukaan näiden evästeiden asettaminen ei vaadi erillistä suostumusta.</li>
            <li><strong>Toiminnalliset evästeet:</strong> Näiden avulla sivusto muistaa tekemäsi valinnat (kuten käyttäjätunnuksen tai alueen) ja tarjoaa parempia ja yksilöllisempiä ominaisuuksia.</li>
            <li><strong>Tilastot ja analytiikka (Tuotekehitys):</strong> Käytämme kolmannen osapuolen työkaluja (kuten Google Analytics) keräämään tietoa siitä, miten sivustoamme käytetään (esim. kävijämäärät, suosituimmat sivut). Tämä auttaa meitä kehittämään verkkosivuston sisältöä ja toimivuutta. Traficomin ohjeiden mukaisesti nämä evästeet ovat oletuksena pois päältä ja vaativat aktiivisen suostumuksesi.</li>
            <li><strong>Markkinointievästeet:</strong> Näitä evästeitä käytetään seuraamaan kävijöitä eri verkkosivustoilla. Tarkoituksena on näyttää mainoksia, jotka ovat yksittäiselle käyttäjille merkityksellisiä ja kiinnostavia (esim. Googlen tai Facebookin kohdennettu mainonta). Myös nämä vaativat aina suostumuksesi.</li>
          </ul>
        </div>

        <div>
          <h4 class="text-lg font-bold text-gray-800 mb-2">Miten voit hallita tai estää evästeitä?</h4>
          <p class="mb-2">Traficomin ja tietosuojasääntelyn mukaisesti suostumuksen antamisen ja siitä kieltäytymisen tulee olla sivustollamme yhtä helppoa. Voit hallita evästeasetuksiasi, muuttaa valintojasi tai peruuttaa suostumuksesi milloin tahansa sivustollamme näkyvän evästebannerin tai sivuston alalaidasta löytyvän evästeasetukset-linkin kautta.</p>
          <p>Vaihtoehtoisesti voit estää evästeiden käytön tai tyhjentää evästehistorian suoraan selaimesi asetuksista. Huomioithan, että välttämättömien evästeiden estäminen saattaa vaikuttaa verkkosivuston toimivuuteen, eikä osa palveluista välttämättä toimi oikein.</p>
        </div>

        <div>
          <h4 class="text-lg font-bold text-gray-800 mb-2">Lisätietoja evästeistä</h4>
          <p>Voit lukea lisää evästeistä, niiden tarkoituksesta ja Suomen kansallisista evästesuosituksista Liikenne- ja viestintävirasto Traficomin viralliselta verkkosivustolta: Traficomin evästeohjeistus palveluntarjoajille.</p>
        </div>

        <div>
          <h4 class="text-lg font-bold text-gray-800 mb-2">Muutokset evästekäytäntöön</h4>
          <p>Varaamme oikeuden päivittää tätä evästekäytäntöä esimerkiksi palveluidemme kehityksen tai muuttuvan lainsäädännön vuoksi.</p>
        </div>
      </div>
    </div>
  </div>
"""

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'id="privacy-modal"' not in content:
        content = content.replace('</body>', modal_html + '\n</body>')
    
    content = re.sub(r'<a class="[^"]*" href="#">Tietosuoja</a>', r'<a class="hover:text-white transition-colors cursor-pointer" onclick="openLegalModal(\'privacy-modal\', event)">Tietosuoja</a>', content)
    content = re.sub(r'<a class="[^"]*" href="#">Käyttöehdot</a>', r'<a class="hover:text-white transition-colors cursor-pointer" onclick="openLegalModal(\'terms-modal\', event)">Eväste- ja käyttöehdot</a>', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Modals inserted successfully.")
