🛒 NexaShop — Loja Virtual
Sistema de loja virtual em linha de comando, feito em Python com banco de dados SQLite. Permite cadastrar produtos, montar um carrinho, finalizar compras com baixa automática de estoque e avaliar produtos.
Funcionalidades
Cadastro de produtos com nome, categoria, descrição, preço e estoque
Catálogo com todos os produtos disponíveis
Carrinho de compras: adicionar, visualizar e remover itens
Finalização de compra com baixa automática de estoque
Histórico de pedidos com itens, valores e data
Avaliações de 1 a 5 estrelas com comentário e nota média por produto
Persistência de dados em SQLite: nada se perde ao fechar o programa
Tecnologias
Python 3.8+
SQLite (módulo sqlite3, já incluso no Python, sem dependências externas)
Como executar
# 1. Clone o repositório
git clone https://github.com/LucasR-creator/Loja-Virtual-E-commerce-.git
cd Loja-Virtual-E-commerce-

# 2. Execute o sistema
python app.py
O arquivo nexashop.db é criado automaticamente na primeira execução.
Estrutura do projeto
.
├── app.py              # Interface de linha de comando (menu, carrinho, fluxo de compra)
├── banco.py            # Camada de banco de dados (tabelas e consultas SQLite)
├── nexashop_site/      # Versão web da loja (front-end)
├── .gitignore
└── README.md
Modelo de dados
Tabela
Descrição
produtos
Catálogo: nome, categoria, descrição, preço, estoque
avaliacoes
Notas (1 a 5) e comentários, ligados a um produto
pedidos
Compras finalizadas: cliente, total e data
itens_pedido
Produtos de cada pedido, com quantidade e preço no momento da compra
Decisões técnicas
Consultas parametrizadas (?) em todo acesso ao banco, o que previne SQL injection.
Transação na compra: o pedido, os itens e a baixa de estoque são gravados juntos. Se qualquer produto estiver sem estoque, nada é gravado (rollback).
Preço histórico: o preço de cada item fica salvo no pedido, então mudanças futuras de preço não alteram compras antigas.
Integridade no banco: CHECK para preço, estoque e nota, e chaves estrangeiras ativadas com PRAGMA foreign_keys.
Separação de responsabilidades: app.py cuida da interação com o usuário e banco.py cuida dos dados.
Próximos passos
[ ] Editar e remover produtos
[ ] Busca e filtro por categoria
[ ] Cadastro e login de clientes
[ ] Testes automatizados
[ ] API REST com Flask ou FastAPI conectada ao nexashop_site
Autor
Lucas R. — @LucasR-creator
