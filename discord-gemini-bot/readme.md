# Bot Discord com Gemini AI

## Sobre o Projeto
Este é um bot para Discord que utiliza a API Gemini AI para responder perguntas e interagir com os usuários. O bot permite consultas diretas à IA por meio de comandos personalizáveis, incluindo aliases e opções de resposta privada.

## Funcionalidade
- Integração com a API Gemini AI
- !gemini (prompt) para começar.

## Instalação e Configuração
### 1. Clonar o repositório
```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
```

### 2. Criar e ativar um ambiente virtual (opcional, mas recomendado)
```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate     # Windows
```

### 3. Instalar dependências
```bash
    pip install -r requirements.txt
```

### 4. Configurar variáveis de ambiente
Crie um arquivo `.env` na raiz do projeto e adicione:
```
DISCORD_TOKEN=seu_token_do_discord
GEMINI_KEY=sua_chave_api_gemini
```

### 5. Executar o bot
```bash
    python main.py
```

## Como Usar
No Discord, utilize:
```bash
!gemini Qual o significado da vida?
```
O bot responderá diretamente no chat.

## Contribuição
1. Fork o repositório
2. Crie uma branch (`feature/minha-feature`)
3. Faça suas alterações e commit (`git commit -m "Minha melhoria"`)
4. Envie um Pull Request

