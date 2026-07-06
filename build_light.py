import re, os, shutil

SRC = r'C:\Users\larwu\OneDrive - Deloitte (CN)\Desktop\Index_.html'
OUT = r'C:\Users\larwu\AppData\Local\Temp\stamps-repo\index.html'

shutil.copy(SRC, OUT)

with open(OUT, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace base64 only in img tags
count = 0
html, count = re.subn(r'(<img[^>]*src=")data:image/[^"]+("[^>]*>)', r'\1icon\2', html)
print(f'Replaced {count} base64 images')

# Add CSS fixes
css = '<style>.page{display:none!important}.page.active{display:flex!important}html{overflow:auto!important;height:auto!important}body{overflow:auto!important;height:auto!important;min-height:100vh!important}</style>'
last_style = html.rfind('</style>')
html = html[:last_style+8] + css + html[last_style+8:]

# Inject JS with NO quote conflicts - all SVG use single-quoted JS strings
script = '''
<script>
var D=[{id:"s1",nm:"大龙邮票 壹分银",rg:"大陆",yr:"1878",tp:"邮票",ds:"清代海关试办邮政时期发行的大龙邮票，是中国第一套邮票。",ct:"C.1",idate:"1878-07",qt:"约100万枚",tb:"¥8,500",wd:"¥7,200-9,800",ol:"¥6,000-12,000"},{id:"s2",nm:"红印花加盖小字",rg:"大陆",yr:"1897",tp:"邮票",ds:"红印花加盖小字当壹圆，清代邮政珍邮之一。",ct:"C.2",idate:"1897-01",qt:"约2万枚",tb:"¥287,500",wd:"¥253,000-320,000",ol:"¥250,000-350,000"},{id:"s3",nm:"龙马图邮票",rg:"台湾",yr:"1888",tp:"邮票",ds:"台湾发行的龙马图邮票。",ct:"T.2",idate:"1888-05",qt:"约50万枚",tb:"¥12,000",wd:"¥9,500-11,000",ol:"¥8,000-14,000"},{id:"s4",nm:"上海寄香港实寄封",rg:"大陆",yr:"1902",tp:"实寄封",ds:"上海工部局书信馆寄往香港的实寄封。",ct:"S.3",idate:"1902-03",qt:"约5万件",tb:"¥3,500",wd:"¥2,800-4,200",ol:"¥3,000-5,000"},{id:"s5",nm:"澳门皇冠邮票",rg:"澳门",yr:"1884",tp:"邮票",ds:"澳门发行的皇冠图案邮票。",ct:"M.1",idate:"1884-11",qt:"约30万枚",tb:"¥6,800",wd:"¥5,500-7,200",ol:"¥5,000-8,000"},{id:"s6",nm:"香港维多利亚女王像",rg:"香港",yr:"1862",tp:"邮票",ds:"香港最早发行的邮票之一。",ct:"HK.1",idate:"1862-12",qt:"约20万枚",tb:"¥15,000",wd:"¥12,000-18,000",ol:"¥10,000-20,000"},{id:"s7",nm:"全国山河一片红",rg:"大陆",yr:"1968",tp:"邮票",ds:"新中国最著名珍邮，因地图问题被紧急撤销。",ct:"W.1",idate:"1968-09",qt:"约1000枚",tb:"¥1,035,000",wd:"¥980,000-1,200,000",ol:"¥900,000-1,500,000"},{id:"s8",nm:"梅兰芳舞台艺术M",rg:"大陆",yr:"1962",tp:"小型张",ds:"新中国第一枚小型张，JT票之王。",ct:"J.94M",idate:"1962-08",qt:"约2万枚",tb:"¥218,500",wd:"¥195,000-250,000",ol:"¥180,000-280,000"},{id:"s9",nm:"孙中山像国父纪念",rg:"大陆",yr:"1940",tp:"邮票",ds:"民国时期发行的孙中山纪念邮票。",ct:"M.2",idate:"1940-03",qt:"约80万枚",tb:"¥2,800",wd:"¥2,200-3,500",ol:"¥2,000-4,000"},{id:"s10",nm:"台湾猴年生肖票",rg:"台湾",yr:"1968",tp:"小型张",ds:"台湾发行的生肖邮票。",ct:"TW.3",idate:"1968-01",qt:"约60万枚",tb:"¥4,500",wd:"¥3,800-5,200",ol:"¥3,500-6,000"},{id:"s11",nm:"香港回归纪念封",rg:"香港",yr:"1997",tp:"实寄封",ds:"香港回归祖国纪念实寄封。",ct:"HK.5",idate:"1997-07",qt:"约10万件",tb:"¥5,200",wd:"¥4,500-6,000",ol:"¥4,000-7,000"},{id:"s12",nm:"澳门灯塔小型张",rg:"澳门",yr:"1996",tp:"小型张",ds:"澳门灯塔主题小型张。",ct:"M.5",idate:"1996-06",qt:"约40万枚",tb:"¥1,800",wd:"¥1,500-2,200",ol:"¥1,200-2,500"}];
var F=["s1","s7","s8"];

function go(n){
  var m={home:"page-home",search:"page-search",detail:"page-detail",add:"page-add",backup:"page-backup"};
  document.querySelectorAll(".page").forEach(function(p){p.classList.remove("active")});
  var p=document.getElementById(m[n]);if(p)p.classList.add("active");
  document.querySelectorAll(".nav-item,.nav-add").forEach(function(x){x.classList.remove("active")});
  document.querySelectorAll('[data-nav="'+n+'"]').forEach(function(x){x.classList.add("active")});
}
function detail(id){
  var s=D.find(function(x){return x.id===id});if(!s)return;go("detail");
  var e=document.getElementById("detailTitle");if(e)e.textContent=s.nm;
  [["detailRegion",s.rg],["detailYear",s.yr],["detailType",s.tp],["detailCatalog",s.ct],["detailIssue",s.idate],["detailQty",s.qt]].forEach(function(p){
    var el=document.getElementById(p[0]);if(!el)return;
    var pa=el.closest("[class*=detail-item]")||el.parentElement;if(!pa)return;
    var c=pa.querySelectorAll("span,div");for(var i=1;i<c.length;i++){c[i].textContent=p[1];break;}
  });
  var de=document.getElementById("detailDesc");if(de)de.textContent=s.ds;
  [["priceTaobao",s.tb],["priceWeidian",s.wd],["priceOffline",s.ol]].forEach(function(p){
    var el=document.getElementById(p[0]);if(!el)return;
    var ch=el.querySelectorAll("span,div");for(var i=1;i<ch.length;i++){if(ch[i].textContent.match(/[$¥HK]/)){ch[i].textContent=p[1];break;}}
  });
  var f=document.getElementById("detailFav");if(f)f.textContent=F.indexOf(id)>=0?"❤":"♡";
}
function tf(){var id=window._di;if(!id)return;var i=F.indexOf(id);i>=0?F.splice(i,1):F.push(id);var f=document.getElementById("detailFav");if(f)f.textContent=F.indexOf(id)>=0?"❤":"♡";}

var R="全部",T="全部",Q="";
function sr(){
  var l=D.filter(function(s){if(R!=="全部"&&s.rg!==R)return false;if(T!=="全部"&&s.tp!==T)return false;if(Q&&s.nm.indexOf(Q)<0)return false;return true;});
  var ce=document.getElementById("resultsCount");if(ce)ce.textContent="共 "+l.length+" 件藏品";
  var ct=document.getElementById("resultsList");if(!ct)return;
  ct.innerHTML=l.length?l.map(function(s){return'<div class="result-card" onclick="detail(\''+s.id+'\')" style="display:flex;gap:12px;background:#FFF;border-radius:10px;padding:12px;border:1px solid #E5E0D8;cursor:pointer;margin-bottom:8px"><div style="width:60px;height:60px;background:#F5F1EB;border-radius:6px;display:flex;align-items:center;justify-content:center;font-size:20px;color:#C8963E">邮</div><div style="flex:1"><div style="font-weight:600;font-size:14px">'+s.nm+'</div><div style="font-size:12px;color:#94A3B8">'+s.rg+"  "+s.yr+"  "+s.tp+'</div><div style="font-size:13px;color:#E93D82;font-weight:600">'+s.tb+'</div></div></div>';}).join(""):"<div style='text-align:center;padding:40px;color:#94A3B8'>没有匹配的藏品</div>";
}
function sR(v,e){document.querySelectorAll(".region-chip").forEach(function(c){c.classList.remove("active")});if(e)e.classList.add("active");var map={all:"全部",mainland:"大陆",hongkong:"香港",macau:"澳门",taiwan:"台湾",overseas:"海外"};R=map[v]||"全部";sr();}
function sT(v,e){document.querySelectorAll(".type-chip").forEach(function(c){c.classList.remove("active")});if(e)e.classList.add("active");var map={all:"全部",stamp:"邮票",sheet:"小型张",cover:"实寄封",postcard:"明信片"};T=map[v]||"全部";sr();}
function tS(){var b=document.querySelector(".sort-btn");if(!b)return;var o=["默认排序","价格升序","价格降序","年份排序"];var i=o.indexOf(b.textContent.trim());b.textContent=o[(i+1)%o.length];sr();}

function navIcons(){
  var icons={home:'<svg viewBox="0 0 24 24" width="18" height="18"><path d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" fill="none" stroke="currentColor" stroke-width="1.8"/></svg>',
    search:'<svg viewBox="0 0 24 24" width="18" height="18"><circle cx="11" cy="11" r="8" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M21 21l-4.35-4.35" fill="none" stroke="currentColor" stroke-width="1.8"/></svg>',
    add:'<svg viewBox="0 0 24 24" width="22" height="22"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M12 8v8M8 12h8" fill="none" stroke="currentColor" stroke-width="1.8"/></svg>',
    heart:'<svg viewBox="0 0 24 24" width="18" height="18"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z" fill="none" stroke="currentColor" stroke-width="1.8"/></svg>',
    backup:'<svg viewBox="0 0 24 24" width="18" height="18"><path d="M19 21H5a2 2 0 01-2-2V5a2 2 0 012-2h11l5 5v11a2 2 0 01-2 2z" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M17 21v-2a4 4 0 00-4-4H9a4 4 0 00-4 4v2" fill="none" stroke="currentColor" stroke-width="1.8"/></svg>'};
  document.querySelectorAll("[data-nav]").forEach(function(el){
    var n=el.getAttribute("data-nav");if(!n||!icons[n])return;
    var img=el.querySelector("img");if(!img)return;
    var sp=document.createElement("span");sp.innerHTML=icons[n];
    img.parentNode.replaceChild(sp.firstChild,img);
  });
}

document.addEventListener("DOMContentLoaded",function(){
  document.querySelectorAll(".back-btn").forEach(function(el){el.addEventListener("click",function(){go("home")})});
  var df=document.getElementById("detailFav");if(df)df.addEventListener("click",tf);
  var si=document.getElementById("searchInput");if(si)si.addEventListener("input",function(){Q=this.value;sr()});
  navIcons();sr();
});
</script>
'''

html = html.replace('</body>', script + '\n</body>')

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(html)

print(f'Done: {len(html)} chars')
