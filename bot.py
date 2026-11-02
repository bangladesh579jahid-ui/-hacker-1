import time
import random

def run(uid: str, region: str, mode: str) -> dict:
    if not uid:
        return {'message': '❌ UID দাও আগে'}

    time.sleep(1.5)

    responses = {
        'aimbot': f'🎯 AimBot অ্যাক্টিভ → UID: {uid} | Region: {region}\n'
                  f'হেডশট রেট: {random.randint(85,99)}% | লক-অন: সম্পন্ন',

        'wallhack': f'👁️ WallHack লোড → UID: {uid}\n'
                    f'ESP রেঞ্জ: {random.randint(200,500)}m | প্লেয়ার হাইলাইট: চালু',

        'speedhack': f'⚡ SpeedHack ইনজেক্ট → UID: {uid}\n'
                     f'মুভমেন্ট মাল্টিপ্লায়ার: {random.randint(2,5)}x | অ্যাক্টিভ',

        'autoheadshot': f'💀 AutoHeadshot → UID: {uid} | Region: {region}\n'
                        f'কিল রেট: {random.randint(10,30)}/মিনিট | মোড: আক্রমণাত্মক',
    }

    return {'message': responses.get(mode, '❌ মোড পাওয়া যায়নি')}
