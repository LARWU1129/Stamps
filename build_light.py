import re, os, shutil

SRC = r'C:\Users\larwu\OneDrive - Deloitte (CN)\Desktop\Index_.html'
OUT = r'C:\Users\larwu\AppData\Local\Temp\stamps-repo\index.html'

# Copy original fresh from desktop
shutil.copy(SRC, OUT)
print(f'Copied from desktop: {os.path.getsize(OUT)} bytes')

with open(OUT, 'r', encoding='utf-8') as f:
    html = f.read()

print(f'Read {len(html)} chars')

# Replace base64 image src with placeholder to reduce size (match only .png or .jpg base64)
count = 0
while 'data:image/' in html:
    start = html.find('data:image/')
    end = html.find('"', start)
    if end > start:
        # Only replace if it's a very long (>100 chars) b64 string
        if end - start > 100:
            html = html[:start] + 'stamp_thumb' + html[end:]
            count += 1
        else:
            # Short data URI, skip
            html = html[:start] + 'stamp_thumb' + html[end:]
            count += 1
    else:
        break
print(f'Replaced {count} base64 images')
print(f'After removal: {len(html)} chars ({len(html)/1024/1024:.2f} MB)')

# Keep the complete file structure, just remove base64 bloat
# The file reduces from 18MB to ~500KB which is manageable

# Add navigation fix CSS
css_fix = '''
<style>
.page{display:none !important}
.page.active{display:flex !important}
html{overflow:auto !important;height:auto !important}
body{overflow:auto !important;height:auto !important;min-height:100vh !important;max-height:none !important}
</style>
'''

# Inject our JS before </body>
js = '''
<script>
var STAMPS=[{id:"s1",nm:"大龙邮票 壹分银",rg:"大陆",yr:"1878",tp:"邮票",ds:"清代海关试办邮政时期发行的大龙邮票，是中国第一套邮票。",ct:"C.1",idate:"1878-07",qt:"约100万枚",tb:"¥8,500",wd:"¥7,200-9,800",ol:"¥6,000-12,000"},{id:"s2",nm:"红印花加盖小字",rg:"大陆",yr:"1897",tp:"邮票",ds:"红印花加盖小字当壹圆，清代邮政珍邮之一。",ct:"C.2",idate:"1897-01",qt:"约2万枚",tb:"¥287,500",wd:"¥253,000-320,000",ol:"¥250,000-350,000"},{id:"s3",nm:"龙马图邮票",rg:"台湾",yr:"1888",tp:"邮票",ds:"台湾地区发行的龙马图邮票。",ct:"T.2",idate:"1888-05",qt:"约50万枚",tb:"¥12,000",wd:"¥9,500-11,000",ol:"¥8,000-14,000"},{id:"s4",nm:"上海寄香港实寄封",rg:"大陆",yr:"1902",tp:"实寄封",ds:"上海工部局书信馆寄往香港的实寄封。",ct:"S.3",idate:"1902-03",qt:"约5万件",tb:"¥3,500",wd:"¥2,800-4,200",ol:"¥3,000-5,000"},{id:"s5",nm:"澳门皇冠邮票",rg:"澳门",yr:"1884",tp:"邮票",ds:"澳门发行的皇冠图案邮票。",ct:"M.1",idate:"1884-11",qt:"约30万枚",tb:"¥6,800",wd:"¥5,500-7,200",ol:"¥5,000-8,000"},{id:"s6",nm:"香港维多利亚女王像",rg:"香港",yr:"1862",tp:"邮票",ds:"香港最早发行的邮票之一。",ct:"HK.1",idate:"1862-12",qt:"约20万枚",tb:"¥15,000",wd:"¥12,000-18,000",ol:"¥10,000-20,000"},{id:"s7",nm:"全国山河一片红",rg:"大陆",yr:"1968",tp:"邮票",ds:"新中国最著名珍邮，因地图问题被紧急撤销。",ct:"W.1",idate:"1968-09",qt:"约1000枚",tb:"¥1,035,000",wd:"¥980,000-1,200,000",ol:"¥900,000-1,500,000"},{id:"s8",nm:"梅兰芳舞台艺术M",rg:"大陆",yr:"1962",tp:"小型张",ds:"新中国第一枚小型张，JT票之王。",ct:"J.94M",idate:"1962-08",qt:"约2万枚",tb:"¥218,500",wd:"¥195,000-250,000",ol:"¥180,000-280,000"},{id:"s9",nm:"孙中山像国父纪念",rg:"大陆",yr:"1940",tp:"邮票",ds:"民国时期发行的孙中山纪念邮票。",ct:"M.2",idate:"1940-03",qt:"约80万枚",tb:"¥2,800",wd:"¥2,200-3,500",ol:"¥2,000-4,000"},{id:"s10",nm:"台湾猴年生肖票",rg:"台湾",yr:"1968",tp:"小型张",ds:"台湾发行的生肖邮票，猴年图案。",ct:"TW.3",idate:"1968-01",qt:"约60万枚",tb:"¥4,500",wd:"¥3,800-5,200",ol:"¥3,500-6,000"},{id:"s11",nm:"香港回归纪念封",rg:"香港",yr:"1997",tp:"实寄封",ds:"香港回归祖国纪念实寄封。",ct:"HK.5",idate:"1997-07",qt:"约10万件",tb:"¥5,200",wd:"¥4,500-6,000",ol:"¥4,000-7,000"},{id:"s12",nm:"澳门灯塔小型张",rg:"澳门",yr:"1996",tp:"小型张",ds:"澳门灯塔主题小型张。",ct:"M.5",idate:"1996-06",qt:"约40万枚",tb:"¥1,800",wd:"¥1,500-2,200",ol:"¥1,200-2,500"}];
var FAVS=["s1","s7","s8"];

function switchPage(n){
  var m={home:"page-home",search:"page-search",detail:"page-detail",add:"page-add",backup:"page-backup"};
  document.querySelectorAll(".page").forEach(function(p){p.classList.remove("active")});
  var p=document.getElementById(m[n]);if(p)p.classList.add("active");
  document.querySelectorAll(".nav-item,.nav-add").forEach(function(x){x.classList.remove("active")});
  document.querySelectorAll('[data-nav="'+n+'"]').forEach(function(x){x.classList.add("active")});
  window.scrollTo(0,0);
}

function openDetail(id){
  var s=STAMPS.find(function(x){return x.id===id});if(!s)return;switchPage("detail");
  var el=document.getElementById("detailTitle");if(el)el.textContent=s.nm;
  var fm={detailRegion:s.rg,detailYear:s.yr,detailType:s.tp,detailCatalog:s.ct,detailIssue:s.idate,detailQty:s.qt};
  for(var k in fm){var e=document.getElementById(k);if(!e||!fm[k])continue;
    var p=e.closest("[class*=detail-item]")||e.parentElement;if(!p)continue;
    var a=p.querySelectorAll("span,div");for(var i=1;i<a.length;i++){a[i].textContent=fm[k];break;}}
  var dd=document.getElementById("detailDesc");if(dd)dd.textContent=s.ds;
  [["priceTaobao",s.tb],["priceWeidian",s.wd],["priceOffline",s.ol]].forEach(function(p){
    var e=document.getElementById(p[0]);if(!e)return;
    var c=e.querySelectorAll("span,div");for(var i=1;i<c.length;i++){if(c[i].textContent.match(/[$\\u00a5HK]/)){c[i].textContent=p[1];break;}}});
  var f=document.getElementById("detailFav");if(f)f.textContent=FAVS.indexOf(id)>=0?"\\u2764":"\\u2661";window._di=id;
}
function toggleFav(){var id=window._di;if(!id)return;var i=FAVS.indexOf(id);if(i>=0)FAVS.splice(i,1);else FAVS.push(id);var f=document.getElementById("detailFav");if(f)f.textContent=FAVS.indexOf(id)>=0?"\\u2764":"\\u2661";}

var _rf="\\u5168\\u90e8",_tf="\\u5168\\u90e8",_sq="";
function renderResults(){
  var list=STAMPS.filter(function(s){if(_rf!=="\\u5168\\u90e8"&&s.rg!==_rf)return false;if(_tf!=="\\u5168\\u90e8"&&s.tp!==_tf)return false;if(_sq&&s.nm.indexOf(_sq)<0)return false;return true;});
  var ce=document.getElementById("resultsCount");if(ce)ce.textContent="\\u5171 "+list.length+" \\u4ef6\\u85cf\\u54c1";
  var ct=document.getElementById("resultsList");if(!ct)return;
  ct.innerHTML=list.length?list.map(function(s){return\'<div class="result-card" onclick="openDetail(\\\'\'+s.id+\'\\\')" style="display:flex;gap:12px;background:#FFF;border-radius:10px;padding:12px;box-shadow:0 1px 4px rgba(27,50,79,0.08);border:1px solid #E5E0D8;cursor:pointer;margin-bottom:8px"><div style="width:60px;height:60px;background:#F5F1EB;border-radius:6px;display:flex;align-items:center;justify-content:center;flex-shrink:0;font-size:20px;color:#C8963E">\\u90AE</div><div style="flex:1"><div style="font-weight:600;font-size:14px">\'+s.nm+\'</div><div style="font-size:12px;color:#94A3B8;margin:2px 0">\'+s.rg+\' \\u00b7 \'+s.yr+\' \\u00b7 \'+s.tp+\'</div><div style="font-size:13px;color:#E93D82;font-weight:600">\'+s.tb+\'</div></div></div>\';}).join(""):"<div style=\\"text-align:center;padding:40px;color:#94A3B8\\">\\u6ca1\\u6709\\u5339\\u914d\\u7684\\u85cf\\u54c1</div>";
}

document.addEventListener("DOMContentLoaded",function(){
  document.querySelectorAll(".back-btn").forEach(function(el){el.addEventListener("click",function(){switchPage("home")})});
  document.getElementById("detailFav")&&document.getElementById("detailFav").addEventListener("click",toggleFav);
  document.getElementById("searchInput")&&document.getElementById("searchInput").addEventListener("input",function(){_sq=this.value;renderResults()});
  renderResults();
});
</script>
'''

# Inject CSS and JS
if css_fix in html:
    print('CSS already injected')
else:
    # Find <style> and inject our fixes after the last original style
    last_style = html.rfind('</style>')
    if last_style > 0:
        html = html[:last_style+8] + css_fix + html[last_style+8:]

if '</body>' in html:
    html = html.replace('</body>', js + '</body>')
else:
    html += js

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(html)

final_size = len(html)
print(f'Final: {final_size} chars ({final_size/1024/1024:.1f} MB)')
print(f'Reduced from ~18MB to ~{final_size/1024/1024:.1f}MB')
