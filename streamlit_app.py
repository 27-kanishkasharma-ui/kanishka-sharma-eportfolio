"""Kanishka Sharma - professional e-portfolio (single-page Streamlit microsite)."""
import base64
from pathlib import Path

import streamlit as st

ROOT = Path(__file__).parent
ASSETS = ROOT / "assets"
PROJ = ASSETS / "projects"

st.set_page_config(
    page_title="Kanishka Sharma | Finance Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

MIME = {
    ".pdf": "application/pdf",
    ".xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    ".pbix": "application/octet-stream",
    ".html": "text/html",
}

LINKEDIN = "https://www.linkedin.com/in/kanishkasharma2203/"
EMAIL = "27-kanishka.sharma@fiib.edu.in"
PHONE = "+91 9582472900"


@st.cache_resource(show_spinner=False)
def read_bytes(path: str) -> bytes:
    return Path(path).read_bytes()


def img_b64(path: Path) -> str:
    return base64.b64encode(read_bytes(str(path))).decode()


def download(label: str, path: Path, key: str, primary: bool = False):
    """Download button that quietly skips a file that is missing from the repo."""
    if not path.exists():
        return
    st.download_button(
        label,
        data=read_bytes(str(path)),
        file_name=path.name,
        mime=MIME.get(path.suffix, "application/octet-stream"),
        key=key,
        type="primary" if primary else "secondary",
        width="stretch",
    )


# ---------------------------------------------------------------- styling
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Source+Serif+4:opsz,wght@8..60,600;8..60,700&display=swap');

:root{
  --navy:#1F3864; --navy-deep:#14264a; --ink:#1f2733; --muted:#5d6675;
  --line:#e2e6ee; --paper:#ffffff; --bg:#f6f7fa; --gold:#b8892d; --gold-soft:#f6efe1;
  --teal:#2c6e74; --teal-soft:#e5f0f0;
}
html, body, .stApp{background:var(--bg) !important; color:var(--ink);}
.stApp{font-family:'Inter',sans-serif;}
.stMarkdown p, .stMarkdown li, .stMarkdown div, .stMarkdown span, button p{font-family:'Inter',sans-serif;}
[data-testid="stIconMaterial"], .material-symbols-rounded{font-family:'Material Symbols Rounded' !important;}
#MainMenu, footer, [data-testid="stToolbar"], [data-testid="stDecoration"]{visibility:hidden; height:0;}
header[data-testid="stHeader"]{background:transparent; height:0;}
.block-container{max-width:1120px; padding-top:1.4rem; padding-bottom:3rem;}

/* hero */
.hero{background:linear-gradient(135deg,var(--navy) 0%,var(--navy-deep) 100%); color:#fff;
  border-radius:18px; margin-bottom:14px; padding:34px 38px; display:flex; gap:32px; align-items:center;}
.hero img{width:150px; height:150px; border-radius:50%; object-fit:cover; flex:none;
  border:4px solid rgba(255,255,255,.18);}
.hero h1{font-family:'Source Serif 4',serif !important; font-size:2.35rem; font-weight:700; margin:0; color:#fff !important; line-height:1.1; padding:0;}
.hero .headline{color:#e7c98a; font-weight:600; font-size:1rem; margin:8px 0 12px; letter-spacing:.2px;}
.hero p{color:#dbe3f1 !important; font-size:.95rem; line-height:1.6; margin:0; max-width:760px;}
@media (max-width:760px){
  .hero{flex-direction:column; text-align:center; padding:26px 20px; gap:16px;}
  .hero h1{font-size:1.8rem;}
  .hero img{width:118px; height:118px;}
}

/* stats + nav */
.stats{display:grid; grid-template-columns:repeat(4,1fr); gap:12px; margin:16px 0 6px;}
.stat{background:var(--paper); border:1px solid var(--line); border-radius:12px; padding:14px 16px;}
.stat .n{font-family:'Source Serif 4',serif; font-size:1.55rem; font-weight:700; color:var(--navy); line-height:1;}
.stat .l{font-size:.78rem; color:var(--muted); margin-top:5px;}
@media (max-width:760px){.stats{grid-template-columns:repeat(2,1fr);}}
.nav{display:flex; flex-wrap:wrap; gap:8px; margin:12px 0 4px;}
.nav a{font-size:.82rem; font-weight:600; color:var(--navy) !important; text-decoration:none;
  background:var(--paper); border:1px solid var(--line); border-radius:20px; padding:6px 14px;}
.nav a:hover{border-color:var(--navy);}

/* sections */
.sec{margin:38px 0 14px; scroll-margin-top:20px;}
.sec .kicker{font-size:.74rem; font-weight:700; letter-spacing:1.6px; text-transform:uppercase; color:var(--gold);}
.sec h2{font-family:'Source Serif 4',serif !important; font-size:1.65rem; color:var(--navy) !important; margin:2px 0 0; padding:0;}
.sec .sub{color:var(--muted); font-size:.92rem; margin-top:4px;}

/* cards */
.card-title{font-family:'Source Serif 4',serif; font-size:1.18rem; font-weight:700; color:var(--navy); margin:0 0 6px; line-height:1.3;}
.tags{display:flex; flex-wrap:wrap; gap:6px; margin-bottom:10px;}
.tag{font-size:.72rem; font-weight:600; padding:3px 9px; border-radius:20px; background:#eef1f7; color:var(--navy);}
.tag.team{background:var(--gold-soft); color:#8a6418;}
.tag.solo{background:var(--teal-soft); color:var(--teal);}
.stMarkdown p.row, .row{font-size:.9rem !important; line-height:1.55; margin:0 0 7px; color:var(--ink);}
.row b{color:var(--navy); font-weight:600;}
.stMarkdown .result, .result{font-size:.86rem !important; background:#f3f6fb; border-left:3px solid var(--navy); border-radius:0 8px 8px 0;
  padding:9px 12px; font-size:.86rem; line-height:1.5; margin:10px 0 12px; color:var(--ink);}
.stMarkdown p.note, .note{font-size:.8rem !important; color:var(--muted); line-height:1.5;}
[data-testid="stVerticalBlockBorderWrapper"]{background:var(--paper); border-radius:14px !important; border-color:var(--line) !important;}

.feature{background:var(--paper); border:1px solid var(--line); border-top:4px solid var(--gold); border-radius:14px; padding:22px 24px;}
.kpis{display:grid; grid-template-columns:repeat(4,1fr); gap:10px; margin:14px 0 4px;}
.kpi{background:var(--bg); border-radius:10px; padding:10px 12px;}
.kpi .n{font-family:'Source Serif 4',serif; font-size:1.25rem; font-weight:700; color:var(--navy);}
.kpi .l{font-size:.74rem; color:var(--muted);}
@media (max-width:760px){.kpis{grid-template-columns:repeat(2,1fr);}}

/* timeline */
.item{background:var(--paper); border:1px solid var(--line); border-radius:14px; padding:18px 22px; margin-bottom:12px;}
.item .top{display:flex; justify-content:space-between; gap:12px; flex-wrap:wrap;}
.item .role{font-weight:700; color:var(--navy); font-size:1rem;}
.item .when{font-size:.82rem; color:var(--muted); font-weight:600;}
.item .where{font-size:.84rem; color:var(--muted); margin:2px 0 8px;}
.item ul{margin:0; padding-left:18px;}
.stMarkdown .item li, .item li{font-size:.88rem !important; line-height:1.55; margin-bottom:4px;}

.skillgrp{background:var(--paper); border:1px solid var(--line); border-radius:14px; padding:18px 20px; height:100%;}
.skillgrp h4{font-size:.9rem !important; color:var(--navy) !important; margin:0 0 10px; padding:0; font-weight:700;}
.chip{display:inline-block; font-size:.8rem; background:var(--bg); border:1px solid var(--line); border-radius:16px; padding:4px 11px; margin:0 6px 7px 0;}

.contact{background:linear-gradient(135deg,var(--navy) 0%,var(--navy-deep) 100%); color:#fff; border-radius:16px; padding:26px 30px; margin-top:36px;}
.contact h3{font-family:'Source Serif 4',serif !important; color:#fff !important; margin:0 0 10px; padding:0;}
.contact a{color:#e7c98a !important; font-weight:600; text-decoration:none;}
.contact p{color:#dbe3f1 !important; margin:4px 0; font-size:.95rem;}

/* buttons */
.stDownloadButton button, .stLinkButton a{border-radius:9px !important; font-weight:600 !important; font-size:.84rem !important;}
.stDownloadButton button[kind="secondary"], .stLinkButton a[kind="secondary"]{background:#fff !important; color:var(--navy) !important; border:1px solid #c9d1df !important;}
.stDownloadButton button[kind="primary"], .stLinkButton a[kind="primary"]{background:var(--navy) !important; border-color:var(--navy) !important; color:#fff !important;}
[data-testid="stExpander"]{background:var(--paper); border-radius:12px;}
</style>
""",
    unsafe_allow_html=True,
)


def section(anchor: str, kicker: str, title: str, sub: str = ""):
    st.markdown(
        f'<div class="sec" id="{anchor}"><div class="kicker">{kicker}</div>'
        f'<h2>{title}</h2>{f"<div class=sub>{sub}</div>" if sub else ""}</div>',
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------------- hero
photo = ASSETS / "profile.jpg"
photo_html = f'<img src="data:image/jpeg;base64,{img_b64(photo)}" alt="Kanishka Sharma">' if photo.exists() else ""
st.markdown(
    f"""
<div class="hero">
  {photo_html}
  <div>
    <h1>Kanishka Sharma</h1>
    <div class="headline">PGDM Finance Candidate, FIIB &nbsp;|&nbsp; Financial Modelling · Valuation · Portfolio Analysis</div>
    <p>I'm a PGDM Finance candidate at FIIB, New Delhi, with a B.Com (Hons.) from the University of Delhi.
    Most of my work sits in Excel: integrated three-statement models, DCF and relative valuation,
    scenario and sensitivity analysis, and fund performance analysis. At Ummeed Housing Finance I mapped
    manual finance processes, built the cost-benefit case for automating them, and demonstrated a working
    risk-based audit sampling tool to the CFO. I'm looking for roles in financial modelling, valuation and
    portfolio reporting. Every project below comes with its actual files, so you can check the work, not just read about it.</p>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

c1, c2, c3, c4 = st.columns(4)
with c1:
    download("⬇ Resume: Modelling roles", ASSETS / "resume" / "Kanishka_Sharma_Resume_Financial_Modelling.pdf", "cv1", primary=True)
with c2:
    download("⬇ Resume: Valuation roles", ASSETS / "resume" / "Kanishka_Sharma_Resume_Portfolio_Valuation.pdf", "cv2", primary=True)
with c3:
    st.link_button("LinkedIn ↗", LINKEDIN, width="stretch")
with c4:
    st.link_button("Email me ✉", f"mailto:{EMAIL}", width="stretch")

st.markdown(
    """
<div class="stats">
  <div class="stat"><div class="n">9.58</div><div class="l">PGDM CGPA, FIIB (2025–27)</div></div>
  <div class="stat"><div class="n">6</div><div class="l">finance projects with downloadable files</div></div>
  <div class="stat"><div class="n">2</div><div class="l">internships: housing finance &amp; social sector</div></div>
  <div class="stat"><div class="n">Top 20</div><div class="l">global finish, Global Scaling Challenge</div></div>
</div>
<div class="nav">
  <a href="#featured">Featured tool</a><a href="#projects">Projects</a><a href="#experience">Experience</a>
  <a href="#skills">Skills</a><a href="#education">Education</a><a href="#achievements">Achievements</a><a href="#contact">Contact</a>
</div>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------- featured
section("featured", "Featured · Internship prototype", "Risk-Based Audit Sample Builder",
        "Built during my internship at Ummeed Housing Finance and demonstrated to the CFO")

st.markdown(
    """
<div class="feature">
  <p class="row"><b>Problem.</b> The 8-member internal audit team rebuilt its branch sampling plan by hand every year across
  130 branches. RBI's Risk Based Internal Audit (RBIA) framework expects audit coverage to rest on a documented, annually
  refreshed assessment of inherent risk and control risk.</p>
  <p class="row"><b>What I built.</b> An interactive tool that scores each branch on inherent risk (disbursement volume,
  loan-book growth, NPA %) and control risk (past audit findings, staff vacancy, manual overrides), ranks branches against the
  team's audit capacity, and adds three safeguards: a materiality floor for the largest branches, a blind random sample,
  and forced inclusion of branches not audited for 2+ cycles. It writes the reason each branch is in or out, and an
  Audit Committee summary.</p>
  <p class="row"><b>Business case (from my internship report).</b> One-time cost of Rs.3.10 lakh for the full 130-branch rollout,
  with a net gain of about Rs.3.57 lakh a year from Year 2. Alongside it, I built the cost-benefit case for automating
  Accounts Payable and Procurement:</p>
  <div class="kpis">
    <div class="kpi"><div class="n">Rs.19.5 L</div><div class="l">Year-1 investment</div></div>
    <div class="kpi"><div class="n">Rs.95.2 L</div><div class="l">projected annual benefit</div></div>
    <div class="kpi"><div class="n">3.4 mo</div><div class="l">payback period</div></div>
    <div class="kpi"><div class="n">4.8x</div><div class="l">benefit-cost ratio</div></div>
  </div>
  <p class="note">Tools: HTML/JavaScript prototype, Chart.js, Excel cost-benefit model, RBI RBIA framework.
  The demo below runs on 15 sample branches with illustrative figures, not Ummeed's live data.</p>
</div>
""",
    unsafe_allow_html=True,
)

audit_html = ASSETS / "audit_sample_builder.html"
if audit_html.exists():
    with st.expander("Try the live tool: move the capacity slider, switch risk factors off, click any branch", expanded=False):
        st.iframe(audit_html, height=1650)

# ---------------------------------------------------------------- projects
section("projects", "Evidence", "Projects", "Each project includes the files I actually produced.")

PROJECTS = [
    {
        "title": "Titan Company: Equity Valuation Model",
        "tags": [("Individual", "solo"), ("Equity Analysis & Business Valuation", "")],
        "problem": "Is Titan's share price of about Rs.3,300 supported by its fundamentals?",
        "did": "Built a 16-sheet model: macro and industry analysis, 7 years of actuals, a 5-year forecast with a "
               "3-scenario switch (optimistic / base / worst), a CAPM beta regressed on ~3,700 daily SENSEX and Titan prices "
               "(2011–25), WACC of 10.51%, a 2-stage FCFF DCF, EVA, a dividend discount model and relative valuation "
               "against 4 listed peers (P/E, EV/EBITDA, EV/Sales, P/BV).",
        "tools": "Excel (VLOOKUP scenario switch, SLOPE regression), DCF, DDM, comparable companies",
        "result": "HOLD. A 5×5 WACC vs terminal-growth sensitivity grid showed even the most optimistic DCF case sits below "
                  "the market price, meaning investors are paying for growth beyond the 5-year forecast window. "
                  "The model includes a cash-flow-to-balance-sheet reconciliation check.",
        "files": [("Excel model", "titan-valuation/Titan_Valuation_Model.xlsx"), ("Valuation report (PDF)", "titan-valuation/Titan_Valuation_Report.pdf")],
    },
    {
        "title": "Integrated Three-Statement Financial Model",
        "tags": [("Individual", "solo"), ("Excel modelling test", "")],
        "problem": "Build a 5-year forecast for a company from a fixed set of operating and financing assumptions.",
        "did": "Linked the Income Statement, Balance Sheet and Cash Flow Statement with a debt schedule, an interest rate "
               "that steps up from 6% to 7% if interest coverage falls below 6x, convertible bond conversion, a subsidiary "
               "stake bought and later sold in two stages, and warranty provisions with separate cash payouts.",
        "tools": "Excel, three-statement modelling, debt schedule, FCFF valuation",
        "result": "The balance sheet balances in every forecast year. Calculated DSCR, interest coverage, ROCE and ROE, "
                  "and valued the business with an FCFF model using a year-wise WACC.",
        "files": [("Excel model", "three-statement-model/Three_Statement_Financial_Model.xlsx")],
    },
    {
        "title": "Nutri-Box: Seed Funding Investment Report & Pitch",
        "tags": [("Team of 6", "team"), ("Private Equity & Venture Capital", "")],
        "problem": "Build an investor-ready case for a seed-stage, subscription-based daily meal delivery startup.",
        "did": "As a team, we sized the market, built unit economics and 5-year projections, set the valuation, "
               "modelled investor returns under three scenarios, and presented it as an investment report and pitch deck.",
        "tools": "Excel, forward revenue-multiple valuation, MOIC / IRR, scenario analysis, PowerPoint",
        "result": "Rs.1.75 crore raise at Rs.12.83 crore pre-money (~12% equity); projected ~17.3x MOIC and ~77% IRR on a "
                  "5-year exit in the base case; LTV:CAC of ~13.9:1.",
        "files": [("Investment report (PDF)", "nutribox-seed-investment/NutriBox_Investment_Report.pdf"), ("Pitch deck (PDF)", "nutribox-seed-investment/NutriBox_Investor_Pitch_Deck.pdf")],
    },
    {
        "title": "Mutual Fund Performance Analysis: Multi Cap Funds",
        "tags": [("Individual", "solo"), ("Portfolio analysis", "")],
        "problem": "Which of three multi-cap funds delivered the best risk-adjusted return against a common benchmark?",
        "did": "Aligned NAV data for Nippon India, ICICI Prudential and Quant multi-cap funds with the NIFTY500 Multicap "
               "50:25:25 TRI over 1,204 common trading days (Sep 2021 – Aug 2026), then calculated annualised return "
               "and risk, beta, Sharpe, Treynor and Jensen's alpha.",
        "tools": "Excel (STDEV, SLOPE, SQRT), CAPM-based performance metrics",
        "result": "Nippon India Multi Cap came out ahead: 17.80% annualised return vs 11.47% for the benchmark, "
                  "Sharpe ratio of 0.74 and Jensen's alpha of +6.46%.",
        "files": [("Excel analysis", "mutual-fund-analysis/Mutual_Fund_Analysis.xlsx"), ("Report (PDF)", "mutual-fund-analysis/Mutual_Fund_Analysis_Report.pdf")],
    },
    {
        "title": "Jewellery Industry: KPI Dashboard & Titan Analytics",
        "tags": [("Team of 5 + individual Excel", "team"), ("Financial Analytics for Managers", "")],
        "problem": "How do India's listed jewellers compare on growth, profitability and financial strength?",
        "did": "As a team, we compared Titan, Kalyan, Senco, PC Jeweller and Thangamayil in a Power BI dashboard and report. "
               "In my individual Excel workbook on Titan, I analysed ratios and operating, financial and total leverage, "
               "projected FCFF, and ran a ~1,000-iteration Monte Carlo simulation (NORM.INV / RAND) on its cash-flow drivers.",
        "tools": "Power BI, Excel, Monte Carlo simulation, ratio and leverage analysis",
        "result": "Titan led on scale, margins and balance-sheet strength; Kalyan and Senco showed the fastest growth. "
                  "The .pbix file needs Power BI Desktop to open.",
        "files": [("Team report (PDF)", "jewellery-industry-analysis/Jewellery_Industry_Report.pdf"),
                  ("My Excel: Titan analytics", "jewellery-industry-analysis/Titan_Financial_Analytics_Monte_Carlo.xlsx"),
                  ("Power BI dashboard (.pbix)", "jewellery-industry-analysis/Jewellery_Industry_Dashboard.pbix")],
    },
    {
        "title": "SBI Funds Management: Institutional Investor Deck",
        "tags": [("Individual", "solo"), ("Corporate Mentorship Programme", "")],
        "problem": "Is SBI Funds Management positioned for a public listing, and how would investors assess it?",
        "did": "Built a 37-slide investor deck covering the fee-based business model, AUM growth, risk management, "
               "financials and ESG, and a peer comparison with HDFC, ICICI Prudential, Nippon India and Kotak AMCs.",
        "tools": "PowerPoint, P/AUM and EV/EBITDA comparison, fee-yield trend analysis",
        "result": "Highlighted ~24% 5-year AUM CAGR, a 79% EBITDA margin and 32.8% 5-year PAT CAGR, alongside the main "
                  "risk: fee-yield compression.",
        "files": [("Investor deck (PDF, 19 MB)", "sbi-funds-investor-deck/SBI_Funds_Management_Investor_Deck.pdf")],
    },
]


def project_card(p: dict, idx: int):
    with st.container(border=True):
        tags = "".join(f'<span class="tag {cls}">{t}</span>' for t, cls in p["tags"])
        st.markdown(
            f'<div class="card-title">{p["title"]}</div><div class="tags">{tags}</div>'
            f'<p class="row"><b>Problem.</b> {p["problem"]}</p>'
            f'<p class="row"><b>What I did.</b> {p["did"]}</p>'
            f'<p class="row"><b>Tools.</b> {p["tools"]}</p>'
            f'<div class="result"><b>Output.</b> {p["result"]}</div>',
            unsafe_allow_html=True,
        )
        for j, (label, rel) in enumerate(p["files"]):
            download(f"⬇ {label}", PROJ / rel, f"p{idx}_{j}")


for i in range(0, len(PROJECTS), 2):
    cols = st.columns(2, gap="medium")
    for k, col in enumerate(cols):
        if i + k < len(PROJECTS):
            with col:
                project_card(PROJECTS[i + k], i + k)

# ---------------------------------------------------------------- experience
section("experience", "Work", "Experience")


def item(role, when, where, bullets):
    lis = "".join(f"<li>{b}</li>" for b in bullets)
    st.markdown(
        f'<div class="item"><div class="top"><span class="role">{role}</span><span class="when">{when}</span></div>'
        f'<div class="where">{where}</div><ul>{lis}</ul></div>',
        unsafe_allow_html=True,
    )


item("Finance Intern, Ummeed Housing Finance", "Apr – Jun 2026", "Gurugram · Corporate mentor: Chief Financial Officer", [
    "Mapped as-is and to-be workflows for Accounts Payable, Procurement and Internal Audit, identifying a 12–18 day "
    "approval-routing bottleneck and audit-trail gaps against RBI's IT governance directions.",
    "Built the cost-benefit case for a connected automation system (~550 invoices a month): Rs.19.5 lakh Year-1 investment, "
    "Rs.95.2 lakh annual benefit, 3.4-month payback and 4.8x benefit-cost ratio, tested across conservative, base and optimistic scenarios.",
    "Designed and demonstrated to the CFO a risk-based audit sampling prototype aligned with RBI's RBIA framework (featured above).",
    "Enabled a data-backed Rs.3 crore treasury vendor decision by benchmarking quotes from 2 vendors across a 6-category, "
    "25+ parameter comparison framework.",
    "Cross-verified 30–40 client transactions on the NESL platform, uncovering inaccurate balance data reported by a client.",
])
item("Social Work Intern, Habitat India", "Jan 2026", "New Delhi", [
    "Built an Excel model benchmarking circular-economy and emissions practices of 5 leading tech companies against "
    "industry standards, and flagged potential greenwashing risks in their sustainability disclosures.",
])

# ---------------------------------------------------------------- skills
section("skills", "Capabilities", "Skills", "Each skill below is used in at least one project on this page.")


def skill_group(title, chips):
    st.markdown(
        f'<div class="skillgrp"><h4>{title}</h4>' + "".join(f'<span class="chip">{c}</span>' for c in chips) + "</div>",
        unsafe_allow_html=True,
    )


s1, s2, s3 = st.columns(3, gap="medium")
with s1:
    skill_group("Valuation & Corporate Finance", ["DCF (FCFF)", "Comparable companies", "Dividend discount model",
                                                  "WACC & CAPM", "EVA", "MOIC / IRR", "Cost-benefit analysis"])
with s2:
    skill_group("Modelling & Analysis", ["Three-statement modelling", "Debt schedules", "Scenario analysis",
                                         "Sensitivity analysis", "Monte Carlo simulation", "Ratio analysis",
                                         "Fund performance (Sharpe, Treynor, alpha)"])
with s3:
    skill_group("Tools", ["Excel", "Power BI", "PowerPoint", "Word", "Python (basics)", "Tally ERP"])

# ---------------------------------------------------------------- education
section("education", "Academics", "Education & Certifications")
e1, e2 = st.columns(2, gap="medium")
with e1:
    item("PGDM – Finance Management", "2025 – 2027", "Fortune Institute of International Business (FIIB), New Delhi",
         ["CGPA: 9.58"])
    item("Bachelor of Commerce (Hons.)", "2021 – 2024", "University of Delhi", ["CGPA: 7.50"])
with e2:
    item("Certifications", "", "LinkedIn Learning", [
        "Corporate Finance Foundations", "Understanding Capital Markets",
        "Excel for Accounting", "Accounting Foundations – Budgeting"])

# ---------------------------------------------------------------- achievements
section("achievements", "Beyond the classroom", "Achievements & Leadership")
a1, a2 = st.columns(2, gap="medium")
with a1:
    item("Achievements", "", "", [
        "Top 20 global finish at the Global Scaling Challenge, after leading the team to a Top 3 position in the Asia-Oceania regional round.",
        "Led Satyawati College's first-ever online management fest, ranked among the Top 10 UG festivals at the Unstop UG Awards 2024.",
    ])
with a2:
    item("Positions of responsibility", "", "", [
        "<b>Mentee, Corporate Mentorship Program</b> (Oct 2025 – Feb 2026): evaluated IPO subscription trends, pricing and "
        "post-listing performance under a corporate mentor; built the SBI Funds Management investor deck above.",
        "<b>Student Ambassador, Centre of Behavioral Insights</b> (Aug 2025 – Feb 2026): managed the development and "
        "selection of case studies for student competitions.",
        "<b>Student Council, SPAC</b> (Aug 2025 – present).",
    ])

# ---------------------------------------------------------------- contact
st.markdown(
    f"""
<div class="contact" id="contact">
  <h3>Let's talk</h3>
  <p>Open to roles in financial modelling, valuation and portfolio reporting.</p>
  <p>✉ <a href="mailto:{EMAIL}">{EMAIL}</a> &nbsp;·&nbsp; ☎ {PHONE} &nbsp;·&nbsp;
     <a href="{LINKEDIN}" target="_blank">LinkedIn ↗</a> &nbsp;·&nbsp; New Delhi, India</p>
</div>
""",
    unsafe_allow_html=True,
)
