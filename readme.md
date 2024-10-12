# TXT-TO-NOTION: Software Open-source para Integração de Arquivos com Notion

## Descrição

Este é um software open-source que sincroniza arquivos `.txt` locais com o Notion de maneira prática e eficiente. A ferramenta utiliza **Python** para interagir com a **API do Notion** (via **Requests**) e conta com uma interface gráfica desenvolvida em **PyQt6**. 

O projeto também utiliza um banco de dados **SQLite** local para armazenar informações necessárias, garantindo o funcionamento offline. 

## Funcionalidades

- **Sincronização de arquivos `.txt` com o Notion**.
- **Criação automática de páginas** no Notion baseadas na estrutura de pastas locais.
- **Sincronização bidirecional** para enviar modificações locais ou receber atualizações do Notion.
- **Geração de "diffs"** em HTML para comparação quando há conflito de modificações entre Notion e arquivos locais.
- **Interface gráfica** amigável para configuração e operação.
- **Executável** disponível para Windows, compilado com **PyInstaller**.

## Requisitos

- **Python 3.8+**
- **Notion API Key** (é necessário criar uma integração no Notion)
- **Bibliotecas Python**:
  - `requests`
  - `PyQt6`
  - `sqlite3` (incluso no Python)
  
## Instalação para Usuários

### Passos para criar uma integração com o Notion:

1. Crie uma integração em [Notion Developer](https://www.notion.so/profile/integrations/form/new-integration).
2. Adicione a integração à sua página conforme as instruções [aqui](https://developers.notion.com/docs/create-a-notion-integration#give-your-integration-page-permissions).

### Configuração e execução do aplicativo

1. Baixe a pasta `dist` do repositório, onde está localizado o arquivo executável `.exe`.
2. Execute o `.exe` diretamente no Windows.
3. No aplicativo, adicione a **Chave da Integração do Notion** e a **URL da Página** onde deseja sincronizar os arquivos `.txt`.
4. Selecione uma pasta local e clique em "Sincronizar" para criar páginas e arquivos no Notion ou atualizar as modificações existentes.

## Instalação para Desenvolvedores

### Configurar o ambiente virtual Python
```bash
python -m venv venv
```

### Ativar o ambiente virtual

- No Windows:
  ```bash
  venv\Scripts\activate
  ```

- No macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

### Instalar dependências

Instale as dependências necessárias para rodar o projeto:

```bash
pip install -r requirements.txt
```

### Executar o projeto

Para iniciar o projeto, execute o arquivo principal:

```bash
python .\src\main.py
```

### Compilar o executável com PyInstaller

Para gerar um executável `.exe` no Windows com todas as dependências, siga os passos:

1. Instale o PyInstaller:
   ```bash
   pip install -U pyinstaller
   ```

2. Gere o executável com os recursos adicionais:
   ```bash
   pyinstaller --add-data=".\_internal\assets:assets" --add-data=".\_internal\diffs:diffs" .\src\main.py
   ```

O executável será criado na pasta `dist`, e pode ser distribuído diretamente para os usuários.

## Contribuindo

Contribuições são bem-vindas! Se você encontrar um bug ou quiser adicionar novas funcionalidades, sinta-se à vontade para abrir uma issue ou enviar um pull request.

### Passos para contribuir:
1. Faça um fork deste repositório.
2. Crie uma nova branch para suas alterações:
   ```bash
   git checkout -b minha-nova-funcionalidade
   ```
3. Commit suas mudanças:
   ```bash
   git commit -m 'Adiciona nova funcionalidade'
   ```
4. Envie sua branch para o GitHub:
   ```bash
   git push origin minha-nova-funcionalidade
   ```
5. Abra um pull request.

## Licença

Este projeto está licenciado sob a **GPL**. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

## Autor

[Juliano Urias](https://www.linkedin.com/in/julianourias/)