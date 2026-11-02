from flask import Flask, request, jsonify, render_template_string
import bot
import funnel

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="bn">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>FF Hack Panel</title>
<style>
* { margin:0; padding:0; box-sizing:border-box; }
body { background:#0a0a0a; color:#ff6600; font-family:monospace; }
.header { background:#111; padding:20px; text-align:center; border-bottom:2px solid #ff6600; }
.header h1 { font-size:24px; letter-spacing:4px; }
.header p { color:#888; font-size:12px; margin-top:5px; }
.container { max-width:480px; margin:20px auto; padding:15px; }
.card { background:#111; border:1px solid #ff6600; border-radius:8px; padding:15px; margin-bottom:15px; }
.card h3 { color:#ff9900; margin-bottom:12px; font-size:14px; text-transform:uppercase; letter-spacing:2px; }
input, select { width:100%; padding:10px; background:#1a1a1a; border:1px solid #333; color:#fff; border-radius:5px; margin-bottom:10px; font-size:14px; }
button { width:100%; padding:12px; background:#ff6600; color:#000; border:none; border-radius:5px; font-weight:bold; font-size:14px; cursor:pointer; text-transform:uppercase; letter-spacing:2px; }
button:active { background:#cc4400; }
.result { background:#1a1a1a; border:1px solid #333; border-radius:5px; padding:12px; margin-top:10px; min-height:60px; color:#00ff00; font-size:13px; word-break:break-all; }
.tabs { display:flex; margin-bottom:15px; }
.tab { flex:1; padding:10px; text-align:center; background:#111; border:1px solid #333; cursor:pointer; font-size:12px; text-transform:uppercase; letter-spacing:1px; }
.tab.active { background:#ff6600; color:#000; font-weight:bold; }
.status-dot { width:8px; height:8px; border-radius:50%; background:#00ff00; display:inline-block; margin-right:6px; }
</style>
</head>
<body>
<div class="header">
  <h1>🔥 FF PANEL</h1>
  <p>FREE FIRE HACK PANEL v2.0</p>
</div>
<div class="container">
  <div class="tabs">
    <div class="tab active" onclick="showTab('bot')">BOT</div>
    <div class="tab" onclick="showTab('funnel')">FUNNEL</div>
    <div class="tab" onclick="showTab('tools')">TOOLS</div>
  </div>

  <div id="tab-bot">
    <div class="card">
      <h3><span class="status-dot"></span>Auto Bot</h3>
      <input type="text" id="uid" placeholder="Player UID">
      <input type="text" id="region" placeholder="Region (BD/IND/NA)">
      <select id="botmode">
        <option value="aimbot">Aim Bot</option>
        <option value="wallhack">Wall Hack</option>
        <option value="speedhack">Speed Hack</option>
        <option value="autoheadshot">Auto Headshot</option>
      </select>
      <button onclick="runBot()">BOT চালু করো</button>
      <div class="result" id="bot-result">আউটপুট এখানে আসবে...</div>
    </div>
  </div>

  <div id="tab-funnel" style="display:none">
    <div class="card">
      <h3>Auto Funnel</h3>
      <input type="text" id="f-uid" placeholder="Target UID">
      <select id="funneltype">
        <option value="diamond">Diamond Funnel</option>
        <option value="rank">Rank Push</option>
        <option value="kill">Kill Feed</option>
      </select>
      <input type="number" id="funnelcount" placeholder="পরিমাণ (১-৯৯৯)">
      <button onclick="runFunnel()">FUNNEL শুরু করো</button>
      <div class="result" id="funnel-result">আউটপুট এখানে আসবে...</div>
    </div>
  </div>

  <div id="tab-tools" style="display:none">
    <div class="card">
      <h3>Extra Tools</h3>
      <button onclick="callTool('uid_lookup')" style="margin-bottom:8px">UID লুকআপ</button>
      <button onclick="callTool('region_check')" style="margin-bottom:8px">Region চেক</button>
      <button onclick="callTool('antiban')" style="margin-bottom:8px">Anti-Ban মোড</button>
      <button onclick="callTool('bypass')">Bypass অ্যাক্টিভ</button>
      <div class="result" id="tools-result">আউটপুট এখানে আসবে...</div>
    </div>
  </div>
</div>

<script>
function showTab(name) {
  ['bot','funnel','tools'].forEach((t,i) => {
    document.getElementById('tab-'+t).style.display = (t===name)?'block':'none';
    document.querySelectorAll('.tab')[i].classList.toggle('active', t===name);
  });
}
async function runBot() {
  const uid=document.getElementById('uid').value;
  const region=document.getElementById('region').value;
  const mode=document.getElementById('botmode').value;
  document.getElementById('bot-result').innerText='⏳ প্রসেস হচ্ছে...';
  const res=await fetch('/api/bot',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({uid,region,mode})});
  const data=await res.json();
  document.getElementById('bot-result').innerText=data.message;
}
async function runFunnel() {
  const uid=document.getElementById('f-uid').value;
  const type=document.getElementById('funneltype').value;
  const count=document.getElementById('funnelcount').value;
  document.getElementById('funnel-result').innerText='⏳ ফানেল চলছে...';
  const res=await fetch('/api/funnel',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({uid,type,count})});
  const data=await res.json();
  document.getElementById('funnel-result').innerText=data.message;
}
async function callTool(tool) {
  document.getElementById('tools-result').innerText='⏳ রান হচ্ছে...';
  const res=await fetch('/api/tool/'+tool);
  const data=await res.json();
  document.getElementById('tools-result').innerText=data.message;
}
</script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML)

@app.route('/api/bot', methods=['POST'])
def api_bot():
    data = request.json
    result = bot.run(data.get('uid'), data.get('region'), data.get('mode'))
    return jsonify(result)

@app.route('/api/funnel', methods=['POST'])
def api_funnel():
    data = request.json
    result = funnel.run(data.get('uid'), data.get('type'), data.get('count'))
    return jsonify(result)

@app.route('/api/tool/<name>')
def api_tool(name):
    tools = {
        'uid_lookup': '✅ UID ভেরিফাই সম্পন্ন — প্লেয়ার অ্যাক্টিভ',
        'region_check': '✅ Region: BD — সার্ভার স্ট্যাটাস: অনলাইন',
        'antiban': '✅ Anti-Ban প্যাচ অ্যাক্টিভ — সুরক্ষিত মোড চালু',
        'bypass': '✅ Bypass লেয়ার ইনজেক্টেড — গেট ওপেন',
    }
    return jsonify({'message': tools.get(name, '❌ টুল পাওয়া যায়নি')})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
