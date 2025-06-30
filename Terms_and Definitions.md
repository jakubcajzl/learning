# Terms

## General:
- CL = Competency Leader = directs a group of people (can be 10-100 people, or more) with one competency, e.g. Big Data, etc.
- PL = People Leader = directs usually 1-10 people. PL is under Competency Leader.
- Mentor = Helps a newcomer with it’s onboarding process
- PQS = Product Quality Standard

## Authentication, protection:
- MFA = Multi-Factor Authentication = requires to prove the indentity multiple times
- 2FA = Two-Factor Authentication = requires to prove the indentity twice
- AD / AAD = 
- ISO = International Organization for Standardization
- Firewall = 
- EDR/XDR = End-Point Detection and Response. XDR is EDR with AI and automatization
- NDA = Non-Disclosure Agreement
- GDPR = General Data Protection Regulation
- TCP/IP = Transmission Control Protocol / Internet Protocol
- SSH = Secure Shell = a cryptographic network protocol for operating network services securely over an unsecured network

## Data Engineering:
- AWS = Amazon Web Services
- DBX = Databricks (Microsoft Azure Databricks)
- GC, GCP = Google Cloud Platform
- Snowflake = platform for 
- VDF = Vodafone data platform

## Data Science:
- Gradient Boosting
    - Machine learning technique for regression – gives a prediction model, usually a decision tree
    - When a decision tree is the weak learner, the resulting algorithm is called gradient-boosted trees (it usually outperforms random forest)
- Decision tree learning (Supervised Learning)
o	Regression decision tree is used as a predictive model to draw conclusions about a set of observations

## Finance, Banking:
- Revolving loans = kontokorent + credit cards
- ERM = Expected Risk Margin = represents the expected margin amount in percent points that needs to be added to the cash loan interest rate in order to mitigate the loss of money that is caused by the client’s default or prepayment (here, default and prepayment are competing events – i.e. if the client prepays a loan than the default cannot happen)
- ECL = Expected Credit Loss = očekávaná kreditní ztráta
- FTP = Fund Transfer Price – main quantity which shows the profit of the solution = the value of the money (comparing e.g. with depositing the money to savings at ČNB, etc.). V podstatě „náklad ušlé příležitosti“.
- RWA = Risk Weighted Assets = how much capital do I need to hold for a given product
- DPD = Days Past Due – i.e. how many days there is from the moment the client did not pay the first monthly payment (i.e. after the monthly payment limit). E.g. 90 DPD = 90 days from the last not-paid day
- PD = Probability of Default (calculated usually for 12 months)
- MPD = Marginal PD
- Vintage report = Report about the past unpaid monthly payments (DPDs) 
- Prepayment/Repayment = celkové splacení
- Score card = Application (Socio-demographic, Behavioral, CCB bankovní registry) and Behavioral (Socio-demographic, Transaction, …) 
- NTB = New-to-Bank client; and NTM = New-to-Market client
- DI = Disposable Income
- DTI = Debt-to-Income ratio = poměr celkového zadlužení proti celkovému ročnímu čistému příjmu
- DSTI = Debt-Service-to-Income = procentní vyjádření podílu ročních průměrných výdajů žadatele o úvěr vyplývajících z jeho celkového zadlužení (tzv. dluhová služba) vůči jeho ročnímu čistému příjmu. Tzn. že vyjadřuje poměr mezi dluhovou službou (měsíční splátkou) veškerých úvěrů (kontokorent, kreditní karta, hypotéka, apod.) včetně aktuálně žádaného úvěru proti celkovému čistému měsíčnímu příjmu. 
- LTI = Loan-to-Income = poměr výše úvěru k příjmům žadatele
- LTV = Loan-to-Value = poměr výše úvěru k hodnotě zajištění žadatele
- LGD = Loss Given Default = volume of money that was lost due to deafult of a loan considering remaining interest till the end of the loan. Calculated as the LGD multiplied by both the probability of default and the exposure at default. 
- Exposure at default = total value of the loan at the time of a loan default
- NPS = Net Promoter Score
- DM&O = Decision Modelling & Optimization
- Price = usually interest rate in % p.a.
- Loan amount offered = % of DI (Disponible Income)
- Waived payments = Certain number of monthly payments which as a bonus to the client can be waived/canceled – usually this means last for example 5 monthly payments. Waived payments result in a better IR (interest rate) for a client. 
- CM = jsou různé kalkulace příspěvků k zisku banky = Příspěvková struktura profitability
- CM4 = provozní výsledek = CM3 + celkové náklady
- CM3 = bankovní výnosy po zohlednění nákladů na kapitál
- PPI = Payment Protection Insurance fee
- CoC = Cost of Capital, i.e. annualized return on the capital
- PDI = Percent of Disponible Income 
- CLUID = client unified identifier 
- APS = Aplikační scoring = Aplikace slouží ke stanovení interního ratingu klienta a pro rozhodnutí o úvěrové žádosti klienta. Systém umožňuje hodnotit tyto klientské segmenty: FO, SME (malé a střední podniky) a korporace v podmínkách ČS
- Decision codes: AP = Approved, AR = Archived, CA = Cancelled, GR = Granted, RB = Rejected by bank, RC = Rejected by client, RE = Recommended, RS = Reset, WD = Waiting for decision
- GINI = Giniho Koeficient = Číselná charakteristika diverzifikační schopnosti modelu. Poměřuje plochu mezi Lorenzovou křivkou a diagonálou jednotkového čtverce ku celkové ploše pod diagonálou. 
- OPEX = fixed costs on loan agreement
- Marginal Hazard (Hazard Ratio) = the probability of an event happening at a certain time, given that it hasn't happened yet. Also known as the hazard function or hazard rate. 
- Cumulative Hazard = the sum of the hazard over time. So basically, it evaluates the accumulated risk. The cumulative hazard function, also known as the cumulative hazard rate, is the integral of the hazard function over time. It represents the accumulated risk of the event of interest occurring over time. 

## Data spaces (databases):
- DWH (Data Warehouse) = Datový sklad
- ADS (Analytical Data Storage) = Datové úložiště sloužící k analýzám, jako podklad pro reporting, ve své prototypové části umožňuje ad-hoc přípravu dat a je připraveno na rychlejší průběh vývoje, především díky většímu odladění zadání prostřednictvím prototypů. Analytické úložiště zapadá do datové architektury banky - viz také stránky věnované BI Landscape (CSBIL), resp. specificky DWH a Analytickému úložišti.Analytické úložiště se postupně plní daty z Data Lake i daty ze zapojených zdrojových systémů, které je budou poskytovat uživatelům mnohem rychleji než do stávajícího DWH, a i daty z DWH (systém). Naže na vývoji a rozvoji analytického úložiště, se kromě vývojářů z IT podílejí i business útvary ČS. DWH a ADS jsou komponenty, které spolu úzce souvisejí a plní obdobnou funkci. Za rozdělením do dvou komponent stojí především historický vývoj a potřeba rozdílné governance a flexibility obou komponent. Obě komponenty dohromady pak plní funkci standardního Enterprise DWH (EDW). Komponenty zpracovávají a poskytují strukturovaná data napříč celou organizací a to jak pro ostatní komponenty BI (reporting, analytika…), tak i mimo BI.
- CPT/PCP (Client /) = Algorithms used for calculation of different metrics 
- CPS (Client  ) = CPT frontend used for an interaction with CPT
- SBD (Starbank Database) = Database of Starbank for clients
- ACL () = 
- BICC () = 
- Rating R = znamena, ze klient je v Defaultu jiz při zadosti, není potřeba ho scorovat, nebude mit zadne application score, a pokud ano tak není relevantni, protože pravdepodobnost defaultu je zbytecna.

## Banking – loans optimization:
- Constraints = market share (total volume), interest rate, risk level, …
- Uplift = usually in percentage above 100% – shows the increase in profit above the baseline (usually BAU strategy = current verified strategy)
- pBet model = probability of loan default (bet is analogous with default)  
- Analytics maturity = Descriptive (), Diagnostic (proč k něčemu dochází), Predictive (pravděpodobnost), Prescriptive (optimalizace, efficient frontier)
- Assign = Price and Limit
- Objective function = Maximize Lifetime Profit
- RWA = Risk-Weighted Assets = Risk-weighted assets are used to determine the minimum amount of capital a bank must hold in relation to the risk profile of its lending activities and other assets. This is done in order to reduce the risk of insolvency and protect depositors. The more risk a bank has, the more capital it needs on hand. The capital requirement is based on a risk assessment for each type of bank asset. 
- Credit line and Standard (both are in Process_TOP): these are two different processes of evaluation of clients used for approving unsecured loans. Credit line process is used mostly for existing clients which have or had in a past at least one loan with us – that means that we have some information about loan history (in our bank). Standard process is used for clients that are NTM, NTB or who are too much in debt. Credit line and Standard processes use different decision scores that are calculated using different algorithms. 
- BESC and BEIN decision score: both are behavioral decision scores, however BESC is calculated for existing clients where we have some information on their loan history, while BEIN is calculated for clients who didn‘t have any loans with us in the past, or who are in the border area (e.g. have too many loans or too big loans according to their disponible income) and therefore would pose a high risk to the bank. 
- Score bands and Ratings: both represent certaing ranges of decision scores. There can for example be different score bands for the same rating (e.g. R1) for a credit card loans and cash loans, because the risks can be different for both products. Ratings are usually from best to worst decreasing. e.g. R1–R7. Majority of score bands are usually in the range of 0–1000 points. where higher score is better. 
- MTE = Mean Target Encoding, i.e. target encoding is the process of replacing a categorical value with the mean of the target variable.

## ČS simulations and models:
Scenarios:
1)	BAU (Business As Usual): current scenario which runs on production
2)	AL (Account Level): classic selection according to criteria
3)	BB (Black Box): maximum possible profit using decision tree
4)	PLY (People Like You): mainly for deposits

1)	BAU (Business As Usual):
- The BAU strategy is a representation of the “actual” treatments that customers would receive using our current strategy. 
- The BAU scenario has two purposes: a) to verify if the components produce real results, (b) as a benchmark for different optimization strategies to calculate uplift. 
- BAU strategy does not involve any optimization modelling.
- For each of the loan applications a treatment is set based on the interest rate and the % of DI.
- The crucial thing in the BAU scenario is to validate the results – portfolio profit, approval rate, take-up rate, probability of becoming bad, average price, price per ratings or score bands, etc.
- Components are being checked according to Profit Project Schema (one component can influence others) 
- Applications rejected due to reasons which can be overruled by the different treatment set-ups have been included in the input sample
- Loan amount bands: loan amounts from [20 000, 50 000) to [750 000,+inf.) assigned to loan amount bands from 1.05 to 1.8
- Score bands: scores from (-inf, 400] to (800,+inf.) assigned to score bands from 400 to 900
- Price: usually means the interest rate in %
- Two types of optimizations: (a) Unconstrained (unrealistic scenario to show the maximum potential of optimization) and (b) Constrained (set of scenarios with different constraint set-ups to see the what-if impacts and also to comply with business and management requests) 
- Two types of contraints: (a) Global (population level constraints; determined by the results of BAU scenario; to achieve monotone bahaviour of prices) and (b) Local (aimed at the customer level; must always be met, even over the global constraints)
- Two main developed optimization contrained scenarios: Titan (prices slightly higher than BAU) and VR68 (have higher increase in price – follows the increase in FTP costs in previous months) 

Machine learning methods that we use:
- Logistic regression
- Logistic regression with polynomials
- XGBoost regression (type of Decision tree)
- Support vector
- Neural networks
- Discriminant analysis

Survival analysis methods that we use:
1)	Non-parametric: Kaplan-Meier estimate, …
2)	Semi-parametric: Cox proportional hazards regression, …
3)	Parametric: Accelerated Failure Time model, …
Survival curve: T0 = 100% and then e.g. exponential decrease to T
Naše křivky: T0 = 0 a pak T1, T2, … Tn; vyhodnocuje se PD (probability of default) a PP (probability of prepaiment)
Efficient frontier
Efficient frontier = efektivní hranice profitu; z definice se nedá dostat nad ní; vše pod ní značí nějaký tradeoff neboli sub-optimální řešení

Decision Optimizer (DO)
Decision Tree (asi 800 větví) 
Treatment = úroková míra a DI (Disponible Income)
Take Up rate = procento klientů, kteří vzali půjčku

## Reporting:
- Expected profit = sum(profit na daném scénáři) / (reálné % zastoupení scénáře na všech příchozích žádostech)*100

- Expected volume = sum(LA granted na daném scénáři) / (reálné % zastoupení scénáře na všech příchozích žádostech)*100

- Disbursement rate = Kolik z příchozích žádostí je jako granted (GR) (vystupuje tam také-up rate a  (disbursement rate means an annual rate of interest equal to the greater of the following (as of the date of determination): (a) the interest rate, or (b) the per annum rate for 10 year U.S. Treasury Obligations, as published in The Wall Street Journal, plus 200 basis points. Disbursement = disbursement means paying out money from a fund.)

- Profit: Vsechny jsou pro CL i CONSO, rid se tim FTP_REAL. Je tam vzdy kombinace FTP a NO FTP a pak REAL a DO. Real ma mesicni rezy a je presnejsi, protoze nic neaproximuje. Ten DO je jako to mame v DO, ale je mene presny. Takze teoreticky to co mame v DO tak cilime na ten FTP_DO, ale ten FTP_REAL je pak realita, ktera muze byt trochu odlisna. Uprimne ten  Profit CONSO uz by tam nemel byt, protoze je stejny jako ten standartni, to uz jsem jednou psal Ondrovi at to uplne odstrani. 
Takze se rid pro CONSO i CL tim FTP_REAL. Az to zmenim, tak pak se to nekde v pozadi napred zmeni pro CL a CONSO zutsane pod starymi modely, ale ty to neuvidis, Pak to zmenim i rpo CONSO a zase se to propise sem, ale to zase nepoznas. 

## SQL databáze:
- Scoring A, C, D, G, O: 
    - A = Žadatel
    - C = Spolužadatel/spoludlužník
    - D = Rozhodnutí
    - G = Ručitel
    - O = Spolužadatel plátce

- Units: 6610, 6620, 6630:
    - 6610  Hypotéky
    - 6620  Fyzické osoby (FO), Private Individuals (PI)
    - 6630  Malé a střední podniky, Small Business (SMB), Medium and Small Enterprise (MSE or SME)

