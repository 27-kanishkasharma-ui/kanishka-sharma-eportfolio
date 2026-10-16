"""Kanishka Sharma - professional e-portfolio (single-page Streamlit microsite)."""
import base64
from pathlib import Path

import streamlit as st

ROOT = Path(__file__).parent
ASSETS = ROOT / "assets"
PROJ = ASSETS / "projects"
IMG = ASSETS / "img"

st.set_page_config(page_title="Kanishka Sharma | Finance Portfolio", page_icon="📊",
                   layout="wide", initial_sidebar_state="collapsed")

MIME = {".pdf": "application/pdf",
        ".xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        ".pbix": "application/octet-stream", ".html": "text/html"}
LINKEDIN = "https://www.linkedin.com/in/kanishkasharma2203/"
EMAIL = "27-kanishka.sharma@fiib.edu.in"
PHONE = "+91 9582472900"
GITHUB_REPO = "https://github.com/27-kanishkasharma-ui/kanishka-sharma-eportfolio"


# ---------------------------------------------------------------- helpers
@st.cache_resource(show_spinner=False)
def read_bytes(path: str) -> bytes:
    return Path(path).read_bytes()


def locate(path: Path):
    """Find a file in its folder, or at the top level of the repo if folders were flattened on upload."""
    if path.exists():
        return path
    flat = ROOT / path.name
    return flat if flat.exists() else None


def img_b64(path) -> str:
    return base64.b64encode(read_bytes(str(path))).decode()


def github_view_url(path: Path) -> str:
    return f"{GITHUB_REPO}/blob/main/{path.relative_to(ROOT).as_posix()}"


def download(label, path, key, primary=False):
    path = locate(path)
    if path is None:
        return
    st.download_button(label, data=read_bytes(str(path)), file_name=path.name,
                       mime=MIME.get(path.suffix, "application/octet-stream"), key=key,
                       type="primary" if primary else "secondary", width="stretch")


def file_buttons(files, key_prefix):
    for j, (label, rel) in enumerate(files):
        found = locate(PROJ / rel)
        if not found:
            continue
        d, v = st.columns([3, 1.3], gap="small")
        with d:
            download(f"⬇ {label}", found, f"{key_prefix}_{j}")
        with v:
            st.link_button("View ↗", github_view_url(found), width="stretch")


def picture(name, caption=None):
    p = locate(IMG / name)
    if p:
        st.image(str(p), width="stretch")
        if caption:
            st.markdown(f'<div class="cap">{caption}</div>', unsafe_allow_html=True)


def html(s):
    st.markdown(s, unsafe_allow_html=True)


# ---------------------------------------------------------------- styling
html("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,600;0,800;0,900;1,600&display=swap');
:root{--navy:#14264a;--navy2:#1F3864;--ink:#1d2430;--muted:#667085;--line:#e4e1d8;
      --paper:#ffffff;--cream:#f7f4ee;--gold:#c0912f;--gold-soft:#f5ead2;--teal:#2c6e74;}
html, body, .stApp{background:var(--cream) !important; color:var(--ink);}
.stApp{font-family:'Inter',sans-serif;}
.stMarkdown p, .stMarkdown li, .stMarkdown div, .stMarkdown span, button p{font-family:'Inter',sans-serif;}
[data-testid="stIconMaterial"]{font-family:'Material Symbols Rounded' !important;}
#MainMenu, footer, [data-testid="stToolbar"], [data-testid="stDecoration"]{visibility:hidden;height:0;}
header[data-testid="stHeader"]{background:transparent;height:0;}
.block-container{max-width:1160px;padding-top:1.2rem;padding-bottom:3rem;}

/* ---------- hero ---------- */
.hero{position:relative;background:var(--navy);border-radius:22px;padding:44px 46px 40px;overflow:hidden;
      display:grid;grid-template-columns:1fr 230px;gap:34px;align-items:center;margin-bottom:14px;}
.hero:before{content:"₹";position:absolute;right:-30px;bottom:-120px;font-family:'Playfair Display',serif;
      font-size:420px;font-weight:900;color:rgba(255,255,255,.04);line-height:1;}
.hero .eyebrow{font-size:.68rem;letter-spacing:3.5px;text-transform:uppercase;color:#e7c98a;font-weight:700;}
.hero h1{font-family:'Playfair Display',serif !important;font-weight:900;font-size:4.6rem;line-height:.95;
      color:#fff !important;margin:10px 0 14px;padding:0;letter-spacing:-1px;}
.hero h1 em{font-style:italic;color:#e7c98a;font-weight:600;}
.hero .tagline{font-size:1.25rem;color:#fff;font-weight:300;line-height:1.45;max-width:640px;}
.hero .tagline b{color:#e7c98a;font-weight:600;}
.hero .small{font-size:.85rem;color:#b7c3d9;margin-top:14px;line-height:1.6;max-width:640px;}
.hero img{width:230px;height:230px;object-fit:cover;border-radius:50% 50% 50% 12px;
      border:5px solid rgba(231,201,138,.55);position:relative;}
@media (max-width:800px){.hero{grid-template-columns:1fr;padding:30px 22px;text-align:center}
  .hero h1{font-size:3rem}.hero img{width:150px;height:150px;margin:0 auto;grid-row:1}
  .hero .tagline{font-size:1.05rem}}

/* ---------- numbers strip ---------- */
.strip{display:grid;grid-template-columns:repeat(4,1fr);background:var(--paper);border:1px solid var(--line);
      border-radius:18px;margin:18px 0 8px;overflow:hidden;}
.strip div{padding:20px 22px;border-right:1px solid var(--line);}
.strip div:last-child{border-right:none;}
.strip .n{font-family:'Playfair Display',serif;font-weight:900;font-size:2.9rem;color:var(--navy);line-height:1;padding:0;border:none;}
.strip .n sup{font-size:1rem;color:var(--gold);}
.strip .l{font-size:.66rem;letter-spacing:1.8px;text-transform:uppercase;color:var(--muted);margin-top:8px;font-weight:600;padding:0;border:none;}
@media (max-width:800px){.strip{grid-template-columns:repeat(2,1fr)}.strip > div{border-bottom:1px solid var(--line)}
  .strip .n{font-size:2.2rem}}

.nav{display:flex;flex-wrap:wrap;gap:6px;margin:14px 0 0;}
.nav a{font-size:.7rem;letter-spacing:1.6px;text-transform:uppercase;font-weight:700;color:var(--navy) !important;
      text-decoration:none;padding:7px 14px;border-radius:30px;border:1px solid var(--line);background:var(--paper);}
.nav a:hover{background:var(--navy);color:#fff !important;}

/* ---------- section headers: tiny label + huge title ---------- */
.sec{display:flex;align-items:flex-end;gap:18px;margin:64px 0 22px;scroll-margin-top:20px;}
.sec .num{font-family:'Playfair Display',serif;font-weight:900;font-size:5.4rem;line-height:.8;
      color:transparent;-webkit-text-stroke:1.5px var(--gold);}
.sec .k{font-size:.64rem;letter-spacing:3px;text-transform:uppercase;color:var(--gold);font-weight:700;}
.sec h2{font-family:'Playfair Display',serif !important;font-weight:800;font-size:2.9rem;color:var(--navy) !important;
      margin:2px 0 0;padding:0;line-height:1;}
.sec .s{font-size:.88rem;color:var(--muted);margin-top:8px;}
@media (max-width:800px){.sec .num{font-size:3.4rem}.sec h2{font-size:2rem}}

/* ---------- quote band ---------- */
.band{margin:56px 0 0;padding:34px 40px;border-left:6px solid var(--gold);background:var(--gold-soft);border-radius:0 18px 18px 0;}
.band p{font-family:'Playfair Display',serif !important;font-style:italic;font-size:2rem !important;line-height:1.25 !important;
      color:var(--navy) !important;margin:0;font-weight:600;}
.band .who{font-size:.66rem !important;letter-spacing:2.5px;text-transform:uppercase;font-style:normal;
      font-family:'Inter',sans-serif !important;color:var(--muted) !important;margin-top:12px;font-weight:700;}
@media (max-width:800px){.band p{font-size:1.4rem !important}}

/* ---------- cards ---------- */
[data-testid="stVerticalBlockBorderWrapper"]{background:var(--paper);border-radius:18px !important;border-color:var(--line) !important;}
[data-testid="stImage"] img{border-radius:12px;}
[data-testid="stElementContainer"]:has(.covermark){display:none;}
[data-testid="stElementContainer"]:has(.covermark) + [data-testid="stElementContainer"] img{height:auto !important;aspect-ratio:16/9;width:100% !important;object-fit:cover !important;object-position:top center;}
.metric{font-family:'Playfair Display',serif;font-weight:900;font-size:3.3rem;line-height:1;color:var(--navy);margin-top:4px;}
.metric small{font-family:'Inter',sans-serif;font-size:.62rem;letter-spacing:1.8px;text-transform:uppercase;color:var(--gold);
      font-weight:700;display:block;margin-top:6px;}
.ptitle{font-size:1.06rem;font-weight:700;color:var(--ink);margin:12px 0 4px;}
.stMarkdown p.one, .one{font-size:.9rem !important;color:var(--muted) !important;line-height:1.5;margin:0 0 10px;}
.tags{display:flex;flex-wrap:wrap;gap:5px;margin:6px 0 10px;}
.tag{font-size:.6rem;letter-spacing:1.2px;text-transform:uppercase;font-weight:700;padding:4px 9px;border-radius:20px;
      background:#eef1f7;color:var(--navy2);}
.tag.team{background:var(--gold-soft);color:#8a6418;}.tag.solo{background:#e3f0ef;color:var(--teal);}
.stMarkdown p.row, .row{font-size:.87rem !important;line-height:1.55;margin:0 0 8px;}
.row b{color:var(--navy);}
.cap{font-size:.66rem;letter-spacing:1.6px;text-transform:uppercase;color:var(--muted);font-weight:700;margin:6px 2px 14px;}
.tile3{background:var(--navy);border-radius:12px;aspect-ratio:16/9;padding:0 18px;display:flex;align-items:center;justify-content:center;gap:10px;}
.tile3 span{font-family:'Playfair Display',serif;font-weight:900;font-size:2.2rem;color:#fff;}
.tile3 i{font-style:normal;color:#e7c98a;font-size:1.4rem;}
.t3c{font-size:.62rem;letter-spacing:1.6px;text-transform:uppercase;color:var(--muted);text-align:center;margin-top:6px;font-weight:700;}

/* ---------- featured ---------- */
.feat{background:var(--navy);border-radius:20px;padding:32px 34px;color:#dbe3f1;}
.feat .k{font-size:.64rem;letter-spacing:3px;text-transform:uppercase;color:#e7c98a;font-weight:700;}
.feat h3{font-family:'Playfair Display',serif !important;font-size:2.3rem;color:#fff !important;margin:6px 0 10px;padding:0;line-height:1.05;}
.stMarkdown .feat p, .feat p{color:#c9d4e6 !important;font-size:.92rem !important;line-height:1.6;}
.feat p b{color:#fff;}
.kp{display:grid;grid-template-columns:repeat(2,1fr);gap:12px;margin-top:16px;}
.kp > div{border-top:1px solid rgba(255,255,255,.18);padding-top:10px;}
.kp .n{font-family:'Playfair Display',serif;font-size:2.4rem;font-weight:900;color:#fff;line-height:1;border:none;padding:0;}
.kp .l{font-size:.6rem;letter-spacing:1.6px;text-transform:uppercase;color:#e7c98a;margin-top:6px;font-weight:700;border:none;padding:0;}
.stMarkdown p.tiny, .tiny{font-size:.72rem !important;color:#94a3bf !important;margin-top:14px;}

/* ---------- experience ---------- */
.exp{display:grid;grid-template-columns:190px 1fr;gap:26px;padding:26px 0;border-top:1px solid var(--line);}
.exp .when{font-family:'Playfair Display',serif;font-size:1.5rem;font-weight:800;color:var(--gold);line-height:1.1;}
.exp .where{font-size:.62rem;letter-spacing:1.8px;text-transform:uppercase;color:var(--muted);margin-top:8px;font-weight:700;}
.exp .role{font-size:1.25rem;font-weight:700;color:var(--navy);}
.exp ul{margin:8px 0 0;padding-left:18px;}
.stMarkdown .exp li, .exp li{font-size:.88rem !important;line-height:1.55;margin-bottom:5px;}
@media (max-width:800px){.exp{grid-template-columns:1fr;gap:6px}}

/* ---------- skills ---------- */
.skills{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;}
.sk{background:var(--paper);border:1px solid var(--line);border-radius:18px;padding:22px;}
.sk .big{font-family:'Playfair Display',serif;font-weight:900;font-style:italic;font-size:2.6rem;color:var(--navy);line-height:1;}
.sk .lbl{font-size:.6rem;letter-spacing:2px;text-transform:uppercase;color:var(--gold);font-weight:700;margin:6px 0 12px;}
.chip{display:inline-block;font-size:.78rem;background:var(--cream);border:1px solid var(--line);border-radius:16px;padding:4px 11px;margin:0 5px 7px 0;}
@media (max-width:800px){.skills{grid-template-columns:1fr}}

/* ---------- misc ---------- */
.edu{background:var(--paper);border:1px solid var(--line);border-radius:18px;padding:22px 24px;min-height:205px;}
.edu .g{font-family:'Playfair Display',serif;font-weight:900;font-size:3rem;color:var(--navy);line-height:1;}
.edu .gl{font-size:.6rem;letter-spacing:2px;text-transform:uppercase;color:var(--gold);font-weight:700;margin-top:6px;}
.edu .t{font-weight:700;color:var(--ink);margin-top:14px;font-size:1rem;}
.edu .u{font-size:.84rem;color:var(--muted);}
.lst{margin:0;padding-left:18px;}.stMarkdown .lst li, .lst li{font-size:.88rem !important;line-height:1.55;margin-bottom:6px;}
.contact{background:var(--navy);border-radius:22px;padding:40px 42px;margin-top:64px;color:#fff;}
.contact h3{font-family:'Playfair Display',serif !important;font-size:3.4rem;font-weight:900;color:#fff !important;margin:0;padding:0;line-height:1;}
.contact h3 em{color:#e7c98a;font-weight:600;}
.stMarkdown .contact p, .contact p{color:#c9d4e6 !important;font-size:.95rem !important;margin:12px 0 0;}
.contact a{color:#e7c98a !important;font-weight:600;text-decoration:none;}

.stDownloadButton button, .stLinkButton a{border-radius:10px !important;font-weight:600 !important;font-size:.82rem !important;}
.stDownloadButton button[kind="secondary"], .stLinkButton a[kind="secondary"]{background:#fff !important;color:var(--navy) !important;border:1px solid #d6d2c6 !important;}
.stDownloadButton button[kind="primary"], .stLinkButton a[kind="primary"]{background:var(--gold) !important;border-color:var(--gold) !important;color:#fff !important;}
[data-testid="stExpander"]{background:var(--paper);border-radius:12px;border-color:var(--line) !important;}
[data-testid="stExpander"] summary p{font-size:.72rem !important;letter-spacing:1.6px;text-transform:uppercase;font-weight:700;color:var(--navy);}
[data-testid="stSelectbox"] label p{font-size:.62rem !important;letter-spacing:2.4px;text-transform:uppercase;font-weight:700;color:var(--gold) !important;}
</style>
""")


def section(anchor, num, kicker, title, sub=""):
    html(f'<div class="sec" id="{anchor}"><div class="num">{num}</div><div><div class="k">{kicker}</div>'
         f'<h2>{title}</h2>{f"<div class=s>{sub}</div>" if sub else ""}</div></div>')


# ---------------------------------------------------------------- data
PROJECTS = [
    {"key": "titan", "title": "Titan Company: Equity Valuation Model", "cover": "cover_titan.jpg",
     "metric": "HOLD", "metric_l": "Verdict from DCF, comps & DDM",
     "tags": [("Individual", "solo"), ("Equity Valuation", "")],
     "one": "Is Titan's ~Rs.3,300 share price backed by its fundamentals? A 16-sheet model says the market is paying for growth beyond five years.",
     "problem": "Is Titan's share price of about Rs.3,300 supported by its fundamentals?",
     "did": "Macro and industry analysis, 7 years of actuals, a 5-year forecast with a 3-scenario switch, a CAPM beta regressed on ~3,700 daily SENSEX and Titan prices (2011–25), WACC of 10.51%, a 2-stage FCFF DCF, EVA, a dividend discount model and relative valuation against 4 listed peers.",
     "tools": "Excel (VLOOKUP scenario switch, SLOPE regression), DCF, DDM, P/E, EV/EBITDA, EV/Sales, P/BV",
     "result": "A 5×5 WACC vs terminal-growth grid showed even the most optimistic DCF case sits below the market price. The model includes a cash-flow-to-balance-sheet reconciliation check.",
     "files": [("Excel model", "titan-valuation/Titan_Valuation_Model.xlsx"), ("Valuation report", "titan-valuation/Titan_Valuation_Report.pdf")]},
    {"key": "three", "title": "Integrated Three-Statement Financial Model", "cover": None,
     "metric": "5 / 5", "metric_l": "Forecast years that balance",
     "tags": [("Individual", "solo"), ("Excel modelling test", "")],
     "one": "A fully linked 5-year forecast with a debt schedule, a covenant-style interest step-up and a convertible bond.",
     "problem": "Build a 5-year forecast from a fixed set of operating and financing assumptions.",
     "did": "Linked the Income Statement, Balance Sheet and Cash Flow Statement with a debt schedule, an interest rate that steps up from 6% to 7% if interest coverage falls below 6x, convertible bond conversion, a subsidiary stake bought and sold in two stages, and warranty provisions with separate cash payouts.",
     "tools": "Excel, three-statement modelling, debt schedule, FCFF valuation",
     "result": "Balance sheet balances in every forecast year; calculated DSCR, interest coverage, ROCE and ROE, and an FCFF valuation with year-wise WACC.",
     "files": [("Excel model", "three-statement-model/Three_Statement_Financial_Model.xlsx")]},
    {"key": "nutribox", "title": "Nutri-Box: Seed Funding Investment Case", "cover": "cover_nutribox.jpg",
     "metric": "17.3x", "metric_l": "Projected MOIC · ~77% IRR",
     "tags": [("Team of 6", "team"), ("Private Equity & VC", "")],
     "one": "An investor-ready case for a subscription meal startup: Rs.1.75 crore raise at Rs.12.83 crore pre-money.",
     "problem": "Build an investor-ready case for a seed-stage, subscription-based daily meal delivery startup.",
     "did": "As a team, we sized the market, built unit economics and 5-year projections, set the valuation, modelled returns under three scenarios, and presented it as an investment report and pitch deck.",
     "tools": "Excel, forward revenue-multiple valuation, MOIC / IRR, scenario analysis, PowerPoint",
     "result": "Rs.1.75 crore raise at Rs.12.83 crore pre-money (~12% equity); base case ~17.3x MOIC and ~77% IRR on a 5-year exit; LTV:CAC ~13.9:1.",
     "files": [("Investment report", "nutribox-seed-investment/NutriBox_Investment_Report.pdf"), ("Pitch deck", "nutribox-seed-investment/NutriBox_Investor_Pitch_Deck.pdf")]},
    {"key": "mf", "title": "Mutual Fund Performance Analysis", "cover": "cover_mutualfund.jpg",
     "metric": "+6.46%", "metric_l": "Jensen's alpha of the top fund",
     "tags": [("Individual", "solo"), ("Portfolio analysis", "")],
     "one": "Three multi-cap funds, one benchmark, 1,204 trading days. Which one actually earned its returns?",
     "problem": "Which of three multi-cap funds delivered the best risk-adjusted return against a common benchmark?",
     "did": "Aligned NAV data for Nippon India, ICICI Prudential and Quant multi-cap funds with the NIFTY500 Multicap 50:25:25 TRI over 1,204 common trading days (Sep 2021 – Aug 2026), then calculated annualised return and risk, beta, Sharpe, Treynor and Jensen's alpha.",
     "tools": "Excel (STDEV, SLOPE, SQRT), CAPM-based performance metrics",
     "result": "Nippon India Multi Cap led: 17.80% annualised return vs 11.47% for the benchmark, Sharpe 0.74, alpha +6.46%.",
     "files": [("Excel analysis", "mutual-fund-analysis/Mutual_Fund_Analysis.xlsx"), ("Report", "mutual-fund-analysis/Mutual_Fund_Analysis_Report.pdf")]},
    {"key": "jewel", "title": "Jewellery Industry: KPI Dashboard & Titan Analytics", "cover": "cover_jewellery.jpg",
     "metric": "5", "metric_l": "Listed jewellers benchmarked",
     "tags": [("Team of 5 + individual Excel", "team"), ("Financial Analytics", "")],
     "one": "A Power BI dashboard comparing Titan, Kalyan, Senco, PC Jeweller and Thangamayil, plus my own Monte Carlo workbook on Titan.",
     "problem": "How do India's listed jewellers compare on growth, profitability and financial strength?",
     "did": "As a team, we built a Power BI dashboard and report. In my individual Excel workbook on Titan, I analysed ratios and operating, financial and total leverage, projected FCFF, and ran a ~1,000-iteration Monte Carlo simulation (NORM.INV / RAND) on its cash-flow drivers.",
     "tools": "Power BI, Excel, Monte Carlo simulation, ratio and leverage analysis",
     "result": "Titan led on scale, margins and balance-sheet strength; Kalyan and Senco grew fastest. The .pbix file needs Power BI Desktop.",
     "files": [("Team report", "jewellery-industry-analysis/Jewellery_Industry_Report.pdf"),
               ("My Excel: Titan analytics", "jewellery-industry-analysis/Titan_Financial_Analytics_Monte_Carlo.xlsx"),
               ("Power BI file (.pbix)", "jewellery-industry-analysis/Jewellery_Industry_Dashboard.pbix")]},
    {"key": "sbi", "title": "SBI Funds Management: Investor Deck", "cover": "cover_sbi.jpg",
     "metric": "37", "metric_l": "Slide institutional investor deck",
     "tags": [("Individual", "solo"), ("Corporate Mentoring Program", "")],
     "one": "Is India's largest AMC ready to list? Business model, risk, ESG and a 5-AMC peer comparison.",
     "problem": "Is SBI Funds Management positioned for a public listing, and how would investors assess it?",
     "did": "Built a 37-slide deck covering the fee-based business model, AUM growth, risk management, financials and ESG, and a peer comparison with HDFC, ICICI Prudential, Nippon India and Kotak AMCs.",
     "tools": "PowerPoint, P/AUM and EV/EBITDA comparison, fee-yield trend analysis",
     "result": "Highlighted ~24% 5-year AUM CAGR, a 79% EBITDA margin and 32.8% 5-year PAT CAGR, with fee-yield compression as the main risk.",
     "files": [("Investor deck (19 MB)", "sbi-funds-investor-deck/SBI_Funds_Management_Investor_Deck.pdf")]},
]


def cover(p):
    found = locate(IMG / p["cover"]) if p["cover"] else None
    if found:
        html('<span class="covermark"></span>')
        st.image(str(found), width="stretch")
    else:
        html('<div class="tile3"><span>IS</span><i>⇄</i><span>BS</span><i>⇄</i><span>CFS</span></div>'
             '<div class="t3c">Linked statements · debt schedule · DSCR</div>')


# ---------------------------------------------------------------- hero
photo = locate(ASSETS / "profile.jpg")
photo_html = f'<img src="data:image/jpeg;base64,{img_b64(photo)}" alt="Kanishka Sharma">' if photo else ""
html(f"""
<div class="hero">
  <div>
    <div class="eyebrow">PGDM Finance · FIIB New Delhi · 2025–27</div>
    <h1>Kanishka<br><em>Sharma</em></h1>
    <div class="tagline">I build <b>financial models</b>, value companies and analyse portfolios, mostly in Excel.</div>
    <div class="small">B.Com (Hons.), University of Delhi. At Ummeed Housing Finance I mapped manual finance processes,
    built the cost-benefit case for automating them and demonstrated a risk-based audit sampling tool to the CFO.
    Every project below comes with its actual files, so you can check the work, not just read about it.</div>
  </div>
  {photo_html}
</div>
""")

c1, c2, c3, c4 = st.columns(4)
resume = locate(ASSETS / "resume" / "Kanishka_Sharma_Resume.pdf")
with c1:
    download("⬇ Download resume", ASSETS / "resume" / "Kanishka_Sharma_Resume.pdf", "cv1", primary=True)
with c2:
    if resume:
        st.link_button("View resume ↗", github_view_url(resume), width="stretch")
with c3:
    st.link_button("LinkedIn ↗", LINKEDIN, width="stretch")
with c4:
    st.link_button("Email me ✉", f"mailto:{EMAIL}", width="stretch")

# project dropdown, right next to the resume
choice = st.selectbox("Jump to a project", [p["title"] for p in PROJECTS], index=None,
                      placeholder="Pick a project to see it and open its files…")
if choice:
    p = next(x for x in PROJECTS if x["title"] == choice)
    with st.container(border=True):
        a, b = st.columns([1, 1.25], gap="large")
        with a:
            cover(p)
        with b:
            html(f'<div class="metric">{p["metric"]}<small>{p["metric_l"]}</small></div>'
                 f'<div class="ptitle">{p["title"]}</div><p class="one">{p["one"]}</p>')
            file_buttons(p["files"], f"jump_{p['key']}")

html("""
<div class="strip">
  <div><div class="n">9.58</div><div class="l">PGDM CGPA</div></div>
  <div><div class="n">6</div><div class="l">projects with real files</div></div>
  <div><div class="n">4.8<sup>x</sup></div><div class="l">benefit-cost case at Ummeed</div></div>
  <div><div class="n">Top 20</div><div class="l">Global Scaling Challenge</div></div>
</div>
<div class="nav"><a href="#featured">Featured</a><a href="#projects">Projects</a><a href="#experience">Experience</a>
<a href="#skills">Skills</a><a href="#education">Education</a><a href="#recognition">Recognition</a><a href="#moments">Moments</a><a href="#contact">Contact</a></div>
""")

# ---------------------------------------------------------------- 01 featured
section("featured", "01", "Featured · internship prototype", "The audit sample builder")
f1, f2 = st.columns([1.05, 1], gap="large")
with f1:
    html("""<div class="feat"><div class="k">Ummeed Housing Finance · demonstrated to the CFO</div>
    <h3>Which branches should internal audit visit this year?</h3>
    <p>The 8-member audit team rebuilt its sampling plan by hand across <b>130 branches</b>. My tool scores every branch on
    inherent risk (disbursement, growth, NPA) and control risk (findings, vacancies, overrides), fills the team's capacity with the
    riskiest first, then adds a materiality floor, a blind random pick and any branch left unaudited for two cycles, in line with RBI's RBIA framework.</p>
    <div class="kp"><div><div class="n">19.5L</div><div class="l">Year-1 cost, AP automation (Rs.)</div></div>
    <div><div class="n">95.2L</div><div class="l">Annual benefit (Rs.)</div></div>
    <div><div class="n">3.4</div><div class="l">Months to payback</div></div>
    <div><div class="n">4.8x</div><div class="l">Benefit-cost ratio</div></div></div>
    <p class="tiny">Demo runs on 15 sample branches with illustrative figures, not Ummeed's live data.</p></div>""")
with f2:
    picture("cover_audit_tool.jpg", "The tool's branch risk map · bubble size = loan book")
    audit_html = locate(ASSETS / "audit_sample_builder.html")
    if audit_html:
        with st.expander("Try the live tool"):
            st.iframe(audit_html, height=1650)

# ---------------------------------------------------------------- 02 projects
section("projects", "02", "Evidence", "Projects", "Six projects. One number each. Open any file to check it.")
st.link_button("Browse all project files on GitHub ↗", GITHUB_REPO)
for i in range(0, len(PROJECTS), 3):
    cols = st.columns(3, gap="medium")
    for k, col in enumerate(cols):
        if i + k >= len(PROJECTS):
            continue
        p = PROJECTS[i + k]
        with col, st.container(border=True):
            cover(p)
            tags = "".join(f'<span class="tag {c}">{t}</span>' for t, c in p["tags"])
            html(f'<div class="metric">{p["metric"]}<small>{p["metric_l"]}</small></div>'
                 f'<div class="ptitle">{p["title"]}</div><div class="tags">{tags}</div><p class="one">{p["one"]}</p>')
            with st.expander("How I did it"):
                html(f'<p class="row"><b>Problem.</b> {p["problem"]}</p><p class="row"><b>What I did.</b> {p["did"]}</p>'
                     f'<p class="row"><b>Tools.</b> {p["tools"]}</p><p class="row"><b>Output.</b> {p["result"]}</p>')
            file_buttons(p["files"], f"p_{p['key']}")

html('<div class="band"><p>"A model is only as good as the question it answers, and the check that proves it balances."</p>'
     '<div class="who">How I approach every spreadsheet</div></div>')

# ---------------------------------------------------------------- 03 experience
section("experience", "03", "Work", "Experience")
html("""
<div class="exp"><div><div class="when">Apr – Jun<br>2026</div><div class="where">Gurugram · mentor: CFO</div></div>
<div><div class="role">Finance Intern, Ummeed Housing Finance</div><ul>
<li>Mapped as-is and to-be workflows for Accounts Payable, Procurement and Internal Audit, identifying a 12–18 day approval-routing bottleneck and audit-trail gaps against RBI's IT governance directions.</li>
<li>Built the cost-benefit case for a connected automation system (~550 invoices a month): Rs.19.5 lakh Year-1 investment, Rs.95.2 lakh annual benefit, 3.4-month payback and 4.8x benefit-cost ratio, across three scenarios.</li>
<li>Designed and demonstrated to the CFO a risk-based audit sampling prototype aligned with RBI's RBIA framework.</li>
<li>Enabled a data-backed Rs.3 crore treasury vendor decision by benchmarking quotes from 2 vendors across a 6-category, 25+ parameter framework.</li>
<li>Cross-verified 30–40 client transactions on the NESL platform, uncovering inaccurate balance data reported by a client.</li></ul></div></div>
<div class="exp"><div><div class="when">Jan<br>2026</div><div class="where">New Delhi</div></div>
<div><div class="role">Social Work Intern, Habitat India</div><ul>
<li>Built an Excel model benchmarking circular-economy and emissions practices of 5 leading tech companies against industry standards, and flagged potential greenwashing risks in their sustainability disclosures.</li></ul></div></div>
""")

# ---------------------------------------------------------------- 04 skills
section("skills", "04", "Capabilities", "Skills", "Each one is used in at least one project above.")
html("""<div class="skills">
<div class="sk"><div class="big">Value</div><div class="lbl">Valuation & corporate finance</div>
<span class="chip">DCF (FCFF)</span><span class="chip">Comparable companies</span><span class="chip">DDM</span><span class="chip">WACC & CAPM</span>
<span class="chip">EVA</span><span class="chip">MOIC / IRR</span><span class="chip">Cost-benefit analysis</span></div>
<div class="sk"><div class="big">Model</div><div class="lbl">Modelling & analysis</div>
<span class="chip">Three-statement models</span><span class="chip">Debt schedules</span><span class="chip">Scenario analysis</span>
<span class="chip">Sensitivity analysis</span><span class="chip">Monte Carlo</span><span class="chip">Ratio analysis</span><span class="chip">Sharpe · Treynor · alpha</span></div>
<div class="sk"><div class="big">Tools</div><div class="lbl">What I work in</div>
<span class="chip">Excel</span><span class="chip">Power BI</span><span class="chip">PowerPoint</span><span class="chip">Word</span>
<span class="chip">Python (basics)</span><span class="chip">Tally ERP</span></div></div>""")

# ---------------------------------------------------------------- 05 education
section("education", "05", "Academics", "Education")
e1, e2, e3 = st.columns(3, gap="medium")
with e1:
    html('<div class="edu"><div class="g">9.58</div><div class="gl">CGPA</div><div class="t">PGDM – Finance Management</div>'
         '<div class="u">Fortune Institute of International Business, New Delhi · 2025–27</div></div>')
with e2:
    html('<div class="edu"><div class="g">7.50</div><div class="gl">CGPA</div><div class="t">B.Com (Hons.)</div>'
         '<div class="u">University of Delhi · 2021–24</div></div>')
with e3:
    html('<div class="edu"><div class="g">4</div><div class="gl">Certifications · LinkedIn Learning</div><ul class="lst" style="margin-top:12px">'
         '<li>Corporate Finance Foundations</li><li>Understanding Capital Markets</li><li>Excel for Accounting</li>'
         '<li>Accounting Foundations – Budgeting</li></ul></div>')

# ---------------------------------------------------------------- 06 recognition
section("recognition", "06", "Beyond the classroom", "Recognition & leadership")
r1, r2 = st.columns([1, 1.15], gap="large")
with r1:
    picture("cmp_certificate.jpg", "Certificate of completion · Corporate Mentoring Program")
with r2:
    html("""<div class="metric">Mentee<small>Corporate Mentoring Program · Nov 2025 – Feb 2026</small></div>
    <p class="row" style="margin-top:12px">Evaluated IPO subscription trends, pricing and post-listing performance under my corporate mentor,
    and built the <b>SBI Funds Management investor deck</b> shown in Projects.</p>""")
    html("""<div style="margin-top:22px"><div class="metric">Top 20<small>Global finish · Global Scaling Challenge</small></div>
    <p class="row" style="margin-top:10px">Led the team to a Top 3 position in the Asia-Oceania regional round.</p></div>""")
    html("""<ul class="lst" style="margin-top:18px">
    <li>Led Satyawati College's first-ever online management fest, ranked among the Top 10 UG festivals at the Unstop UG Awards 2024.</li>
    <li><b>Student Ambassador</b>, Centre of Behavioral Insights (Aug 2025 – Feb 2026): managed the development and selection of case studies for student competitions.</li>
    <li><b>Student Council</b>, SPAC (Aug 2025 – present).</li></ul>""")

# ---------------------------------------------------------------- 07 moments
section("moments", "07", "Gallery", "Moments")
g = st.columns(3, gap="medium")
with g[0]:
    picture("cmp_grand_finale.jpg", "Corporate Mentoring Program 2026 · Grand Finale")
    picture("photo_discussion.jpg")
    picture("photo_group_session.jpg")
with g[1]:
    picture("phdcci_delegate_badge.jpg", "Delegate · PHDCCI 120th Annual Session · Bharat Mandapam, 9 Oct 2025")
    picture("photo_guest_session.jpg")
with g[2]:
    picture("photo_champion_within_session.jpg", "\"Awaken the Champion Within\" session at FIIB")
    picture("photo_delegation.jpg")

# ---------------------------------------------------------------- contact
html(f"""<div class="contact" id="contact"><h3>Let's <em>talk.</em></h3>
<p>Open to roles in financial modelling, valuation and portfolio reporting.</p>
<p>✉ <a href="mailto:{EMAIL}">{EMAIL}</a> &nbsp;·&nbsp; ☎ {PHONE} &nbsp;·&nbsp;
<a href="{LINKEDIN}" target="_blank">LinkedIn ↗</a> &nbsp;·&nbsp; New Delhi, India</p></div>""")
