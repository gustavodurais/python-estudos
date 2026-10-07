# Automação de processo: login, download de CSV e envio por e-mail

Automação de desktop em Python que:

1. abre o sistema pelo menu Iniciar do Windows;
2. digita o **usuário** no login;
3. **espera você digitar a senha** e concluir o login;
4. aciona a exportação e aguarda o **CSV** ser baixado;
5. envia o CSV **por e-mail**.

> Status: em desenvolvimento. As etapas de interface (abrir o sistema,
> campo de login e botão de exportar) dependem da tela do seu sistema e
> precisam ser ajustadas e testadas no seu ambiente.

## Segurança

- A **senha do sistema nunca passa pelo código**: você a digita.
- Credenciais e dados pessoais ficam no arquivo `.env`, que está no
  `.gitignore` e **não deve ser enviado ao GitHub**. Use o `.env.example`
  como modelo.
- A senha do e-mail pode ficar vazia no `.env`: o script a pede no
  terminal.
- O PyAutoGUI controla mouse e teclado. Para abortar a qualquer momento,
  **leve o mouse ao canto superior esquerdo da tela**.

## Estrutura

| Arquivo | Função |
|---|---|
| `automacao_processo.py` | Fluxo principal (abrir, login, baixar, enviar) |
| `config.py` | Lê as configurações do `.env` |
| `enviador_email.py` | Monta e envia o e-mail com anexo |
| `requirements.txt` | Dependências (`pyautogui`, `python-dotenv`) |
| `.env.example` | Modelo de configuração |

## Instalação

```
cd projetos/automacao-processo
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
```

Depois edite o `.env` com seus dados.

## Configuração

| Variável | Para quê |
|---|---|
| `NOME_SISTEMA` | Nome digitado no menu Iniciar para abrir o sistema |
| `USUARIO_SISTEMA` | Usuário digitado no login |
| `BOTAO_EXPORTAR` | Coordenadas `x,y` do botão de exportar CSV (vazio = você clica) |
| `PASTA_DOWNLOADS` | Onde o CSV é salvo (vazio = pasta Downloads) |
| `TEMPO_MAX_DOWNLOAD` | Segundos de espera pelo download |
| `SMTP_HOST` / `SMTP_PORTA` | Servidor de e-mail (padrão: `smtp.gmail.com` / `465`) |
| `EMAIL_REMETENTE` / `EMAIL_DESTINATARIO` | De quem e para quem enviar |
| `EMAIL_SENHA` | Senha do e-mail (vazio = digitada no terminal) |

**Descobrir as coordenadas do botão de exportar:** deixe o mouse sobre o
botão e rode:

```
python -c "import time, pyautogui; time.sleep(5); print(pyautogui.position())"
```

**Gmail:** normalmente é necessário usar uma *senha de app* (exige
verificação em duas etapas). Confira a documentação do seu provedor.

## Como usar

Primeiro simule, sem mexer no mouse/teclado nem enviar e-mail:

```
python automacao_processo.py --simular
```

Depois execute de verdade. O script espera 5 segundos para você deixar a
tela pronta:

```
python automacao_processo.py
```

Quando pedir, digite a senha no sistema, conclua o login e pressione
ENTER na janela do terminal.

## Limitações conhecidas

- Depende da resolução e do layout da tela (coordenadas e foco dos campos).
- Pressupõe que, ao abrir o sistema, o cursor já está no campo de usuário
  e que a tecla Tab leva ao campo de senha.
- `pyautogui.write` não digita bem caracteres com acento; prefira um
  usuário sem acentos.
- Só funciona com a tela desbloqueada e a janela do sistema visível.

## Ideias para evoluir

- Reconhecer a tela por imagem em vez de coordenadas fixas.
- Agendar a execução (Agendador de Tarefas do Windows).
- Testes automatizados para a lógica que não depende da interface.
