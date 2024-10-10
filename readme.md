# Para Desenvolvedor

### Configurar ambiente virtual Python
```
python -m venv venv
```

### Instalar depedências

```
pip install -r requirements.txt
```

### Executar Projeto

```
python .\src\main.py
```

### Instalar pyinstaller para gerar dist
```
pip install -U pyinstaller
```

### Gerar um dist (.exe)
```
pyinstaller --add-data="assets:assets" .\src\main.py
```

<br>
<br>

# Para Usuário

### Criar uma Integração do Notion 
https://www.notion.so/profile/integrations/form/new-integration

### Adicionar Integração à sua página
https://developers.notion.com/docs/create-a-notion-integration#give-your-integration-page-permissions

### Executar app e configurar
- Adicione a Chave do Notion da integração no app 
- Adicione a URL da Página (ou ID da Página) no app
