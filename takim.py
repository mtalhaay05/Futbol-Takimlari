import ssl
import aiohttp
import urllib.parse

# 1. Antivirüs ve Windows SSL engellerini aşan bağlam
ctx_unverified = ssl.create_default_context()
ctx_unverified.check_hostname = False
ctx_unverified.verify_mode = ssl.CERT_NONE

_original_wrap = aiohttp.connector.TCPConnector._wrap_create_connection
async def _patched_wrap(self, *args, **kwargs):
    if kwargs.get('ssl') is not None:
        kwargs['ssl'] = ctx_unverified
    return await _original_wrap(self, *args, **kwargs)

aiohttp.connector.TCPConnector._wrap_create_connection = _patched_wrap

# 2. Discord Kütüphanesini Başlatma
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# 3. Atık Veritabanı
TAKIM_REHBERI = {
    "fenerbahce": {
        "Kurulus_Yili": "1907",
        "Stadyum": "Şükrü Saracoğlu Stadyumu (İstanbul)",
        "Renkler": "Sarı, Lacivert",
        "Takim_adi": "Fenerbahçe_(futbol_takımı)"
    },
    "galatasaray": {
        "Kurulus_Yili": "1905",
        "Stadyum": "RAMS Park (İstanbul)",
        "Renkler": "Sarı, Kırmızı",
        "Takim_adi": "Galatasaray_(futbol_takımı)"
    },

    "besiktas": {
        "Kurulus_Yili": "1903",
        "Stadyum": "Tüpraş Stadyumu (İstanbul)",
        "Renkler": "Siyah, Beyaz",
        "Takim_adi": "Beşiktaş_(futbol_takımı)"
    },
    "trabzonspor": {
        "Kurulus_Yili": "1967",
        "Stadyum": "Papara Park (Trabzon)",
        "Renkler": "Bordo, Mavi",
        "Takim_adi": "Trabzonspor_(futbol_takımı)"
    },
    "basaksehir": {
        "Kurulus_Yili": "1990",
        "Stadyum": "Başakşehir Fatih Terim Stadyumu (İstanbul)",
        "Renkler": "Turuncu, Lacivert",
        "Takim_adi": "İstanbul_Başakşehir_FK"
    },
    "samsunspor": {
        "Kurulus_Yili": "1965",
        "Stadyum": "Samsun 19 Mayıs Stadyumu (Samsun)",
        "Renkler": "Kırmızı, Beyaz",
        "Takim_adi": "Samsunspor"
    },
    "eyupspor": {
        "Kurulus_Yili": "1919",
        "Stadyum": "Recep Tayyip Erdoğan Stadyumu (İstanbul)",
        "Renkler": "Eflatun, Sarı",
        "Takim_adi": "Eyüpspor"
    },
    "goztepe": {
        "Kurulus_Yili": "1925",
        "Stadyum": "Gürsel Aksel Stadyumu (İzmir)",
        "Renkler": "Sarı, Kırmızı",
        "Takim_adi": "Göztepe_(futbol_takımı)"
    },
    "kasimpasa": {
        "Kurulus_Yili": "1921",
        "Stadyum": "Recep Tayyip Erdoğan Stadyumu (İstanbul)",
        "Renkler": "Lacivert, Beyaz",
        "Takim_adi": "Kasımpaşa_SK"
    },
    "sivasspor": {
        "Kurulus_Yili": "1967",
        "Stadyum": "BG Grup 4 Eylül Stadyumu (Sivas)",
        "Renkler": "Kırmızı, Beyaz",
        "Takim_adi": "Sivasspor"
    },
    "antalyaspor": {
        "Kurulus_Yili": "1966",
        "Stadyum": "Corendon Airlines Park (Antalya)",
        "Renkler": "Kırmızı, Beyaz",
        "Takim_adi": "Antalyaspor"
    },
    "rizespor": {
        "Kurulus_Yili": "1953",
        "Stadyum": "Çaykur Didi Stadyumu (Rize)",
        "Renkler": "Yeşil, Mavi",
        "Takim_adi": "Çaykur_Rizespor"
    },
    "alanyaspor": {
        "Kurulus_Yili": "1948",
        "Stadyum": "Gain Park Stadyumu (Antalya)",
        "Renkler": "Turuncu, Yeşil",
        "Takim_adi": "Alanyaspor"
    },
    "konyaspor": {
        "Kurulus_Yili": "1922",
        "Stadyum": "Medaş Konya Büyükşehir Stadyumu (Konya)",
        "Renkler": "Yeşil, Beyaz",
        "Takim_adi": "Konyaspor"
    },
    "kayserispor": {
        "Kurulus_Yili": "1966",
        "Stadyum": "RHG Enertürk Enerji Stadyumu (Kayseri)",
        "Renkler": "Sarı, Kırmızı",
        "Takim_adi": "Kayserispor"
    },
    "gaziantep": {
        "Kurulus_Yili": "1988",
        "Stadyum": "Kalyon Stadyumu (Gaziantep)",
        "Renkler": "Kırmızı, Siyah",
        "Takim_adi": "Gaziantep_FK"
    },
    "bodrum": {
        "Kurulus_Yili": "1931",
        "Stadyum": "Bodrum İlçe Stadyumu (Muğla)",
        "Renkler": "Yeşil, Beyaz",
        "Takim_adi": "Bodrum_FK"
    },
    "hatayspor": {
        "Kurulus_Yili": "1967",
        "Stadyum": "Mersin Stadyumu (Mersin)",
        "Renkler": "Bordo, Beyaz",
        "Takim_adi": "Hatayspor"
    },
    "adanademir": {
        "Kurulus_Yili": "1940",
        "Stadyum": "Yeni Adana Stadyumu (Adana)",
        "Renkler": "Mavi, Lacivert",
        "Takim_adi": "Adana_Demirspor"
    }
}
# 4. İnternetten Özet Bilgi Çekme
async def fetch_takim_bilgisi(Takim_adi: str) -> str:
    guvenli_baslik = urllib.parse.quote(Takim_adi.replace(' ', '_'))

    url = f"https://tr.wikipedia.org/api/rest_v1/page/summary/{guvenli_baslik}?redirect=true"
    headers = {"User-Agent": "DiscordTakimBotu/1.0"}
    
    try:
        connector = aiohttp.TCPConnector(ssl=ctx_unverified)
        async with aiohttp.ClientSession(headers=headers, connector=connector) as session:
            async with session.get(url, timeout=5) as response:
                if response.status == 200:
                    data = await response.json()
                    return data.get("extract", "Detaylı takım bilgisi bulunamadı.")
                return "Bu takım hakkında harici kaynakta ek özet bulunamadı."
    except Exception:
        return "İnternet üzerinden ek bilgi alınırken bir bağlantı hatası oluştu."

# 5. Discord Arayüz Bileşenleri (Select Menu)
class TakimSelect(discord.ui.Select):
    def __init__(self):
        # Sözlükteki 19 takımı tek tek elle yazmak yerine döngüyle otomatik listeye çeviriyoruz:
        options = [
            discord.SelectOption(
                label=bilgi["Takim_adi"].replace("_(futbol_takımı)", "").replace("_", " "),
                value=anahtar,
                description=f"{bilgi['Kurulus_Yili']} | {bilgi['Renkler']}",
                emoji="⚽"
            )
            for anahtar, bilgi in TAKIM_REHBERI.items()
        ]
        
        super().__init__(
            placeholder="Bilgi almak istediğiniz takımı seçin...", 
            min_values=1, 
            max_values=1, 
            options=options
        )

    async def callback(self, interaction: discord.Interaction):
        secilen_anahtar = self.values[0]
        takim_verisi = TAKIM_REHBERI.get(secilen_anahtar)

        await interaction.response.defer()

        ek_bilgi = await fetch_takim_bilgisi(takim_verisi["Takim_adi"])

        # Embed kısmına dokunmana gerek yok; sözlükten dinamik olarak çeker
        embed = discord.Embed(
            title=f"⚽ {takim_verisi['Takim_adi'].replace('_(futbol_takımı)', '').replace('_', ' ')}",
            color=discord.Color.gold()
        )
        embed.add_field(name="📅 Kuruluş Yılı", value=takim_verisi["Kurulus_Yili"], inline=True)
        embed.add_field(name="🎨 Renkler", value=takim_verisi["Renkler"], inline=True)
        embed.add_field(name="🏟️ Stadyum", value=f"**{takim_verisi['Stadyum']}**", inline=False)
        embed.add_field(name="📖 Kulüp Bilgisi (Wikipedia)", value=ek_bilgi[:600] + ("..." if len(ek_bilgi) > 600 else ""), inline=False)
        embed.set_footer(text="Futbol Bilgi Sistemi")

        await interaction.followup.send(embed=embed)
class TakimView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=180)
        self.add_item(TakimSelect())

# 6. Bot Olayları ve Komutları
@bot.event
async def on_ready():
    print(f"Bot başarıyla aktif oldu: {bot.user.name} ({bot.user.id})")

@bot.command(name="takım", aliases=["takim"])
async def takim_komutu(ctx):
    view = TakimView()
    await ctx.send("Lütfen bilgi almak istediğiniz takımı seçin:", view=view)

# Reset Token diyerek aldığınız YENİ tokeni aşağıdaki tırnakların içine yapıştırın:
bot.run("TOKENİ_BURAYA_YAZIN")
