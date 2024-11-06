import os
os.system("cls || clear")

from sqlalchemy import create_engine, Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
from datetime import date

Base = declarative_base()

class Profissional(Base):
    __tablename__ = 'profissionais'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    endereco = Column(String)
    data_nascimento = Column(Date)
    profissao = Column(String)
    contratos = relationship("Contrato", back_populates="profissional")

class Empresa(Base):
    __tablename__ = 'empresas'
    cnpj = Column(String, primary_key=True)
    nome = Column(String, nullable=False)
    endereco = Column(String)
    contratos = relationship("Contrato", back_populates="empresa")

class Contrato(Base):
    __tablename__ = 'contratos'
    id = Column(Integer, primary_key=True)
    data_inicio = Column(Date, nullable=False)
    data_termino = Column(Date, nullable=False)
    valor_hora = Column(Float, nullable=False)
    profissional_id = Column(Integer, ForeignKey('profissionais.id'))
    empresa_cnpj = Column(String, ForeignKey('empresas.cnpj'))
    profissional = relationship("Profissional", back_populates="contratos")
    empresa = relationship("Empresa", back_populates="contratos")

engine = create_engine('sqlite:///agencia.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def adicionar_empresa_e_profissional():
    cnpj = input("Digite o CNPJ da empresa: ")
    nome_empresa = input("Digite o nome da empresa: ")
    endereco_empresa = input("Digite o endereço (ou CEP) da empresa: ")

    empresa = session.query(Empresa).filter_by(cnpj=cnpj).first()
    if not empresa:
        empresa = Empresa(cnpj=cnpj, nome=nome_empresa, endereco=endereco_empresa)
        session.add(empresa)
        session.commit()
        print("Empresa adicionada com sucesso!")
    else:
        print("Empresa já existe no banco de dados.")

    os.system("clear||cls")

    while True:
        nome_profissional = input("Digite o nome do profissional: ")
        endereco_profissional = input("Digite o endereço do profissional: ")
        
        while True:
            try:
                data_nascimento_str = input("Digite a data de nascimento do profissional (YYYY-MM-DD): ")
                data_nascimento = date.fromisoformat(data_nascimento_str)  
                break  
            except ValueError:
                print("Formato de data inválido! Por favor, use o formato YYYY-MM-DD.")
        
        profissao = input("Digite a profissão do profissional: ")

        profissional = Profissional(
            nome=nome_profissional, 
            endereco=endereco_profissional, 
            data_nascimento=data_nascimento, 
            profissao=profissao
        )
        session.add(profissional)
        session.commit()
        print("Profissional adicionado com sucesso!")

        contrato = Contrato(
            data_inicio=date.today(),  
            data_termino=date.today(), 
            valor_hora=20.0, 
            profissional_id=profissional.id,
            empresa_cnpj=empresa.cnpj
        )
        session.add(contrato)
        session.commit()
        print("Contrato entre empresa e profissional criado com sucesso!")

        cadastrar_mais = input("Deseja cadastrar mais um profissional? (s/n): ").strip().lower()
        if cadastrar_mais != 's':
            break

os.system("clear||clear")
def buscar_empresa_por_nome():
    while True:
        visualizar_empresas = input("\nDeseja visualizar todas as empresas cadastradas? (s/n): ").strip().lower()
        if visualizar_empresas == 's':
            print("\nEmpresas cadastradas no banco de dados:")
            empresas = session.query(Empresa).all()
            if empresas:
                for empresa in empresas:
                    print(f"- {empresa.nome}")
            else:
                print("Nenhuma empresa cadastrada.")
        
        nome_empresa = input("\nDigite o nome da empresa para buscar suas informações: ")
        empresa = session.query(Empresa).filter_by(nome=nome_empresa).first()
        
        if empresa:
            print(f"\nInformações da Empresa: {empresa.nome}")
            print(f"CNPJ: {empresa.cnpj}")
            print(f"Endereço: {empresa.endereco}")
            print("Contratos:")
            for contrato in empresa.contratos:
                print(f"  - Contrato {contrato.id}")
                print(f"    Data de Início: {contrato.data_inicio}")
                print(f"    Data de Término: {contrato.data_termino}")
                print(f"    Valor por Hora: {contrato.valor_hora}")
                print(f"    Profissional: {contrato.profissional.nome}")

            while True:
                verificar_profissionais = input("Deseja verificar os profissionais cadastrados? (s/n): ").strip().lower()
                if verificar_profissionais == 's':
                    print("\nProfissionais cadastrados na empresa:")
                    for contrato in empresa.contratos:
                        print(f"- {contrato.profissional.nome}")

                    nome_profissional = input("\nDigite o nome do profissional para ver suas informações: ")
                    profissional = session.query(Profissional).filter_by(nome=nome_profissional).first()
                    if profissional:
                        print(f"\nInformações do Profissional: {profissional.nome}")
                        print(f"Endereço: {profissional.endereco}")
                        print(f"Data de Nascimento: {profissional.data_nascimento}")
                        print(f"Profissão: {profissional.profissao}")
                    else:
                        print("Profissional não encontrado.")
                else:
                    break

        else:
            print("Empresa não encontrada. Por favor, tente novamente.")

        nova_pesquisa = input("Deseja fazer uma nova pesquisa de empresa? (s/n): ").strip().lower()
        os.system("clear || cls")
        if nova_pesquisa != 's':
            break
os.system("clear || cls")
def iniciar():
    empresas = session.query(Empresa).all()
    
    if empresas:
        opcao = input("\nJá existem empresas cadastradas. Deseja adicionar uma nova empresa ou pesquisar uma existente? (nova/pesquisar): ").strip().lower()
        if opcao == 'nova':
            adicionar_empresa_e_profissional()
        elif opcao == 'pesquisar':
            buscar_empresa_por_nome()
        else:
            print("Opção inválida. Por favor, digite 'nova' ou 'pesquisar'.")
            iniciar()
    else:
        print("\nNenhuma empresa cadastrada. Vamos adicionar uma nova empresa.")
        adicionar_empresa_e_profissional()

iniciar()
