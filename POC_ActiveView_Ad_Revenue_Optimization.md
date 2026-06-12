# Dossiê para NotebookLM — Entrevista ActiveView + POC Ad Revenue Optimization

**Candidato:** Valdomiro Vega García, PhD.  
**Vaga:** Data Scientist Sênior — ActiveView  
**Foco:** AdTech, Google Ad Manager, CDP, performance de anúncios, comportamento do usuário, previsão de receita/CTR/impressões, dashboards, testes A/B, integração com engenharia e produto.  
**Objetivo deste material:** servir como fonte única para o NotebookLM gerar perguntas e respostas, podcast, roteiro de estudo, apresentação, vídeo e simulado de entrevista.

---

## 1. Como usar este arquivo no NotebookLM

Carregue este `.md` no NotebookLM e peça para ele gerar, nesta ordem:

1. **Resumo executivo da vaga e da empresa.**
2. **Glossário de conceitos AdTech e métricas de publicidade.**
3. **Perguntas e respostas de entrevista**, separando perguntas técnicas, de negócio, de produto, de engenharia e perguntas difíceis/hostis.
4. **Podcast de preparação**, em tom de conversa, com 10 a 15 minutos.
5. **Apresentação de estudo**, com 10 a 12 slides.
6. **Roteiro de vídeo curto**, de 3 a 5 minutos, explicando a POC e sua conexão com a vaga.
7. **Checklist final de entrevista**, com pontos fortes, gaps e frases para memorizar.

### Prompt sugerido para NotebookLM

> Use este documento como base para me preparar para uma entrevista de Data Scientist Sênior na ActiveView. Gere perguntas prováveis, perguntas difíceis, respostas modelo em português natural, explicações dos conceitos de AdTech e uma apresentação de estudo. Considere meu histórico profissional, meus pontos fortes e minhas lacunas. Quero parecer preparado, honesto e estratégico, sem afirmar experiência direta que eu não tenho com Google Ad Manager em produção.

---

## 2. Contexto da empresa ActiveView

A ActiveView atua com tecnologia, dados e estratégia para **publishers que monetizam sites com anúncios**. Segundo o site da empresa, ela é parceira certificada do Google para administração de inventários de publicidade em websites de terceiros e gerencia um portfólio de mais de **1.000 sites monetizados com anúncios**.

A empresa se posiciona como uma operação de tecnologia e monetização para ajudar publishers a aumentar receita publicitária de maneira sustentável. O foco não é apenas colocar anúncios, mas **otimizar inventário, performance, receita e experiência do usuário**.

### Serviços e conceitos relevantes

#### App.ActiveView

O App.ActiveView é descrito como o centro operacional da inteligência da empresa: um ambiente onde **dados, automação e estratégia** se unem para escalar resultados de forma previsível e sustentável.

Pontos relevantes:

- ambiente orientado por dados reais;
- foco em otimizar valor do inventário;
- comparação de resultados;
- transformação de dados em decisões;
- possível conexão com interface visual, automação e operação dos publishers.

#### Script Personalizado

O Script ActiveView é o componente técnico que conecta o site do publisher ao ecossistema ActiveView.

Pontos relevantes:

- integração segura;
- carregamento otimizado;
- execução automática de tecnologias da plataforma;
- Pricing Rules;
- Redirect;
- otimizações de inventário;
- gestão centralizada do inventário;
- automações sem ajustes manuais.

#### Ad Optimization

O time de Ad Optimization trabalha com estratégia de monetização, estrutura de anúncios e performance de inventário.

Métricas citadas ou relacionadas:

- **RPS** — Revenue per Session ou receita por sessão;
- **eCPM** — receita por mil impressões;
- **CTR** — taxa de cliques;
- **viewability** — visibilidade real do anúncio;
- volume;
- qualidade;
- experiência do usuário.

O site enfatiza crescimento sustentável, melhoria contínua, análise de dados e validação por grandes publishers.

#### Customer Success e Atendimento

O atendimento é descrito como parte da estratégia, com atuação consultiva e personalizada para acompanhar a jornada dos publishers, adoção tecnológica e alavancagem de resultados.

---

## 3. Descrição resumida da vaga

A vaga pede um(a) **Data Scientist Sênior** para trabalhar com dados de publicidade e comportamento de usuário.

### Fontes de dados citadas

- **Google Ad Manager (GAM):** solicitações de anúncios, impressões, receita.
- **CDP:** visualizações de página, comportamento do usuário, solicitações de anúncios, impressões e visualizações.

### Principais responsabilidades

1. **Análise de dados e insights**  
   Analisar grandes conjuntos de dados do GAM e CDP para descobrir tendências, oportunidades e insights acionáveis.

2. **Otimização de desempenho de anúncios**  
   Usar dados para melhorar posicionamentos, formatos e segmentação de anúncios, aumentando receita sem prejudicar experiência do usuário.

3. **Modelos de Machine Learning**  
   Construir modelos para prever desempenho de anúncios, como impressões, receita e CTR.

4. **Integração de dados**  
   Trabalhar com engenharia para integrar e transformar dados de múltiplas fontes em datasets unificados.

5. **Relatórios e dashboards**  
   Criar dashboards para visualizar métricas de performance de anúncios, comportamento de usuário e tendências de negócio.

6. **Testes A/B**  
   Desenhar e analisar experimentos para avaliar impacto de mudanças de produto, layout, formato ou estratégia.

7. **Colaboração**  
   Trabalhar com produto, engenharia e stakeholders de negócio para definir requisitos e apoiar decisões orientadas por dados.

---

## 4. Perfil provável do entrevistador técnico: Bruno Azzi

O perfil encontrado de **Bruno Azzi** indica uma atuação mais técnica e de produto/engenharia.

### Sinais relevantes do perfil

- Senior Software Engineer na ActiveView.
- Experiência como Tech Lead e CTO.
- Forte histórico em desenvolvimento de software, frontend, produto, processos e liderança técnica.
- Experiência com POCs e demos usando:
  - OpenAI APIs;
  - Streamlit;
  - LangChain;
  - Python;
  - Next.js;
  - embeddings;
  - vector databases;
  - imagens;
  - speech;
  - completions;
  - automação de processos.
- Experiência em refatoração de código, APIs, testes, CI/CD, design systems, micro-frontends e liderança de times.

### Implicação para a entrevista

Com esse entrevistador, a conversa provavelmente não ficará apenas em métricas e machine learning. Ele pode avaliar:

- se o candidato entende o problema de produto;
- se sabe transformar análise em aplicação funcional;
- se consegue colaborar com engenharia;
- se estrutura bem código, pipeline, dashboard e integração;
- se sabe priorizar escopo e entregar uma POC útil;
- se entende limitações de modelos e dados;
- se consegue explicar como um modelo vira produto.

### Mensagem estratégica para esse entrevistador

> Eu não quero entregar apenas um notebook ou uma análise isolada. Quero ajudar a transformar dados de anúncios, usuários e receita em um produto analítico funcional, rastreável e útil para Produto, Engenharia e Negócio.

---

## 5. Perfil do candidato Valdomiro Vega García

### Resumo profissional

Valdomiro Vega García é PhD em Engenharia Elétrica pela USP, com trajetória que combina Engenharia, Ciência de Dados, Machine Learning, IA aplicada, docência, consultoria, energia, varejo/CRM, dados financeiros e produtos analíticos.

### Pontos fortes técnicos

- Python;
- SQL;
- PySpark;
- Databricks;
- Machine Learning;
- séries temporais;
- modelos preditivos;
- classificação;
- clustering;
- sistemas de recomendação;
- dashboards;
- tabelas GOLD;
- MLflow, AutoML e Jobs/Workflows em nível prático/prototipagem;
- GitHub;
- documentação em Markdown, Confluence e Unity Catalog;
- análise de grandes volumes de dados;
- comunicação com áreas técnicas e não técnicas.

### Experiência recente mais relevante

Na CRMBonus, atuou como Cientista de Dados Sênior em projetos de Data Science, ML, séries temporais, GenAI/LLMs e produtos analíticos aplicados a CRM, varejo, financeiro e tomada de decisão.

Experiências conectáveis com ActiveView:

- criação de tabelas GOLD;
- dashboards interativos;
- modelos preditivos;
- segmentações;
- churn;
- LTV;
- frequência;
- ticket médio;
- análise de impacto de campanhas;
- projeção de receita incremental;
- comportamento de clientes e marcas;
- aplicações web para segmentação e automação;
- agentes de IA para consulta e interpretação de indicadores.

### Experiências anteriores úteis

- ENEL: modelos preditivos para manutenção e grandes volumes de dados operacionais.
- FUSP/Petrobras: ML e NLP para gêmeos digitais.
- Mackenzie e institutos: professor de IA, ML, estatística, energia e dados.
- Consultoria: projetos de Data Science, recomendação, AWS, Python e KNIME.

---

## 6. Encaixe entre a vaga e o perfil do candidato

### Aderências fortes

| Demanda da vaga | Experiência do candidato |
|---|---|
| Análise de grandes volumes | SQL, PySpark, Databricks, tabelas GOLD, dashboards |
| Comportamento do usuário | CRM, varejo, RFV, LTV, churn, ticket médio, frequência |
| Modelos preditivos | ML, séries temporais, classificação, previsão de pagamento, receita incremental |
| Dashboards | Databricks dashboards, Power BI, SpotFire, produtos analíticos |
| Comunicação com negócio | Professor, consultor, Data Scientist Sênior, documentação |
| Integração com engenharia | Trabalho com Data Engineers, GitHub, workflows, produtos analíticos |
| Produto analítico | Aplicações web, self-service, dashboards, agentes de IA |
| A/B testing e impacto | Análise de campanhas, comparação entre grupos, impacto incremental |

### Gaps principais

| Gap | Como responder com honestidade |
|---|---|
| Experiência direta com Google Ad Manager | “Ainda não trabalhei diretamente com GAM em produção, mas conheço a lógica de eventos, métricas, dashboards, receita e comportamento. Estudei as principais métricas como ad requests, impressions, CTR, eCPM, fill rate e viewability.” |
| Domínio profundo de AdTech | “Meu domínio direto está em comportamento de clientes, CRM, receita e modelos. Estou transferindo essa experiência para AdTech, onde a lógica é semelhante: eventos, usuário, segmentação, performance e otimização.” |
| Produto de anúncios em produção | “Tenho experiência em produtos analíticos e dashboards; para AdTech eu construiria a solução em parceria com engenharia, garantindo dados confiáveis, métricas claras e consumo adequado.” |
| Testes A/B em escala AdTech | “Tenho base estatística e análise de impacto; estruturaria hipóteses, controle/tratamento, métricas primárias e métricas de proteção para experiência do usuário.” |

### Frase central de posicionamento

> Eu não venho diretamente de AdTech, mas venho de Ciência de Dados aplicada a comportamento, segmentação, modelos preditivos, dashboards e receita. Vejo uma conexão clara com a ActiveView: transformar dados de anúncios e usuários em insights, previsões e recomendações para otimizar monetização sem comprometer a experiência do usuário.

---

## 7. Conceitos essenciais de AdTech para estudar

### Google Ad Manager (GAM)

Plataforma usada por publishers para gerenciar inventário publicitário, campanhas, blocos de anúncios, demanda, relatórios, impressões e receita.

### CDP — Customer Data Platform

Sistema que consolida dados de usuários, sessões, comportamento, page views, origem de tráfego, dispositivos e outros sinais de engajamento.

### Publisher

Site ou empresa de mídia que disponibiliza inventário de anúncios para monetização.

### Inventário publicitário

Espaços disponíveis para anúncios em páginas, apps ou experiências digitais.

### Ad request

Solicitação de anúncio gerada quando uma página ou app tenta carregar um anúncio.

### Impression

Registro de que um anúncio foi efetivamente exibido.

### Click

Clique do usuário no anúncio.

### CTR — Click-through Rate

Fórmula:

```text
CTR = clicks / impressions
```

Indica a taxa de cliques sobre os anúncios exibidos.

### eCPM — Effective Cost per Mille

Fórmula:

```text
eCPM = revenue / impressions * 1000
```

Indica a receita gerada a cada mil impressões.

### Fill rate

Fórmula:

```text
Fill Rate = impressions / ad_requests
```

Indica quantas solicitações de anúncio foram preenchidas com uma impressão efetiva.

### Viewability

Percentual de impressões que foram realmente visíveis para o usuário.

### RPS — Revenue per Session

Fórmula:

```text
RPS = revenue / sessions
```

Indica receita média por sessão de usuário.

### RPM — Revenue per Mille pageviews

Fórmula aproximada:

```text
RPM = revenue / page_views * 1000
```

### Header Bidding

Mecanismo em que múltiplas fontes de demanda competem por uma impressão antes do chamado ao ad server, buscando aumentar a competição e a receita.

### Pricing Rules

Regras de preço mínimo ou estratégias de leilão para maximizar valor do inventário.

### Ad Optimization

Processo de testar e ajustar formatos, posicionamentos, regras e segmentações para aumentar receita, mantendo qualidade e experiência do usuário.

---

## 8. POC recomendada: ActiveView Ad Revenue Optimization Lab

### Objetivo da POC

Criar uma aplicação funcional em Streamlit que simule a integração de dados do Google Ad Manager e CDP, calcule métricas de monetização, gere dashboards, treine um modelo simples e simule um teste A/B.

### Objetivo estratégico da POC na entrevista

Mostrar que o candidato:

- entendeu o negócio da ActiveView;
- sabe traduzir uma descrição de vaga em produto analítico;
- consegue trabalhar com dados de anúncios e comportamento;
- entende métricas de monetização;
- sabe construir modelo preditivo e dashboard;
- pensa em integração com engenharia;
- conhece suas lacunas e está suprindo o gap de AdTech com estudo aplicado.

### Nome da POC

```text
ActiveView Ad Revenue Optimization Lab
```

### Pergunta de negócio

> Quais combinações de página, formato, dispositivo, horário e comportamento de usuário geram melhor receita publicitária, e como prever ou otimizar CTR, eCPM e receita sem prejudicar a experiência do usuário?

---

## 9. Arquitetura funcional da POC

```text
Dados sintéticos GAM + CDP
        ↓
Camada Bronze
        ↓
Camada Silver
        ↓
Camada Gold com métricas e features
        ↓
Dashboard Streamlit
        ↓
Modelo preditivo de receita/CTR
        ↓
Simulação A/B
        ↓
Recomendações de negócio
```

### Camada Bronze

Dados brutos simulados.

Tabelas:

- `gam_ad_events.csv`
- `cdp_user_events.csv`

### Camada Silver

Dados limpos, tipados, padronizados e unidos.

Validações:

- datas válidas;
- campos obrigatórios;
- impressões <= ad requests;
- clicks <= impressions;
- receita >= 0;
- user/session/page IDs não nulos;
- ausência de duplicidade na granularidade definida.

### Camada Gold

Tabela analítica final com métricas:

- CTR;
- eCPM;
- fill rate;
- viewability rate;
- RPS;
- RPM;
- receita por categoria;
- receita por device;
- receita por ad unit;
- sessões;
- page views;
- scroll depth médio;
- time on page médio;
- returning user rate.

---

## 10. Dados sintéticos da POC

### Tabela `gam_ad_events`

Colunas sugeridas:

```text
timestamp
publisher_id
site_id
page_id
page_category
ad_unit
ad_format
device
country
traffic_source
ad_requests
impressions
viewable_impressions
clicks
revenue
```

### Tabela `cdp_user_events`

Colunas sugeridas:

```text
timestamp
user_id
session_id
site_id
page_id
page_category
device
traffic_source
page_views
time_on_page
scroll_depth
returning_user
bounce
```

### Granularidade recomendada

Para simplificar:

```text
hora + site + page_category + ad_unit + device + traffic_source
```

---

## 11. Métricas do dashboard

### Métricas principais

```text
Total Revenue
Ad Requests
Impressions
Clicks
CTR
eCPM
Fill Rate
Viewability Rate
Revenue per Session
Page Views
Sessions
Average Time on Page
Bounce Rate
```

### Visualizações recomendadas

1. Receita por dia.
2. eCPM por formato de anúncio.
3. CTR por dispositivo.
4. Fill rate por categoria de página.
5. Viewability por ad unit.
6. Revenue per session por origem de tráfego.
7. Matriz de oportunidade: alto tráfego + baixo eCPM.
8. Ranking de páginas/categorias com maior potencial de otimização.

---

## 12. Modelo preditivo da POC

### Modelo 1 — previsão de receita

Target:

```text
revenue_next_day
```

Features:

```text
page_category
device
ad_unit
ad_format
traffic_source
hour
weekday
historical_impressions
historical_ctr
historical_ecpm
viewability_rate
fill_rate
avg_time_on_page
scroll_depth
returning_user_rate
```

Modelos recomendados:

- baseline: média móvel ou regressão linear;
- modelo principal: Random Forest Regressor ou XGBoost/LightGBM se disponível;
- alternativa simples: GradientBoostingRegressor do scikit-learn.

Métricas:

- MAE;
- RMSE;
- MAPE, com cuidado quando receita é próxima de zero;
- comparação visual previsto vs real.

### Modelo 2 — previsão de CTR ou alta performance

Target:

```text
high_ctr = 1 se CTR está acima do percentil 75
```

Modelos:

- Logistic Regression;
- Random Forest;
- Gradient Boosting.

Métricas:

- AUC;
- precision;
- recall;
- matriz de confusão;
- feature importance.

---

## 13. Simulação de teste A/B

### Hipótese

> Um novo formato ou posicionamento de anúncio aumenta o eCPM e a receita por sessão sem prejudicar a experiência do usuário.

### Grupos

- Grupo A: layout atual.
- Grupo B: novo layout/formato/posição.

### Métrica primária

- eCPM;
- revenue per session;
- CTR.

### Métricas de proteção

- time on page;
- scroll depth;
- bounce rate;
- page views per session;
- returning user rate.

### Decisão

O teste só deve ser considerado positivo se:

1. houver ganho em receita ou eCPM;
2. a diferença for estatisticamente significativa;
3. as métricas de experiência não piorarem além de um limite aceitável.

### Frase para entrevista

> Eu não avaliaria somente receita. Uma mudança pode aumentar receita no curto prazo, mas piorar experiência e reduzir valor futuro. Por isso eu usaria métricas de monetização junto com métricas de proteção de experiência do usuário.

---

## 14. Requisitos técnicos da POC para Codex/Cursor

### Stack recomendada

- Python 3.11+
- pandas
- numpy
- scikit-learn
- scipy
- plotly
- streamlit
- pydantic ou pandera opcional para validação
- duckdb opcional para simular SQL

### Estrutura do projeto

```text
activeview-ad-revenue-lab/
├── README.md
├── requirements.txt
├── app.py
├── data/
│   ├── bronze/
│   ├── silver/
│   └── gold/
├── notebooks/
│   ├── 01_generate_synthetic_data.ipynb
│   ├── 02_create_gold_metrics.ipynb
│   ├── 03_model_revenue_forecast.ipynb
│   └── 04_ab_test_analysis.ipynb
├── src/
│   ├── data_generation.py
│   ├── data_quality.py
│   ├── transformations.py
│   ├── metrics.py
│   ├── modeling.py
│   ├── ab_testing.py
│   └── recommendations.py
└── docs/
    ├── architecture.md
    ├── metric_dictionary.md
    └── interview_talking_points.md
```

### Páginas do app Streamlit

1. **Overview**  
   KPIs gerais e contexto da POC.

2. **Ad Performance**  
   CTR, eCPM, fill rate, revenue, viewability.

3. **User Behavior**  
   page views, sessions, time on page, scroll depth, bounce rate.

4. **Revenue Forecast**  
   previsão de receita, métricas do modelo e importância de variáveis.

5. **A/B Test Simulator**  
   comparação controle vs tratamento.

6. **Business Recommendations**  
   recomendações automáticas baseadas em regras simples.

7. **Engineering Handoff**  
   entradas, saídas, granularidade, frequência de atualização, riscos e próximos passos para produção.

---

## 15. Recomendações automáticas da POC

Criar regras simples como:

```text
Se page_category tem alto tráfego e baixo eCPM:
    recomendar revisão de ad unit ou pricing rules.

Se viewability é baixa em determinado ad unit:
    recomendar testar nova posição ou formato.

Se CTR é alta mas receita é baixa:
    recomendar avaliar demanda, leilão ou eCPM.

Se fill rate é baixo:
    recomendar investigar demanda, configuração de inventário ou regras de preço.

Se revenue cresce mas bounce rate piora:
    recomendar cuidado com experiência do usuário.
```

---

## 16. Como a POC supre lacunas do candidato

### Lacuna: não ter experiência direta com Google Ad Manager

A POC mostra domínio conceitual das principais métricas do GAM:

- ad requests;
- impressions;
- clicks;
- revenue;
- CTR;
- eCPM;
- fill rate;
- viewability.

### Lacuna: não vir diretamente de AdTech

A POC conecta a experiência anterior do candidato com:

- comportamento de usuários;
- segmentação;
- receita;
- previsão;
- dashboards;
- otimização;
- testes A/B.

### Lacuna: entrevistador com perfil forte de engenharia

A POC mostra:

- app funcional;
- código modular;
- camada de dados;
- validações;
- handoff para engenharia;
- documentação;
- visão de produto.

### Lacuna: produto em produção

A POC inclui uma seção de evolução para produção:

- pipeline agendado;
- dados reais GAM/CDP;
- validações automatizadas;
- API ou tabela consumível;
- monitoramento de drift;
- monitoramento de métricas de negócio;
- observabilidade.

---

## 17. Perguntas prováveis de entrevista e respostas modelo

### 17.1. Me conte sobre você e sua conexão com a vaga.

Resposta sugerida:

> Sou Cientista de Dados Sênior, engenheiro eletricista com doutorado, e tenho uma trajetória combinando modelagem matemática, machine learning, análise de dados, Databricks, Python, SQL, dashboards e comunicação com negócio. Nos últimos projetos, trabalhei com dados transacionais e comportamentais, criando tabelas analíticas, features, modelos preditivos e dashboards para apoiar decisões. Embora eu não venha diretamente de AdTech, vejo uma conexão clara com a ActiveView: transformar dados de comportamento, anúncios e receita em insights, previsões e recomendações práticas para otimização.

### 17.2. Você já trabalhou com Google Ad Manager?

Resposta sugerida:

> Ainda não trabalhei diretamente com Google Ad Manager em produção. Minha experiência está mais em dados transacionais, comportamento de clientes, segmentação, modelos preditivos, dashboards e produtos analíticos. Mas entendo que, no contexto da ActiveView, o desafio analítico é trabalhar com eventos, usuários, impressões, receita, CTR, eCPM e segmentações. Eu já estudei essas métricas e consigo conectar rapidamente essa lógica com minha experiência anterior em comportamento, campanhas e receita.

### 17.3. Como você desenharia uma solução para integrar GAM e CDP?

Resposta sugerida:

> Eu começaria entendendo a granularidade de cada fonte. No GAM, teria solicitações de anúncios, impressões, cliques, receita, formatos e blocos de anúncio. No CDP, teria sessões, page views, origem de tráfego, dispositivo e comportamento. Depois criaria uma camada bruta, uma camada tratada e uma camada analítica com métricas unificadas por página, categoria, dispositivo, formato, horário e segmento. O cuidado principal seria garantir chaves corretas, granularidade consistente, ausência de duplicidade e validações de qualidade.

### 17.4. Como prever receita de anúncios?

Resposta sugerida:

> Eu começaria com um baseline simples, como média móvel por categoria, formato e dispositivo. Depois testaria modelos como Random Forest, Gradient Boosting ou XGBoost, usando variáveis como histórico de impressões, CTR, eCPM, fill rate, viewability, origem de tráfego, dispositivo, categoria da página, horário e dia da semana. A validação teria que respeitar o tempo: treinar no passado e testar no futuro.

### 17.5. Como avaliar CTR?

Resposta sugerida:

> Dependendo da granularidade, eu trataria CTR como uma taxa agregada ou como um problema de classificação no nível da impressão. Avaliaria features de contexto, como categoria, formato, posição, dispositivo, origem de tráfego e comportamento do usuário. Também tomaria cuidado para não otimizar apenas CTR, porque um clique alto não necessariamente significa maior receita ou melhor experiência.

### 17.6. Como faria um teste A/B para formato de anúncio?

Resposta sugerida:

> Primeiro definiria a hipótese, por exemplo: um novo formato aumenta eCPM sem prejudicar experiência. Depois separaria grupos controle e tratamento, definiria métrica primária, como eCPM ou revenue per session, e métricas de proteção, como bounce rate, time on page e scroll depth. Analisaria significância estatística, duração do teste e consistência por segmentos antes de recomendar rollout.

### 17.7. Como você equilibraria receita e experiência do usuário?

Resposta sugerida:

> Eu não olharia somente receita. Um anúncio mais agressivo pode aumentar eCPM no curto prazo, mas reduzir tempo na página, retorno do usuário e confiança no produto. Então acompanharia métricas de monetização junto com métricas de experiência, como bounce rate, page views por sessão, scroll depth e tempo na página.

### 17.8. Como transformaria um modelo em algo útil para engenharia?

Resposta sugerida:

> Eu evitaria entregar apenas um notebook. Documentaria entradas, saídas, granularidade, frequência de atualização, regras de validação, limites do modelo e forma de consumo. A saída poderia ser uma tabela analítica, dashboard, API ou alerta. Para engenharia, entregaria uma especificação clara e modular, facilitando integração e manutenção.

### 17.9. Como garantir qualidade dos dados?

Resposta sugerida:

> Eu validaria duplicidades, granularidade, chaves, datas, campos nulos e consistência das métricas. Por exemplo, clicks não podem ser maiores que impressions, impressions não deveriam ultrapassar ad requests no mesmo recorte, receita não deve ser negativa e mudanças bruscas de volume precisam ser investigadas.

### 17.10. Como você colaboraria com Produto e Engenharia?

Resposta sugerida:

> Eu trabalharia próximo desde o início. Com produto, alinharia hipóteses, métricas de sucesso e decisão esperada. Com engenharia, alinharia fontes, chaves, granularidade, frequência de atualização e forma de consumo. Meu papel seria conectar problema de negócio, dados e solução técnica.

---

## 18. Perguntas difíceis ou hostis que podem aparecer

### 18.1. “Você nunca trabalhou com AdTech. Por que deveríamos te contratar?”

Resposta:

> É verdade que minha experiência direta não é em AdTech. Mas tenho experiência forte em Ciência de Dados aplicada a comportamento, segmentação, previsão, receita, dashboards e produtos analíticos. A lógica central é muito parecida: entender eventos, usuários, métricas, segmentar comportamento, prever resultados e gerar recomendação de negócio. Além disso, já estudei o contexto da ActiveView e montei uma POC justamente para acelerar minha curva de aprendizado no domínio.

### 18.2. “Você conhece Google Ad Manager de verdade?”

Resposta:

> Ainda não usei Google Ad Manager em produção. O que já fiz foi estudar as métricas e a lógica do domínio: ad requests, impressions, clicks, revenue, CTR, eCPM, fill rate e viewability. Minha força é aprender rapidamente o domínio e transformar dados em análise, modelos e dashboards. Eu seria transparente nessa curva, mas acredito que minha base técnica reduz bastante o tempo de adaptação.

### 18.3. “Você é mais acadêmico do que prático?”

Resposta:

> Minha formação acadêmica é forte, mas minha atuação recente é bem prática. Trabalhei com Databricks, Python, SQL, PySpark, dashboards, tabelas GOLD, modelos preditivos, automações e produtos analíticos usados por áreas de negócio. Minha vantagem é combinar rigor metodológico com entrega aplicada.

### 18.4. “Seu modelo tem boa métrica técnica, mas não melhora receita. O que você faz?”

Resposta:

> Eu revisaria a definição do problema. Um modelo só é útil se impacta a decisão de negócio. Verificaria se o target está correto, se a métrica técnica está alinhada ao objetivo e se a saída do modelo é acionável. Talvez a solução correta não seja melhorar AUC ou RMSE, mas mudar a recomendação, o recorte, o threshold ou a forma de consumo pelo produto.

### 18.5. “Como você lida com pressão por entrega rápida?”

Resposta:

> Eu separo o problema em camadas. Primeiro entregaria uma versão simples e útil, com métricas confiáveis e dashboard. Depois evoluiria para modelo preditivo, teste A/B e automação. Prefiro uma POC pequena, correta e acionável do que uma solução complexa sem validação.

### 18.6. “Como você explica para um stakeholder que a mudança aumentou receita, mas piorou experiência?”

Resposta:

> Eu mostraria as duas dimensões: ganho de monetização e perda de experiência. Explicaria que a decisão depende do objetivo estratégico, mas recomendaria cautela se a piora em experiência comprometer retenção, tempo de permanência ou retorno do usuário. A melhor decisão deve equilibrar receita de curto prazo com sustentabilidade.

### 18.7. “Como você evitaria que a POC vire um protótipo impossível de manter?”

Resposta:

> Desde o início eu separaria código em módulos, documentaria métricas, criaria validações de dados, definiria entradas e saídas, e deixaria claro o que é experimental e o que precisaria ser refeito para produção. A POC deve testar valor de negócio sem criar dívida técnica desnecessária.

### 18.8. “Qual é sua maior lacuna para essa vaga?”

Resposta:

> Minha maior lacuna é não ter trabalhado diretamente com Google Ad Manager em produção. Para reduzir isso, estudei o domínio, métricas e contexto da ActiveView, e preparei uma POC simulando dados GAM e CDP. Minha base em dados, comportamento, receita e modelos me permite aprender o domínio rapidamente.

---

## 19. Perguntas inteligentes para fazer ao entrevistador

1. Hoje a maior dor da ActiveView está mais em integração de dados, qualidade dos dados, modelagem preditiva ou geração de insights acionáveis?
2. Os dados de GAM e CDP já estão integrados em uma camada analítica ou parte do desafio será estruturar essa base?
3. Os modelos esperados seriam consumidos por dashboards, APIs internas ou diretamente por produtos da ActiveView?
4. Como vocês equilibram otimização de receita com experiência do usuário?
5. Quais métricas são mais críticas hoje: eCPM, RPS, CTR, fill rate, viewability ou retenção do usuário?
6. Como o time de Data Science interage com Engenharia e Produto no dia a dia?
7. A expectativa é que o cientista de dados entregue apenas insights ou também participe do desenho técnico para produção?
8. Quais seriam os primeiros problemas que a pessoa contratada deveria resolver nos primeiros 90 dias?

---

## 20. Plano de estudo rápido antes da entrevista

### Dia 1 — Domínio AdTech

Estudar:

- GAM;
- CDP;
- publisher;
- ad request;
- impression;
- CTR;
- eCPM;
- fill rate;
- viewability;
- RPS;
- header bidding;
- pricing rules.

Entregável:

- glossário de 1 página.

### Dia 2 — POC funcional

Implementar:

- dados sintéticos;
- app Streamlit;
- dashboard;
- métricas;
- modelo simples;
- teste A/B.

Entregável:

- app rodando localmente.

### Dia 3 — Entrevista

Treinar:

- apresentação pessoal;
- resposta sobre não conhecer GAM em produção;
- explicação da POC;
- perguntas de A/B testing;
- perguntas sobre engenharia e integração.

Entregável:

- roteiro de 2 minutos + 5 perguntas difíceis respondidas.

---

## 21. Prompt para Codex/Cursor implementar a POC

> Crie uma aplicação funcional em Streamlit chamada `ActiveView Ad Revenue Optimization Lab`. A aplicação deve gerar dados sintéticos simulando Google Ad Manager e CDP, calcular métricas de monetização como CTR, eCPM, fill rate, viewability rate, RPS e RPM, exibir dashboards interativos, treinar um modelo simples para prever receita futura ou alta CTR, simular um teste A/B de formato ou posicionamento de anúncio e gerar recomendações de negócio. Estruture o projeto com `src/`, `data/`, `notebooks/`, `docs/`, `requirements.txt` e `README.md`. O código deve ser modular, com funções para geração de dados, validação de qualidade, transformação Bronze/Silver/Gold, métricas, modelagem, teste A/B e recomendações. Inclua uma página no app chamada `Engineering Handoff` explicando entradas, saídas, granularidade, frequência de atualização, limitações e próximos passos para produção.

---

## 22. Prompt para NotebookLM gerar perguntas e respostas

> Gere 30 perguntas de entrevista para a vaga de Data Scientist Sênior na ActiveView, considerando o perfil técnico do entrevistador Bruno Azzi, a descrição da vaga, o contexto da empresa e o perfil do candidato Valdomiro Vega García. Separe as perguntas em: negócio AdTech, métricas de anúncios, modelagem preditiva, A/B testing, engenharia de dados, produto/POC, comunicação com stakeholders e perguntas hostis. Para cada pergunta, gere uma resposta natural em português, em tom de entrevista, com 60 a 90 segundos de fala.

---

## 23. Prompt para NotebookLM gerar podcast

> Crie um podcast de preparação para entrevista, em português, com dois apresentadores. Um apresentador deve atuar como mentor de carreira e outro como entrevistador técnico da ActiveView. O podcast deve explicar a empresa, a vaga, o perfil do entrevistador, os conceitos de AdTech, os pontos fortes e gaps do candidato, a POC proposta e as principais perguntas difíceis. O tom deve ser prático, direto e natural. Duração estimada: 12 a 15 minutos.

---

## 24. Prompt para NotebookLM gerar apresentação

> Crie uma apresentação de 12 slides para estudar antes da entrevista. Tema: preparação para vaga de Data Scientist Sênior na ActiveView. Slides: 1) objetivo da entrevista, 2) contexto da ActiveView, 3) descrição da vaga, 4) perfil do entrevistador Bruno Azzi, 5) encaixe do candidato, 6) gaps e como responder, 7) conceitos AdTech, 8) métricas principais, 9) POC proposta, 10) perguntas difíceis, 11) perguntas para o entrevistador, 12) checklist final.

---

## 25. Prompt para NotebookLM gerar roteiro de vídeo

> Crie um roteiro de vídeo de 4 minutos para eu estudar e apresentar mentalmente a POC `ActiveView Ad Revenue Optimization Lab`. O vídeo deve explicar o problema de negócio, os dados simulados de GAM e CDP, as métricas calculadas, o dashboard, o modelo preditivo, o teste A/B, as recomendações de negócio e como essa POC mostra que consigo aprender rapidamente AdTech e transformar análise em produto funcional.

---

## 26. Roteiro de apresentação da POC em 2 minutos

> Para me preparar melhor para a entrevista, eu montei uma POC simples chamada ActiveView Ad Revenue Optimization Lab. A ideia foi simular dados semelhantes aos que aparecem na vaga, como eventos de anúncios do Google Ad Manager e dados de comportamento de usuários de um CDP.
>
> A POC calcula métricas como CTR, eCPM, fill rate, viewability e receita por sessão. Também possui dashboards para entender performance por página, formato, dispositivo e origem de tráfego. Além disso, inclui um modelo simples para prever receita ou identificar combinações com maior probabilidade de alta performance, e uma simulação de teste A/B para avaliar mudanças de layout ou formato.
>
> Eu fiz isso para demonstrar como penso o problema de ponta a ponta: primeiro entender o negócio, depois estruturar dados, criar métricas confiáveis, testar modelos e transformar resultados em recomendações. Também incluí uma visão de handoff para engenharia, porque acredito que o trabalho de Data Science precisa ser consumível por produto, engenharia e negócio, não apenas ficar em notebook.

---

## 27. Frases para memorizar

1. **“Eu não venho diretamente de AdTech, mas venho de comportamento, segmentação, receita, modelos e produtos analíticos.”**
2. **“A lógica central é transformar eventos de usuários e anúncios em decisões de monetização.”**
3. **“Eu não olharia só receita; acompanharia também experiência do usuário.”**
4. **“Eu evitaria entregar apenas notebook; pensaria em pipeline, dashboard, tabela consumível ou API.”**
5. **“Minha maior lacuna é GAM em produção, mas já estou estudando métricas e construí uma POC para acelerar a curva.”**
6. **“Meu diferencial é combinar Ciência de Dados, comunicação técnica, visão de negócio e entrega prática.”**
7. **“Em A/B testing, eu definiria hipótese, métrica primária, métricas de proteção e significância antes da decisão.”**
8. **“Uma solução boa precisa ser tecnicamente correta, interpretável e acionável para o negócio.”**

---

## 28. Checklist final antes da entrevista

### Estudar conceitos

- [ ] Google Ad Manager
- [ ] CDP
- [ ] ad request
- [ ] impression
- [ ] CTR
- [ ] eCPM
- [ ] fill rate
- [ ] viewability
- [ ] RPS
- [ ] A/B testing
- [ ] revenue forecasting
- [ ] user behavior analytics

### Preparar respostas

- [ ] Me conte sobre você
- [ ] Você já trabalhou com GAM?
- [ ] Como preveria receita?
- [ ] Como faria teste A/B?
- [ ] Como equilibraria receita e experiência?
- [ ] Como integraria dados GAM + CDP?
- [ ] Como colaboraria com engenharia?
- [ ] Como explicaria a POC?

### Evitar

- [ ] Não dizer que tem experiência direta com GAM se não tem.
- [ ] Não falar só de modelo; falar de negócio e produto.
- [ ] Não ignorar experiência do usuário.
- [ ] Não apresentar POC como solução final de produção.
- [ ] Não usar jargão sem explicar.

### Reforçar

- [ ] Databricks, PySpark, SQL, Python.
- [ ] Tabelas GOLD e dashboards.
- [ ] Modelos preditivos.
- [ ] Segmentação, LTV, churn e comportamento.
- [ ] Comunicação com stakeholders.
- [ ] Capacidade de aprendizado rápido.
- [ ] POC funcional e foco em entrega.

---

## 29. Nota de honestidade para entrevista

A melhor estratégia é ser forte, mas honesto.

Não dizer:

> “Tenho experiência em Google Ad Manager.”

Melhor dizer:

> “Ainda não trabalhei diretamente com Google Ad Manager em produção, mas já estudei as principais métricas e entendo como conectar esse domínio com minha experiência em comportamento de usuários, receita, modelos, dashboards e produtos analíticos.”

Não dizer:

> “Minha POC resolve o problema real da ActiveView.”

Melhor dizer:

> “A POC foi criada para demonstrar meu raciocínio de ponta a ponta e acelerar meu entendimento do domínio. Com dados reais e colaboração do time, ela poderia evoluir para algo mais próximo de produção.”

---

## 30. Objetivo final da preparação

Após estudar este material, o candidato deve conseguir explicar com segurança:

1. O que a ActiveView faz.
2. O que a vaga precisa.
3. O que o entrevistador técnico provavelmente valoriza.
4. Quais são as principais métricas de anúncios.
5. Como integrar dados GAM + CDP.
6. Como prever receita, CTR ou impressões.
7. Como desenhar um teste A/B.
8. Como equilibrar receita e experiência do usuário.
9. Como transformar análise em produto funcional.
10. Como seu histórico se conecta com a vaga, mesmo sem experiência direta em AdTech.

