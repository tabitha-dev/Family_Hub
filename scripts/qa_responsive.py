#!/usr/bin/env python3
"""Isolated Chromium smoke tests for Family Hub across desktop/mobile widths."""
import asyncio, json
from pathlib import Path
from playwright.async_api import async_playwright

ROOT="http://127.0.0.1:8000/"
OUT=Path("qa-output")
OUT.mkdir(exist_ok=True)

async def main():
 results=[]
 async with async_playwright() as p:
  browser=await p.chromium.launch(headless=True,args=["--no-sandbox"])
  for width,height,label in [(320,740,"small-phone"),(390,844,"phone"),(768,900,"tablet"),(1024,768,"laptop"),(1440,900,"desktop")]:
   context=await browser.new_context(viewport={"width":width,"height":height},accept_downloads=True,reduced_motion="reduce")
   page=await context.new_page()
   errors=[]
   page.on("pageerror", lambda e: errors.append(str(e)))
   await page.goto(ROOT,wait_until="domcontentloaded",timeout=30000)
   await page.locator("#fh-hero-heading").wait_for(state="visible",timeout=12000)
   await page.wait_for_timeout(450)
   metrics=await page.evaluate("""() => ({w:innerWidth,scroll:document.documentElement.scrollWidth,css:!![...document.styleSheets].find(s=>s.href?.includes('family-hub-ui.css')),hero:document.querySelector('.fh-hero').getBoundingClientRect().width})""")
   assert metrics["scroll"]<=width+2,(label,"horizontal overflow",metrics)
   assert metrics["css"],(label,"stylesheet missing")
   assert metrics["hero"]>220,(label,"hero missing",metrics)
   assert await page.locator("#fh-stat-chores").is_visible()
   if width<768:
    button=page.locator("#fh-more-trigger")
    assert await button.is_visible(),(label,"mobile More missing")
    await button.click()
    assert await page.locator("#fh-more-panel").is_visible(),(label,"More panel not open")
    await page.locator('#fh-more-panel a[href="#settings"]').click()
   else:
    await page.locator('#sidebar-nav a[href="#settings"]').click()
   await page.locator("#user-name-input").wait_for(state="visible")
   await page.locator("#user-name-input").fill("Demo Family")
   await page.locator("#family-member-name").fill("Alex")
   await page.locator("#add-family-member-form button[type=submit]").click()
   assert await page.locator("#family-members-container").get_by_text("Alex").is_visible()
   await page.goto(ROOT+"#grocery-lists",wait_until="domcontentloaded")
   await page.locator("#add-grocery-item-btn").wait_for()
   await page.locator("#add-grocery-item-btn").click()
   await page.locator("#grocery-item-name").fill("Oats & milk")
   await page.locator("#grocery-item-category").fill("Breakfast")
   await page.locator('#add-grocery-item-form button[type="submit"]').click()
   assert await page.locator("#grocery-list-container").get_by_text("Oats & milk").count()==1,(label,"grocery add")
   await page.reload(wait_until="domcontentloaded")
   assert await page.locator("#grocery-list-container").get_by_text("Oats & milk").count()==1,(label,"grocery persistence")
   await page.goto(ROOT+"#calendar",wait_until="domcontentloaded")
   assert await page.locator("#month-year-header").is_visible()
   await page.locator("#next-month-btn").click()
   assert await page.locator("#calendar-grid button").count()>=28
   await page.goto(ROOT+"#meal-plans",wait_until="domcontentloaded")
   cell=page.locator('.meal-cell[data-day-index="0"][data-meal="dinner"]')
   await cell.fill("Veggie pasta")
   await cell.press("Tab")
   await page.reload(wait_until="domcontentloaded")
   assert "Veggie pasta" in await page.locator('.meal-cell[data-day-index="0"][data-meal="dinner"]').inner_text(),(label,"meal persistence")
   if label in ("desktop","phone","small-phone"):
    await page.goto(ROOT,wait_until="domcontentloaded")
    await page.wait_for_timeout(300)
    await page.screenshot(path=str(OUT/f"{label}-dashboard.png"),full_page=False)
   assert not errors,(label,"JavaScript errors",errors)
   results.append({"viewport":label,"width":width,"responsive":"pass","grocery":"pass","calendar":"pass","mealPersistence":"pass","javascriptErrors":errors})
   await context.close()
  await browser.close()
 (OUT/"results.json").write_text(json.dumps(results,indent=2))
 print(json.dumps(results,indent=2))

if __name__=="__main__":asyncio.run(main())
