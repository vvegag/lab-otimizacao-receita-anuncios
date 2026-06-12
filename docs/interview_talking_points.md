# Pontos de fala para a entrevista

Este arquivo é seu roteiro de preparação rápida. A ideia não é decorar tudo, mas conseguir explicar a POC com segurança em uma conversa técnica.

## Mensagem principal

A POC mostra que você não pensou apenas em um notebook ou em um gráfico isolado. Você montou um fluxo ponta a ponta:

1. gerar dados sintéticos parecidos com GAM e CDP;
2. validar qualidade dos dados;
3. organizar os dados em Bronze, Silver e Gold;
4. calcular métricas de monetização e comportamento;
5. visualizar resultados em Streamlit;
6. treinar um modelo simples;
7. simular teste A/B;
8. documentar o handoff para engenharia.

Frase boa para usar:

> Eu montei a POC para demonstrar como penso o problema de ponta a ponta: dados confiáveis, métrica bem definida, dashboard acionável, modelo simples e um caminho claro para engenharia transformar isso em algo produtivo.

## Como explicar a POC em 60 segundos

> A POC se chama Laboratório de Otimização de Receita de Anúncios. Ela simula a integração de dados do Google Ad Manager com dados comportamentais de uma CDP. Do lado de anúncios, eu simulo requisições, impressões, cliques, receita e impressões visíveis. Do lado de comportamento, simulo sessão, usuário, origem de tráfego, tempo na página, scroll depth e bounce.
>
> Depois organizo esses dados numa arquitetura medalhão: Bronze para dados brutos, Silver para dados limpos e validados, e Gold para a tabela analítica final. Na Gold eu calculo métricas como CTR, eCPM, fill rate, viewability rate, RPS e bounce rate.
>
> O Streamlit apresenta dashboards por formato de anúncio, categoria, dispositivo e origem de tráfego. Também inclui um modelo simples de previsão de receita e um simulador A/B que compara ganho de receita com métricas de proteção de experiência do usuário.
>
> O ponto principal é mostrar que otimização de receita precisa caminhar junto com qualidade de dados, engenharia e experiência do usuário.

## Como responder sobre sua lacuna em AdTech

Não tente fingir experiência direta em Google Ad Manager em produção. A resposta mais forte é honesta e estratégica.

Resposta sugerida:

> Eu ainda não trabalhei diretamente com Google Ad Manager em produção. Minha experiência vem mais de dados comportamentais, receita, segmentação, modelos preditivos e dashboards. Para reduzir essa lacuna, estudei as principais métricas de AdTech e montei uma POC simulando GAM e CDP. Então eu não estou vendendo experiência operacional profunda em GAM, mas sim mostrando que consigo aprender o domínio rapidamente e estruturar uma solução analítica com boas práticas.

## O que o entrevistador técnico deve gostar

Pontos fortes para reforçar:

- A POC tem código modular em `src/`, não tudo misturado no `app.py`.
- Existe uma separação clara entre dados brutos, dados limpos e tabela analítica.
- As regras de qualidade são explícitas: `clicks <= impressions`, `impressions <= ad_requests`, `revenue >= 0`.
- O modelo é simples de propósito, porque dados sintéticos não provam performance real.
- O simulador A/B não olha só receita; ele também olha tempo na página e bounce rate.
- A aba de handoff mostra preocupação com produção, atualização, granularidade e monitoramento.

Frase boa para usar:

> Eu preferi uma POC simples, mas bem estruturada, porque numa conversa com engenharia o mais importante é mostrar rastreabilidade, contrato de dados e clareza de evolução para produção.

## Perguntas prováveis e respostas curtas

### Por que usar Bronze, Silver e Gold?

> Para separar responsabilidades. Bronze guarda o dado bruto, Silver limpa e valida, Gold entrega a visão analítica pronta para dashboard, modelo e negócio. Isso reduz confusão, facilita auditoria e aproxima a POC de um fluxo real de engenharia de dados.

### Por que unir GAM com CDP?

> Porque dados de anúncios dizem quanto monetizamos, mas dados de CDP ajudam a entender o comportamento que gerou essa monetização. A combinação permite analisar receita junto com origem de tráfego, dispositivo, tempo na página, scroll depth e bounce.

### Por que não otimizar só receita?

> Porque aumentar receita no curto prazo pode piorar a experiência do usuário. Mais anúncios ou formatos agressivos podem elevar eCPM, mas também aumentar rejeição e reduzir tempo na página. Por isso eu usaria métricas primárias de receita junto com métricas de proteção de UX.

### O modelo preditivo é suficiente para produção?

> Não. Ele é propositalmente simples e serve para demonstrar o caminho: criar features, treinar um baseline, explicar variáveis importantes e pensar em monitoramento. Para produção, eu precisaria de dados reais, validação temporal, acompanhamento de drift e comparação com baseline de negócio.

### O que faltaria para colocar em produção?

> Substituir CSVs por conectores reais GAM/CDP, orquestrar o pipeline, criar contratos de dados, monitorar qualidade, versionar o modelo, medir drift e definir como produto e engenharia consumiriam a tabela Gold ou os scores.

## Plano de estudo de 1 hora

Se você tem só uma hora, use assim:

1. 10 min: leia este arquivo e memorize a explicação de 60 segundos.
2. 15 min: leia `docs/metric_dictionary.md` e entenda CTR, eCPM, fill rate, viewability e RPS.
3. 10 min: leia `docs/architecture.md` e saiba explicar Bronze, Silver e Gold.
4. 15 min: abra o Streamlit e navegue pelas abas principais.
5. 10 min: pratique responder: "você já trabalhou com GAM?", "por que A/B com guardrails?", "o que falta para produção?".

## Fechamento forte

Use esta ideia no final da explicação:

> Minha intenção com essa POC não é afirmar que resolvi um problema real de produção com dados sintéticos. É demonstrar meu raciocínio: eu entendo a relação entre monetização, comportamento, qualidade de dados, modelagem e engenharia. Esse é o tipo de base que eu levaria para evoluir com dados reais junto com o time.
