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
function cdgSelect(id){
  document.querySelectorAll("#cdg-svg g.node rect").forEach(function(r){r.setAttribute("stroke","#333");r.setAttribute("stroke-width","1");});
  var g=document.querySelector("#cdg-svg g.node[data-id='"+id+"']");
  if(g){var r=g.querySelector("rect");r.setAttribute("stroke","#d70000");r.setAttribute("stroke-width","4");
    var b=r.getBoundingClientRect();window.scrollTo(b.left-window.innerWidth/2, b.top-window.innerHeight/2);}
  var d=DETAILS[id];var p=document.getElementById("panel");
  if(!d){p.className="hidden";return;}p.className="";
  var html='<h2>'+esc(d.id)+'</h2><div class="m">'+esc(d.entity_type)+' &bull; status: '+esc(d.status)+'</div>'
    +'<p><b>Label:</b> '+esc(d.label)+'</p><p><b>Subject:</b> '+esc(d.subject)+'</p>'
    +'<p><b>Legacy IDs:</b> '+esc((d.legacy_ids||[]).join(", "))+'</p><h3>Connections ('+d.connections.length+')</h3>'
    +d.connections.map(connRow).join("");
  p.innerHTML=html;
}
