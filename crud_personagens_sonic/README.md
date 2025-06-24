
# CRUD de Personagens do Universo Sonic 🌀🦔

Este projeto é um CRUD (Create, Read, Update, Delete) feito em **Python + SQLite**, inspirado no universo de personagens do Sonic. A aplicação funciona inteiramente via terminal, com foco em aprendizagem de banco de dados, manipulação de arquivos SQL e organização de código com funções reutilizáveis.

> 💡 O projeto foi desenvolvido como um exercício prático para explorar **conceitos de banco de dados com SQLite**, **integração com Python**, **validações de entrada**, **menu interativo** e **estrutura modular**.

---

## 🎮 Funcionalidades

- [x] Adicionar personagem
- [x] Listar todos os personagens cadastrados
- [x] Atualizar dados de um personagem existente (com visualização dos dados atuais)
- [x] Remover personagem com confirmação e visualização prévia
- [x] Buscar personagens por **campo específico** (nome, tipo, time, cor ou poderes)
- [x] Importar dados iniciais sugeridos com opção de **adicionar** ou **substituir** a tabela existente
- [x] Exportar todos os personagens para um arquivo `.csv` com acentuação correta e nome fixo (mas ignorado no Git)

---

## 📋 Estrutura do personagem

Cada personagem cadastrado possui os seguintes campos:

- `nome`: Nome do personagem (ex: Sonic)
- `tipo`: Speed, Power ou Fly
- `time`: Time ao qual pertence (Sonic, Dark, Chaotix, etc.)
- `cor`: Cor predominante do personagem
- `poderes`: Habilidades especiais ou características marcantes

---

## 🧠 Tecnologias utilizadas

- **Python 3**
- **SQLite** (banco de dados local)
- **VSCode**
- Extensão recomendada: *SQLite Viewer* para explorar `sonic.db` graficamente

---

## 🗃️ Organização do projeto

| Arquivo                 | Descrição |
|------------------------|-----------|
| `main.py`              | Código principal com o menu interativo e chamadas das funções |
| `database.py`          | Funções de banco de dados (CRUD, busca, importação, limpeza) |
| `dados_iniciais.sql`   | Script SQL com dados padrão de personagens do universo Sonic |
| `.gitignore`           | Arquivo que impede o versionamento de arquivos temporários ou sensíveis como `.db`, `__pycache__` e `.csv` |



---

## 💾 Como executar

1. Clone este repositório:
```bash
git clone https://github.com/leomacedo/python-banco-de-dados.git
cd crud_personagens_sonic
```

2. Execute o script principal:
```bash
python main.py
```

3. Escolha as opções do menu para interagir com o banco de dados!

---

## 📝 Exemplo de uso do menu

```bash
--- Banco de Dados do Universo Sonic 🌀 ---
1. Adicionar personagem
2. Listar todos
3. Atualizar personagem
4. Remover personagem
5. Buscar personagem por campo
6. Sair
7. Importar dados iniciais sugeridos
8. Exportar backup da tabela para CSV
```

> 🗒️ Observação: O arquivo `.csv` gerado pelo menu (opção 8) **não é salvo no GitHub**, pois está incluído no `.gitignore`. Isso evita poluir o repositório com backups locais e mantém seu repositório limpo e profissional.

---

## 🤝 Créditos

Projeto criado por [@leomacedo](https://github.com/leomacedo)
