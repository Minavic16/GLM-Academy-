const DETAILS = __DETAILS__;
function esc(s){return String(s==null?"":s).replace(/[&<>]/g,function(m){return {"&":"&amp;","<":"&lt;",">":"&gt;"}[m];});}
function connRow(c){
  var q=c.qualifiers||{};
  var qs=Object.keys(q).length?(" <i>["+Object.entries(q).map(function(kv){return kv[0]+"="+kv[1];}).join(", ")+"]</i>"):"";
  var evs=(c.evidence||[]).map(function(e){
    return '<div class="ev">&#8226; '+esc(e.id)+' &rarr; '+esc(e.source_id)+' (legacy '+esc(e.legacy_id)+'): '+esc((e.excerpt||"").slice(0,140))+'</div>';
  }).join("");
  return '<div class="c"><b>'+c.dir+' '+esc(c.predicate)+'</b> '+esc(c.other)+' <span class="m">['+esc(c.other_type)+'] '+esc(c.other_label)+'</span>'+qs+(evs?'<div>'+evs+'</div>':'')+'</div>';
}
var LAST_HIGHLIGHT=null;
function cdgSelect(id, evt){
  document.querySelectorAll("#cdg-svg g.node rect").forEach(function(r){r.setAttribute("stroke","#333");r.setAttribute("stroke-width","1");});
  var g=document.querySelector("#cdg-svg g.node[data-id='"+id+"']");
  var card=document.getElementById("ccard");
  var d=DETAILS[id];
  if(!d){card.className="hidden";return;}
  var html='<div class="x" onclick="cdgClose()">&times;</div><h2>'+esc(d.id)+'</h2><div class="m">'+esc(d.entity_type)+' &bull; status: '+esc(d.status)+'</div>'
    +'<p><b>Label:</b> '+esc(d.label)+'</p><p><b>Subject:</b> '+esc(d.subject)+'</p>'
    +'<p><b>Legacy IDs:</b> '+esc((d.legacy_ids||[]).join(", "))+'</p><h3>Connections ('+d.connections.length+')</h3>'
    +d.connections.map(connRow).join("");
  card.innerHTML=html;
  // position the card just below the clicked node, clamped to the viewport
  var r=g?g.querySelector("rect").getBoundingClientRect():null;
  card.className="";
  var cw=card.offsetWidth, ch=card.offsetHeight;
  var left, top;
  if(r){left=r.left+window.scrollX-140;top=r.bottom+window.scrollY+34;}
  else {left=(evt?evt.clientX:200)+window.scrollX;top=(evt?evt.clientY:200)+window.scrollY;}
  left=Math.max(8,Math.min(left,window.innerWidth-cw-8));
  top=Math.max(8,Math.min(top,window.scrollY+window.innerHeight-ch-8));
  card.style.left=left+"px";card.style.top=top+"px";
  if(g){var rect=g.querySelector("rect");rect.setAttribute("stroke","#d70000");rect.setAttribute("stroke-width","4");LAST_HIGHLIGHT=rect;}
}
function cdgClose(){
  document.getElementById("ccard").className="hidden";
  if(LAST_HIGHLIGHT){LAST_HIGHLIGHT.setAttribute("stroke","#333");LAST_HIGHLIGHT.setAttribute("stroke-width","1");LAST_HIGHLIGHT=null;}
}
document.addEventListener("keydown",function(e){if(e.key==="Escape")cdgClose();});
