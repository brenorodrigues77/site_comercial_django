# Site Comercial Django

Este projeto é um site comercial desenvolvido com Django, focado em soluções digitais para empresas que desejam impulsionar sua presença online. O site oferece uma apresentação profissional, rápida e otimizada para conversão, com design moderno e responsivo.

## Funcionalidades
- Página inicial com subheader, carrossel de imagens e textos institucionais
- Seção de apresentação dos serviços: Visão, Projetos, Planejamento e Inovação
- Área de feedback com depoimento
- Seção de projetos realizados
- Formulário de contato integrado
- Estrutura pronta para adicionar novos produtos e serviços
- Layout responsivo utilizando Bootstrap 5

## Estrutura do Projeto
```
db.sqlite3
manage.py
app/
    settings.py
    urls.py
    ...
home/
    models.py
    views.py
    urls.py
    templates/
        home.html
media/
static/
```

## Como executar
1. Clone o repositório:
   ```bash
   git clone https://github.com/<usuario>/<repositorio>.git
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute as migrações:
   ```bash
   python manage.py migrate
   ```
4. Inicie o servidor:
   ```bash
   python manage.py runserver
   ```
5. Acesse `http://127.0.0.1:8000/` no navegador.

## Personalização
- Adicione suas imagens em `media/images/`
- Edite os textos e seções em `home/templates/home.html`
- Modifique estilos em `static/app/base.css`

## Tecnologias Utilizadas
- Python 3
- Django
- Bootstrap 5

## Licença
Este projeto está sob a licença MIT.

---
Desenvolvido por Breno Rodrigues.