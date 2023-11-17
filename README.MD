 ##### guarda_contatos  ##############
 #
###         Arquivos descrição ###

###     add_contatos - main do projeto
###     agenda.db - banco de dados, local onde se armazenará, os contatos 
###     agenda.ui - tela do programa, gerada no qt designer
###     db.py - arquivo que contem as funçoes necessárias para o bando de dados
###     ui_agenda.py - convertido do agenda.ui para ser importado para add_contatos,para      manipulação dos itens da janela
###

### Programa Simples que é composto de um tela, com 3 campos para preenchimento(nome, telefone, email), 4 botões(Buscar,Salvar,Daletar, Limpar), 1 banco de dados(agenda.db)- para salvar as informções inseridas pelo usuário

###         descrição botoes #######

###  ==> buscar - realiza um busca em agenda.db, caso  nao encontre abre um popup de nao encontrado, caso o campo nome esteja vazio apresenta uma mensagem informando que a busca deve ser feita pelo nome. Caso seja encontrado, os dados do contato preencheram os campos da tela.

###  ==> Salvar - Salva os dados inseridos pelo usuario em agenda.db, caso algum campo esteja vazio apresenta erro e mensagem de aviso
###  ==> Deletar -  após realizada uma busca e os dados do contato ter preenchido os campos, deleta o usuário caso seja dado o clique no botão
###  ==> Limpar -  simples, limpar os campos de preenchimento


PS: Programa simples apenas para prática
