import time
import random

def run(uid: str, ftype: str, count: str) -> dict:
    if not uid or not count:
        return {'message': '❌ UID এবং পরিমাণ দাও'}

    try:
        count = int(count)
    except ValueError:
        return {'message': '❌ পরিমাণ সংখ্যা হতে হবে'}

    time.sleep(2)

    responses = {
        'diamond': f'💎 Diamond Funnel সম্পন্ন!\n'
                   f'UID: {uid} → {count} ডায়মন্ড ট্রান্সফার\n'
                   f'ট্রানজেকশন ID: FF{random.randint(100000,999999)}',

        'rank': f'🏆 Rank Push চালু!\n'
                f'UID: {uid} → {count} র‍্যাংক পয়েন্ট যোগ\n'
                f'বর্তমান টায়ার: গোল্ড → ডায়মন্ড',

        'kill': f'🔫 Kill Feed অ্যাক্টিভ!\n'
                f'UID: {uid} → {count} কিল অ্যাড\n'
                f'K/D রেশিও আপডেট: {round(random.uniform(2.5, 9.9), 2)}',
    }

    return {'message': responses.get(ftype, '❌ ফানেল টাইপ ভুল')}
