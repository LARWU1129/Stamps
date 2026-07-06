import re, os, shutil

SRC = r'C:\Users\larwu\OneDrive - Deloitte (CN)\Desktop\Index_.html'
OUT = r'C:\Users\larwu\AppData\Local\Temp\stamps-repo\index.html'

# Copy original fresh from desktop
shutil.copy(SRC, OUT)
print(f'Copied from desktop: {os.path.getsize(OUT)} bytes')

with open(OUT, 'r', encoding='utf-8') as f:
    html = f.read()

print(f'Read {len(html)} chars')

# Replace base64 images only inside <img src="data:image/...">
# This avoids breaking href, CSS, and other contexts
count = 0
img_pattern = re.compile(r'(<img[^>]*src=")data:image/[^"]+("[^>]*>)', re.IGNORECASE)
html, count = img_pattern.subn(r'\1stamp_thumb\2', html)
print(f'Replaced {count} img base64 sources')

# Replace data URIs in CSS url() references (background images)
# These are typically small icons, replace with empty
html = re.sub(r'url\("data:image/[^"]+"\)', 'none', html)
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
var STAMPS=[{id:"s1",nm:"大龙邮票 壹分银",rg:"大陆",yr:"1878",tp:"邮票",ds:"清代海关试办邮政时期发行的大龙邮票，是中国第一套邮票。",ct:"C.1",idate:"1878-07",qt:"约100万枚",tb:"¥8,500",wd:"¥7,200-9,800",ol:"¥6,000-12,000"},{id:"s2",nm:"红印花加盖小字",rg:"大陆",yr:"1897",tp:"邮票",ds:"红印花加盖小字当壹圆，清代邮政珍邮之一。",ct:"C.2",idate:"1897-01",qt:"约2万枚",tb:"¥287,500",wd:"¥253,000-320,000",ol:"¥250,000-350,000"},{id:"s3",nm:"龙马图邮票",rg:"台湾",yr:"1888",tp:"邮票",ds:"台湾发行的龙马图邮票。",ct:"T.2",idate:"1888-05",qt:"约50万枚",tb:"¥12,000",wd:"¥9,500-11,000",ol:"¥8,000-14,000"},{id:"s4",nm:"上海寄香港实寄封",rg:"大陆",yr:"1902",tp:"实寄封",ds:"上海工部局书信馆寄往香港的实寄封。",ct:"S.3",idate:"1902-03",qt:"约5万件",tb:"¥3,500",wd:"¥2,800-4,200",ol:"¥3,000-5,000"},{id:"s5",nm:"澳门皇冠邮票",rg:"澳门",yr:"1884",tp:"邮票",ds:"澳门发行的皇冠图案邮票。",ct:"M.1",idate:"1884-11",qt:"约30万枚",tb:"¥6,800",wd:"¥5,500-7,200",ol:"¥5,000-8,000"},{id:"s6",nm:"香港维多利亚女王像",rg:"香港",yr:"1862",tp:"邮票",ds:"香港最早发行的邮票之一。",ct:"HK.1",idate:"1862-12",qt:"约20万枚",tb:"¥15,000",wd:"¥12,000-18,000",ol:"¥10,000-20,000"},{id:"s7",nm:"全国山河一片红",rg:"大陆",yr:"1968",tp:"邮票",ds:"新中国最著名珍邮，因地图问题被紧急撤销。",ct:"W.1",idate:"1968-09",qt:"约1000枚",tb:"¥1,035,000",wd:"¥980,000-1,200,000",ol:"¥900,000-1,500,000"},{id:"s8",nm:"梅兰芳舞台艺术M",rg:"大陆",yr:"1962",tp:"小型张",ds:"新中国第一枚小型张，JT票之王。",ct:"J.94M",idate:"1962-08",qt:"约2万枚",tb:"¥218,500",wd:"¥195,000-250,000",ol:"¥180,000-280,000"},{id:"s9",nm:"孙中山像国父纪念",rg:"大陆",yr:"1940",tp:"邮票",ds:"民国时期发行的孙中山纪念邮票。",ct:"M.2",idate:"1940-03",qt:"约80万枚",tb:"¥2,800",wd:"¥2,200-3,500",ol:"¥2,000-4,000"},{id:"s10",nm:"台湾猴年生肖票",rg:"台湾",yr:"1968",tp:"小型张",ds:"台湾发行的生肖邮票，猴年图案。",ct:"TW.3",idate:"1968-01",qt:"约60万枚",tb:"¥4,500",wd:"¥3,800-5,200",ol:"¥3,500-6,000"},{id:"s11",nm:"香港回归纪念封",rg:"香港",yr:"1997",tp:"实寄封",ds:"香港回归祖国纪念实寄封。",ct:"HK.5",idate:"1997-07",qt:"约10万件",tb:"¥5,200",wd:"¥4,500-6,000",ol:"¥4,000-7,000"},{id:"s12",nm:"澳门灯塔小型张",rg:"澳门",yr:"1996",tp:"小型张",ds:"澳门灯塔主题小型张。",ct:"M.5",idate:"1996-06",qt:"约40万枚",tb:"¥1,800",wd:"¥1,500-2,200",ol:"¥1,200-2,500"}];
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

var _rf="全部",_tf="全部",_sq="";
function renderResults(){
  var list=STAMPS.filter(function(s){if(_rf!=="全部"&&s.rg!==_rf)return false;if(_tf!=="全部"&&s.tp!==_tf)return false;if(_sq&&s.nm.indexOf(_sq)<0)return false;return true;});
  var ce=document.getElementById("resultsCount");if(ce)ce.textContent="共 "+list.length+" 件藏品";
  var ct=document.getElementById("resultsList");if(!ct)return;
  ct.innerHTML=list.length?list.map(function(s){return'<div class="result-card" onclick="openDetail(\''+s.id+'\')" style="display:flex;gap:12px;background:#FFF;border-radius:10px;padding:12px;box-shadow:0 1px 4px rgba(27,50,79,0.08);border:1px solid #E5E0D8;cursor:pointer;margin-bottom:8px"><div style="width:60px;height:60px;background:#F5F1EB;border-radius:6px;display:flex;align-items:center;justify-content:center;flex-shrink:0;font-size:20px;color:#C8963E">邮</div><div style="flex:1"><div style="font-weight:600;font-size:14px">'+s.nm+'</div><div style="font-size:12px;color:#94A3B8;margin:2px 0">'+s.rg+' · '+s.yr+' · '+s.tp+'</div><div style="font-size:13px;color:#E93D82;font-weight:600">'+s.tb+'</div></div></div>';}).join(""):"<div style=\"text-align:center;padding:40px;color:#94A3B8\">没有匹配的藏品</div>";
}

// Replace nav images with SVG icons
function addNavIcons() {
  var icons = {home:"home",search:"search",add:"add",detail:"heart",backup:"backup"};
  var svgs = {
    home:"<svg viewBox=\"0 0 24 24\" width=\"20\" height=\"20\"><path d=\"M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/></svg>",
    search:"<svg viewBox=\"0 0 24 24\" width=\"20\" height=\"20\"><circle cx=\"11\" cy=\"11\" r=\"8\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><path d=\"M21 21l-4.35-4.35\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/></svg>",
    add:"<svg viewBox=\"0 0 24 24\" width=\"24\" height=\"24\"><circle cx=\"12\" cy=\"12\" r=\"9\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><path d=\"M12 8v8M8 12h8\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/></svg>",
    heart:"<svg viewBox=\"0 0 24 24\" width=\"20\" height=\"20\"><path d=\"M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/></svg>",
    backup:"<svg viewBox=\"0 0 24 24\" width=\"20\" height=\"20\"><path d=\"M19 21H5a2 2 0 01-2-2V5a2 2 0 012-2h11l5 5v11a2 2 0 01-2 2z\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/><path d=\"M17 21v-2a4 4 0 00-4-4H9a4 4 0 00-4 4v2\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"/></svg>"
  };
  document.querySelectorAll("[data-nav]").forEach(function(el){
    var nav = el.getAttribute("data-nav");
    if(nav && svgs[nav]) {
      var img = el.querySelector("img");
      if(img) {
        var span = document.createElement("span");
        span.innerHTML = svgs[nav];
        img.parentNode.replaceChild(span.firstChild, img);
      }
    }
  });
}

document.addEventListener("DOMContentLoaded",function(){
  document.querySelectorAll(".back-btn").forEach(function(el){el.addEventListener("click",function(){switchPage("home")})});
  document.getElementById("detailFav")&&document.getElementById("detailFav").addEventListener("click",toggleFav);
  document.getElementById("searchInput")&&document.getElementById("searchInput").addEventListener("input",function(){_sq=this.value;renderResults()});
  addNavIcons();
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
