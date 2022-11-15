'''Tema 1:  Gravações Musicais
Uma   aplicação   para   gerenciamento   de   músicas   gravadas   por   cantores   para   algum   álbum.
Os dados a serem armazenados são apresentados a seguir: 
Música = (Título, DataRegistro, Estilo, Tempo, Compositor)
Cantor = (NomeArtístico, NomeReal, DataNascimento, email, telefone)
Gravação = (Título, NomeArtístico, Data, Álbum, InstrumentosMusicais)
Atenção: os atributos (dados) sublinhados NÃO podem se repetir no cadastro (chave). 
Utilizando   os   conhecimentos   aprendidos   sobre   Dicionários,   Listas   e   Funções,   desenvolva   um
programa em Python que apresente o seguinte menu de opções para o usuário e implemente cada
operação usando função. Escolha a estrutura de dados mais apropriada para armazenar os dados
de cada entidade descrita anteriormente. 
Menu Principal:
1. Submenu de Músicas
2.Submenu de Cantores
3.Submenu de Gravações
4. Submenu Relatórios
5. Sair
Cada   Submenu   deverá   oferecer   as   opções:   Listar   todos,   Listar   um   elemento   específico   do
conjunto, Incluir (sem repetição), Alterar e Excluir (após confirmação dos dados) um elemento do
conjunto. Observe que as informações que estão no plural significam que deve ser possível incluir
vários   itens   do   mesmo   atributo,   por   exemplo,   o   atributo  IntrumentosMusicais  indica   que   a
gravação   pode   ter  um   número   indefinido   de   Instrumentos   Musicais.  Portanto,   deve-se   utilizar
uma estrutura que seja adequada para armazenar todos eles.
A opção “Relatório” deverá:
•Mostrar todos os dados da música e do cantor para todas as gravações realizadas a partir de
uma data inicial X até uma data final Y, onde ambas as datas são fornecidas pelo usuário.
Obs: Não utilize variáveis globais. Use parâmetros para fazer a transferência de valores 
entre as funções. '''

