import requests
from bs4 import BeautifulSoup

SIGN_SLUG = {
    1: 'aries',2:'taurus',3:'gemini',4:'cancer',
    5:'leo',6:'virgo',7:'libra',8:'scorpio',
    9:'sagittarius',10:'capricorn',11:'aquarius',12:'pisces'
}

def get_horoscope(sign_number: int) -> str:
    try:
        slug = SIGN_SLUG.get(sign_number, None)
        if not slug:
            return "⚠️ Cung không hợp lệ (1–12)."
        urls = [
            f"https://astrostyle.com/horoscopes/daily/{slug}-daily-horoscope/",
            f"https://www.ganeshaspeaks.com/horoscopes/daily-horoscope/{slug}/"
        ]
        for u in urls:
            try:
                r = requests.get(u, timeout=8, headers={'User-Agent':'Mozilla/5.0'})
                if r.status_code == 200:
                    soup = BeautifulSoup(r.text, 'html.parser')
                    el = soup.find('article') or soup.find('div', class_='main-horoscope') or soup.find('div')
                    if el:
                        p = el.find('p')
                        if p and p.get_text(strip=True):
                            return p.get_text(' ', strip=True)
            except Exception:
                continue
        return "(Không tìm thấy nội dung trực tuyến.)"
    except Exception:
        return "(Lỗi khi lấy horoscope.)"
