#!/usr/bin/env python3
"""Automated axe-core audit; manual screen-reader review is still required."""
import asyncio,json
from pathlib import Path
from playwright.async_api import async_playwright

async def run():
  failures=[]
  records=[]
  async with async_playwright() as p:
    browser=await p.chromium.launch(headless=True,args=["--no-sandbox"])
    for width,height in [(390,844),(1440,900)]:
      context=await browser.new_context(viewport={"width":width,"height":height},reduced_motion="reduce")
      page=await context.new_page()
      for route in ["dashboard","calendar","grocery-lists","settings"]:
        await page.goto("http://127.0.0.1:8000/#"+route,wait_until="domcontentloaded")
        await page.wait_for_timeout(170)
        await page.add_script_tag(path="node_modules/axe-core/axe.min.js")
        results=await page.evaluate("""async ()=> {
           const out=await axe.run(document,{runOnly:{type:'tag',values:['wcag2a','wcag2aa','wcag21aa','wcag22aa']}});
           return out.violations.map(x=>({id:x.id,impact:x.impact,nodes:x.nodes.slice(0,3).map(y=>({html:y.html,summary:y.failureSummary}))}));
        }""")
        records.append({"width":width,"route":route,"violations":results})
        for item in results:
          if item["impact"] in ("critical","serious"):
            failures.append({"width":width,"route":route,**item})
      await context.close()
    await browser.close()
  Path("qa-output").mkdir(exist_ok=True)
  Path("qa-output/axe-results.json").write_text(json.dumps(records,indent=2))
  print(json.dumps({"issues":records,"criticalOrSerious":failures},indent=2))
  if failures:raise SystemExit("Serious/critical accessibility violations detected")

if __name__=="__main__":asyncio.run(run())
