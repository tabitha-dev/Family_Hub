"use strict";
// Progressive enhancements for the standalone Family Hub. No storage-key changes.
(function(){
  const $ = id=>document.getElementById(id);
  const pages={dashboard:"Today's overview", "meal-plans":"Weekly meal planner","grocery-lists":"Grocery checklist",chores:"Chore assignments",calendar:"Family calendar",guide:"How Family Hub works",settings:"Family Hub settings"};
  const announce=text=>{const el=$("fh-status");if(el)el.textContent=text;};
  const closeMore=(restore=false)=>{
    const panel=$("fh-more-panel"),trigger=$("fh-more-trigger");
    if(!panel||!trigger)return;
    const wasOpen=!panel.hidden;
    panel.hidden=true;trigger.setAttribute("aria-expanded","false");
    if(restore&&wasOpen)trigger.focus();
  };
  function updateNavigation(){
    const hash=location.hash.slice(1)||"dashboard";
    const active=Object.hasOwn(pages,hash)?hash:"dashboard";
    const title=$("fh-topbar-heading");if(title)title.textContent=pages[active];
    const moreActive=["chores","settings","guide"].includes(active);
    document.querySelectorAll(".fh-tab").forEach(tab=>{
      const matches=tab.dataset.route===active||(tab.id==="fh-more-trigger"&&moreActive);
      tab.classList.toggle("is-active",matches);
      if(matches)tab.setAttribute("aria-current","page");else tab.removeAttribute("aria-current");
    });
    closeMore(false);
    const main=$("fh-main");
    if(main)main.scrollTop=0;
    document.title=(active==="dashboard"?"Family Hub":pages[active]+" | Family Hub")+" | Free Local-First Family Planner";
  }
  const originalDashboardMeals=Dashboard.renderMeals;
  Dashboard.renderMeals=()=>{
    const container=$("dashboard-meals");if(!container)return;
    const plan=AppData.get("mealPlan")||[];
    const day=(new Date().getDay()+6)%7;
    const upcoming=plan.slice(day).concat(plan.slice(0,day)).filter(x=>x.dinner&&String(x.dinner).trim()!=="...").slice(0,4);
    container.replaceChildren();
    if(!upcoming.length){
      const wrap=document.createElement("div");wrap.className="fh-meal-empty";
      const emblem=document.createElement("span");emblem.className="fh-meal-glyph";emblem.setAttribute("aria-hidden","true");emblem.textContent="🍽️";
      const p=document.createElement("p");p.textContent="No dinner plans yet. Start with your weekly meal planner.";
      const a=document.createElement("a");a.href="#meal-plans";a.textContent="Plan your first meal";
      wrap.append(emblem,p,a);container.appendChild(wrap);return;
    }
    const accents=["🍲","🥘","🥗","🍜"];
    upcoming.forEach((meal,i)=>{
      const card=document.createElement("article");card.className="fh-meal-tile";
      const illustration=document.createElement("div");illustration.className="fh-meal-illustration fh-meal-tone-"+i;illustration.setAttribute("aria-hidden","true");illustration.textContent=accents[i];
      const title=document.createElement("strong");title.textContent=String(meal.dinner);
      const label=document.createElement("span");label.textContent=String(meal.day);
      card.append(illustration,title,label);container.appendChild(card);
    });
  };
  const baseDashboardRender=Dashboard.render;
  Dashboard.render=()=>{
    baseDashboardRender();
    const chores=AppData.get("chores")||[];
    const events=AppData.get("calendarEvents")||{};
    const groceries=AppData.get("groceryList")||{};
    const now=new Date(),key=[now.getFullYear(),String(now.getMonth()+1).padStart(2,"0"),String(now.getDate()).padStart(2,"0")].join("-");
    const remaining=chores.filter(x=>x.status!=="Completed").length;
    const eventsCount=Array.isArray(events[key])?events[key].length:0;
    const groceryCount=Object.values(groceries).reduce((total,arr)=>total+(Array.isArray(arr)?arr.filter(x=>!x.checked).length:0),0);
    const numbers={"fh-stat-chores":remaining,"fh-stat-events":eventsCount,"fh-stat-grocery":groceryCount};
    Object.entries(numbers).forEach(([id,count])=>{const el=$(id);if(el)el.textContent=String(count);});
    const date=$("fh-date-label");if(date)date.textContent=now.toLocaleDateString(undefined,{weekday:"long",month:"long",day:"numeric"});
  };
  function initialize(){
    const button=$("fh-more-trigger"),panel=$("fh-more-panel");
    button?.addEventListener("click",()=>{
      panel.hidden=!panel.hidden;
      button.setAttribute("aria-expanded",String(!panel.hidden));
      if(!panel.hidden)panel.querySelector("a")?.focus();
    });
    panel?.addEventListener("click",event=>{if(event.target.closest("a"))closeMore(false)});
    document.addEventListener("pointerdown",event=>{
      if(panel&&!panel.hidden&&!panel.contains(event.target)&&!button.contains(event.target))closeMore(false);
    });
    document.addEventListener("keydown",event=>{
      if(event.key==="Escape"&&panel&&!panel.hidden){event.preventDefault();closeMore(true);}
    });
    window.addEventListener("hashchange",updateNavigation);
    updateNavigation();
    const exportButton=$("export-data-btn");
    // Existing export and import remain functional and local to this browser.
    if(exportButton)exportButton.setAttribute("aria-label","Download a JSON backup of family information");
    document.querySelectorAll(".fh-tab").forEach(el=>el.addEventListener("click",event=>{
      if(el.id!=="fh-more-trigger")closeMore(false);
    }));
    announce("Family Hub is ready. Plans are stored in this browser.");
  }
  document.addEventListener("DOMContentLoaded",initialize);
})();
