import shutil

SRC = r'C:\Users\larwu\OneDrive - Deloitte (CN)\Desktop\Index_.html'
OUT = r'C:\Users\larwu\AppData\Local\Temp\stamps-repo\index.html'

shutil.copy(SRC, OUT)

with open(OUT, 'r', encoding='utf-8') as f:
    html = f.read()

fixes = '''
<style>
html{overflow:auto !important;height:auto !important}
body{overflow:auto !important;height:auto !important;min-height:100vh !important;max-height:none !important}
.page{overflow-y:auto !important;height:auto !important;min-height:100vh !important;display:none}
.page.active{display:flex !important}
.stamp-card{cursor:pointer;transition:opacity .15s}
.stamp-card:active{opacity:.7}
.ft-row{display:flex;gap:6px;flex-wrap:wrap;padding:8px 16px}
.ft-chip{padding:4px 12px;border-radius:999px;background:#FFF;border:1px solid #E5E0D8;font-size:12px;cursor:pointer;color:#64748B}
.ft-chip.act{background:#1B324F;color:#FFF;border-color:#1B324F}
#searchResults{display:grid;grid-template-columns:1fr 1fr;gap:8px;padding:0 16px 24px}
.sr-item{background:#FFF;border-radius:8px;border:1px solid #E5E0D8;overflow:hidden;cursor:pointer}
.sr-item .sn{font-weight:600;font-size:13px;padding:8px 10px 2px}
.sr-item .sm{font-size:11px;color:#94A3B8;padding:0 10px 8px}
.sr-item .sp{font-size:12px;color:#E93D82;font-weight:600;padding:0 10px 8px}
</style>
<script>
// ===== Stamp Data =====
var STAMPS = [
  {id:'stamp-1',nm:'大龙邮票 壹分银',rg:'大陆',yr:'1878',tp:'邮票',ds:'清代海关试办邮政时期发行的大龙邮票，是中国第一套邮票。图案为云龙戏珠，寓意吉祥。',ct:'C.1',idate:'1878-07',qt:'约100万枚',rt:'',tb:'¥8,500',wd:'¥7,200-9,800',ol:'¥6,000-12,000'},
  {id:'stamp-2',nm:'龙马图邮票',rg:'台湾',yr:'1888',tp:'邮票',ds:'台湾地区发行的龙马图邮票，图案为龙马精神，寓意吉祥如意。',ct:'T.2',idate:'1888-05',qt:'约50万枚',rt:'',tb:'¥12,000',wd:'¥9,500-11,000',ol:'¥8,000-14,000'},
  {id:'stamp-3',nm:'上海寄香港实寄封',rg:'大陆',yr:'1902',tp:'实寄封',ds:'上海工部局书信馆寄往香港的实寄封，盖有上海海关日戳，是研究清末邮政史的珍贵实物。',ct:'S.3',idate:'1902-03',qt:'约5万件',rt:'上海→香港',tb:'¥3,500',wd:'¥2,800-4,200',ol:'¥3,000-5,000'},
  {id:'stamp-4',nm:'澳门皇冠邮票',rg:'澳门',yr:'1884',tp:'邮票',ds:'澳门发行的皇冠图案邮票，葡萄牙殖民时期邮政用品，设计精美。',ct:'M.1',idate:'1884-11',qt:'约30万枚',rt:'',tb:'¥6,800',wd:'¥5,500-7,200',ol:'¥5,000-8,000'},
  {id:'stamp-5',nm:'香港维多利亚女王像',rg:'香港',yr:'1862',tp:'邮票',ds:'香港最早发行的邮票之一，维多利亚女王侧面像，雕刻版印刷。',ct:'HK.1',idate:'1862-12',qt:'约20万枚',rt:'',tb:'¥15,000',wd:'¥12,000-18,000',ol:'¥10,000-20,000'},
  {id:'stamp-6',nm:'红印花加盖小字',rg:'大陆',yr:'1897',tp:'邮票',ds:'红印花加盖小字当壹圆，清代邮政珍邮之一，存世稀少。',ct:'C.2',idate:'1897-01',qt:'约2万枚',rt:'',tb:'¥287,500',wd:'¥253,000-320,000',ol:'¥250,000-350,000'},
  {id:'stamp-7',nm:'孙中山像国父纪念',rg:'大陆',yr:'1940',tp:'邮票',ds:'孙中山先生国父纪念邮票，民国时期发行，雕刻版印刷。',ct:'M.2',idate:'1940-03',qt:'约80万枚',rt:'',tb:'¥2,800',wd:'¥2,200-3,500',ol:'¥2,000-4,000'},
  {id:'stamp-8',nm:'台湾猴年生肖票',rg:'台湾',yr:'1968',tp:'小型张',ds:'台湾发行的生肖邮票，猴年图案，设计活泼。',ct:'TW.3',idate:'1968-01',qt:'约60万枚',rt:'',tb:'¥4,500',wd:'¥3,800-5,200',ol:'¥3,500-6,000'},
  {id:'stamp-9',nm:'澳门灯塔小型张',rg:'澳门',yr:'1996',tp:'小型张',ds:'澳门灯塔主题小型张，画面为东望洋灯塔，色彩绚丽。',ct:'M.5',idate:'1996-06',qt:'约40万枚',rt:'',tb:'¥1,800',wd:'¥1,500-2,200',ol:'¥1,200-2,500'},
  {id:'stamp-10',nm:'香港回归纪念封',rg:'香港',yr:'1997',tp:'实寄封',ds:'香港回归祖国纪念实寄封，加盖1997年7月1日香港日戳。',ct:'HK.5',idate:'1997-07',qt:'约10万件',rt:'香港→北京',tb:'¥5,200',wd:'¥4,500-6,000',ol:'¥4,000-7,000'},
  {id:'stamp-11',nm:'梅兰芳舞台艺术M',rg:'大陆',yr:'1962',tp:'小型张',ds:'梅兰芳舞台艺术小型张，新中国第一枚小型张，JT票之王。',ct:'J.94M',idate:'1962-08',qt:'约2万枚',rt:'',tb:'¥218,500',wd:'¥195,000-250,000',ol:'¥180,000-280,000'},
  {id:'stamp-12',nm:'全国山河一片红',rg:'大陆',yr:'1968',tp:'邮票',ds:'新中国最著名珍邮，因地图问题被紧急撤销，少量流出。',ct:'W.1',idate:'1968-09',qt:'约1000枚',rt:'',tb:'¥1,035,000',wd:'¥980,000-1,200,000',ol:'¥900,000-1,500,000'},
];

var FAVS = ['stamp-1','stamp-6','stamp-11','stamp-12'];

// ===== Page Switching =====
function switchPage(name) {
  var map = {home:'page-home', search:'page-search', add:'page-add', detail:'page-detail', backup:'page-backup'};
  var id = map[name] || 'page-home';
  document.querySelectorAll('.page').forEach(function(p){p.classList.remove('active')});
  var page = document.getElementById(id);
  if(page) page.classList.add('active');
  document.querySelectorAll('.nav-item, .nav-add').forEach(function(n){n.classList.remove('active')});
  document.querySelectorAll('[data-nav="'+name+'"]').forEach(function(n){n.classList.add('active')});
  window.scrollTo(0,0);
}

// ===== Open Detail =====
function openDetail(id) {
  var s = STAMPS.find(function(x){return x.id===id});
  if(!s) return;
  switchPage('detail');

  var el = document.getElementById('detailTitle');
  if(el) el.textContent = s.nm;

  var fields = {detailRegion:s.rg, detailYear:s.yr, detailType:s.tp, detailCatalog:s.ct, detailIssue:s.idate, detailQty:s.qt};
  for(var k in fields) {
    var e = document.getElementById(k);
    if(e && fields[k]) {
      var p = e.closest('[class*="detail-item"]') || e.parentElement;
      if(p) {
        var all = p.querySelectorAll('span, div');
        for(var i=0;i<all.length;i++) {
          if(i>0 && all[i].textContent.trim() !== e.textContent.trim()) {
            all[i].textContent = fields[k]; break;
          }
        }
      }
    }
  }

  var de = document.getElementById('detailDesc');
  if(de) de.textContent = s.ds;

  var prices = {priceTaobao:s.tb, priceWeidian:s.wd, priceOffline:s.ol};
  for(var k in prices) {
    var pe = document.getElementById(k);
    if(pe && prices[k]) {
      var ch = pe.querySelectorAll('span, div');
      for(var j=1;j<ch.length;j++) {
        if(ch[j].textContent.trim().indexOf('¥')>=0 || ch[j].textContent.trim().indexOf('HK')>=0 || ch[j].textContent.trim().indexOf('$')>=0) {
          ch[j].textContent = prices[k]; break;
        }
      }
    }
  }

  var favEl = document.getElementById('detailFav');
  if(favEl) favEl.textContent = FAVS.indexOf(id)>=0 ? '❤' : '♡';
  window._detailId = id;
}

function toggleFav() {
  var id = window._detailId;
  if(!id) return;
  var idx = FAVS.indexOf(id);
  if(idx>=0) FAVS.splice(idx,1); else FAVS.push(id);
  var el = document.getElementById('detailFav');
  if(el) el.textContent = FAVS.indexOf(id)>=0 ? '❤' : '♡';
}

// ===== Search & Filter =====
var _regionFilter = '全部';
var _typeFilter = '全部';
var _searchQuery = '';

function renderSearchResults() {
  var list = STAMPS.filter(function(s) {
    if(_regionFilter!=='全部' && s.rg!==_regionFilter) return false;
    if(_typeFilter!=='全部' && s.tp!==_typeFilter) return false;
    if(_searchQuery && s.nm.indexOf(_searchQuery)<0 && s.rg.indexOf(_searchQuery)<0) return false;
    return true;
  });

  var container = document.getElementById('searchResults');
  if(!container) return;

  // Update count
  var countEl = document.querySelector('#page-search [class*="藏品"]');
  if(countEl) countEl.textContent = '共 ' + list.length + ' 件藏品';

  container.innerHTML = list.length ? list.map(function(s) {
    return '<div class="sr-item" onclick="openDetail(\''+s.id+'\')">'
      + '<div class="sn">' + s.nm + '</div>'
      + '<div class="sm">' + s.rg + ' · ' + s.yr + ' · ' + s.tp + '</div>'
      + '<div class="sp">' + s.tb + '</div></div>';
  }).join('') : '<div style="grid-column:1/-1;text-align:center;padding:40px 0;color:#94A3B8">没有匹配的藏品</div>';
}

function setRegionFilter(el, val) {
  document.querySelectorAll('#page-search .ft-row:first-child .ft-chip').forEach(function(c){c.classList.remove('act')});
  if(el) el.classList.add('act');
  _regionFilter = val;
  renderSearchResults();
}

function setTypeFilter(el, val) {
  document.querySelectorAll('#page-search .ft-row:nth-child(3) .ft-chip').forEach(function(c){c.classList.remove('act')});
  if(el) el.classList.add('act');
  _typeFilter = val;
  renderSearchResults();
}

function doSearch() {
  var input = document.getElementById('searchInput');
  if(input) _searchQuery = input.value;
  renderSearchResults();
}

// ===== Home Page: render stamps =====
function renderHomeStamps() {
  // Make stamp items in home page clickable
  var homeStampItems = document.querySelectorAll('#page-home [class*="stamp-card"], #page-home .stamp-card, #page-home [onclick*="stamp"]');
  homeStampItems.forEach(function(el) { el.style.cursor = 'pointer'; });

  // The original stamps in the design have fixed names, wire them up
  var homeItems = document.querySelectorAll('#page-home [class*="recent"] [class*="item"], #page-home [class*="stamp"]');
  homeItems.forEach(function(el, i) {
    if(i < STAMPS.length) {
      el.style.cursor = 'pointer';
      el.addEventListener('click', function(){ openDetail(STAMPS[i].id); });
    }
  });
}

// ===== Init =====
document.addEventListener('DOMContentLoaded', function() {
  // Back buttons
  document.querySelectorAll('.back-btn, [class*="back"]').forEach(function(el) {
    if(el.tagName==='BUTTON'||el.tagName==='DIV'||el.tagName==='SPAN') {
      el.addEventListener('click', function(e){e.stopPropagation();switchPage('home')});
    }
  });

  // Favorite toggle
  var favEl = document.getElementById('detailFav');
  if(favEl) favEl.addEventListener('click', toggleFav);

  // Wire up region filter chips
  var regionChips = document.querySelectorAll('#page-search .ft-row:first-child .ft-chip');
  regionChips.forEach(function(chip) {
    chip.addEventListener('click', function() {
      setRegionFilter(this, this.textContent.trim());
    });
  });

  // Wire up type filter chips
  var typeChips = document.querySelectorAll('#page-search .ft-row:nth-child(3) .ft-chip');
  typeChips.forEach(function(chip) {
    chip.addEventListener('click', function() {
      setTypeFilter(this, this.textContent.trim());
    });
  });

  // Wire up search input
  var searchInput = document.getElementById('searchInput');
  if(searchInput) {
    searchInput.addEventListener('input', doSearch);
    searchInput.addEventListener('keyup', function(e) { if(e.key==='Enter') doSearch(); });
  }

  // Wire up "查看全部" links on home page
  document.querySelectorAll('[onclick*="switchPage"], [onclick*="switchPage"]').forEach(function(el) {
    // already handled by inline onclick
  });

  // Make home page stamp cards clickable
  var stampCards = document.querySelectorAll('#page-home [class*="stamp-card"], #page-home [class*="item"]');
  stampCards.forEach(function(card, idx) {
    if(idx < STAMPS.length) {
      card.addEventListener('click', function(){ openDetail(STAMPS[idx].id); });
    }
  });

  // Add search results container if missing
  var sr = document.getElementById('searchResults');
  if(!sr) {
    var searchPage = document.getElementById('page-search');
    if(searchPage) {
      var container = document.createElement('div');
      container.id = 'searchResults';
      searchPage.appendChild(container);
    }
  }

  // Initial render
  renderSearchResults();
});
</script>
'''

if '</body>' in html:
    html = html.replace('</body>', fixes + '</body>')
    print('Injected before </body>')
else:
    html += fixes
    print('Appended')

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(html)

print(f'Done. Size: {len(html)} chars')
