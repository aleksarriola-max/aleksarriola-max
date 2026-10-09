# Aleks Arriola

### Agentic AI, built for finance.

Finance & Accounting student at Hult International Business School, building AI agents for real financial workflows. In everything I ship, the LLM proposes and deterministic, tested code decides, especially when money moves.

🔭 **Now:** building a LangGraph M&A "Deal Swarm", an agent system that replicates an investment-banking deal team. LLM agents extract structured data; deterministic Python (NumPy/SciPy) runs the corporate-finance math.
💼 **Open to:** finance & AI internships, research, and builder collaborations.
🌐 **Portfolio, case studies & writing:** [aleksarriola-max.github.io](https://aleksarriola-max.github.io/)

---

## Featured projects

**[PitMind](https://github.com/aleksarriola-max/pitMind)**: F1 strategy intelligence · 🏅 Most Innovative, IBM SkillsBuild AI Builders Challenge · [live demo](https://pitmind-de6surgjaau5yewdynmxdp.streamlit.app/?race=bahrain_2025&driver=VER&lap=1)
Built in 6 days. Combines 2025 F1 telemetry and team-radio sentiment with XGBoost + SHAP models and pit-stop scenario simulation, explained by IBM Granite in two voices: plain language for fans, raw numbers for engineers.
`Python` `Streamlit` `XGBoost` `IBM Granite` · 36 tests

**[OpsFlow](https://github.com/aleksarriola-max/opsflow)**: policy-bound AI procurement agent on Sui
Natural-language spend requests become audited on-chain workflows. The agent's authority is a revocable on-chain capability, and it suspends itself after repeated incidents. Detects structuring (payments split to dodge approval limits), runs an independent AI auditor pass, and anchors a hash of every decision on-chain.
`TypeScript` `Sui Move` `React` · 84 tests · CI on every push

**[MatchMind](https://github.com/aleksarriola-max/matchMind)**: explainable AI for football refereeing decisions
Retrieval over the Laws of the Game plus IBM Granite, with a two-layer hallucination firewall (lexical evidence check + Granite entailment pass). Offside calls are modeled probabilistically with error bars. Ships a 75-question eval harness and a red-team report that documents where the verifier fails.
`Python` `Streamlit` `RAG` `IBM Granite` · 129 tests

**[DeepBook Market OS](https://github.com/aleksarriola-max/deepbook-market-os)**: analytics & execution console for Sui's DeepBookV3 · [live demo](https://aleksarriola-max.github.io/deepbook-market-os/)
Reads live mainnet order books and runs market-microstructure analytics in the browser: transaction-cost analysis, Kyle's lambda, impact curves, and ladder backtests. Every estimated value is explicitly labeled as simulated.
`TypeScript` `React` `Sui SDK`

**[Adaptive Funding Engine](https://github.com/aleksarriola-max/adaptive-funding-engine)**: milestone-based grants on Sui
Replaces fixed payouts with adaptive vesting: bonuses for on-time delivery, decay for late work, and withheld funds recycled to the next recipient. Deployed on testnet.
`Move` `React` · 27 Move unit tests

**Company Health Red-Flag Scanner**: screens 600+ US-listed companies on SEC EDGAR XBRL data with 6 academic distress and quality scores (Altman Z in three variants, Springate, Zmijewski, Piotroski F), Beneish manipulation indices and 80 ratios, producing a composite health score and fraud-risk card. [Case study](https://aleksarriola-max.github.io/#case-scanner) · [sample workbook](https://aleksarriola-max.github.io/Company_Health_Scanner.xlsx)
`Python` `SEC EDGAR API`

**Auto Company Valuation Kit (Orcen Capital)**: one YAML config produces an 84-sheet Excel model, a Word report and a slide deck covering DCF, comps, LBO and precedent transactions, with bias-correction modules. Verified end-to-end on Apple FY2024 data. [Case study](https://aleksarriola-max.github.io/#case-orcen) · [Apple model](https://aleksarriola-max.github.io/Apple_Valuation_v45.xlsx)
`Python` `DCF · LBO · Comps`

---

## Stack
**Languages:** Python · TypeScript · Move
**AI & agents:** LangGraph · IBM Granite (watsonx / Ollama) · RAG · XGBoost · SHAP · evaluation harnesses
**Finance:** DCF / LBO / comps modeling · Bloomberg Terminal · Excel
**Web & chain:** React · Streamlit · Sui SDK · GitHub Actions

## Credentials
Google Cybersecurity Certificate · Bloomberg Essentials (Equity & Fixed Income) · IBM SkillsBuild. Plus Forage job simulations with Goldman Sachs, J.P. Morgan, Citi and others.

## How I work
Reliability is a design choice, not a model upgrade. Most of what makes a system trustworthy is unglamorous: schema validation, policy layers, reconciling three data sources that claim to report the same number. I'd rather ship a narrow agent that does one policy-bound thing reliably than a broad one I can't verify. I build with AI coding assistants; the design decisions, invariants and tests are mine, and I'm happy to walk through any of them.

### 💭 Quote of the Day

<!--QUOTE:START-->
> *"It is remarkable how much long-term advantage people have gotten by trying to be consistently not stupid, instead of trying to be very intelligent."*
> — **Charlie Munger**
<!--QUOTE:END-->

<sub>Rotates daily via [GitHub Actions](.github/workflows/daily-quote.yml) from a [curated list](quotes.json) on risk, markets, persistence, and building.</sub>

---

[Portfolio](https://aleksarriola-max.github.io/) · [LinkedIn](https://www.linkedin.com/in/aleks-arriola/) · [Email](mailto:aleksarriola@gmail.com)
