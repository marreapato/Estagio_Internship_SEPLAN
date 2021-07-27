import pandas as pd
import numpy as np

#Criação de Dataset para a revista Terra-Mãe


programa=np.repeat(['Infraestrutura (pg 148)','Desenvolvimento Rural (pg 106 e pg 144)'
           ,'Cultura (pg 188-189)','Ciência e Tecnologia(pg 96)'
          ,'Recursos Hídricos (pg 118)',
          'Meio Ambiente e Sustentabilidade (pg 140)',
          'Desenvolvimento Produtivo (pg 132)',
          'Gestão Governamental (pg 234)'],[16,12,9,4,11,2,3,2])


data = {'Programa':  programa,
        'Evento':np.array(['Entrega de Rodovias e Estradas',
                   'BA-148 (Irecê - Ibititá - Barra dos Mendes)',
                   'BA-210 (Curaçá - BR-116)',
                   'BA-438 (Itaguaçu da Bahia - Entroncamento BA-052)',
                   'BA-504 (Itanagra - Linha Verde)',
                   'BA-290 (Itanhém - Entroncamento Vila Rezende)',
                   'BA-270 (Maiquinique - Povoado de Mangerona)',
                   'BA-263 (Licínio de Almeida -Urandi)',
                   'BA-140 e BA-160',
                   'BA-223 entre o entroncamento da BR-110 (Sátiro Dias)',
                   'BA-131, Senhor do Bonfim - Saúde - Caem - BR-324',
                   'BA-001 Duplicação (Ponte Ilhéus- Pontal)',
                   'Redução de distâncias (Construção ou Recuperação de Pontes)',
                   'Obras de construção ou recuperação de pontes concluídas-2020',
                   'Obras de construção ou recuperação de pontes EM ANDAMENTO-2020',
                   'Ponte Salvador-Itaparica (p. 158-159)',
                   'Positividade pós pandemia (crescimento)',
                   'Agricultura Familiar',
                   'Da Caatinga para o mercado europeu',
                   'Coopercuc (Cooperativa de Agropecuária Familiar de Canudos, Uauá e Curaçá)',
                   'Coopercaju (Cooperativa da Cajucultura Familiar do Nordeste da Bahia)',
                   'Coopfesba (Cooperativa da Agricultura Familiar e Economia Solidária da Bacia do Rio Salgado e Adjacências)',
                   'Coopessba (Cooperativa de Serviços Sustentáveis da Bahia)',
                   'Cooperleite (Cooperativa de Produtores de Leite do Oeste da Bahia)',
                   'Ampliação da assistência técnica e extensão rural (Ater).',
                   'Parques eólicos.',
                   'Feiras Livres Readequadas Covid-19.',
                   'Feiras Livres Readequadas Covid-19. (Investimentos SDR)',
                   'Situação pandemia:',
                   'Protocolo De Prevenção a Covid-19 do sistema estadual de bibliotecas',
                   'Premiações',
                   'Programa Aldir Blanc Bahia',
                   'Recursos da Aldir Blanc Bahia',
                   'Bate-papos sobre as culturas populares e identitárias (Virtual)',
                   'Teatro Castro Alves (Digital)',
                   'Obras e Reformas',
                   'Arquivo Público do Estado da Bahia',
                   'Telecoronavírus',
                   'Rede de Coworkings',
                   'Internet',
                   'Espaço Colaborar',
                   'Obras Estruturantes',
                   'Mais Conclusões de obras',
                   'Aquífero de Tucano',
                   'Barragem do Catolé',
                   'Barragem de Baraúnas',
                   'Segurança de Barragens',
                   'Investimentos da Embasa',
                   'Investimentos da CERB',
                   'Esgotamento Sanitário.',
                   'Esgotamento Sanitário (Mais Informações)',
                   'Obras em andamento',
                   'Preservação e outros',
                   'Projetos sociais',
                   'Informações',
                   'Energias Renováveis',
                   'Destaques',
                   'Contas',
                   'Pandemia']),
        'Descrição':[],
        }

df = pd.DataFrame (data, columns = ['Programa','Evento'])

print (df)
