# Validação e demonstração da POC

Este documento mostra, de forma prática, como validar a solução do início ao fim.

A ideia é servir como roteiro para:

- conferir se o ambiente está funcionando;
- gerar dados sintéticos;
- verificar as camadas Bronze, Silver e Gold;
- abrir a aplicação no Streamlit;
- checar se os testes passam;
- entender rapidamente o que um avaliador deve observar.

## O que este roteiro cobre

1. execução local no Bash;
2. execução da aplicação;
3. geração dos dados sintéticos;
4. validação dos testes;
5. conferência do resultado final;
6. validação visual no Streamlit.

## Pré-requisitos

Antes de começar, confirme que você tem:

- Python instalado;
- um ambiente virtual criado;
- dependências instaladas com `pip install -r requirements.txt`;
- o repositório aberto na pasta correta.

## 1. Preparar o ambiente no Bash

Se você estiver usando Git Bash no Windows, ative o ambiente virtual assim:

```bash
. .venv/Scripts/activate
```

Resultado esperado:

- o prompt passa a mostrar `(.venv)`;
- os comandos `python` e `pip` passam a usar o ambiente isolado do projeto.

Se o ambiente virtual ainda não existir:

```bash
python -m venv .venv
. .venv/Scripts/activate
pip install -r requirements.txt
```

## 2. Rodar os testes automatizados

Execute a suíte de testes:

```bash
pytest -q
```

Resultado esperado:

- os testes passam sem erro;
- podem aparecer warnings de biblioteca, mas sem quebrar a execução;
- isso confirma que a base funcional do projeto está estável.

Se `pytest` não estiver disponível no seu Bash, use a forma mais robusta:

```bash
.venv\Scripts\python.exe -m pytest -q
```

## 3. Gerar os dados sintéticos

Abra a aplicação com:

```bash
streamlit run app.py
```

Resultado esperado:

- o Streamlit abre no navegador;
- a pipeline sintética é carregada;
- as camadas Bronze, Silver e Gold são construídas a partir dos dados gerados;
- os painéis passam a mostrar métricas de receita e comportamento.

## 4. Verificar a camada Bronze

A camada Bronze representa os dados brutos.

O que observar:

- os dados originais ficam preservados;
- a ideia é ter rastreabilidade;
- se houver um problema mais à frente, é possível voltar ao dado original.

Resultado esperado:

- arquivos brutos aparecem na estrutura de dados do projeto;
- o dado bruto não é alterado para cálculo de métrica.

## 5. Verificar a camada Silver

A camada Silver representa os dados limpos e validados.

O que observar:

- tipos corretos;
- valores coerentes;
- ausência de duplicidade quando aplicável;
- regras de consistência sendo respeitadas.

Exemplos de regras esperadas:

- `clicks <= impressions`;
- `impressions <= ad_requests`;
- `viewable_impressions <= impressions`;
- `revenue >= 0`.

Resultado esperado:

- os dados ficam prontos para análise;
- inconsistências são tratadas antes de chegar na camada final.

## 6. Verificar a camada Gold

A camada Gold é a tabela analítica final.

O que observar:

- métricas consolidadas;
- visão pronta para dashboard;
- agrupamento por data, site, categoria, bloco, formato, dispositivo e origem de tráfego.

Resultado esperado:

- a tabela Gold mostra CTR, eCPM, fill rate, viewability rate, RPS, RPM, bounce rate, tempo médio na página e profundidade de rolagem;
- esta é a camada que um avaliador deve enxergar como produto analítico.

## 7. Validar a interface no Streamlit

No Streamlit, percorra as abas principais:

- visão geral;
- performance de anúncios;
- comportamento do usuário;
- previsão de receita;
- simulador de teste A/B;
- recomendações de negócio;
- handoff para engenharia.

Resultado esperado:

- os gráficos carregam corretamente;
- os filtros funcionam;
- os números mudam de acordo com a seleção;
- a aplicação fica pronta para demonstração.

## 8. Conferência final do fluxo

Use esta sequência como checklist rápido:

```bash
pytest -q
streamlit run app.py
```

Depois confirme no navegador:

- a interface abre sem erros;
- as métricas aparecem;
- a camada Gold está consistente;
- o simulador A/B mostra comparação entre cenários;
- o handoff explica o que falta para produção.

Resultado esperado:

- a POC demonstra um fluxo ponta a ponta;
- o avaliador consegue entender os dados, a transformação e a entrega final;
- você consegue explicar a solução sem depender de improviso.

## 9. O que dizer ao avaliador

Uma fala curta e profissional:

> Eu validei a solução localmente, rodei os testes, gerei dados sintéticos e conferi o resultado nas camadas Bronze, Silver e Gold. Depois abri a aplicação no Streamlit para checar se o fluxo analítico estava coerente. A ideia da POC é mostrar um caminho claro de dados brutos até consumo analítico, com regras de qualidade explícitas.

## 10. Leitura rápida do resultado

Se você quiser uma resposta curta para entrevista:

> A validação confirma que a POC funciona do ambiente local até a interface final. Os dados sintéticos são gerados, tratados e consolidados em uma tabela analítica, e a aplicação apresenta as métricas principais com um fluxo fácil de auditar.
