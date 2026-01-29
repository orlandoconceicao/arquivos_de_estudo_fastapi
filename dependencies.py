from models import db
from sqlalchemy.orm import sessionmaker

def pegar_sessao():
    try: #try tenta fazer oque tem abaixo #mas assim voce pode forçar ele fechar independente se der erro na outra funcao
        Session = sessionmaker(bind=db)
        session = Session()
        yield session # Quase igual o return mas ele não encerra a sessao
        # Se o try der errado usa para executar outra coisa nao sendo nosso caso
        #except:
        # Se a funçao que estamos colocando essa funçao der erro ele para no yield 
    finally: # executa independente do que acontecer ele fecha a sessao
        session.close() # com o yield pode encerrar a sessao com o session.close()