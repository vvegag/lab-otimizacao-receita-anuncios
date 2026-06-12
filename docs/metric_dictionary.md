# Dicionário de métricas

Este documento explica as principais métricas da POC em português simples. Use como cola de revisão antes da entrevista.

## Visão rápida

| Métrica | Fórmula | Interpretação curta |
|---|---|---|
| CTR | cliques / impressões | Mede o quanto os usuários clicam nos anúncios exibidos. |
| eCPM | receita * 1000 / impressões | Receita gerada a cada mil impressões. |
| Fill rate | impressões / requisições de anúncio | Mede quanto do inventário solicitado foi preenchido. |
| Viewability rate | impressões visíveis / impressões | Mede a parcela de anúncios realmente visíveis. |
| RPS | receita / sessões | Receita por sessão de usuário. |
| RPM | receita * 1000 / page views | Receita por mil visualizações de página. |
| Bounce rate | rejeições / page views | Métrica de proteção da experiência do usuário. |
| Scroll depth | profundidade média de rolagem | Quanto da página o usuário percorreu. |
| Time on page | tempo médio na página | Quanto tempo o usuário ficou consumindo a página. |

## Conceitos básicos

### Ad request

É uma requisição de anúncio.

Exemplo:

> A página carregou e pediu ao servidor de anúncios que preenchesse um espaço publicitário.

Nem toda requisição vira impressão. Pode não haver demanda, pode haver bloqueio, configuração, regra de preço ou problema técnico.

### Impression

É uma impressão de anúncio.

Significa que um anúncio foi efetivamente servido/exibido em um espaço publicitário.

Regra importante:

```text
impressions <= ad_requests
```

Se impressões forem maiores que requisições, existe problema de dado.

### Click

É um clique no anúncio.

Regra importante:

```text
clicks <= impressions
```

Se cliques forem maiores que impressões, a métrica está incoerente.

### Revenue

É a receita gerada pelos anúncios.

Regra importante:

```text
revenue >= 0
```

Receita negativa nesse contexto seria suspeita para a POC e deve ser tratada.

## CTR

CTR significa **Click-Through Rate**, ou taxa de cliques.

Fórmula:

```text
CTR = clicks / impressions
```

Exemplo:

Se um anúncio teve 10 cliques e 1.000 impressões:

```text
CTR = 10 / 1000 = 1%
```

Como interpretar:

- CTR alto pode indicar anúncio, formato ou posição atraente.
- CTR baixo pode indicar pouca relevância, baixa atratividade ou posição ruim.

Cuidado:

> CTR alto não significa necessariamente maior receita. Um segmento pode clicar muito, mas gerar baixo eCPM.

## eCPM

eCPM significa **effective Cost per Mille**, ou receita efetiva por mil impressões.

Fórmula:

```text
eCPM = revenue * 1000 / impressions
```

Exemplo:

Se 2.000 impressões geraram 10 dólares:

```text
eCPM = 10 * 1000 / 2000 = 5 dólares
```

Como interpretar:

- eCPM alto indica que aquele inventário gera boa receita por impressão.
- eCPM baixo pode indicar demanda fraca, formato ruim, baixa qualidade do inventário ou regra de preço inadequada.

Frase útil:

> eCPM é uma métrica central porque normaliza a receita pelo volume de impressões.

## Fill rate

Fill rate é a taxa de preenchimento.

Fórmula:

```text
fill rate = impressions / ad_requests
```

Exemplo:

Se houve 1.000 requisições e 850 impressões:

```text
fill rate = 850 / 1000 = 85%
```

Como interpretar:

- Fill rate alto significa que a maior parte do inventário foi preenchida.
- Fill rate baixo pode indicar falta de demanda, problema de configuração, preço mínimo alto ou restrições de inventário.

Cuidado:

> Fill rate alto sozinho não garante boa monetização. É preciso olhar junto com eCPM e receita.

## Viewability rate

Viewability rate é a taxa de visibilidade.

Fórmula:

```text
viewability rate = viewable_impressions / impressions
```

Uma impressão pode existir, mas o usuário talvez não tenha visto o anúncio de fato. Por exemplo, o anúncio pode estar muito abaixo na página.

Como interpretar:

- Viewability alta indica que o anúncio tem maior chance de ser visto.
- Viewability baixa pode prejudicar valor do inventário e performance.

Frase útil:

> Em AdTech, não basta o anúncio ser servido. Ele precisa ter chance real de ser visto.

## RPS

RPS significa **Revenue per Session**, ou receita por sessão.

Fórmula:

```text
RPS = revenue / sessions
```

Como interpretar:

- Ajuda a medir quanto cada sessão de usuário gera de receita.
- É útil para comparar origem de tráfego, dispositivo ou categoria de página.

Exemplo:

Se uma origem de tráfego gera muitas sessões, mas baixo RPS, talvez ela traga volume sem boa monetização.

## RPM

RPM significa **Revenue per Mille page views**, ou receita por mil visualizações de página.

Fórmula:

```text
RPM = revenue * 1000 / page_views
```

Como interpretar:

- Ajuda a comparar páginas/categorias com volumes diferentes.
- É parecido com eCPM, mas usa page views em vez de impressões.

Diferença simples:

- eCPM olha receita por mil impressões de anúncio;
- RPM olha receita por mil visualizações de página.

## Bounce rate

Bounce rate é a taxa de rejeição.

Na POC, é usada como métrica de proteção de experiência do usuário.

Fórmula:

```text
bounce rate = bounces / page_views
```

Como interpretar:

- Bounce rate alto pode indicar que o usuário saiu rápido.
- Se uma mudança aumenta receita, mas também aumenta bounce rate, ela pode ser ruim no longo prazo.

Frase boa para entrevista:

> Receita não pode ser analisada isoladamente. Se uma otimização aumenta receita, mas piora muito bounce rate, existe risco de prejudicar a experiência e o valor futuro do usuário.

## Scroll depth

Scroll depth é a profundidade de rolagem.

Ela mede quanto da página o usuário percorreu.

Exemplo:

- 20%: usuário viu pouco conteúdo;
- 80%: usuário rolou bastante a página.

Como interpretar:

- Scroll depth maior pode indicar engajamento.
- Também ajuda a entender se certos anúncios estão em posições realmente visíveis.

## Time on page

Time on page é o tempo médio na página.

Como interpretar:

- Tempo maior pode indicar maior engajamento.
- Tempo muito baixo pode indicar baixa qualidade de tráfego, experiência ruim ou conteúdo desalinhado.

Na POC, ele é usado como guardrail no teste A/B.

## Como conectar as métricas numa fala

Resposta curta para entrevista:

> Eu olharia métricas de monetização e comportamento juntas. CTR mostra interação, eCPM mostra valor por impressão, fill rate mostra preenchimento de inventário, viewability mostra se o anúncio teve chance real de ser visto, e RPS/RPM conectam receita com sessão e página. Ao mesmo tempo, eu monitoraria bounce rate, scroll depth e time on page para garantir que a otimização de receita não prejudique a experiência do usuário.

## Erros comuns que você pode evitar

- Não dizer que CTR alto sempre é bom.
- Não dizer que receita alta sempre é boa.
- Não olhar eCPM sem volume.
- Não olhar fill rate sem eCPM.
- Não esquecer métricas de experiência do usuário.
- Não vender modelo sintético como prova de produção.

## Cola final

Se tiver que lembrar só cinco coisas:

1. **CTR** mede clique.
2. **eCPM** mede valor por mil impressões.
3. **Fill rate** mede preenchimento do inventário.
4. **Viewability** mede chance real de o anúncio ser visto.
5. **RPS/RPM + bounce/time/scroll** conectam monetização com experiência do usuário.
