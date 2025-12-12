# Jornada até agora

## Em busca das variáveis

Nosso próximo objetivo seria desbloquear a atribuição de variáveis (35 cenouras).

Plantar uma cenoura custa 1 grama e 1 madeira.

Temos um mapa de 3x3 e para aproveitar o máximo dele com o cultivo de cenouras (que demoram para crescer), temos que navegar para a próxima coluna.

O drone sempre volta para primeira linha quando ultrapassa a última linha ou para a primeira coluna quando ultrapassa a última coluna.

Minha ideia é um loop simples, chegou no final, move para a direita, chegou no final novamente, volta para o começo.

<img width="1252" height="858" alt="image" src="https://github.com/user-attachments/assets/bb8927a7-468c-41df-bcba-324921eabc08" />

## Melhorando a rota

Variáveis desbloqueadas \o/

Gostaria de não perder tempo com o drone descendo para só depois recomeçar
<img width="1332" height="891" alt="image" src="https://github.com/user-attachments/assets/817bc098-8c84-4036-8283-f43111994ae1" />

Quero que ele suba colhendo e depois desça colhendo:
<img width="1332" height="891" alt="image" src="https://github.com/user-attachments/assets/213a1c4c-528c-4342-a001-d84205ebf599" />

## Funções e imports

Rota aprimorada, mas o código ficou meio grande...

Aproveitando que liberamos funções e imports, o objetivo agora é melhorar o código.
