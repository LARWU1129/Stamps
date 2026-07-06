import shutil

SRC = r'C:\Users\larwu\OneDrive - Deloitte (CN)\Desktop\Index_.html'
OUT = r'C:\Users\larwu\AppData\Local\Temp\stamps-repo\index.html'

# Copy original
shutil.copy(SRC, OUT)

with open(OUT, 'r', encoding='utf-8') as f:
    html = f.read()

fixes = '''
<style>
html{overflow:auto !important;height:auto !important}
body{overflow:auto !important;height:auto !important;min-height:100vh !important;max-height:none !important}
.page{overflow-y:auto !important;height:auto !important;min-height:100vh !important;display:none}
.page.active{display:flex !important}
</style>
<script>
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

function openDetail(id, name, region, year, type, desc, catalog, issueDate, qty, route, priceTb, priceWd, priceOl) {
  switchPage('detail');
  var el = document.getElementById('detailTitle');
  if(el) el.textContent = name;

  var fields = [
    {id:'detailRegion', val:region},
    {id:'detailYear', val:year},
    {id:'detailType', val:type},
    {id:'detailCatalog', val:catalog},
    {id:'detailIssue', val:issueDate},
    {id:'detailQty', val:qty},
  ];
  fields.forEach(function(f) {
    var e = document.getElementById(f.id);
    if(e && f.val) {
      var p = e.closest('[class*="detail-item"]') || e.parentElement;
      if(p) {
        var all = p.querySelectorAll('span, div');
        for(var i=0;i<all.length;i++) {
          if(i>0 && all[i].textContent.trim() !== e.textContent.trim()) {
            all[i].textContent = f.val; break;
          }
        }
      }
    }
  });

  var de = document.getElementById('detailDesc');
  if(de) de.textContent = desc;

  var prices = {priceTaobao:priceTb, priceWeidian:priceWd, priceOffline:priceOl};
  for(var k in prices) {
    var pe = document.getElementById(k);
    if(pe && prices[k]) {
      var ch = pe.querySelectorAll('span, div');
      for(var j=1;j<ch.length;j++) {
        if(ch[j].textContent.trim().indexOf('¥')>=0 || ch[j].textContent.trim().indexOf('HK')>=0) {
          ch[j].textContent = prices[k]; break;
        }
      }
    }
  }
}

function toggleFav() {
  var el = document.getElementById('detailFav');
  if(!el) return;
  el.textContent = el.textContent.indexOf('❤')>=0 ? '♡' : '❤';
}

document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('.back-btn, [class*="back"]').forEach(function(el) {
    if(el.tagName==='BUTTON'||el.tagName==='DIV'||el.tagName==='SPAN') {
      el.addEventListener('click', function(e){e.stopPropagation();switchPage('home')});
    }
  });
  var favEl = document.getElementById('detailFav');
  if(favEl) favEl.addEventListener('click', toggleFav);
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
