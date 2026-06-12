# Arquitetura da POC

Este documento explica a arquitetura da POC em linguagem simples. Ele serve para você conseguir responder perguntas técnicas sem precisar decorar código.

## Ideia geral

A POC simula um produto analítico de otimização de receita de anúncios.

Ela combina duas fontes:

- **GAM**, ou Google Ad Manager: dados de monetização de anúncios.
- **CDP**, ou Customer Data Platform: dados de comportamento do usuário.

O objetivo é responder:

> Quais combinações de página, formato de anúncio, dispositivo, origem de tráfego e comportamento geram mais receita sem prejudicar a experiência do usuário?

## Fluxo completo

```text
Dados sintéticos GAM + CDP
        |
        v
Camada Bronze
        |
        v
Camada Silver
        |
        v
Camada Gold
        |
        v
Streamlit
        |
        v
Dashboard + modelo + teste A/B + recomendações + handoff
```

## Camada Bronze

A Bronze é a camada de dados brutos.

Na POC, ela fica em:

```text
data/bronze/
```

Arquivos principais:

- `gam_ad_events.csv`
- `cdp_user_events.csv`

Como explicar:

> A Bronze preserva os dados como chegaram. Em produção, ela seria a camada mais próxima da ingestão real do GAM e da CDP. A ideia é manter rastreabilidade: se algo der errado depois, eu consigo voltar ao dado bruto.

## Camada Silver

A Silver é a camada de dados limpos, tipados, deduplicados e validados.

Na POC, ela fica em:

```text
data/silver/
```

Arquivos principais:

- `gam_ad_events_clean.csv`
- `cdp_user_events_clean.csv`
- `gam_cdp_joined.csv`

Principais validações:

- `clicks <= impressions`;
- `impressions <= ad_requests`;
- `viewable_impressions <= impressions`;
- `revenue >= 0`;
- IDs obrigatórios não podem ser nulos;
- `event_id` não pode estar duplicado.

Como explicar:

> A Silver é onde eu garanto que os dados fazem sentido antes de calcular métricas. Por exemplo, cliques não podem ser maiores que impressões, e impressões não podem ser maiores que requisições de anúncio. Sem essas regras, métricas como CTR, eCPM e fill rate podem ficar erradas.

## Camada Gold

A Gold é a tabela analítica final, pronta para consumo.

Na POC, ela fica em:

```text
data/gold/ad_revenue_gold.csv
```

Ela agrega os dados por:

- data;
- site;
- categoria da página;
- bloco de anúncio;
- formato de anúncio;
- dispositivo;
- origem de tráfego.

Ela calcula métricas como:

- CTR;
- eCPM;
- fill rate;
- viewability rate;
- RPS;
- RPM;
- bounce rate;
- tempo médio na página;
- profundidade média de rolagem.

Como explicar:

> A Gold é a camada que produto, negócio, dashboard e modelo consumiriam. Ela transforma eventos em uma visão analítica útil para decisão.

## Por que usar arquitetura medalhão?

A arquitetura medalhão separa o fluxo em três níveis:

| Camada | Função | Exemplo na POC |
|---|---|---|
| Bronze | Guardar dado bruto | CSVs sintéticos GAM e CDP |
| Silver | Limpar, validar e unir | Dados limpos e join por `event_id` |
| Gold | Entregar métrica de negócio | Tabela final para dashboard e modelo |

Frase boa para entrevista:

> Eu usei Bronze, Silver e Gold porque isso mostra uma preocupação de engenharia: separar ingestão, qualidade e consumo analítico. Isso evita que o dashboard dependa diretamente de dados brutos.

## Papel do Streamlit

O Streamlit é a interface da POC.

Ele lê a tabela Gold e mostra:

- visão geral do portfólio;
- performance de anúncios;
- comportamento do usuário;
- previsão de receita;
- simulador A/B;
- recomendações de negócio;
- handoff para engenharia.

Como explicar:

> O Streamlit é só a camada de apresentação. A lógica principal fica em `src/`, e isso é importante porque facilita manutenção, testes e reutilização.

## Papel do modelo preditivo

O modelo usa Random Forest para prever receita.

Ele não é o ponto mais importante da POC. Ele serve como baseline para mostrar:

- criação de features;
- treino de modelo;
- avaliação com MAE e R2;
- importância de variáveis;
- caminho para produção.

Como explicar:

> O modelo é propositalmente simples. Com dados sintéticos, eu não posso afirmar performance real. O objetivo é mostrar como eu estruturaria um baseline e como ele poderia evoluir com dados reais.

## Papel do teste A/B

O simulador A/B compara:

- **Controle**: situação atual;
- **Tratamento**: uma mudança de formato, posicionamento ou estratégia.

Ele mostra dois grupos de métricas:

- métricas primárias: receita e eCPM;
- métricas de proteção: tempo na página e taxa de rejeição.

Como explicar:

> Eu não avaliaria um experimento só por receita. Se o tratamento aumenta receita, mas piora bounce rate e tempo na página, ele pode destruir valor futuro.

## O que faltaria para produção

Para transformar a POC em algo produtivo, seria necessário:

1. conectar dados reais do GAM e da CDP;
2. orquestrar o pipeline com jobs agendados;
3. criar contratos de dados;
4. monitorar qualidade e frescor;
5. versionar modelo e features;
6. monitorar drift;
7. definir consumo por dashboard, API ou tabela;
8. integrar com fluxo real de experimentos A/B.

Frase final:

> A POC não tenta substituir uma arquitetura real de produção. Ela mostra um desenho inicial que conversa com engenharia e pode evoluir de forma organizada.
